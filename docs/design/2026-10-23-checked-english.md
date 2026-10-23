# An independent later check of English

Ticket 09 round 3 implements the accepted checked-English proposal. Supplied
titles and translations may carry `checked_against`; absence leaves the existing
contract unchanged. A present check is complete, strict, and non-null. It names
the content item, SHA-256 of exact reading and English UTF-8 bytes, the retained
judgement and its file SHA-256, and the checking agent's attribution. No whitespace
or Unicode normalisation is permitted. Original `based_on` and `attribution`
remain separate and unchanged.

`judgement_id` is an opaque, non-empty identifier without whitespace, followed
by `:title` for a supplied title or `:text` for a translation. The field suffix
prevents one judgement being presented as a check of the other field, even for
equal text. For example, `J42:title` and `urn:archive:judgement/J42#review:text`
are valid. Repository paths, dates and fragment syntax are not part of the
shared contract. The steps writer still emits
`corrections/english-choice/YYYY-MM-DD.json#KEY:title` or `:text`.
The producer verifies completed retained evidence, mutually unique pairing,
program identity, hand selection and exact English before emitting a check.
Post-judgement corrections need their own independent check. A consumer accepts
it only for the named item and matching reading and English digests, calculated
once when loading. File integrity is the producer's responsibility; a public
browser does not fetch the private judgement.

Read on 23 October 2026: `standards/README.md`, `standards/ehri-0.2.0.json` and
`standards/rico-1.1.json`. Of the nine new standard mappings, keep only the
three concepts the files record: `checked_against` is a `rico:Activity`, its
`attribution` names an `ehri:Agent`, and `judgement_id` references the retained
`rico:Record`. These describe the stored check and its references; they do not
claim that the site stores a separate RDF graph.

Drop the separate performed-by, subject, creation-date, Date, identifier and
source-of-information mapping entries. The files do not record those relation
or date nodes; the checking agent and judgement reference are already covered
by the retained concepts. In particular, `attribution.on` dates the check,
not the creation of the judgement record.

Keep the exact-byte binding and three digests as local terms:
`pc:site_checked_against_text`, `pc:site_reading_sha256`,
`pc:site_english_sha256`, `pc:site_judgement_sha256`. Each is
declared with its scope and one-line reason in `vocabulary/site-content.profile.ttl`
and mapped in `vocabulary/site-content.json`, using the existing
`https://pruzhany.org/ns/sourced-entities#` namespace. These are needed because
neither pinned ontology expresses the exact reading, English and judgement
byte bindings stored in the check. They extend the proposed site profile,
without changing the released vocabulary or pinned standards.

`bin/verify` exercises field-specific checks and shared Zod/Pydantic valid,
missing, unknown, malformed and wrong-field cases and round trips. The session
committed this change in `094ae61`, merged the same tree as `9a21339`, pinned the
site in `fcdc1c1`, and refreshed the steps shapes in `e5ee79f4`. The site then
rewrote all 238 issues in `f94a99b`: 434 checks, all recomputed successfully; every
translation on the five hand-made dates shows. The old pre-commit symlink and
fixture results are superseded by this integration. The real-data site CI exposed
a stale leak-test title expectation, repaired in ticket 09 round 3c; it was not a
schema or person-page display mismatch.

Round 3c moves the typed non-null validator onto the base that declares
`checked_against`, retaining the narrower title/translation suffix checks.
`pc:site_checked_against_text` now follows the adjacent NamedIndividual/comment
pattern: it names the application binding, rather than asserting an RDF object
property that the application does not store. Its registered one-line reason is
unchanged. The three digest properties retain their datatype-property declarations.
The Zod data contract and generated vocabulary are unchanged by these cleanups.

The [verification record](2026-10-23-checked-english-verification.json) contains
this worktree's current counts: all seven runnable verification steps pass,
including 56 Zod tests, 117 Pydantic models, 44 twins, 425 shared site cases and
122 round trips. Default `bin/verify` stops at `scan` because gitleaks is absent.
These two cleanups were committed by the session as the commit after `9a21339`;
the site pins it and the steps' shapes are refreshed from it.
