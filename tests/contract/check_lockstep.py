"""Zod <-> Pydantic lockstep: the twins in zod/ and pydantic/ must not drift.

Moved here from pruzhany-press/tests/contract/test_schema_contract.py on
2026-10-22, when that repository was retired and no consumer was left to run
it. For each paired model it compares the set of field names and the value-set
of every top-level enum field, from the JSON Schema each side emits (Zod by
``z.toJSONSchema()``, through dump_zod_schemas.ts under bun; Pydantic by
``model_json_schema()``). Current site documents and their page/reference
components also compare required fields and run shared validation fixtures.
Runtime-specific optional-null behavior remains unchanged.

    python -P tests/contract/check_lockstep.py   # from the repository root

Exits 1 and names every difference when the twins drift.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[2]
SITE_MODELS = set(json.loads((ROOT / 'tests/contract/site-shapes.fixtures.json').read_text(encoding='utf-8'))['models'])
SITE_MODELS |= {'Holder', 'SourceDerivation', 'PlaceIdentifier', 'SiteCitation', 'SharedName', 'LifeEventDate', 'LifeEventMainPerson', 'Block', 'Page', 'PagesData', 'CrossReference', 'ExternalReference'}
SITE_MODELS |= {'MediaDecision', 'MediaText', 'MediaMaster', 'MediaDerivative', 'Media', 'PublicMedia'}

# Pydantic class name -> Zod export key. Identical today, kept explicit so that a
# rename on one side is a visible one-line change and never a silent skip.
SITE_MODELS |= {'MediaFamilyWords', 'MediaConsent', 'MediaFixity', 'MediaConsentScope', 'MediaPortrait', 'MediaDepicted', 'MediaWithdrawal', 'MediaRegion'}
SITE_MODELS |= {'Edition', 'EditionsCatalog', 'HistoricalEvent', 'Holiday'}

MODEL_PAIRS = {
    "Edition": "Edition",
    "EditionsCatalog": "EditionsCatalog",
    "HistoricalEvent": "HistoricalEvent",
    "Holiday": "Holiday",
    "MediaRegion": "MediaRegion",
    "MediaDepicted": "MediaDepicted",
    "MediaPortrait": "MediaPortrait",
    "MediaWithdrawal": "MediaWithdrawal",
    "MediaConsentScope": "MediaConsentScope",
    "MediaConsent": "MediaConsent",
    "MediaFamilyWords": "MediaFamilyWords",
    "MediaFixity": "MediaFixity",

    "MediaDecision": "MediaDecision",
    "MediaText": "MediaText",
    "MediaMaster": "MediaMaster",
    "MediaDerivative": "MediaDerivative",
    "Media": "Media",
    "PublicMedia": "PublicMedia",
    "EnglishCheck": "EnglishCheck",
    "TitleCheck": "TitleCheck",
    "TranslationCheck": "TranslationCheck",
    "PrintedAddress": "PrintedAddress",
    "TextBasis": "TextBasis",
    "CitedTextBasis": "CitedTextBasis",
    "CitedTranslation": "CitedTranslation",
    "Authorship": "Authorship",
    "PrintedTitle": "PrintedTitle",
    "SuppliedTitle": "SuppliedTitle",
    "Translation": "Translation",
    "ContentItemBlockRef": "ContentItemBlockRef",
    "ContentItem": "ContentItem",
    "PrintedSection": "PrintedSection",
    "ContentItemsData": "ContentItemsData",
    "SharedFact": "SharedFact",
    "SourcedRelation": "SourcedRelation",
    "SharedPerson": "SharedPerson",
    "SharedFamily": "SharedFamily",
    "PlaceIdentifier": "PlaceIdentifier",
    "Holder": "Holder",
    "SourceDerivation": "SourceDerivation",
    "SharedPlace": "SharedPlace",
    "SharedOrganization": "SharedOrganization",
    "SharedEvent": "SharedEvent",
    "SharedName": "SharedName",
    "SiteCitation": "SiteCitation",
    "LifeEventDate": "LifeEventDate",
    "LifeEventMainPerson": "LifeEventMainPerson",
    "SharedRecord": "SharedRecord",
    "IssueMention": "IssueMention",
    "IssueMentionsData": "IssueMentionsData",
    "ContentItemRef": "ContentItemRef",
    "IssueLifeEvent": "IssueLifeEvent",
    "IssueLifeEventsData": "IssueLifeEventsData",
    "SiteIssue": "SiteIssue",
    "SiteArchive": "SiteArchive",
    "Block": "Block",
    "Page": "Page",
    "PagesData": "PagesData",
    "CrossReference": "CrossReference",
    "ExternalReference": "ExternalReference",
    "SourcedDate": "SourcedDate",
    "Review": "Review",
    "Attribution": "Attribution",
    "Source": "Source",
    "Citation": "Citation",
    "Fact": "Fact",
    "Name": "Name",
    "Fate": "Fate",
    "Mention": "Mention",
}


def load_pydantic(root: Path) -> ModuleType:
    """Load pydantic/ under another name: it would shadow the library if imported as is."""
    name = "pruzhany_schema_pydantic"
    tree = root / "pydantic"
    sys.modules.pop(name, None)
    spec = importlib.util.spec_from_file_location(
        name, tree / "__init__.py", submodule_search_locations=[str(tree)]
    )
    assert spec is not None and spec.loader is not None
    package = importlib.util.module_from_spec(spec)
    sys.modules[name] = package
    spec.loader.exec_module(package)
    return package


def dump_zod(root: Path) -> dict:
    proc = subprocess.run(
        ["bun", str(root / "tests/contract/dump_zod_schemas.ts")],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        sys.exit(f"dump_zod_schemas.ts failed:\n{proc.stderr}")
    return json.loads(proc.stdout)


def resolve(node, root, depth: int = 0):
    """Follow $ref chains into the schema's own $defs/definitions."""
    while isinstance(node, dict) and "$ref" in node and depth < 20:
        key = node["$ref"].split("/")[-1]
        defs = root.get("$defs") or root.get("definitions") or {}
        node = defs.get(key, {})
        depth += 1
    return node


