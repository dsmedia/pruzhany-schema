# Working on pruzhany-schema

This repository holds the LinkML data model and the contracts both other repositories consume.
`pruzhany-steps` holds the record, the pipeline, the one plan (`PLAN.md`) and the shared decision
record (`decisions/`); `pruzhany-svelte` is the website, whose data steps generates. Read
[README.md](README.md) and [linkml/README.md](linkml/README.md) before changing the model. The model
must grow to cover every kind of data and exchange: physical pages, regions, lines, words and boxes;
semantic items and what they name; provenance (sources, readings, corrections); model exchanges; and
products (pruzhany-steps decision 214). Where a skill's or tool's defaults differ from this file, this
file holds.

## Standards

- Use an EHRI class where EHRI has one; otherwise a RiC-O term present in EHRI's RiC-O version;
  otherwise a local term in a profile, with its reason. Read the ontology in `standards/` before
  mapping, and run `bin/verify standards` for every mapping change.
- A new EHRI or RiC-O version enters only at the owner's word, as a new `standards/` file, with every
  mapping re-checked; a pinned list is never edited in place.
- Persons, life events and relations use the standards' shapes, with one identity per person across
  issues and tests of meaning. Before changing how any of them is identified, shaped or related, read
  the [standards foundation vetting](docs/design/2026-10-23-standards-foundation-vetting.md) and
  [ADR 0001](docs/adr/0001-which-standard-governs-what.md).

## Privacy and vocabulary

- **During the build-out, this public repository and its issues hold no facts about real people.**
  Notes, examples and evidence about real people go to pruzhany-steps; issues, design notes and tests here name the type,
  the field and its mapping, with fictional examples. What is already here stays (steps decision 214).
- New vocabulary types need the owner's approval in batches, each with its mapping, in the
  [approval record](docs/vocabulary-approvals.md); their real examples stay in pruzhany-steps and are
  shown to the owner privately. Until approval a fact stays `other` with its `proposed_type`. A
  released type is never removed or renamed.

## Contracts

- `linkml/schema/` is the one definition; change it first. Vocabulary enums start in
  `vocabulary/*.json`, whose generator writes `linkml/schema/vocabulary.yaml`. Regenerate with
  `linkml/generate.py` ([commands](linkml/README.md#commands)); generated files are never edited.
  Zod and Python twins stay in step with the definition and each other; their retained refinements
  remain the runtime validators.
- Keep the wire behaviour of pages and blocks, cross-references and external references; keep released
  vocabulary and snapshots, standards pins, the LLM extraction models and the sourced-entities pilot,
  which stays isolated from production models ([current site files](README.md#current-site-files)).
- Read the [bun-only test rules](.claude/rules/zod-tests.md) before adding or changing tests under `zod/`.

## Verify

`mise install && bun install --frozen-lockfile && bin/verify` (versions in `mise.toml`; bash, git and
uv too; [verification](docs/agents/verification.md)). `bin/verify <step>...` runs selected steps while
working; run it whole before merging. **A change here is checked against its consumers before it
merges**: the five pruzhany-svelte checks in [consumer checks](docs/agents/verification.md#consumer-checks),
run against this checkout's schema files. In pruzhany-steps, `site_shapes refresh` needs a clean
committed schema HEAD; preview generated differences separately until then.

## Issues

GitHub Issues in `dsmedia/pruzhany-schema` follow [issue tracker conventions](docs/agents/issue-tracker.md)
and the five [triage labels](docs/agents/triage-labels.md); domain docs follow [domain conventions](docs/agents/domain.md),
with contract design notes in `docs/design/`.
