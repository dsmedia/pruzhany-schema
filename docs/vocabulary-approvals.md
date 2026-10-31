# Vocabulary approvals

This document is the continuing channel and record for the owner's vocabulary
approvals. It replaces the completed stage-1 issue as a place to send future
batches. The contract itself is in [`vocabulary/`](../vocabulary/README.md);
[ADR 0001](adr/0001-which-standard-governs-what.md) governs which standard applies.

## Propose and approve a batch

After a research round, collect proposed types into one batch. For each type,
give its identifier, definition, two or three real examples and mapping. Show
real examples and their English to the owner privately; do not put people's
research or the private approval sheet in this public repository.

The owner says yes or no to the batch in one message. Until approval, retain a
fact as `other` with its `proposed_type`. A session cannot turn a proposal into
an approved type merely by implementing it or passing tests.

For every approved type, prefer an EHRI class; otherwise use a RiC-O term in
EHRI's pinned RiC-O version; otherwise declare a local term in the profile and
explain why. Read the pins in [`standards/`](../standards/README.md), rather than
copying a version from the historical decisions below. New pins need the
owner's word and every mapping must then be checked again.

Record the owner's answer, date, batch, private evidence location and mapping
here or in a dated design note linked here. Update the vocabulary's approval
metadata, version, release snapshot and generated contracts together. Never
remove or rename a released identifier; deprecations retain it and name its
replacement. Run `bin/verify` and the affected consumers' checks as
[`CLAUDE.md`](../CLAUDE.md) requires. Approval of vocabulary does not itself
approve publication of evidence or private notes.

## Approval history

- **20 October 2026 — standing process and vocabulary 1.0.0.** The owner chose
  the standards-first mapping rule and batch approval with real examples. The
  owner then approved the recommended types in advance for that release and
  permitted the rollout under its verification gates. That permission applied
  to that rollout; future additions still need their own batch approval.
  The owner also required existing site IDs to stay.
- **22 October 2026 — vocabulary 1.1.0.** The owner's word added the claim
  status `proposed`, retained without publication. The approval is recorded in
  [`released/1.1.0.json`](../vocabulary/released/1.1.0.json).
- **23 October 2026 — vocabulary 1.2.0.** After reviewing printed notices and
  their English, the owner answered **"yes to all"**. The release adds the
  seven event parts (`parent`, `baby`, `bride`, `groom`, `boy`, `deceased`,
  `remembered`), the `memorial` event kind and `supplied` name kind. It
  deprecates `parenthood` in favour of `parent_of` relations to a child person
  and corrects grandparent/great-grandparent descent mappings, including
  inverses. A son's bris greeting stays with his birth; it adds no kind.
  See the [standards vetting](design/2026-10-23-standards-foundation-vetting.md)
  and [`released/1.2.0.json`](../vocabulary/released/1.2.0.json).
