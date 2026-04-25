# Cross-edition entity identity (adopting Impresso + open NIL question)

**Status:** finalized decisions in this doc. Open NIL-clustering question lives in [#1](https://github.com/dsmedia/pruzhany-schema/issues/1).

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
{ci_id}:{lOffset}:{rOffset}:{type}:{ner_model}|{nel_model}
```

Example:

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

## Open question: NIL clustering across editions

The decisions above cover Wikidata-linkable entities cleanly. But for Pruzhany, **most residents are NIL** — they will never have a Wikidata entry. Impresso emits `wkd_id: "NIL"` and stops there.

This is the residual novel design question for Pruzhany, tracked as a live discussion in **[#1](https://github.com/dsmedia/pruzhany-schema/issues/1)**:

- Cluster mechanism — separate `cluster_id` field, local QID-equivalents (e.g., `PRU-Q123`), or lazy surface-form fingerprinting?
- Minimum NIL assertions to make a person stably referenceable.
- Human-review surface for ambiguous NIL matches.
- Frontend UX intent as a design constraint (see below).

This doc will be updated when those decisions land — the issue is the working space; this doc captures the conclusions.

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
- **Open NIL-clustering decisions:** [`#1`](https://github.com/dsmedia/pruzhany-schema/issues/1) in this repo.
- **Upstream Impresso reference:** [`docs/impresso/05-entities-and-ner.md`](https://github.com/dsmedia/pruzhany-svelte/blob/master/docs/impresso/05-entities-and-ner.md) in `pruzhany-svelte`.
- **Impresso ↔ Pruzhany crosswalk:** [`docs/impresso/12-crosswalk-to-pruzhany.md`](https://github.com/dsmedia/pruzhany-svelte/blob/master/docs/impresso/12-crosswalk-to-pruzhany.md) in `pruzhany-svelte`.
- **Historical framing:** [`docs/plans/2026-04-17-data-model-review-prompt.md`](https://github.com/dsmedia/pruzhany-svelte/blob/master/docs/plans/2026-04-17-data-model-review-prompt.md) §4–5 in `pruzhany-svelte` — the original questions this doc answers.
