# Site-content 1.0.0 release, 2026-10-25

The owner approved the proposed subtypes and subjects as they stand on
2026-10-25 (pruzhany-steps decision 164, item 1; fresh-start ticket 02). This
schema-only change releases site-content **1.0.0** with **21 subtypes** and
**11 subjects**. Counts were read from `vocabulary/site-content.json` and its
generated `vocabulary/released/site-content-1.0.0.json` snapshot in this run.
Their identifiers exactly match the private approval sheet's proposal headings.
Labels, parents, definitions, mappings and original `added_in` values are
unchanged from the pre-release vocabulary. Existing shape bindings and Impresso
types are unchanged too. Sourced-entities and its historical releases are intact.

The approval sheet's full routing table still has **38 unresolved values**,
counted from its nonempty unresolved column in this run. They stay `other` with
their exact `proposed_type` in the producer's retained records. This release adds
no subtype or subject for them and performs no data migration. The two existing
title-type concepts remain proposed: their entries say `status: proposed`, and
`released_groups` names only `content_item_subtypes` and `subjects`.

`vocabulary/generate.py` generates both language modules and the separate
site-content snapshot. The checker requires the current snapshot to match the
source vocabulary, a release date and approval record, a matching profile
version, and preservation of historical identifiers. Site-content and
sourced-entities snapshots are checked independently. Tests exercise both
release lifecycles, snapshot mismatch/missing cases, retained identifiers,
approval metadata and proposed concepts.

The released labels have the same meaning as the proposal. Both contracts
explicitly accept the old `0.1.0` content-document stamp alongside `1.0.0`, using
the generated version set from `compatible_versions` plus the current version.
Unknown stamps and unknown subtype/subject identifiers remain invalid. Shared
contract fixtures cover these cases in both runtimes. The new writer must stamp
the generated current version; retaining the old stamp permits validation of the
site's existing documents before that separate refresh.

## Sources read on 2026-10-25

- Local pinned ontology documentation: `standards/README.md`,
  `standards/ehri-0.2.0.json`, `standards/rico-1.1.json` and the relevant entries in
  `standards/rico-1.1-axioms.json`. No standard pin was changed. Subtypes remain
  local SKOS concepts typed `rico:DocumentaryFormType`, reached through
  `rico:hasDocumentaryFormType`; subjects remain local SKOS concepts reached
  through `rico:hasOrHadSubject`. The local reasons remain beside every mapping
  in the vocabulary and profile. Title and shape mappings are retained.
