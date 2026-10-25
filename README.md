# pruzhany-schema

Shared data schemas for the [Pruzhany Digital Archive](https://pruzhanychronicles.org) — an interactive archive of the Yiddish weekly *Pruzaner Sztyme* (1935–1939).

Consumed by the SvelteKit frontend through its pinned git submodule and by pruzhany-steps through exports recorded from a clean schema commit. Zod and Pydantic define the two language contracts in the same repository.

## Layout

```
zod/       TypeScript Zod schemas (frontend model)
pydantic/  Python Pydantic schemas (pipeline model)
```

Schema modules cover the four issue documents (pages, content items, mentions and life events), one shared record of people, families, places, organizations, events and sourced assertions, shared reference types, and the multi-edition catalog. LLM extraction contracts remain separate from persisted site documents.

## Cross-language contract

Zod and Pydantic models are kept in lock-step. When you change a type on one side, update its counterpart on the other — a contract test compares the two via JSON Schema to catch drift.

## Verify

`bin/verify` is the one verify entry point, and CI runs all eight steps (`gitleaks.yml` runs `scan`, `ci.yml` the rest): history secret scanning; Zod tests, strict typechecking and formatting; Pydantic model loading and JSON Schema emission; the cross-language contract; the isolated pilot; standards alignment; released vocabulary and generation checks; and sourced-entity parity in the current `SiteArchive` carrier, including its exported JSON Schema. The toolchain is pinned in `package.json`/`bun.lock` to pruzhany-svelte's versions. The Zod↔Pydantic lockstep check moved here from pruzhany-press on 2026-10-22.

## License

TBD.

The [2026-04-25 cross-edition design](docs/design/2026-04-25-cross-edition-entities.md) is historical; [ADR 0001](docs/adr/0001-which-standard-governs-what.md) settles identity across issues.
The [2026-10-19 people, facts and sources proposal](docs/design/2026-10-19-people-facts-and-sources.md) includes the decisions and changes of 20 October.
The [vocabulary approval record](docs/vocabulary-approvals.md) is the continuing channel for the owner's batches and keeps the release approval history.

## Current site files

The owner approved the site switch on 2026-10-24. `content-item.schema.ts` defines content
items with printed and supplied titles, Impresso types, subtypes, subjects and printed
sections. `site-common.schema.ts` supplies printed addresses, authorship and translations
pinned to their source text. `shared-record.schema.ts` reuses production sourced facts,
names, sources, fate and standing for one shared record. `site-issue.schema.ts` adds
per-issue mentions and life events, plus checks of the four documents and their shared
references. Each module has a Pydantic twin.

`PagesData`, `Page` and `Block` live in `zod/page.schema.ts` and `pydantic/page.py`;
`CrossReference` lives in the site-common modules, and `ExternalReference` in the
shared modules. Their wire behavior is unchanged, including existing field names,
defaults and runtime-specific null handling. The old article, content-unit,
life-event, enrichment and edition-bundle persisted models and exports are retired;
the mixed `pydantic/project_output.py` module is gone. Released sourced vocabulary,
its compatibility helpers, `llm_output.py` and `bbox_review.py` remain available.

`vocabulary/site-content.json` is **1.0.0, released 2026-10-25** for the owner's
approved subtypes and subjects, separate from released sourced-entities 1.2.0.
Title types remain proposed. See the [release record](docs/design/2026-10-25-site-content-release.md)
and [contract and preservation notes](docs/design/2026-10-22-site-files.md).
`bin/verify contract` checks fictional valid/invalid cases in both runtimes and round trips.

The [sources contract](docs/design/2026-10-24-sources-implementation.md) adds holders,
source ancestry and citation fields. Both twins read the advisory per-kind rules
from `vocabulary/citation-requirements.json`; missing evidence is reported separately
from the reference checks that refuse invalid records.

The [checked-English addition](docs/design/2026-10-23-checked-english.md) adds an
optional independent check to each supplied title and translation, preserving
its original source and author. Exact-byte bindings and field-specific judgement
identifiers are shared by both language contracts.

The [one-life-event contract](docs/design/2026-10-23-one-life-event.md) moves the
event's main people (`main_people`), parts and dates into the shared record; issue entries keep
only the event id and their content items. The round-4 writer and site now use this
contract. Event parts, memorial and supplied names are in released vocabulary 1.2.0;
semantic fixtures run in `contract`, and tests that
read RiC-O's pinned axioms run in `standards` outside the bun-only `zod/` tree.
Round 4d reuses released engagement, locates new notice citations without rewriting
older citations, and refuses a content item assigned to two life events.

## Issue 14 pilot

The [sourced-entities pilot](pilots/sourced-entities/README.md) is an isolated,
executable review of corpus-wide people, role-bearing mentions and sourced
assertions aligned with EHRI 0.2.0 / RiC-O 1.1; its terms also exist in RiC-O 1.0.2. Start with its
[generated review](pilots/sourced-entities/generated/review.md).
Run it with `bin/verify zod pydantic pilot standards`. The pilot remains isolated from the current site contracts.
