# Cross-edition entity identity (adopting Impresso + open NIL question)

**Status:** finalized decisions in this doc. Open questions live in [#1](https://github.com/dsmedia/pruzhany-schema/issues/1) (NIL clustering) and [#3](https://github.com/dsmedia/pruzhany-schema/issues/3) (type-taxonomy extensions).

**Date:** 2026-04-25

---

## Problem

Pruzhany has ~200 weekly newspaper editions in the source corpus (1935–1939). A person mentioned in 50 editions today produces 50 separate `EnrichedPerson` records — one per edition's enrichment file — because edition-scoping is enforced at the schema level (see [pruzhany-press#48](https://github.com/dsmedia/pruzhany-press/issues/48)).

That edition-scoping is intentional and correct: each edition bundle must be self-contained for the SvelteKit consumer to load. What's missing is the **cross-edition identity layer**: how does a consumer know "this person also appears in 49 other editions?" — without scanning every edition's enrichment file at read time?

Two consumers care:

- **`pruzhany-svelte`** needs to render "appears in N editions" badges and cross-edition jump links in the detail panel.
- **`pruzhany-press`** needs to cluster repeat mentions during ingestion so the corpus stays browseable as new editions land.

Both depend on a stable, schema-level convention for cross-edition identity. This doc is that convention.

---

## Decision: adopt the Impresso `entities.schema.json` shape

**Impresso** ([impresso-project.ch](https://impresso-project.ch)) is the canonical reference for historical-newspaper NLP. Its `entities.schema.json` defines a mature mention-encoding format refined over six years across HIPE-2020, HIPE-2022, and HIPE-2026 shared tasks.

We adopt the following Impresso conventions wholesale:

### 1. Wikidata QID linking with `NIL` literal

Each entity mention carries a `wkd_id` field:

- For Wikidata-known entities: the QID, e.g., `Q12345`.
- For unlinkable entities: the literal string `"NIL"` (Quaero/HIPE convention; *not* `null`).

**Why:** all editions mentioning the same Wikidata-known person automatically share the same `wkd_id`. Cross-edition clustering for these entities is trivial — group by QID. This is the easy half of the cross-edition problem, and Impresso solves it.

For Pruzhany, only public figures (rabbis with Wikidata entries, politicians of the era, well-known towns) benefit directly. Most residents are NIL — addressed under "Open question" below.

### 2. Self-describing mention IDs

Mention IDs are pipe/colon-separated tuples:

```
{ci_id}:{lOffset}:{rOffset}:{type}:{ner_model}[|{nel_model}]
```

The `|{nel_model}` half is optional and omitted when a single model performs both NER and NEL. For Pruzhany's current pipeline (Gemini doing both), the example below has no pipe; when separate NER and NEL models are used, the pipe-and-NEL-model is appended.

Example (single-model, Pruzhany today):

```
pruzhany-1938-12-16-a-i5763:120:148:pers.ind:gemini-3-flash-preview
```

**Why:** running the same NER model twice produces identical IDs, so dedup is trivial. Two models running on the same content item coexist without collision. Consumers can decompose the ID into span + type + model without DB access.

### 3. Fine-grained type taxonomy

Adopt the full HIPE/Impresso type hierarchy: `pers.ind`, `pers.coll`, `pers.ind.articleauthor`, `loc.adm.town`, `loc.adm.reg`, `loc.adm.nat`, `org.adm`, `org.ent.pressagency`, `prod.media`, `time.date.abs`, etc. ([full list](https://github.com/dsmedia/pruzhany-svelte/blob/master/docs/impresso/05-entities-and-ner.md)).

**Why:** don't reinvent the taxonomy. The HIPE typology is retro-compatible with Quaero, has six years of annotator buy-in, and includes the sub-types that matter for newspaper text — for example `pers.ind.articleauthor` for bylines, and `org.ent.pressagency` with a closed list of canonical agencies.

### 4. Person components (`name`, `title`, `function`)

For `pers.ind` mentions, decompose into:

- `name` — the bare name
- `title` — honorific (Rabbi, Mr., Dr.)
- `function` — occupation/role-in-context (midwife, baker, partisan)

**Why:** "Rabbi Chaim Feldman, the spiritual leader" should not be a single opaque blob. Components let downstream tools work on the individual parts (search by occupation, render by name, etc.).

### 5. Manifest-based provenance

Each run produces a manifest with `model_id`, `code_git_commit`, `prompts_sha`, and similar reproducibility fields. The existing `runs/{id}` doc in `pruzhany-press` is a proto-manifest; this doc commits to filling in the rest over time.

**Why:** entity work is iterative — re-run NER, re-run NEL, re-run translation. The manifest lets a future developer reconstruct exactly what produced any given record, and lets a `diff` between two runs be semantically meaningful.

### Reference

For the full upstream schema and Pruzhany-specific adoption rationale (with concrete examples), see (in the `pruzhany-svelte` repo, kept there because it predates this schema repo's `docs/`):

- [`docs/impresso/05-entities-and-ner.md`](https://github.com/dsmedia/pruzhany-svelte/blob/master/docs/impresso/05-entities-and-ner.md) — full upstream schema reference (~230 lines).
- [`docs/impresso/12-crosswalk-to-pruzhany.md`](https://github.com/dsmedia/pruzhany-svelte/blob/master/docs/impresso/12-crosswalk-to-pruzhany.md) — Impresso ↔ Pruzhany alignment with concrete adoption suggestions (canonical IDs, mention IDs, manifest).

---

## Current schema state and migration scope

The Impresso adoption above is a **target**. The current Zod schemas in this repo (`zod/`) predate this decision and diverge from the target in named ways. **This PR adds no schema type changes** — only the design intent and the open-question issues. Each migration below is a separate PR, with the contract test confirming Zod ↔ Pydantic parity at every step.

| Concern | Current schema | Impresso target | Migration action |
|---|---|---|---|
| Location Wikidata field | `wikidata_id: z.string().optional()` (`zod/enrichment.schema.ts` line 134) | `wkd_id: string` (required; `"NIL"` literal for unlinkable) | Rename + tighten in a future PR |
| Person Wikidata field | absent (only generic `external_references`) | `wkd_id: string` (required; `"NIL"`) | Add in a future PR |
| Event Wikidata field | absent (only generic `external_references`) | `wkd_id: string` (required; `"NIL"`) | Add in a future PR |
| Person components | `name`, `occupation` (no `title`) | `name`, `title`, `function` | Add `title`; rename `occupation` → `function` |
| Type taxonomy | Flat enum (`town`, `shtetl`, `ghetto`, `camp`, `massacre_site`, …) | Dotted hierarchy (`loc.adm.town`, `loc.fac`, …) **plus** Pruzhany subtypes (see #3) | Migrate after #3 resolves |
| Mention IDs | absent (entities carry no per-mention identity yet) | `{ci_id}:{lOffset}:{rOffset}:{type}:{ner_model}[\|{nel_model}]` | Add in a future PR (tied to NEL pipeline work in `pruzhany-press#13`) |

Migration follows an **additive-first** pattern: new optional fields land before any tightening to required, so the two consumers (`pruzhany-svelte`, `pruzhany-press`) can adopt at their own cadence.

---

## Open questions

Two design questions remain open. Both block parts of the migration above.

### NIL clustering across editions — [#1](https://github.com/dsmedia/pruzhany-schema/issues/1)

The decisions above cover Wikidata-linkable entities cleanly. But for Pruzhany, **most residents are NIL** — they will never have a Wikidata entry. Impresso emits `wkd_id: "NIL"` and stops there.

Sub-questions tracked in #1:

- Cluster mechanism — separate `cluster_id` field, local QID-equivalents (e.g., `PRU-Q123`), or lazy surface-form fingerprinting?
- Minimum NIL assertions to make a person stably referenceable.
- Human-review surface for ambiguous NIL matches.
- Frontend UX intent as a design constraint (see below).

### Pruzhany type-taxonomy extensions — [#3](https://github.com/dsmedia/pruzhany-schema/issues/3)

Adopting Impresso's general taxonomy doesn't address the Pruzhany-specific types currently in `LocationTypeSchema`: `shtetl`, `ghetto`, `camp`, `massacre_site`, `deportation_point`, `forest`. These are domain-meaningful for Holocaust-era Yiddish content and shouldn't collapse into Impresso's coarser equivalents.

Sub-questions tracked in #3:

- Subtype under Impresso (`loc.fac.ghetto`, `loc.adm.town.shtetl`, …)?
- Parallel `pruzhany_type` field alongside Impresso `type`?
- Use Impresso's `comp.qualifier` escape hatch?
- Petition Impresso/HIPE to extend upstream?

This doc will be updated when both questions land — the issues are the working space; this doc captures the conclusions.

---

## Frontend UX intent (design constraint on the open question)

Whatever NIL-clustering mechanism we pick must support, cheaply, the following consumer-side operations:

1. **"Appears in N other editions" badge** — given an entity ID, count distinct editions in O(1) or O(N editions) without loading every enrichment file.
2. **Cross-edition jump** — from a person's detail panel in edition A, navigate to edition B where they also appear.
3. **Cross-corpus search** — "find all content units across all editions referencing X" — possibly handled by a separate index, but the schema must make it computable.

Implication: cross-edition identity must be *expressible at the schema level*, not deferred to consumer-side fuzzy matching.

---

## Versioning and cross-repo consumption

This schema is consumed as a git submodule by `pruzhany-svelte` and `pruzhany-press`. Submodule pins should bump in lockstep for breaking changes; additive changes (like this doc, and any new optional fields) can be adopted at each consumer's pace.

Schema changes follow contract-first discipline:

1. Propose change in this repo (issue or PR).
2. Run contract test (Zod ↔ Pydantic parity).
3. Land on `main`.
4. Bump submodule pin in each consumer.

---

## References

- **Pipeline tracking:** [`pruzhany-press#13`](https://github.com/dsmedia/pruzhany-press/issues/13) — entity-resolution algorithm + eval set.
- **Open: NIL clustering:** [`#1`](https://github.com/dsmedia/pruzhany-schema/issues/1) in this repo.
- **Open: type-taxonomy extensions:** [`#3`](https://github.com/dsmedia/pruzhany-schema/issues/3) in this repo.
- **Upstream Impresso reference:** [`docs/impresso/05-entities-and-ner.md`](https://github.com/dsmedia/pruzhany-svelte/blob/master/docs/impresso/05-entities-and-ner.md) in `pruzhany-svelte`.
- **Impresso ↔ Pruzhany crosswalk:** [`docs/impresso/12-crosswalk-to-pruzhany.md`](https://github.com/dsmedia/pruzhany-svelte/blob/master/docs/impresso/12-crosswalk-to-pruzhany.md) in `pruzhany-svelte`.
- **Historical framing:** [`docs/plans/2026-04-17-data-model-review-prompt.md`](https://github.com/dsmedia/pruzhany-svelte/blob/master/docs/plans/2026-04-17-data-model-review-prompt.md) §4–5 in `pruzhany-svelte` — the original questions this doc answers.
