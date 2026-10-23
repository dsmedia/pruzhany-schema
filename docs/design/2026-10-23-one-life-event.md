# One life event, its main people and their parts

Round 4a, revised in 4d and 4f, 23 October 2026. Implementation contract for the writer
(pruzhany-steps) and site (pruzhany-svelte), following ADR 0001 and brief 09's fourth grilling. The present
brief brings the evidence correction into round 4, as ADR 0001 now says. The
owner's batch below is **released in vocabulary 1.2.0, 2026-10-23**.

## Stored once

`SharedRecord.events` holds `{id, type, proposed_type?, name, main_people, dates,
location_id?, description?}` once per happening. Each main person is exactly
`{person_id, part}`. Each issue's life-event entry is only `{id, content_items}`;
each content item keeps its existing `{content_item_id, role}`. Every issue entry resolves
to a shared event. Research events may exist without an issue entry. Shared ids
are unique; the same event id can occur in many issue files. No second name, kind,
date or main person list can disagree with it there. Empty `main_people` preserve
unresolved events for the writer's review list; they do not license a join.
The new main person type is `LifeEventMainPerson`; the existing edition bundle's
`EventParticipant` keeps its `role` contract. Dates use `LifeEventDate` in both twins.
Each content item occurs once in one life event. Duplicate roles on a content item
are refused, as are assignments to a second event, including an event with no
main people. A content item's `event_id`, when present, must agree with its life-event
reference. The writer chooses one content-item role by a documented precedence
and redirects an emptied duplicate event to the event retaining its content item.

The public projection in 4c copies the public shared event into the issue's
`record.events`, and the issue entry retains only its content items. Views join by id;
the event page gathers content items across all issues, in date order, and a person's
page lists each event once with their part. `shared-projection.ts` currently
filters principals to mentions **in this issue** and `validate-data.ts` enforces
that rule. Replace that filter with the existing publication eligibility applied
across the archive: include eligible main people and their public person records
even if mentioned in another issue. Do not infer eligibility from participation.
A described child needs a real mention on the words designating them. Display
“their daughter, not named in the paper”, and give the child a person page titled
by the supplied name until a sourced later name is available.

## Parts, kinds and dates

The released vocabulary owns each part's allowed event kinds and person range;
its generator emits the same lookup for both languages. The profile declares
Event → Person subproperties. Doctor, midwife, greeter, mourners and the couple's
parents remain mentions, not main people. There is no participation-role node.
The seven parts are direct released values. `parent` uses
`rico:hasOrHadParticipant`; `baby` and the other five use `rico:affectsOrAffected`,
as proposed and as the owner's batch page showed them ("filed under 'affected by the
event'" for the baby), approved on 23 October 2026.

One released `memorial` kind covers annual and 30-day commemorations: both remember
the deceased; their printed date and description distinguish the occurrence.
Each commemoration is a separate event, and neither is the death. Engagement and
wedding are also separate. Memorial uses `type: "memorial"`; engagement uses
the released `event_types` value `engagement` and its existing mapping
`pc:event_types_engagement`, released in 1.0.0. Shared events reuse `EventTypes`
in both languages, including `holocaust_event` for retained research events.
Engagement needs no new release. The generated `lifeEventKinds`
and `LIFE_EVENT_KINDS` take the released event types (excluding `other` and
`holocaust_event`), so consumers share one vocabulary list.
An unrecognised proposed kind may be retained with no main people, for review.
A released kind, including `memorial`, is refused as `other/proposed_type`.

**The bris decision (4f):** on the private batch page the owner answered **"Yes"**
to **"yes to all"** on 23 October 2026, including keeping a greeting on a son's
bris (circumcision) with that birth's event. It is not a separate event or a new
vocabulary word. `שלום זכר` is not a bris. After the schema review and commit,
the writer must check every bris greeting in the written files, including spellings
of `ברית`, `ברית מילה` and `ברית-מילה`, and report its birth event.

