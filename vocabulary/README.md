# Sourced entities vocabulary

`sourced-entities.json` is the released production application vocabulary, version
1.0.0, dated 2026-10-20. The owner approved the recommended types in advance on
that date, as recorded on #16. `approved_by` records this decision. The generator
writes `released/1.0.0.json`; validation requires the current release snapshot to
equal the current vocabulary and preserves every identifier from every snapshot.
Future changes belong in a new version; historical release snapshots remain
unchanged. A future `status: proposed` version has not yet been released and has
no release date.

This directory contains definitions and mappings only. Real examples and the
owner's approval sheet stay private, outside this public repository. The
application profile in `profile.ttl` is separate from the pilot's profile; its
namespace identifies local terms and does not imply hosted ontology content.

Only add identifiers. Never remove or rename a released identifier. Deprecate an
entry with `deprecated_in` and `replaced_by` pointing to an existing entry in its
group; retain its original mapping. The owner approves additions in batches,
with real examples reviewed privately. Every addition names its pinned EHRI or
RiC-O term, or a local term declared and explained in `profile.ttl`. Prefer EHRI
where applicable, then RiC-O terms shared by 1.0.2 and 1.1, then a local term with
a reason. Mappings describe correspondence, not unconditional RDF assertions.
Disputed and pending claims must not become unqualified historical triples.

Links between identified people use `relationship_types`, with the
subject-to-related-person direction and symmetric inverses. A source's claim
about a named relative who need not have an identified record uses the `kinship`
fact, with `relationship_type` and `related_name` (fields added in ticket 3).
Its RiC-O FamilyRelation can connect a Person node without an otherwise resolved
identity. Parenthood of an unnamed child remains the separate `parenthood` fact.
Names use `name_kinds`: maiden names are birth
names. Events use `event_types`; taking part uses the `event_participation` fact
and a mention role. There is no marriage, name, or parent-name fact type.
`other` facts require a nonempty `proposed_type`. Emigration is dated evidence,
never a fate outcome or proof of survival.

`fate_outcomes`, `location_types`, `compatibility_event_types`,
`content_unit_roles`, `life_event_types`, and `gender` preserve today's production
values exactly. The released `event_types` also includes engagement. Existing
production schemas and package exports are untouched. Compatibility categories
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
group and Python Literals plus the vocabulary version. Ticket 3 will integrate
these standalone modules into the production contracts. `check.py` validates
mapping forms, local declarations and reasons, replacement targets, relationship
inverses, crosswalk routing and every snapshot's retained identifiers. The
standards alignment gate independently validates ontology terms and relation
classes, including the production profile. Tests exercise release preservation,
current snapshot equality, kinship direction, and compatibility using temporary
fixtures.
