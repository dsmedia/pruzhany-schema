"""Check RDF mappings against owner-approved pinned lists, without RDF dependencies."""
import argparse
import ast
import json
import re
from pathlib import Path

RICO = "https://www.ica.org/standards/RiC/ontology#"
EHRI = "http://lod.ehri-project-test.eu/ontology#"
# The pinned lists every mapping is checked against: EHRI's ontology and the RiC-O
# version it imports (EHRI 0.2.0 imports RiC-O 1.1; the owner's word of 2026-10-22).
RICO_LIST, EHRI_LIST = "rico-1.1.json", "ehri-0.2.0.json"
# RiC-O 1.1's own axioms (domains, ranges, inverses, characteristics, chains, disjointness,
# cardinalities), pinned from the same file as its terms: the owner's word of 2026-10-23.
RICO_AXIOMS = "rico-1.1-axioms.json"
PROVENANCE = ("repo", "commit", "path", "sha256")
# The LinkML definition (linkml/README.md): every schema file and the generated vocabulary.yaml
# under linkml/, read as text since this checker needs nothing beyond Python itself. Its planted
# files, under linkml/tests/, are not the definition and are left to their own tests.
LINKML_MAPPING_KEYS = {"meaning", "class_uri", "slot_uri", "mappings", "exact_mappings", "close_mappings",
                       "related_mappings", "narrow_mappings", "broad_mappings", "via"}


def check_axioms(standards):
    """The axioms list is read from the very file its terms list was, and names only pinned terms."""
    terms = json.loads((standards / RICO_LIST).read_text(encoding="utf-8"))
    axioms = json.loads((standards / RICO_AXIOMS).read_text(encoding="utf-8"))
    errors = [f"standards/{RICO_AXIOMS}: {key} differs from {RICO_LIST}"
              for key in PROVENANCE if axioms.get(key) != terms.get(key)]
    known = {term["iri"] for term in terms["terms"]}
    for iri in sorted(set(re.findall(re.escape(RICO) + r'[A-Za-z_][\w-]*', json.dumps(axioms["axioms"]))) - known):
        errors.append(f"standards/{RICO_AXIOMS}: {iri} is not a pinned term")
    return errors


def linkml_scalars(text):
    """Yield (line number, key, value) for every scalar of a block-style YAML file.

    The key is the nearest mapping key holding the value: its own for `key: value`, a list's for
    an item `- value` or a flow list `key: [a, b]`. Comments and the lines of a block scalar
    (`>-`, `|`) are passed over. It reads what the LinkML files hold (block style, the generated
    vocabulary's JSON scalars), not every form YAML allows.
    """
    keys, block = [], None
    for number, line in enumerate(text.splitlines(), 1):
        content = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if block is not None:
            if not content or indent > block:
                continue
            block = None
        if not content or content.startswith("#"):
            continue
        content = strip_comment(content)
        if content.startswith("- ") or content == "-":
            content, indent = content[1:].strip(), indent + 2
            while keys and keys[-1][0] >= indent:
                keys.pop()
            item = re.match(r"^([\w'\"-]+):(?:\s+(.*))?$", content)
            if not item:
                if keys and content:
                    yield number, keys[-1][1], unquote(content)
                continue
        else:
            item = re.match(r"^([\w'\"-]+):(?:\s+(.*))?$", content)
            if not item:
                continue
            while keys and keys[-1][0] >= indent:
                keys.pop()
        key, value = item.group(1).strip("'\""), (item.group(2) or "").strip()
        keys.append((indent, key))
        if value in (">", ">-", ">+", "|", "|-", "|+"):
            block = indent
        elif value.startswith("[") and value.endswith("]"):
            for part in value[1:-1].split(","):
                yield number, key, unquote(part.strip())
        elif value:
            yield number, key, unquote(value)


def strip_comment(content):
    """The line without its comment: a # after white space and outside quotes."""
    quote, previous, skip = None, " ", False
    for index, char in enumerate(content):
        if skip:
            skip, previous = False, "escaped"
            continue
        if (quote == '"' and char == "\\") or (quote == "'" and content[index:index + 2] == "''"):
            skip = True
            continue
        if quote and char == quote:
            quote = None
        elif not quote and char in "'\"" and previous in " :[,-":
            quote = char
        elif not quote and char == "#" and previous.isspace():
            return content[:index].rstrip()
        previous = char
    return content