`dates` is a nonempty array so both printed calendars can survive. Each entry is
either `{printed, printed_calendar, start?}` or
`{qualifier: "reported_in", reported_in: "1938-12-16"}`. `printed` and calendar
reuse the existing sourced-date names; `start` reuses its ISO year/month/day
validator and means a normalized value **of a printed Gregorian date only**.
Hebrew words remain as printed; no conversion is guessed. The fallback is the
first issue's date, with its qualifier, and cannot coexist with a printed date
or carry `start`, `end`, precision or inferred bounds. A greeting can precede a
wedding. A birth fact can cite the notice and refer to the event without adding
a date: do not manufacture a bound there either.
The writer refuses a join when printed dates of the life event disagree. These
are dates of the birth, death or wedding, never issue datelines; a notice printed
before another notice's printed date of death cannot describe that death.

## A child known by description; notice evidence

An ordinary `SharedPerson` keeps its permanent id. Its site-only `SharedName`
extends `Name`: the supplied description is
`{value: "daughter of Rivtche and Moshe Judewicz", kind: "supplied",
script: "Latn", lang: "en", attribution, citations}`.
The released kind, attribution and nonempty citations are required together in
both `Name` and `SharedName`; a supplied attribution on a printed name is refused.
`SharedName` only extends citations with printed addresses; it no longer has
`other` or `proposed_type`. `isPrintedName` selects printed names only.
Later naming appends a cited printed/birth/later name, updates the display name,
and retains the supplied entry and the person's id.

The birth `SharedFact` reuses `Fact`'s event reference, citations, standing,
attribution and review. Its existing `qualifiers.child_count: "1"` records the
writer's reading that the notice designates exactly one child. This is an
attestation to check against the print, not a linguistic inference by the schema.
Twins, plurals and ambiguity go to the review list. A supplied child's birth fact
must point to the event where that person is `baby`; at least one parent is a
main person. Each parent has one `parent_of` to that child citing the notice.
The birth citation has `edition_date`, `unit_id`, `quote` and `addresses`; a word-grain subject
mention for the child must occur in that cited content item and the quote must contain
its printed designation. Existing address checks bind it to the printed region.
These checks still apply after the child gains a name.
Only a child not named in the notice receives a supplied description. The writer
recognizes singular Hebrew and Yiddish designations beside a birth expression;
kinship uses of “son” or “daughter” alone are not birth evidence.

New relations evidenced by a newspaper content item (a located `SiteCitation`,
with nonempty `addresses`) use `parent_of`, never `child_of`; the latter is refused even when
offered as `other/proposed_type`. The bride's mother is the subject, the bride the
relative, with a quote from that notice. Identical notice-derived relation triples
are stored once with combined citations. This does not migrate old inverse rows,
their ids or directional `shown`; the full merge is the later relations round.
For these new citations, the cited content item must exist in a complete
`SiteArchive`, the quote must occur there and at the citation's printed addresses,
and the addresses must be inside the item's printed regions, using the same check
as mentions. The writer quotes the words stating the fact or relation, not the
whole notice. `SiteCitation` extends the production citation only in site-next;
the production citation contract does not change. Shared facts, relations
and person names accept it. Supplied names and their birth/parent evidence must
all use located citations. A later printed name may retain the supplied name.

Older citations without addresses retain their exact `unit_id`, `record_id` and
quote, even when the old locator or reading no longer matches the current content
item. Their registry sources are still checked. The new quote, location, inverse
and duplicate notice-relation checks apply to located evidence; they do not
migrate old inverse rows. The writer must locate every notice citation it creates
in this round and must test that obligation; absence of addresses is not permission
to write unlocated new evidence. No scope is inferred from an id pattern, source
title or English attribution. Fact/relation citations map to `rico:isEvidencedBy` (Relation →
RecordResource). `relationHasSource` is the relation's first endpoint. Correct
the proposed binding, the isolated pilot and the marked historical design table.

## Identity and the next writer

Keep a joined event's hand-made id when its provenance says it is hand-made,
never by parsing its id; otherwise keep the earliest issue's
id (stable lexical tie-break within that issue). Preserve other addresses in the
existing `data/<old-issue-date>-redirects.json`, `redirects: {old_id: [kept_id]}`,
written by `site_writer._address_redirects` / `write_site`; carry older redirects
forward and resolve chains. People keep their ids forever: never rename, reuse
or delete a published id; merged ids redirect permanently. A split leaves the
old id on the person supported by most of its evidence and mints another.

