# Pinned ontology term lists

These JSON lists record upstream class and property IRIs, kinds and English labels, plus provenance, SHA-256, ontology version metadata, licence and attribution. EHRI entries also record named superclasses and superproperties. They are checked data, not vendored ontologies or a claim of OWL conformance. Upstream ontology metadata is preserved verbatim in `ontology_metadata`.

EHRI `EHRI/ehri-kg-ontology` commit `5d42d2505661bdfb04b3634b27c7b9e73392fe07`, tag v0.1.1, has versionInfo 0.1.1, versionIRI `http://lod.ehri-project-test.eu/ontology/0.1.1`, and imports RiC-O **1.0.2**, not 1.1. Its namespace is the upstream test domain `http://lod.ehri-project-test.eu/ontology#`. Its `ontology/ehri.owl` SHA-256 is `a916194c93c6393a623c38cd51a469fc8a0348801cb3807dd62819a8301b99b3`.

RiC-O's pinned checkout is `ICA-EGAD/RiC-O` commit `06912e1e20343f2e88e51f1b55fa232cb30b6b5b`. Both its 1.0.2 release and 1.1 are checked. The pilot's RiC-O terms exist in both; the gate requires the intersection, preserving compatibility with EHRI's base. Read date: 2026-10-20.

Only at the owner's word, read a new upstream version and add a **new** list file; never edit an existing pinned list in place. Re-check every mapping. No upstream imports are fetched by extraction. No new dependency is required for consumers or the alignment checker.

Generate from clean local upstream checkouts (set `RICO_SRC` and `EHRI_SRC` to their roots):

```sh
uv run --no-project --python 3.11 --with rdflib==7.1.4 python standards/extract_terms.py "$RICO_SRC/ontology/previous-versions/RiC-O_v-1-0-2_release/RiC-O_1-0-2.rdf" --repo ICA-EGAD/RiC-O --commit 06912e1e20343f2e88e51f1b55fa232cb30b6b5b --path ontology/previous-versions/RiC-O_v-1-0-2_release/RiC-O_1-0-2.rdf --out standards/rico-1.0.2.json
uv run --no-project --python 3.11 --with rdflib==7.1.4 python standards/extract_terms.py "$RICO_SRC/ontology/current-version/RiC-O_1-1.rdf" --repo ICA-EGAD/RiC-O --commit 06912e1e20343f2e88e51f1b55fa232cb30b6b5b --path ontology/current-version/RiC-O_1-1.rdf --out standards/rico-1.1.json
uv run --no-project --python 3.11 --with rdflib==7.1.4 python standards/extract_terms.py "$EHRI_SRC/ontology/ehri.owl" --repo EHRI/ehri-kg-ontology --commit 5d42d2505661bdfb04b3634b27c7b9e73392fe07 --path ontology/ehri.owl --out standards/ehri-0.1.1.json
bin/verify standards
```

Output is sorted, UTF-8 with LF, and deterministic. `check_alignment.py` scans pilot RDF profiles, exporter literals, generated review JSON-LD, and vocabulary mappings (also future `vocabulary/*.json`). Local mapping objects require a declared profile term and a one-line reason. Existing pilot enum arrays are identifiers, not mapping entries. Arbitrary computed exporter IRI expressions need an explicit, statically checked mapping.
