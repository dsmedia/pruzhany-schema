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

`bin/verify` runs bun-only field tests and the shared Zod/Pydantic valid, missing,
unknown, malformed and wrong-field cases and round trips. Consumer validation
and the eventual committed schema pin are recorded in ticket 09's handoff.

At the round 3 handoff, all seven runnable `bin/verify` steps passed: 38 Zod tests,
117 Pydantic models, 44 twins, 342 site cases and 106 round trips. The `scan`
step cannot run here because gitleaks is absent. The Svelte consumer was tested
through a temporary symlink to this worktree: 2,349 unit tests, a clean
1,399-file typecheck, data validation for 238 issues, 27 privacy/leak tests and
61 browser tests pass. Its single CI command stopped on Vitest resolving four
schema test paths outside the consumer; temporarily preserving symlinks let
the complete test suite pass, then the remaining CI steps passed separately.
Both temporary settings are restored at handoff. The committed consumer pin
and the steps schema refresh await the session's schema commit.

Round 3b verification: all seven runnable `bin/verify` steps pass, including
56 Zod tests, 425 shared site cases, 122 round trips, standards alignment and
vocabulary generation checks. The default command still stops at `scan`
because gitleaks is absent. Opaque IDs, both field suffixes, empty identifiers,
wrong suffixes and ASCII/Unicode whitespace are exercised in both runtimes.
Steps passes ruff, format, mypy and all 11 touched writer tests; the site passes
all 10 touched tests using an opaque judgement ID against this schema worktree.
Its temporary schema symlink was restored. No schema refresh, commit or paid
call was made. Logs are under `/tmp/t09/round3b/`.