def unquote(value):
    try:
        if value.startswith('"') and value.endswith('"') and len(value) > 1:
            return json.loads(value)
    except ValueError:
        return value
    if value.startswith("'") and value.endswith("'") and len(value) > 1:
        return value[1:-1].replace("''", "'")
    return value


def check_export(root):
    """The generated export uses only pinned standards and explained local declarations."""
    folder = root / 'linkml/generated/rdf'
    if not folder.exists():
        return []  # Older fixture repositories have no export profile.
    ontology = (folder / 'ontology.ttl').read_text(encoding='utf-8')
    context = (folder / 'context.jsonld').read_text(encoding='utf-8')
    profile = (folder / 'profile.json').read_text(encoding='utf-8')
    errors = []
    for prefix, namespace, filename in [('rico', RICO, RICO_LIST), ('ehri', EHRI, EHRI_LIST)]:
        known = {t['iri'] for t in json.loads((root / 'standards' / filename).read_text(encoding='utf-8'))['terms']}
        for term in set(re.findall(re.escape(namespace) + r'[A-Za-z_][\w-]*', ontology + context + profile)):
            if term not in known: errors.append('RDF export: unapproved ' + prefix + ' term ' + term)
    pc = 'https://pruzhany.org/ns/sourced-entities#'
    declared = set(re.findall(r'^<(' + re.escape(pc) + r'[^>]+)> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>', ontology, re.M))
    explained = set(re.findall(r'^<(' + re.escape(pc) + r'[^>]+)> <http://www.w3.org/2000/01/rdf-schema#comment> "[^"\s]', ontology, re.M))
    used = set(re.findall(re.escape(pc) + r'export_[A-Za-z_][\w-]*', context + profile + ontology))
    for term in sorted(used - declared): errors.append('RDF export: undeclared local term ' + term)
    for term in sorted(declared - explained): errors.append('RDF export: unexplained local term ' + term)
    return errors