4b resolves only main people's identities before comparing events, through the
content item's own mention person ids and printed forms. English names and roles
never settle identity or a relation; the printed kinship words must state the
relation beside the printed name. Resolved ids
come first; otherwise across issues require the same kind, full printed Yiddish
names (two words after punctuation, pointing and honorifics), within 56 days of
the first content item. A letter's difference is listed. Within an issue, given names
may join only without conflicting printed surnames; lone-given-name deaths and
ambiguous candidates are listed. Shared content items join only after main people are
filled and conflicts/two-happening content items excluded. A one-person subset joins a
couple through resolved ids across issues, or full printed names within one
issue. A surname shared in the print counts for both parents at births only.
Check whole groups against conflicts and the window from the first content item, not just pairs.
The described child follows the birth, never its description. A later naming
needs resolved parents, compatible birth and no competing child. Preserve the
joins and doubts for review; no fuzzy spelling fold or paid judging this round.
Before joining, the writer reads the content item's own kind: a memorial never
belongs to a death event; another kind or two life events in one notice is listed
for review. The schema checks the resulting structure and evidence locations;
these readings of Hebrew and Yiddish remain the writer's responsibility.

Measured basis: D-data finds 13 Judewicz events in 16/23/30 December, three Vigotov
person ids, and 40 principal references dropped publicly. C §3's strict rule has
69 joins with no surname conflict, versus six definite wrong joins on given names
across issues. F §§1–4 adds 79 within-issue pairs; shared surname adds eight birth
pairs across issues; four or more pairs sharing a content item describe two happenings.
E's recommendation supplies the child pattern; its older inferred date-bound
suggestion is superseded by the later vetting and fourth grilling.

## Owner's batch

All nine terms below moved from `site-content.json` and its profile into
`sourced-entities.json` 1.2.0 and `profile.ttl`, released 2026-10-23. On that day
the owner answered **"Yes"** to **"yes to all"** on the private batch page after
seeing two or three real printed notices and their English for each new term.
`approved_by` records that decision. Subtypes, subjects and title types remain proposed.

| id | mapping and one-line reason |
|---|---|
| `baby` | `pc:part_baby` ⊑ `rico:affectsOrAffected`: the birth happens to this person; no RiC-O baby part |
| `parent` | `pc:part_parent` ⊑ `rico:hasOrHadParticipant`: parent at a birth, not the person born |
| `bride` | `pc:part_bride` ⊑ `rico:affectsOrAffected`: bride at engagement/wedding; no RiC-O bride part |
| `groom` | `pc:part_groom` ⊑ `rico:affectsOrAffected`: groom at engagement/wedding; no RiC-O groom part |
| `boy` | `pc:part_boy` ⊑ `rico:affectsOrAffected`: boy at bar mitzvah; no RiC-O bar-mitzvah part |
| `deceased` | `pc:part_deceased` ⊑ `rico:affectsOrAffected`: the person who died; no RiC-O deceased part |
| `remembered` | `pc:part_remembered` ⊑ `rico:affectsOrAffected`: the person remembered, without asserting another death |
| `memorial` | `pc:site_event_memorial`, a `rico:EventType`: commemorations of either interval |
| `supplied` | `pc:site_name_supplied`, local concept; names use `rico:AgentName` via `hasOrHadAgentName`: marks our description, not print |

The `fact_source` correction to `rico:isEvidencedBy` was already implemented.
The same 1.2.0 batch deprecates `parenthood`, replaced by `relationship_types.parent_of`
to the child as a person (`hasChild` via `ChildRelation`). Its `replaced_by`
object names the target group, id and reason: a same-group fact could not express
the decision. The released identifier and its original mapping remain so legacy
`Fact` and the isolated pilot can read old data; `SharedFact` refuses `parenthood`
both directly and as `other/proposed_type`. New writer output must use relations.

`grandparent_of` and `great_grandparent_of` now map to `hasDescendant` via
`DescendanceRelation`, ascendant → descendant; their inverses `grandchild_of`
and `great_grandchild_of` use the pinned `hasAncestor`, descendant → ascendant.
Their distinct generation meanings and all identifiers remain. Only the 1.2.0
mapping changes; 1.0.0 and 1.1.0 snapshots retain the catch-all mapping. Existing
checks allow a mapping change in a new version; no preservation rule was weakened.

