# Stay close to EHRI and RiC-O

The owner's word of 20 October 2026: 'It's important to me we stick close to EHRI on the schema and to RiC. So we need to embed it.'

- Prefer an EHRI class where EHRI has one; otherwise use a RiC-O term present in EHRI's RiC-O version; otherwise declare a local term in a profile and give a reason.
- Read the ontology through `standards/` before mapping; never map from memory.
- Read and add a new EHRI or RiC-O version as a new `standards/` file only at the owner's word, then re-check every mapping. Never edit a pinned list in place.
- An owner-approved vocabulary addition names its mapping. Run the alignment check for every mapping change.
- **Persons, life events and relations are being vetted** (the owner's direction of 23 October 2026: shaped as the standard shapes them, one identity per person across issues, tests of meaning). Before changing how any of them is identified, shaped or related, read `docs/design/2026-10-23-standards-foundation-vetting.md` (the vetting, 23 October 2026) and `docs/adr/0001-which-standard-governs-what.md` (accepted by the owner, 23 October 2026).

# Working here

The LinkML definition (`linkml/schema/`; read `linkml/README.md`) is the rulebook: the one definition of the record's data. Generated from it today: a JSON Schema for each document, the Python field declarations (`pydantic/generated/`), the data dictionary and the public RDF view (`linkml/generated/rdf/`). Still written by hand, and still the validators: the Zod schemas (`zod/`) and the Python rules retained beside the generated fields. The owner's word of 29 October 2026, 'we can only be organized if we have a data model and contract for everything' (pruzhany-steps decision 214, decision 28 of its map), makes it over time the contract for every kind of data and every exchange, in layers: physical (pages, regions, lines, words and their boxes), semantic (items and what they name), provenance (sources, readings, corrections), the exchanges with models, and the products. Today it defines the website's documents. Change the definition first (an enum in `vocabulary/*.json`, whose generator writes `linkml/schema/vocabulary.yaml`), generate with `linkml/generate.py`, never edit what is generated, then keep the Zod and Python twins in step with it and with each other. The SvelteKit frontend (pruzhany-svelte) and pruzhany-steps consume this repository; the sourced-entities pilot is isolated from production models. See README.md for layout and consumer contract checks.

The site uses four issue documents and one shared record after the owner's switch of 24 October 2026. The old persisted article, content-unit, life-event, enrichment and edition-bundle contracts are retired. Pages and blocks live in the page modules, cross-references in site-common, and external references in shared; their wire behavior is preserved. Keep released vocabulary and snapshots, standards pins, LLM extraction models and the isolated pilot intact.

- **No test under `zod/` may need anything but bun.** pruzhany-svelte runs every `*.test.ts` under `zod/` through its `src/lib/schemas` symlink, with bun only (#15). Pilot and cross-language tests live beside their pilot and are run by `bin/verify`.
- **New vocabulary types are approved by the owner, in batches** ([approval record](docs/vocabulary-approvals.md)): each proposed type with its mapping. Its two or three real examples are kept in pruzhany-steps and shown to the owner privately, never put here. Until then a fact stays `other` with its `proposed_type`. A released type is never removed or renamed.
- **Nothing about real people goes into this public repository or its issues during the build-out** (the owner's word of 29 October 2026: 'Don't make repos public now because I don't want to air laundry in the build out'; pruzhany-steps decision 214, decisions 10 and 23 of its map). Working notes, examples and evidence about real people go to pruzhany-steps; an issue, design note or test here names the type, the field and its mapping, with fictional examples. What is already here stays as it is.
- **A change here is checked against its consumers before it merges**: pruzhany-svelte (`bun run format:check`, `bun run lint`, `bun run check`, `bun run test:run`, `bun run validate:data` against the changed schema files; a temporary copy can preserve its recorded submodule pin). In pruzhany-steps, `site_shapes refresh` requires a clean committed schema HEAD; preview generated differences separately until that commit exists. The Zod↔Pydantic lockstep runs here, in `bin/verify` (step `contract`), since pruzhany-press was retired on 2026-10-22.

`bin/verify` is the single verification entry point, including the standards alignment gate. Its header describes all nine steps and the pinned toolchain. The `entities` step checks sourced assertions in the current `SiteArchive` carrier; consumer checks run separately as described above.

## Agent skills

The plugin `mattpocock-skills` was set up here on 21 October 2026. Where one of its
skills and this file differ, this file holds.

### Issue tracker

GitHub Issues on `dsmedia/pruzhany-schema`. See `docs/agents/issue-tracker.md`.

### Triage labels

The plugin's five default labels, unchanged. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `GLOSSARY.md` and `docs/adr/` at the root, made when first needed. See
`docs/agents/domain.md`.