def check(root):
    standards = root / "standards"
    def load(name):
        return {term["iri"] for term in json.loads((standards / name).read_text(encoding="utf-8"))["terms"]}
    known = {"rico": load(RICO_LIST), "ehri": load(EHRI_LIST)}
    errors = check_axioms(standards) + check_export(root)
    def validate(prefix, term, path):
        iri = term if term.startswith(("http:", "https:")) else {"rico": RICO, "ehri": EHRI}[prefix] + term.removeprefix(prefix + ":")
        if iri not in known[prefix]:
            errors.append(f"{path.relative_to(root)}: unapproved {prefix} term {term}")
    paths = set(root.glob("vocabulary/**/*.ttl")) | set(root.glob("pilots/**/profile.ttl")) | set(root.glob("pilots/**/build.py")) | set(root.glob("pilots/**/review.jsonld"))
    for path in sorted(paths):
        text = path.read_text(encoding="utf-8")
        for prefix, namespace in (("rico", RICO), ("ehri", EHRI)):
            for term in set(re.findall(r'\b' + prefix + r':([A-Za-z_][\w-]*)', text) + re.findall(re.escape(namespace) + r'([A-Za-z_][\w-]*)', text)):
                validate(prefix, term, path)
        if path.name == "build.py":
            tree = ast.parse(text)
            for node in ast.walk(tree):
                if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add) and isinstance(node.left, ast.Name) and node.left.id in {"RICO", "EHRI"}:
                    prefix = node.left.id.lower()
                    right = node.right
                    if isinstance(right, ast.Call) and isinstance(right.func, ast.Attribute) and isinstance(right.func.value, ast.Dict):
                        values = right.func.value.values
                    elif isinstance(right, ast.IfExp):
                        values = [right.body, right.orelse]
                    elif isinstance(right, ast.Constant):
                        values = [right]
                    else:
                        errors.append(f"{path.relative_to(root)}: cannot statically check emitted {prefix} IRI")
                        values = []
                    for value in values:
                        if isinstance(value, ast.Constant) and isinstance(value.value, str) and value.value:
                            validate(prefix, value.value, path)
    vocabularies = set(root.glob("pilots/**/vocabulary.json")) | set(root.glob("vocabulary/*.json"))
    for path in sorted(vocabularies):
        profile = path.with_suffix(".profile.ttl")
        if not profile.exists():
            profile = path.parent / "profile.ttl"
        declarations = profile.read_text(encoding="utf-8") if profile.exists() else ""
        def walk(value, location):
            if isinstance(value, dict):
                if "mapping" in value:
                    walk(value["mapping"], location + ".mapping")
                    return
                # Entries have a definition or an explicit mapping key; container metadata is skipped.
                if any(k in value for k in ("definition", "rico", "ehri", "local")) or (location != "root" and not any(isinstance(v, (dict, list)) for v in value.values())):
                    mapped = False
                    for prefix in ("rico", "ehri"):
                        if value.get(prefix):
                            mapped = True
                            terms = value[prefix] if isinstance(value[prefix], list) else [value[prefix]]
                            for term in terms:
                                validate(prefix, term, path)
                    if value.get("via"):
                        validate("rico", value["via"], path)
                        # A qualification path must name a Relation class, not a property.
                        terms = json.loads((standards / RICO_LIST).read_text(encoding="utf-8"))["terms"]
                        via = value["via"].removeprefix("rico:")
                        if not any(t["iri"] == RICO + via and t["kind"] == "class" and via.endswith("Relation") for t in terms):
                            errors.append(f"{path.relative_to(root)}: via must be a RiC-O Relation class")
                    if not mapped:
                        local, reason = value.get("local"), value.get("reason")
                        if not isinstance(local, str) or not re.search(re.escape(local) + r'\s+a\s+', declarations):
                            errors.append(f"{path.relative_to(root)}:{location}: local mapping must name a term declared in {profile.name}")
                        if not isinstance(reason, str) or not reason.strip() or len(reason.splitlines()) != 1:
                            errors.append(f"{path.relative_to(root)}:{location}: local mapping requires a one-line reason")
                for key, child in value.items():
                    walk(child, location + "." + key)
            elif isinstance(value, list):
                for i, child in enumerate(value):
                    walk(child, f"{location}[{i}]")
        walk(json.loads(path.read_text(encoding="utf-8")), "root")
    # The LinkML definition: every RiC-O or EHRI term it names anywhere is pinned; every local
    # term it maps to (a meaning, a class or slot URI, a mapping, a via) is declared in a
    # vocabulary profile; every via names a RiC-O Relation class.
    declared = set()
    for profile in sorted(root.glob("vocabulary/*.ttl")):
        declared |= set(re.findall(r"(?m)^(pc:[A-Za-z_][\w-]*)\s+a\s", profile.read_text(encoding="utf-8")))
    relation_classes = {t["iri"] for t in json.loads((standards / RICO_LIST).read_text(encoding="utf-8"))["terms"]
                        if t.get("kind") == "class" and t["iri"].endswith("Relation")}
    linkml = root / "linkml"
    for path in sorted(p for p in linkml.glob("**/*.yaml") if "tests" not in p.relative_to(linkml).parts):
        text = path.read_text(encoding="utf-8")
        for prefix, namespace in (("rico", RICO), ("ehri", EHRI)):
            for term in sorted(set(re.findall(r'\b' + prefix + r':([A-Za-z_][\w-]*)', text) + re.findall(re.escape(namespace) + r'([A-Za-z_][\w-]*)', text))):
                validate(prefix, term, path)
        # This JSON-compatible YAML is a projection policy, not a LinkML schema;
        # its omitted Citation.via is prose. check_export checks its generated mappings.
        if path.name == 'rdf-profile.yaml':
            continue
        for number, key, value in linkml_scalars(text):
            if key not in LINKML_MAPPING_KEYS:
                continue
            for term in re.findall(r"(?<![\w:/])pc:[A-Za-z_][\w-]*", value):
                if term not in declared:
                    errors.append(f"{path.relative_to(root)}:{number}: local term {term} is not declared in vocabulary/*.ttl")
            if key == "via" and not (value.startswith("rico:") and value.endswith("Relation")
                                     and RICO + value.removeprefix("rico:") in relation_classes):
                errors.append(f"{path.relative_to(root)}:{number}: via must be a RiC-O Relation class")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        errors = check(args.root)
    except (OSError, ValueError, KeyError) as exc:
        raise SystemExit(f"standards: cannot read pinned term lists: {exc}")
    if errors:
        raise SystemExit("\n".join(errors))
    print("standards: all mappings use pinned terms or declared, explained local terms")


if __name__ == "__main__":
    main()
