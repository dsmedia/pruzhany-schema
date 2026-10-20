# Sourced entities pilot for issue 14

**Start with [the generated review](generated/review.md).** This is an executable companion to [issue #14](https://github.com/dsmedia/pruzhany-schema/issues/14), isolated from the production schemas and both consumers. It follows EHRI ontology 0.1.1 and its RiC-O 1.0.2 base. RiC-O 1.0.2 and 1.1 are both checked; the pilot’s terms exist in both.

The preview groups **12 people, two cross-edition engagements, 22 mentions, six assertions and one relationship**, from ten newspaper excerpts in the editions of 1934-02-02, 1934-02-09 and 1938-12-16. The unjoined observations contain 13 person IDs and four event IDs. Two event joins and one person join are explicit, reversible review proposals.

## What to review

1. Read [the people, assertions and original-language excerpts](generated/review.md). Are the participant roles and three proposed identity joins justified?
2. Inspect [the corpus-wide JSON](generated/pilot.json). Evidence confidence, identity confidence and editorial approval are separate. Printed names are distinct from inherited display labels. Facts cite individual newspaper pieces.
3. Inspect [the RiC-O JSON-LD](generated/review.jsonld) and [mapping decisions](mapping.md). Pending and disputed assertions are RDF statements, not unqualified historical triples. Approved examples are demonstrated with fictional fixtures in tests.
4. Compare [generated edition views](generated/edition-views.json). These are small, self-contained read models generated from the same entity collection, not production `EnrichedPerson` records or full edition bundles.
5. Inspect [the public projection example](generated/public-projection.json). All real assertions and identity joins remain pending; the projection exposes printed names only. It is a conservative demonstration, not a replacement of `pruzhany-svelte`'s privacy policy.

## Run it

Use the existing toolchain (`bun`, `uv`, Python 3.11); dependencies are pinned by the verification commands.

```sh
bin/verify zod pydantic pilot standards

# Rebuild the deterministic, committed artifacts.
uv run --no-project --python 3.11 --with pydantic==2.12.5 \
  python -P pilots/sourced-entities/build.py

# Reverse all three proposed joins in a separate, temporary output folder.
uv run --no-project --python 3.11 --with pydantic==2.12.5 \
  python -P pilots/sourced-entities/build.py \
  --reverse join-person-menachem \
  --reverse join-event-esther-yaakov \
  --reverse join-event-itke-menachem \
  --output /tmp/pruzhany-pilot-unjoined
```

Reversal restores 13 source person records and four source event records while preserving every original mention, its printed name, citation and original ID. Rebuilding without the flags reproduces the baseline. Nothing writes into another checkout, calls a model, updates a register, changes a production submodule pin or deploys the site.

## Files and ownership

| File | Purpose |
|---|---|
| `input/newspaper-extracts.json` | Frozen, narrowly selected source observations from `pruzhany-svelte@35cccf97b326c149e7b1d547b842b2537cbce66f`, including file blob IDs. No private research notes, archive-match dossiers, fates or biographies. |
| `build.py` | Explicit transcript annotations, proposed joins, conversion, projections, report and JSON-LD export. |
| `vocabulary.json` | One versioned vocabulary; generates the pilot's Zod/Pydantic enum files. Null RiC-O mappings identify local extensions. |
| `../../zod/sourced-entities-pilot.schema.ts` | Experimental contract and referential-integrity checks; not re-exported by the production index. Currently uses Node crypto for the offline anchor check. |
| `../../pydantic/sourced_entities_pilot.py` | Strict Python twin; not imported into production model definitions. |
| `contract_cases.py` | Shared positive/negative behavioral parity cases, checked in both languages. |
| `test_pilot.py` | Reversal, temporal residence, contradictions, fate, publication and parsed RDF tests. Entirely fictional edge-case biographies. |
| `ric-o-profile.json` | Verified upstream component IRIs and definitions, source hashes and checked versions. Not a copy of the whole ontology. |
| `profile.ttl` | Explicit local RDF extensions needed alongside RiC-O; no claim of one-to-one equivalence. |
| `generated/` | Deterministic review outputs. `build.py --check` fails on drift. |

These fixture inputs and annotations are the pilot's authoring source; the generated files are read-only projections. This PR does not decide the eventual cross-repository authoring store. Before a production migration, designate one curated entity store and make site data derived from it.

## Validation and limits

`bin/verify pilot` checks generated enums/artifacts, Python behavioral/RDF tests, non-UTF-8 locale portability, and the isolated TypeScript test. It generates parity fixtures with the centrally pinned Python toolchain. The pilot Zod suite runs the same accepted/rejected contract examples through both languages, including the complete real fixture. This is behavioral parity, not a claim that the two emitted JSON Schemas are byte-identical. Existing production schema tests and typechecking still run.

The pilot preserves the selected newspaper transcripts, not independently checked scan readings. Existing identity labels are carried forward, not newly certified. The source contains an engagement date added in English but absent from the selected printed excerpt; the preview deliberately does not promote it to a date fact. There are no real-person fate determinations or external identity matches in this PR. Those require separately reviewed evidence.

Fate edge cases use explicit operational bounds of 1939-09-01 and 1945-05-08 for the European theatre; these are test-profile decisions, not a universal definition of Holocaust scope. Emigration is never equated with survival. A Holocaust-related death must be marked as such in its evidence, and a conclusion cannot outrank its supporting identity match. Production fate criteria need their own review.

Partial dates and printed Hebrew dates are retained without claiming a calendar conversion. Residence is selected by the edition date; conflicting applicable residences cause an error instead of silently choosing one. Bibliographic `work_id` distinguishes an underlying work from its hosted copies; this pilot does not calculate an independent-source score.

Stored mention IDs survive regrouping. A whole-excerpt hash detects changed text. Exact offsets, repeated-occurrence selectors and image regions are intentionally not invented. Sources must eventually be connected to verified scans or stable archival locators before the full positional model is adopted.

This PR is a reviewable vertical slice, not stage 1 or stage 2 of the full rollout. It does not migrate all 238 editions, alter existing production models, or replace the existing site privacy projection. Places, organisations and comprehensive authority reconciliation remain follow-on work.

The source snapshot stays frozen for provenance. Each hand annotation in `build.py` carries its own language and script: the Hebrew opening names in mixed-language `cu-1934-02-02-i0408` are Hebrew; the other February 2 engagement notices are Hebrew and the remaining annotations are Yiddish. Name deduplication includes language and script.

The deterministic privacy presumption copies `pruzhany-svelte/src/lib/privacy/presumption.ts` into `living_presumption`, using recorded `as_of_year: 2026`. Death evidence, birth at least 110 years ago, printing at least 85 years ago, or a named voucher with a valid ISO day permits display, in that order; otherwise the person is held back. Evidence is aggregated across editions per person ID; public verdicts use the original mention bindings and only approved joins, independently of preview grouping. All real pilot people have reason `printed-in-old-source`; this is a display presumption, not a fate assertion.

The preview has 12 people, 2 events, 22 mentions, 6 facts and 1 relationship. The public projection has 13 records: original live site IDs and their own printed names, applying only approved joins. Pending joins remain visible in the reviewer preview. Marriage is stored only as `relationship-rachel-chaim`; both person-facing spouse lists derive from its single approval decision.

Removing `marriage` from vocabulary 0.1.0 is permitted because it has never been released; from the first release onward, issue #14 requires additions only, deprecation with a mapping, and no removals.