- **26 October 2026 — vocabulary 1.3.0.** The session asked the owner:
  "Should a condolence count on a death's page as a voice from the community, as greetings do at a wedding, rather than as the death notice itself? Yes: I add the word 'condolence' to the site's vocabulary and move about 1,300 condolences."
  The owner answered that day: **"The other two points on husband and wife and the condolences, your suggestions are accepted"**.
  This release adds only `content_unit_roles.condolence`, a notice of sympathy
  sent to the mourners by friends or a society, responding to a death as a
  congratulation does to a wedding or birth. The corpus notices and private
  discussion remain outside this public repository; the approval was recorded
  in [the session](https://claude.ai/code/session_01PD6Qzn7cCzwXCWhkmSYE5Y).
  Reading the pinned EHRI 0.2.0 and its imported RiC-O 1.1 term lists establishes
  no precise counterpart for this content-unit role. It maps to the local
  `pc:content_unit_roles_condolence`, declared with that reason in
  [`profile.ttl`](../vocabulary/profile.ttl). See
  [`released/1.3.0.json`](../vocabulary/released/1.3.0.json).

- **31 October 2026 — site-content vocabulary 1.1.0.** Asked
  **"Approve them as released vocabulary?"** for `title_types.printed` and
  `title_types.supplied`, the owner answered **"Approve both"** in
  [the private session](https://claude.ai/code/session_01M8ugJSQUZUYXkNnaMuEm11).
  `printed` means the printed words naming a content item or section;
  `supplied` means an attributed English name pinned to the text it was made
  from. The private evidence and discussion stay in pruzhany-steps and that
  session; no personal examples are published here. The existing mappings are
  retained: `pc:title_type_printed` and `pc:title_type_supplied`, declared local
  SKOS concepts typed `rico:TitleType`, reached through `rico:hasTitleType`
  from a `rico:Title` (`rico:hasOrHadTitle`). The pinned EHRI 0.2.0 and RiC-O
  1.1 lists, read **31 October 2026**, supply no controlled value distinguishing
  printed words from an attributed supplied title; each local reason remains
  in [`site-content.profile.ttl`](../vocabulary/site-content.profile.ttl).
  Identifiers, definitions, mappings and original `added_in` values are
  unchanged. Earlier document stamps `0.1.0` and `1.0.0` remain accepted; the
  subtypes and subjects retain their earlier approval. See
  [`released/site-content-1.1.0.json`](../vocabulary/released/site-content-1.1.0.json).

Later proposals, including the two source kinds in the
[sources-and-citations design](design/2026-10-24-sources-and-citations.md),
follow the process above and need their own owner approval.

## Stage-1 plan and review, retained as history

The completed plan added optional sourced-evidence contracts and vocabulary
without publishing new evidence. Its review was accepted with these changes:
attach only to the private enrichment contracts, not public edition bundles;
crosswalk the fan-out categories instead of seeding duplicate fact types;
use a single corpus source register; and require a citation locator from
`record_id`, `page`, `scan`, `time`, `unit_id` or `url` in both language twins.
Evidence confidence, identity confidence and editorial approval stay separate.
`left_before` is not a fate outcome: emigration alone proves neither survival
nor death. Person pages already existed; the later storage stage added corpus
architecture rather than the first person page.

The rollout required green checks in every affected repository, standards
alignment, unchanged public output apart from the schema version, and no paid
calls except Codex on the owner's subscription. Its sequence was design,
vocabulary/generator, optional contracts/parity, steps' copied schemas, then
consumer pins and privacy checks. The old press consumer was retired later;
the current contracts use issue documents and a shared record. The
[people-facts design](design/2026-10-19-people-facts-and-sources.md) keeps the
detailed historical contract and review.

The same discussion also recorded the owner's publication decisions: retain
all facts privately; show accepted facts with their sources, show thin identity
links folded as possible namesakes, and withhold contradicted links and private
notes. One finding with one review suffices. These are separate from approval
of types and remain subject to the site's current explicit projection rules.

## Sources and citation maintenance

Read on **25 October 2026**: GitHub's stage-1 issue and its full comment history,
including the [accepted review](https://api.github.com/repos/dsmedia/pruzhany-schema/issues/comments/6281076205),
the owner's [standing decisions](https://api.github.com/repos/dsmedia/pruzhany-schema/issues/comments/6281227920),
[rollout authority](https://api.github.com/repos/dsmedia/pruzhany-schema/issues/comments/6281312611),
[publication decisions](https://api.github.com/repos/dsmedia/pruzhany-schema/issues/comments/6287555614)
and [release confirmation](https://api.github.com/repos/dsmedia/pruzhany-schema/issues/comments/6377340483).
The history above also reads the released vocabulary snapshots and ADR 0001.

On that date the citations in `approved_by` were redirected here, including
historical release snapshots, as explicitly requested in the written-records
ticket. Only those provenance pointers change: all other snapshot fields,
identifiers, definitions, mappings, versions and release dates are preserved.