- [Zod, Defining schemas / Enums](https://zod.dev/api#enums): the generated
  version schema uses the existing `z.enum` API, tested with the repository's
  locked Zod 4.3.5, rather than changing dependencies.
- [Python 3.11, typing.Literal](https://docs.python.org/3.11/library/typing.html#typing.Literal):
  the generated Python version alias lists the same permitted string values.
- [Bun, bun install](https://bun.sh/docs/pm/cli/install) and
  [Global cache](https://bun.sh/docs/pm/global-cache): frozen installs and the
  task-local `BUN_INSTALL_CACHE_DIR` used for verification.
- [uv, Environment variables](https://docs.astral.sh/uv/reference/environment/#uv_cache_dir):
  the task-local `UV_CACHE_DIR` used for verification.

## Verification

The schema and consumer commands below were run locally. They do not establish
a GitHub runner result. No CI workflow was changed.

The observed local toolchain was Bash 5.2.21, git 2.43.0, Bun 1.3.11,
Node.js 22.22.0, uv 0.11.32, gitleaks 8.24.3, system Python 3.13.17 and
uv-selected Python 3.11.17. Schema dependencies were Prettier 3.8.0,
TypeScript 5.9.3, Vitest 4.1.9, Zod 4.3.5, Pydantic 2.12.5,
rdflib 7.1.4 and jsonschema 4.26.0. The consumer used its own frozen lock,
including Svelte 5.56.4, SvelteKit 2.69.1, svelte-check 4.7.1,
ESLint 9.39.2 and sharp 0.34.5. These values came from version commands and
installed package metadata in this run. No browser or model call was needed.

The existing schema workflows, read 2026-10-25, install Bun 1.3.11 and
uv 0.11.13 for `bin/verify`'s non-scan steps; those commands select Python 3.11
and their pinned Python dependencies. The scan workflow installs gitleaks
8.24.3. The observed local uv version differs from CI's pin. No GitHub check
was run here, and this record makes no fresh-runner claim.

The temporary consumer was copied from `/home/user/pruzhany-svelte`, without
its git metadata or generated/dependency directories, and installed with
`bun install --frozen-lockfile`. Its schema submodule was first linked to this
working folder. Vitest could not load its schema test files through that external
link (`/@fs/...` module paths), so the same schema source bytes were copied inside
the temporary submodule directory, without schema `node_modules`. No test or
check was filtered, disabled or changed. The complete unit command was rerun and
passed. A byte comparison confirmed the consumer's tracked source and data
matched the original outside the replaced schema submodule.

| Acceptance check | Command run | Result |
| --- | --- | --- |
| Release through generator | `python3 -I -B vocabulary/generate.py` | Generated both language modules and `released/site-content-1.0.0.json`. |
| Snapshot and history | `python3 -I -B vocabulary/check.py` | Passed. |
| Exact generated bytes | `python3 -I -B vocabulary/generate.py --check` | Passed. |
| Named mappings | `python3 -I -B standards/check_alignment.py` | Passed against pinned terms and declared local reasons. |
| Schema verification | `bin/verify` | Passed all steps: scan, zod, pydantic, contract, pilot, standards, vocabulary, entities. The vocabulary suite passed 44 tests. |
| Consumer formatting | `bun run format:check` | Passed. |
| Consumer lint | `bun run lint` | Passed with the existing warning ceiling unchanged. |
| Consumer typecheck | `bun run check` | Failed with the same three pre-existing media-fixture errors reproduced on unmodified schema HEAD. |
| Consumer tests | `bun run test:run` | Passed: 79 files, 3,999 tests, including all schema tests. |
| Consumer data | `bun run validate:data` | Passed: 238 issues; the existing dimension checker passed, retaining its reports for absent images. |
| Patch whitespace | `git diff --check` | Passed. |

For the baseline typecheck, `git archive HEAD` exported the unmodified schema at
`e8a0e3560de662a499420a61c4244f9bfa250c32`. It temporarily replaced the schema
inside the consumer copy, and `bun run check` was run again. Its diagnostics
matched the released working schema exactly: `tests/leaks/sourced-facts.leak.test.ts`
uses `lang` at lines 86 and 87 and `bucket` at line 93, fields absent from the
current media types. `zod/media.schema.ts` and `pydantic/media.py` are unchanged
from that HEAD. This consumer fixture mismatch remains open; no media contract
or consumer test was altered for this vocabulary release.

The temporary consumer, baseline archive and task-local caches were removed
after these checks. The original consumer checkout was not changed. The schema
change is left uncommitted, with its message in the ignored
`.codex-commit-message.txt` for the session to commit. No tag, push or external
release was made.

The remaining cross-repository acceptance work belongs to the later run:
refresh steps from the committed schema, stamp the new writer version, update
steps' decision record and pending-decision wording, then bump the site's schema
pin and regenerate its data through the writer. This schema-only release does
not perform those writes.

## Files changed

- `.gitignore` (ignore the session commit-message handoff), `README.md`,
  `vocabulary/README.md`, `standards/README.md`,
  `docs/design/2026-10-22-site-files.md` and this release record.
- `vocabulary/site-content.json`, `vocabulary/site-content.profile.ttl`,
  `vocabulary/generate.py`, `vocabulary/check.py`, `vocabulary/test_vocabulary.py`
  and generated `vocabulary/released/site-content-1.0.0.json`.
- `zod/content-item.schema.ts`, `pydantic/content_item.py`, generated
  `zod/site-content.vocabulary.ts` and `pydantic/site_content_vocabulary.py`.
- `tests/contract/site-shapes.fixtures.json` (released/unknown stamps and
  unresolved subtype/subject checks).