## Tests and boundaries

| rule | source and a real refusal |
|---|---|
| 5 | RiC-O: Family ⊑ Group, Group disjoint Person; refuse an id in both collections |
| 6 | RiC-O participant range, locally narrowed from Thing to our Person parts; refuse missing/person-in-wrong-collection references, including a family |
| 7 | RiC-O + RiC-CM: single Event Type, mapped by `hasEventType`; refuse an unrecognised direct kind, a released kind as a proposal, missing proposal, or an issue copy of kind/name |
| 8 | Local: every part exists, has an explained Event → Person subproperty and fits the kind; refuse a wedding baby or a doctor part |
| 9 | RiC-CM R070/R072: refuse the same baby in two births, or the deceased in two deaths; memorials remain allowed |
| 10 | RiC-O date property domains/ranges, with local ISO validation and qualifier rules; refuse impossible dates, unprinted normalization, fallback bounds or a later-issue fallback |
| 13 | Local: refuse a supplied name as printed, plural/unspecified child count, absent designation mention, birth fact or parental evidence |
| evidence | RiC-O `isEvidencedBy` domain/range and `hasChild` chain/endpoints; local citation checks refuse missing content items, false quotes and notice-derived inverse/duplicate rows |

RiC-O axioms are read directly from `standards/rico-1.1-axioms.json` by tests under
`standards/`, run by `bin/verify standards`. They are not copied into a test or
loaded under `zod/`. Bun-only behavioral fixtures exercise the shape in Zod and
in the Pydantic contract gate, including the joined birth, later naming, bride's
mother and death/memorial. Rules 1–3 (the full old-relation merge) and the actual
join algorithm belong to later writer work. The schema cannot prove the writer
read a singular child, a date or a kinship correctly; print review remains required.

Terms read in the pinned files: EHRI `Person`, `Family`, `Group`, `RecordResource`
and their superclasses; RiC-O `Event`, `EventType`, `hasEventType`,
`hasOrHadParticipant`, `affectsOrAffected`, `Person`, `Family`, `Group`, `Thing`,
`AgentName`, `hasOrHadAgentName`, `Date`, `expressedDate`, `normalizedDateValue`,
`dateQualifier`, `Relation`, `RecordResource`, `isEvidencedBy`, `evidences`,
`relationHasSource`, `relationHasTarget`, `hasChild`, `ChildRelation`,
`hasDescendant`, `hasAncestor`, `DescendanceRelation`, `Identifier`, `IdentifierType`. Their
kinds, domains, ranges, hierarchy, disjointness and child property chain are read
from the pins. Claim only “mapped to RiC-O 1.1 as EHRI 0.2.0 imports it, with these
rules tested”.

4b must change `site_writer._life_events`, `_event_faults`, `site_people` merging,
hand-made/preservation/carry paths and generated site-next shapes. 4c must change
the projection, public validation, data-to-view adapters, event/person pages and
their fixtures. `content-unit`, `enrichment`, production dates and
`life-event.schema.ts`'s live `LifeEventSchema` stay unchanged. Site-next is an
intentional breaking shape; old site-next data must be rebuilt before publication.

The [round-4a verification record](2026-10-23-one-life-event-verification.json)
preserves that run's failing-before/passing-after counts, gate results, exact
consumer commands and affected paths. Its missing-scanner and consumer-migration
results describe that earlier run. Vocabulary approval was given in round 4f as recorded above.

Round 4d's schema changes are recorded separately in
[`2026-10-23-one-life-event-4d-verification.json`](2026-10-23-one-life-event-4d-verification.json).
The writer must validate the complete proposed output with `SiteArchiveSchema`
under bun before installing any files. Its remaining checks must say what they
add beyond the schema and consume `tests/contract/life-event-shapes.fixtures.json`.
Round 4d stops after the schema gate for the session's review and commit; the
writer then refreshes from that clean HEAD, and the site pins the resulting commit.

Round 4f likewise stops after the schema gate for the session's review and commit.
Then the writer refreshes from that clean HEAD, writes all 238 issues twice to
check byte stability, and lists every changed event against the 4e site baseline.
The site pins the schema commit supplied by the session and takes the released
labels from the released vocabulary. No writer or site regeneration is part of
the schema-only stop.
