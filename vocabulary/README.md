# Sourced entities vocabulary

`site-content.json` is a separate **1.1.0, released 2026-10-31** vocabulary.
The owner approved its 21 content-item subtypes and 11 subjects as proposed
(steps decision 164, item 1), then approved both `printed` and `supplied` title
types on 31 October 2026: **"Approve both"**, answering **"Approve them as released
vocabulary?"**. `released_groups` records all three groups; both title entries
now have `status: released`. See the [approval record](../docs/vocabulary-approvals.md).
The 38 unresolved inventory values stay `other` with their `proposed_type` in the
producer's retained records; they are not new subtype or subject identifiers.
This release does not change sourced-entities or its generated enums. The generator writes the separate
`site-content.vocabulary.ts` / `site_content_vocabulary.py` modules; the validator
checks each subtype's single Impresso parent and the owner's fixed parents.
The type list is read from `impresso_types`; each fixed parent's type and decision
date are recorded in that subtype's `owner_fixed_parent` value. The checker reads
these decisions from the vocabulary rather than inferring them from subtype names.
Since 2026-10-22 the owner has fixed the parent of every subtype listed (the last ten,
announcement to humour, approved as proposed). The subtypes were released unchanged
on 2026-10-25.
The Impresso type list is copied from Impresso's published
[`issue.schema.json`](https://github.com/impresso/impresso-schemas/blob/d55526d/json/canonical/issue.schema.json)
at commit `d55526d`, `$defs.metadata.properties.tp.enum`, read 2026-10-22;
all 13 values, in order, rechecked against that public file on 2026-10-30.
There is no new local base type.

Each subtype is a local SKOS concept typed `rico:DocumentaryFormType`, connected
by `rico:hasDocumentaryFormType`; it is not equivalent to the whole ontology class.
Subjects are declared local SKOS concepts reached by `rico:hasOrHadSubject` because
the pinned ontologies do not enumerate what these content items are about. Printed and supplied titles
use `rico:hasOrHadTitle` / `rico:Title`, with two declared concepts typed
`rico:TitleType` via `rico:hasTitleType`. Every concept's reason is in
`site-content.profile.ttl`, marked with the current release version and day.
The title types' identifiers, definitions and mappings are unchanged. The released
life-event parts, `memorial` and the `supplied` name kind moved to
`sourced-entities.json` and `profile.ttl` in 1.2.0; the site-content identifiers and mappings are unchanged.
New shape mappings are also recorded in `site-content.json` and checked by the
alignment gate. Existing sourced-entity mappings continue to apply to reused fields.

The private approval sheet sorts 338 category values (337 strings and null):
140 values carry subtype candidates, 144 section-heading candidates, 112 subjects
and 38 an unresolved part. These route counts overlap; 95 values carry more than
one route. It gives two or three real examples for each of the 21
subtypes and 11 subjects. No real examples are copied into this repository.
An English heading label is only a lead for recovering the original printed
heading and its address; it cannot create a section by itself.

`sourced-entities.json` is the released production application vocabulary, now
**1.3.0, released 2026-10-26**. The owner approved 1.0.0's recommended types in advance on
2026-10-20, as recorded in the [approval record](../docs/vocabulary-approvals.md). `approved_by` records the decisions. Version 1.1.0,
released 2026-10-22 at the owner's word, adds one claim status, `proposed`: an
assertion put forward and not yet accepted, disputed or rejected, never published
(the site shows only `accepted` facts, and folds some `disputed`). Version 1.2.0
releases the owner's batch ([approval record](../docs/vocabulary-approvals.md)): seven `event_parts`, `event_types.memorial`,
`name_kinds.supplied`, the `parenthood` deprecation, and the grandparent/great-grandparent
descent mappings including their inverses. The owner answered **"Yes"** to **"yes to all"**
on 23 October 2026 after reviewing two or three printed notices and their English
for each new term on the private approval page. Engagement was already released.
The same answer keeps a son's bris greeting with the birth event; no new term.
Version 1.3.0 adds `content_unit_roles.condolence`, approved on 26 October 2026
in the [approval record](../docs/vocabulary-approvals.md): a notice of sympathy
sent to the mourners, responding to a death as a congratulation does to a wedding
or birth. Its local `pc:content_unit_roles_condolence` mapping is declared and
explained in `profile.ttl`; neither pinned EHRI 0.2.0 nor RiC-O 1.1 has a precise
counterpart for this role.
The generator
writes `released/<version>.json`; validation requires the current release snapshot to
equal the current vocabulary and preserves every identifier from every snapshot.
Future vocabulary changes belong in a new version; historical release snapshots remain
unchanged apart from the citation-only maintenance of 25 October 2026: their
`approved_by` pointers now name [`docs/vocabulary-approvals.md`](../docs/vocabulary-approvals.md).
All other snapshot fields are unchanged. A future `status: proposed` version has
not yet been released and has no release date.

Site-content follows the same release path, with independent snapshots named
`released/site-content-<version>.json`. Its current released snapshot must equal
`site-content.json`, and historical identifiers are retained. Run the generator;
never edit snapshots or generated contracts by hand. `compatible_versions`
explicitly retains the existing `0.1.0` and `1.0.0` content-document stamps
alongside `1.1.0`; both twins consume the generated version set and reject other stamps. New writers
use the generated current version. This lets the existing site data pass before
the later steps refresh and site pin. See the [release record](../docs/design/2026-10-25-site-content-release.md).

This directory contains definitions and mappings only. Real examples and the
owner's approval sheet stay private, outside this public repository. The
application profile in `profile.ttl` is separate from the pilot's profile; its
namespace identifies local terms and does not imply hosted ontology content.

Only add identifiers. Never remove or rename a released identifier. Deprecate an
entry with `deprecated_in` and `replaced_by`; retain the deprecated entry's original
mapping. A string replacement still names an existing entry in the same group.
Since 1.2.0 a cross-group replacement may instead be
`{"group": "relationship_types", "id": "parent_of", "reason": "…"}`: the target
must exist, and a nonempty reason explains how to replace the old representation.
This small extension is needed because `parenthood` is a fact kind, while its
replacement is a `parent_of` relation from each parent to the child **as a person**.
A same-group fact replacement would misstate that decision. Both forms are tested.
An owner-approved mapping correction on a retained identifier belongs to a new
version, as the four descent mappings do in 1.2.0. The checks require the current
snapshot to match and retain historical identifiers; they do not forbid a mapping
change in a new version. The 1.0.0 and 1.1.0 snapshots retain their original mappings.
The owner approves additions in batches,
with real examples reviewed privately. Every addition names its pinned EHRI or
RiC-O term, or a local term declared and explained in its vocabulary's profile. Prefer EHRI
where applicable, then RiC-O 1.1 terms (the version EHRI 0.2.0 imports), then a local term with
a reason. Mappings describe correspondence, not unconditional RDF assertions.
Disputed and pending claims must not become unqualified historical triples.

Links between identified people use `relationship_types`, with the
subject-to-related-person direction and symmetric inverses. A source's claim
about a named relative who need not have an identified record uses the `kinship`
fact, with `relationship_type` and `related_name` (fields added in ticket 3).
Its RiC-O FamilyRelation can connect a Person node without an otherwise resolved
identity. `parenthood` is deprecated: represent even an unnamed child as a person
and link each parent with `parent_of`. The legacy `Fact` contract still reads the
released identifier for old data; `SharedFact` refuses it, including as
`other/proposed_type`, so the site writer cannot emit it. The isolated pilot keeps
its historical vocabulary.
Names use `name_kinds`: maiden names are birth names; `supplied` marks our
description and requires attribution and citations in both `Name` and its site
extension `SharedName`. A supplied name no longer uses `other/proposed_type`.
Events use `event_types`; taking part uses the `event_participation` fact
and a mention role. There is no marriage, name, or parent-name fact type.
`other` facts require a nonempty `proposed_type`. Emigration is dated evidence,
never a fate outcome or proof of survival.

`fate_outcomes`, `location_types`, `compatibility_event_types`,
`life_event_types`, and `gender` preserve the original production values exactly.
`content_unit_roles` retains those values and adds `condolence` in 1.3.0.
The released `event_types` also includes engagement. Existing
compatibility enums remain unchanged. Compatibility categories
with no precise pinned ontology value use declared local terms rather than
asserting equivalence to a broader class.

The relationship seed preserves all 18 IDs, labels and inverses from the site's
five hand-made editions' `relationshipTypes`, supplied as an extracted taxonomy.
It adds `great_grandparent_of` and `great_grandchild_of` as a symmetric pair in
1.0.0. All family types use the specific RiC-O relation where available, otherwise
`hasFamilyAssociationWith` via `FamilyRelation`. Friend and colleague use the
broader `isAgentAssociatedWithAgent` via `AgentToAgentRelation`, retaining their
specific vocabulary IDs. `teacher_of` maps from teacher to student using
`hasOrHadStudent`; `student_of` uses `hasOrHadTeacher`, both via `TeachingRelation`.
Since 1.2.0, `grandparent_of` and `great_grandparent_of` map to `hasDescendant`
via `DescendanceRelation`, ascendant → descendant. Their inverses `grandchild_of`
and `great_grandchild_of` map to the pinned inverse `hasAncestor`, through the
same relation class, descendant → ascendant. Their identifiers retain the exact
generation even though RiC-O's descent relation is broader.
`external_source_types` and `holocaust_fate_types` preserve the supplied site's
compatibility registry values and metadata. Fate descriptions are legacy
compatibility text, not new fate criteria or permission to infer survival from
residence. No personal assertions or extracted research findings are included.

For office, the person `occupiesOrOccupied` a `Position`, qualified via
`PositionHoldingRelation`. For membership, the person `isOrWasMemberOf` the group
(the inverse is group `hasOrHadMember`), qualified via `MembershipRelation`.
School attendance is local: the pinned term lists establish `TeachingRelation`
as a term but do not establish its suitability for attendance at a school.
Birth and death mappings name their date predicates; place-only assertions use
`hasBirthPlace` and `hasDeathPlace`, as stated in the definitions. No date should
be invented. Ghetto activities and partisan service use ordinary membership or
office where those fit; the residual categories have local mappings.

`crosswalks/fan-out-fact-kinds.json` translates the ten legacy fan-out kinds.
The four named-relative kinds target `kinship`, require `relationship_type` and
`related_name`, and state `subject_to_named_relative` direction: `parent_name`
means `child_of`, `child_name` means `parent_of`, `spouse_name` means `spouse`, and
`sibling_name` means `sibling`. `giver_of_record` goes to
a **private citation remark, never published**; this routing metadata contains
no actual remark. All destinations are validated vocabulary IDs. This is a
crosswalk specification, not a migration of private data.

Regenerate and verify offline with Python's standard library:

```sh
python3 -I -B vocabulary/generate.py
bin/verify vocabulary
python3 -I -B standards/check_alignment.py
```

`generate.py --check` checks exact UTF-8/LF bytes. It generates a Zod enum per
group and Python Literals plus the vocabulary version, and `linkml/schema/vocabulary.yaml`:
a LinkML enum per group, Impresso's types and the reading states, named as the other
contracts name them, each value with its definition, its `meaning` (the `rico:`, `ehri:`
or declared `pc:` term) and a RiC-O mapping's `via` as an annotation. The production contracts
consume these modules; the released module also owns the parts' allowed kinds
and the life-event kind list. `check.py` validates
mapping forms, local declarations and reasons, replacement targets, relationship
inverses, crosswalk routing and every snapshot's retained identifiers. The
standards alignment gate independently validates ontology terms and relation
classes, including both the released and proposed profiles. Tests exercise release preservation,
current snapshot equality, kinship direction, and compatibility using temporary
fixtures.