def enum_values(prop, root) -> frozenset | None:
    """The value-set of an enum property, through $refs and nullable unions."""
    node = resolve(prop, root)
    if not isinstance(node, dict):
        return None
    if "enum" in node:
        return frozenset(node["enum"])
    if "const" in node:
        return frozenset([node['const']])
    for combinator in ("anyOf", "oneOf", "allOf"):
        if combinator in node:
            values: set = set()
            for sub in node[combinator]:
                values |= enum_values(sub, root) or set()
            if values:
                return frozenset(values)
    return None


def signature(schema: dict) -> dict:
    props = schema.get("properties", {})
    enums = {name: enum_values(node, schema) for name, node in props.items()}
    return {"fields": set(props), "enums": {k: v for k, v in enums.items() if v is not None}}


def problems(zod_schemas: dict, package: ModuleType) -> list[str]:
    found: list[str] = []
    if missing := SITE_MODELS - MODEL_PAIRS.keys():
        found.append(f'site models missing from lockstep pairs: {sorted(missing)}')
    for py_name, zod_name in MODEL_PAIRS.items():
        py_cls = getattr(package, py_name, None)
        zod_schema = zod_schemas.get(zod_name)
        if py_cls is None:
            found.append(f"[{py_name}] missing from the Pydantic package")
            continue
        if zod_schema is None or zod_schema.get("__missing__"):
            found.append(f"[{zod_name}] missing from Zod schema exports")
            continue
        py_sig = signature(py_cls.model_json_schema())
        zod_sig = signature(zod_schema)
        if py_name in SITE_MODELS:
            py_required = set(py_cls.model_json_schema().get('required', []))
            zod_required = set(zod_schema.get('required', []))
            if py_required != zod_required:
                found.append(f'[{py_name}] required fields differ: Pydantic={sorted(py_required)}, Zod={sorted(zod_required)}')
        if only := py_sig["fields"] - zod_sig["fields"]:
            found.append(f"[{py_name}] fields only in Pydantic: {sorted(only)}")
        if only := zod_sig["fields"] - py_sig["fields"]:
            found.append(f"[{py_name}] fields only in Zod: {sorted(only)}")
        for field in py_sig["enums"].keys() & zod_sig["enums"].keys():
            py_vals, zod_vals = py_sig["enums"][field], zod_sig["enums"][field]
            if py_vals != zod_vals:
                found.append(
                    f"[{py_name}.{field}] enum mismatch: "
                    f"Pydantic-only={sorted(py_vals - zod_vals)} "
                    f"Zod-only={sorted(zod_vals - py_vals)}"
                )
        for field in py_sig["enums"].keys() ^ zod_sig["enums"].keys():
            if field in py_sig["fields"] and field in zod_sig["fields"]:
                side = "Pydantic" if field in py_sig["enums"] else "Zod"
                found.append(f"[{py_name}.{field}] is an enum only on the {side} side")
    return found


def main() -> None:
    package = load_pydantic(ROOT)
    zod_schemas = dump_zod(ROOT)
    found = problems(zod_schemas, package)
    if found:
        sys.exit("Zod<->Pydantic contract drift:\n" + "\n".join(f"  - {p}" for p in found))
    print(f"contract: {len(MODEL_PAIRS)} Zod/Pydantic twins in lockstep")
    # Load by path so python -P keeps the local pydantic directory off sys.path.
    spec = importlib.util.spec_from_file_location('site_shape_cases', ROOT / 'tests/contract/check_site_shapes.py')
    cases = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cases)
    cases.check_site_shapes(package)
    spec = importlib.util.spec_from_file_location('linkml_lockstep', ROOT / 'tests/contract/check_linkml.py')
    definition = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(definition)
    definition.check(zod_schemas)


if __name__ == "__main__":
    main()
