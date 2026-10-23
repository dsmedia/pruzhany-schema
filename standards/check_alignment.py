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


def check(root):
    standards = root / "standards"
    def load(name):
        return {term["iri"] for term in json.loads((standards / name).read_text(encoding="utf-8"))["terms"]}
    known = {"rico": load(RICO_LIST), "ehri": load(EHRI_LIST)}
    errors = check_axioms(standards)
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
