# Pinned ontology term lists

These JSON lists record upstream class and property IRIs, kinds and English labels, plus provenance, SHA-256, ontology version metadata, licence and attribution. EHRI entries also record named superclasses and superproperties. They are checked data, not vendored ontologies or a claim of OWL conformance. Upstream ontology metadata is preserved verbatim in `ontology_metadata`.

The gate checks every mapping against **EHRI 0.2.0** (`ehri-0.2.0.json`) and **RiC-O 1.1** (`rico-1.1.json`), the version EHRI 0.2.0 imports: the owner's word of 2026-10-22, after EHRI announced on 2026-09-07 that its knowledge graph is aligned with RiC-O 1.1 (<https://ehri-kg.ehri-project.eu/news/alignment-rico-11-and-additional-services/>). The earlier lists, `ehri-0.1.1.json` and `rico-1.0.2.json`, stay as they were pinned, for history; the gate no longer reads them.

EHRI 0.2.0 is `EHRI/ehri-kg-ontology` commit `4b275a7d8066b7084dda1e76a16ec0cc7a0a5455` on branch `develop` (2026-09-02; PR #15, which closes issue #14 "alignment to RiC-O 1.1"; not yet tagged, and `main` still holds 0.1.1). It has versionInfo 0.2.0, versionIRI `http://lod.ehri-project-test.eu/ontology/0.2.0`, and imports `https://www.ica.org/standards/RiC/ontology/1.1`. Against 0.1.1 it removes `notes` and the misspelt `physicalCharacterisiticsAndTechnicalRequirements` (now `physicalCharacteristicsAndTechnicalRequirements`), and adds `biographicalHistory`, `HasCopyRelation`, `IsCopyOfRelation` and their two role properties; none of the removed terms was used here. Its namespace is still the upstream test domain `http://lod.ehri-project-test.eu/ontology#`, which EHRI says will change when the graph moves to production. Its `ontology/ehri.owl` SHA-256 is `c04f53203e6aecee5aef1dc8f8724092af831bf717698ece6342e2dcc4bcbe50`. Read date: 2026-10-22.

EHRI 0.1.1 was read at commit `5d42d2505661bdfb04b3634b27c7b9e73392fe07` of `main`; tag v0.1.1 is commit `ed5ec57f2fa8ce75902f76b75295fcc361f00891`, and `ontology/ehri.owl` is the same file in both (SHA-256 `a916194c93c6393a623c38cd51a469fc8a0348801cb3807dd62819a8301b99b3`). It imports RiC-O 1.0.2.

RiC-O's pinned checkout is `ICA-EGAD/RiC-O` commit `06912e1e20343f2e88e51f1b55fa232cb30b6b5b`, read on 2026-10-20. RiC-O 1.1 (May 2025) only adds to 1.0.2 but for one rename recorded in its history note: `hasOrHadCategory` and `isOrWasCategoryOf` (with their four member-level forms) became `hasOrHadType` and `isOrWasTypeOf`; none of them was used here. It adds `TitleType` and `hasTitleType`.

**RiC-O 1.1's axioms** (`rico-1.1-axioms.json`) are pinned beside its terms at the owner's word of 2026-10-23 ("yes, pin the rules"), from the same file at the same commit, so that tests of meaning can cite RiC-O's own rules rather than a reading of them. For each term it records, as stated and never inferred or completed: `domain` and `range` (a list, any of which; a union is spelled out), `superclasses`, `superproperties`, `inverse_of`, `characteristics` (symmetric, transitive), `property_chains`, `disjoint_with`, the qualified `cardinalities` on the Relation classes, and `rolified_by` (the property whose self-restriction the Relation class is). 663 terms carry at least one. `owl:inverseOf` is listed only on the term that states it; OWL makes it hold both ways. Read date: 2026-10-23. The gate checks that its repository, commit, path and SHA-256 equal `rico-1.1.json`'s and that every RiC-O IRI in it is a pinned term; its tests check the rules `docs/design/2026-10-23-standards-foundation-vetting.md` cites.

Only at the owner's word, read a new upstream version and add a **new** list file; never edit an existing pinned list in place. Re-check every mapping. No upstream imports are fetched by extraction. No new dependency is required for consumers or the alignment checker.

Generate from clean local upstream checkouts (set `RICO_SRC` and `EHRI_SRC` to their roots):

```sh
uv run --no-project --python 3.11 --with rdflib==7.1.4 python standards/extract_terms.py --read-on 2026-10-20 "$RICO_SRC/ontology/previous-versions/RiC-O_v-1-0-2_release/RiC-O_1-0-2.rdf" --repo ICA-EGAD/RiC-O --commit 06912e1e20343f2e88e51f1b55fa232cb30b6b5b --path ontology/previous-versions/RiC-O_v-1-0-2_release/RiC-O_1-0-2.rdf --out standards/rico-1.0.2.json
uv run --no-project --python 3.11 --with rdflib==7.1.4 python standards/extract_terms.py --read-on 2026-10-20 "$RICO_SRC/ontology/current-version/RiC-O_1-1.rdf" --repo ICA-EGAD/RiC-O --commit 06912e1e20343f2e88e51f1b55fa232cb30b6b5b --path ontology/current-version/RiC-O_1-1.rdf --out standards/rico-1.1.json
uv run --no-project --python 3.11 --with rdflib==7.1.4 python standards/extract_terms.py --axioms --read-on 2026-10-23 "$RICO_SRC/ontology/current-version/RiC-O_1-1.rdf" --repo ICA-EGAD/RiC-O --commit 06912e1e20343f2e88e51f1b55fa232cb30b6b5b --path ontology/current-version/RiC-O_1-1.rdf --out standards/rico-1.1-axioms.json
uv run --no-project --python 3.11 --with rdflib==7.1.4 python standards/extract_terms.py --read-on 2026-10-20 "$EHRI_SRC/ontology/ehri.owl" --repo EHRI/ehri-kg-ontology --commit 5d42d2505661bdfb04b3634b27c7b9e73392fe07 --path ontology/ehri.owl --out standards/ehri-0.1.1.json  # main, 0.1.1
uv run --no-project --python 3.11 --with rdflib==7.1.4 python standards/extract_terms.py --read-on 2026-10-22 "$EHRI_SRC/ontology/ehri.owl" --repo EHRI/ehri-kg-ontology --commit 4b275a7d8066b7084dda1e76a16ec0cc7a0a5455 --path ontology/ehri.owl --out standards/ehri-0.2.0.json  # develop, 0.2.0
bin/verify standards
```

Output is sorted, UTF-8 with LF, and deterministic. `check_alignment.py` scans pilot RDF profiles, exporter literals, generated review JSON-LD, and vocabulary mappings (also future `vocabulary/*.json`). Since 28 October 2026 it also reads the LinkML definition, `linkml/**/*.yaml` outside `linkml/tests/`: every `rico:` or `ehri:` CURIE or namespace IRI must be pinned, every `pc:` term used as a `meaning`, `class_uri`, `slot_uri`, mapping or `via` must be declared in a `vocabulary/*.ttl` profile, and every `via` must be a RiC-O Relation class. Local mapping objects require a declared profile term and a one-line reason. Existing pilot enum arrays are identifiers, not mapping entries. Arbitrary computed exporter IRI expressions need an explicit, statically checked mapping.

All `vocabulary/**/*.ttl` profiles are checked, including the released
`profile.ttl` and `site-content.profile.ttl` (subtypes and subjects released
2026-10-25; printed and supplied title types released 2026-10-31). Local mappings use the
vocabulary's matching `<name>.profile.ttl` when present, otherwise its directory's
`profile.ttl`. Tests check terms and local declarations in the separate proposed profile.

## EHRI person shapes (1.1)

At the owner's word of 30–31 October 2026 (steps `PLAN.md`, “1.0 is done when”),
`ehri-people-1.1-1c2325f9/` pins the **unchanged** `people.shacl.ttl` and
`people.shex` from `EHRI/ehri-kg-mapping`, `src/shapes/1.1/`, develop commit
`1c2325f9d2267a8a0c639cd041be54ec9a73e517`, read **2026-10-31**.
`pin.json` records each source URL, SHA-256, date, attribution and EUPL-1.2
licence; the upstream licence travels with the files. This is a separate mapping
repository pin, not a change to the EHRI 0.2.0 or RiC-O 1.1 ontology pins.
Never edit these files in place; a later pin needs its own directory.

`bin/verify standards` checks their bytes and provenance. `bin/verify linkml`
checks the isolated pilot and fictional controls against both unmodified shapes,
using pySHACL 0.30.1 and PyShEx 0.9.0 already in `linkml/requirements.lock`.
The pilot's person has only `ehri:Person` as type and exactly one plain
`rico:name`. Its source-scoped printed names remain `rico:AgentName` observations;
no unreviewed name association is promoted to a canonical alternate name.

The SHACL and ShEx are **not equivalent**: ShEx's linked alternate/parallel names
and birth/death dates require inverse edges to EHRI's own person IRI stem;
SHACL requires an IRI there. Fictional controls exercise those nested shapes and
that difference. Passing the person focuses does not claim standalone name-shape
conformance for our addresses, RiC-O conformance, or acceptance by EHRI.

## Impresso edition contracts

`impresso-329323c/` is the single home of the unchanged canonical issue, canonical
page and rebuilt paper content-item JSON Schemas from `impresso/impresso-schemas`,
master commit `329323c73712c33110e28531726847210617c418`, read **2026-10-31**.
`pin.json` records each upstream path, URL and SHA-256, the read date, attribution
and AGPL-3.0-or-later licence; the unchanged upstream `LICENSE` travels with them.
These three schema files are byte-identical to the earlier steps copies at
`d55526d`. Never edit a pin in place. `bin/verify standards` checks the bytes and
provenance; `bin/verify linkml` compares the separately described external
contracts against these oracles, including fictional controls and planted faults.
The page oracle reads this pin, with no second fixture copy.

## EHRI corporate-body shapes (1.1)

At the same owner's word of 30–31 October 2026, `ehri-cb-1.1-1c2325f9/`
pins unchanged `src/shapes/1.1/cb.shacl.ttl`, `cb.shex` and `LICENSE.md` from
`EHRI/ehri-kg-mapping` commit `1c2325f9d2267a8a0c639cd041be54ec9a73e517`,
read **2026-10-31**. `pin.json` records URLs, SHA-256, attribution and EUPL-1.2.
`bin/verify standards` checks bytes and provenance; `bin/verify linkml` tests
fictional corporate bodies and planted faults against both unchanged shapes.
No production contract or ontology pin changes. Never edit pinned files in place.

The corporate-body focus is `ehri:CBAndFamily`, requiring a language-tagged
`rico:name`. Steps preserves the public name and uses `und` when its language
is unavailable, rather than inventing one. Person names remain plain strings.
Nested names and dates have the same ShEx-only EHRI inverse-address restriction
as the person pin; tests expose it. These are corporate-body focus checks,
not acceptance by EHRI or a claim about every auxiliary shape or family export.

## IIIF Presentation 3

`iiif-presentation-3-3891f47/` keeps the unchanged Presentation 3 JSON Schema
from IIIF/presentation-validator main `3891f47ce7dbaa896027a5fab5f63a109de4bd70`,
read 31 October 2026. Its README describes the schema, source provenance and
licence limits. `bin/verify standards` checks its bytes; steps validates fictional
manifests and the private real export offline. No site or LinkML contract changes.
