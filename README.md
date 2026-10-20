# pruzhany-schema

Shared data schemas for the [Pruzhany Digital Archive](https://pruzhanychronicles.org) — an interactive archive of the Yiddish weekly *Pruzaner Sztyme* (1935–1939).

Consumed by a SvelteKit frontend (Zod) and a Python extraction pipeline (Pydantic) as a git submodule, so any change to the data contract is visible to both sides in the same commit.

## Layout

```
zod/       TypeScript Zod schemas (frontend model)
pydantic/  Python Pydantic schemas (pipeline model)
```

Schema modules cover: shared types (bboxes, external refs, Holocaust fate), pages and blocks, content units, enrichment entities (people, locations, events, topics), life events, edition bundles, and a multi-edition catalog.

## Cross-language contract

Zod and Pydantic models are kept in lock-step. When you change a type on one side, update its counterpart on the other — a contract test compares the two via JSON Schema to catch drift.

## Verify

`bin/verify` is the one verify entry point, and CI runs it verbatim (`gitleaks.yml` runs its `scan` step, `ci.yml` the rest): a gitleaks history scan, the `zod/*.test.ts` suite plus a strict typecheck (toolchain pinned in `package.json`/`bun.lock` to pruzhany-svelte's versions), and a load-and-emit-JSON-Schema check of every Pydantic model. The Zod↔Pydantic drift gate lives in the private pruzhany-press repo; run it against this checkout with `just test-contract`.

## License

TBD.

## Issue 14 pilot

The [sourced-entities pilot](pilots/sourced-entities/README.md) is an isolated,
executable review of corpus-wide people, role-bearing mentions and sourced
assertions aligned with EHRI 0.1.1 / RiC-O 1.0.2; its terms are checked against both RiC-O 1.0.2 and 1.1. Start with its
[generated review](pilots/sourced-entities/generated/review.md).
Run it with `bin/verify zod pydantic pilot standards`. Existing production models are unchanged.
