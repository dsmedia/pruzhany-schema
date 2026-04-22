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

## License

TBD.
