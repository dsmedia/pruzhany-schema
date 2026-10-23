# Stay close to EHRI and RiC-O

The owner's word of 20 October 2026: 'It's important to me we stick close to EHRI on the schema and to RiC. So we need to embed it.'

- Prefer an EHRI class where EHRI has one; otherwise use a RiC-O term present in EHRI's RiC-O version; otherwise declare a local term in a profile and give a reason.
- Read the ontology through `standards/` before mapping; never map from memory.
- Read and add a new EHRI or RiC-O version as a new `standards/` file only at the owner's word, then re-check every mapping. Never edit a pinned list in place.
- An owner-approved vocabulary addition names its mapping. Run the alignment check for every mapping change.
- **Persons, life events and relations are being vetted** (the owner's direction of 23 October 2026: shaped as the standard shapes them, one identity per person across issues, tests of meaning). Before changing how any of them is identified, shaped or related, read `docs/design/2026-10-23-standards-foundation-vetting.md` (the vetting, 23 October 2026) and `docs/adr/0001-which-standard-governs-what.md` (proposed until the owner agrees).

# Working here

This repo shares schemas between the Pruzhany Digital Archive's SvelteKit frontend and Python extraction pipeline. Keep the two language contracts in step; the sourced-entities pilot is isolated from production models. See README.md for layout and consumer contract checks.

- **No test under `zod/` may need anything but bun.** pruzhany-svelte runs every `*.test.ts` under `zod/` through its `src/lib/schemas` symlink, with bun only (#15). Pilot and cross-language tests live beside their pilot and are run by `bin/verify`.
- **New vocabulary types are approved by the owner, in batches** (#16): each proposed type with two or three real examples and its mapping. Until then a fact stays `other` with its `proposed_type`. A released type is never removed or renamed.
- **A change here is checked against its consumers before it merges**: pruzhany-svelte (`bun run test:run`, `bun run check`, `bun run validate:data` with its submodule pointed at the branch). The Zod↔Pydantic lockstep runs here, in `bin/verify` (step `contract`), since pruzhany-press was retired on 2026-10-22.

`bin/verify` is the single verification entry point, including the standards alignment gate. Its header describes the steps, pinned toolchain and private consumer drift gate.

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
