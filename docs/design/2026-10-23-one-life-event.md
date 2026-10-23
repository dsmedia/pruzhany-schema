# One life event, its main people and their parts

Round 4a, 23 October 2026. Implementation contract for 4b (pruzhany-steps) and 4c
(pruzhany-svelte), following ADR 0001 and brief 09's fourth grilling. The present
brief brings the evidence correction into round 4, as ADR 0001 now says. Vocabulary
additions below remain **proposed**.

## Stored once

`SharedRecord.events` holds `{id, type, proposed_type?, name, participants, dates,
location_id?, description?}` once per happening. Each participant is exactly
`{person_id, part}`. Each issue's life-event entry is only `{id, content_items}`;
each piece keeps its existing `{content_item_id, role}`. Every issue entry resolves
to a shared event. Research events may exist without an issue entry. Shared ids
are unique; the same event id can occur in many issue files. No second name, kind,
date or participant list can disagree with it there. Empty participants preserve
unresolved events for the writer's review list; they do not license a join.
The new participant type is `LifeEventParticipant`; the existing edition bundle's
`EventParticipant` keeps its `role` contract. Dates use `LifeEventDate` in both twins.

The public projection in 4c copies the public shared event into the issue's
`record.events`, and the issue entry retains only its pieces. Views join by id;
the event page gathers pieces across all issues, in date order, and a person's
page lists each event once with their part. `shared-projection.ts` currently
filters principals to mentions **in this issue** and `validate-data.ts` enforces
that rule. Replace that filter with the existing publication eligibility applied
across the archive: include eligible participants and their public person records
even if mentioned in another issue. Do not infer eligibility from participation.
A described child needs a real mention on the words designating them. Display
“their daughter, not named in the paper”, and give the child a person page titled
by the supplied name until a sourced later name is available.

## Parts, kinds and dates

The proposed vocabulary owns each part's allowed event kinds and person range;
its generator emits the same lookup for both languages. The profile declares
Event → Person subproperties. Doctor, midwife, greeter, mourners and the couple's
parents remain mentions, not participants. There is no participation-role node.

One proposed `memorial` kind covers annual and 30-day commemorations: both remember
the deceased; their printed date and description distinguish the occurrence.
Each commemoration is a separate event, and neither is the death. Engagement and
wedding are also separate. Both new kinds use `other/proposed_type`. The released
general `event_types` already includes engagement, but `life_event_types` does
not; this round uses the latter for shared life events, plus the existing general
`holocaust_event` for retained research events. No released identifier is removed.
An unrecognised proposed kind may be retained with no main people, for review.

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

## A child known by description; notice evidence

An ordinary `SharedPerson` keeps its permanent id. Its site-only `SharedName`
extends `Name`: the supplied description is
`{value: "daughter of Rivtche and Moshe Judewicz", kind: "other",
proposed_type: "supplied", script: "Latn", lang: "en", attribution, citations}`.
The proposed kind, attribution and nonempty citations are required together;
`kind: printed` with `proposed_type` is refused. `isPrintedName` selects printed
names only. The existing production `Name` and its released enum stay unchanged.
Later naming appends a cited printed/birth/later name, updates the display name,
and retains the supplied entry and the person's id.

The birth `SharedFact` reuses `Fact`'s event reference, citations, standing,
attribution and review. Its existing `qualifiers.child_count: "1"` records the
writer's reading that the notice designates exactly one child. This is an
attestation to check against the print, not a linguistic inference by the schema.
Twins, plurals and ambiguity go to the review list. A supplied child's birth fact
must point to the event where that person is `baby`; at least one parent is a
participant. Each parent has one `parent_of` to that child citing the notice.
The birth citation has `edition_date`, `unit_id` and `quote`; a word-grain subject
mention for the child must occur in that cited piece and the quote must contain
its printed designation. Existing address checks bind it to the printed region.
These checks still apply after the child gains a name.

New relations evidenced by a newspaper piece (citation with `unit_id` and
`edition_date`) use `parent_of`, never `child_of`; the latter is refused even when
offered as `other/proposed_type`. The bride's mother is the subject, the bride the
relative, with a quote from that notice. Identical notice-derived relation triples
are stored once with combined citations. This does not migrate old inverse rows,
their ids or directional `shown`; the full merge is the later relations round.
Every cited piece must exist in a complete `SiteArchive`, and quotes must occur
there. Fact/relation citations map to `rico:isEvidencedBy` (Relation →
RecordResource). `relationHasSource` is the relation's first endpoint. Correct
the proposed binding, the isolated pilot and the marked historical design table.

## Identity and the next writer

Keep a joined event's hand-made id when present, otherwise the earliest issue's
id (stable lexical tie-break within that issue). Preserve other addresses in the
existing `data/<old-issue-date>-redirects.json`, `redirects: {old_id: [kept_id]}`,
written by `site_writer._address_redirects` / `write_site`; carry older redirects
forward and resolve chains. People keep their ids forever: never rename, reuse
or delete a published id; merged ids redirect permanently. A split leaves the
old id on the person supported by most of its evidence and mints another.

4b resolves only main people's identities before comparing events. Resolved ids
come first; otherwise across issues require the same kind, full printed Yiddish
names (two words after punctuation, pointing and honorifics), within 56 days of
the first piece. A letter's difference is listed. Within an issue, given names
may join only without conflicting printed surnames; lone-given-name deaths and
ambiguous candidates are listed. Shared pieces join only after main people are
filled and conflicts/two-happening pieces excluded. A one-person subset joins a
couple through resolved ids across issues, or full printed names within one
issue. A surname shared in the print counts for both parents at births only.
Check whole groups against conflicts and the first-piece window, not just pairs.
The described child follows the birth, never its description. A later naming
needs resolved parents, compatible birth and no competing child. Preserve the
joins and doubts for review; no fuzzy spelling fold or paid judging this round.

Measured basis: D-data finds 13 Judewicz events in 16/23/30 December, three Vigotov
person ids, and 40 principal references dropped publicly. C §3's strict rule has
69 joins with no surname conflict, versus six definite wrong joins on given names
across issues. F §§1–4 adds 79 within-issue pairs; shared surname adds eight birth
pairs across issues; four or more shared-piece pairs describe two happenings.
E's recommendation supplies the child pattern; its older inferred date-bound
suggestion is superseded by the later vetting and fourth grilling.

## Owner's batch

All ten terms below are proposed in `site-content.json` and its profile. Each
row needs two or three real finished-page examples in 4b/4c, with print beside
English on the one private batch artifact. No synthetic fixture approves a term.

| id | mapping and one-line reason |
|---|---|
| `baby` | `pc:part_baby` ⊑ `rico:affectsOrAffected`: the birth happens to this person; no RiC-O baby part |
| `parent` | `pc:part_parent` ⊑ `rico:hasOrHadParticipant`: parent at a birth, not the person born |
| `bride` | `pc:part_bride` ⊑ `rico:affectsOrAffected`: bride at engagement/wedding; no RiC-O bride part |
| `groom` | `pc:part_groom` ⊑ `rico:affectsOrAffected`: groom at engagement/wedding; no RiC-O groom part |
| `boy` | `pc:part_boy` ⊑ `rico:affectsOrAffected`: boy at bar mitzvah; no RiC-O bar-mitzvah part |
| `deceased` | `pc:part_deceased` ⊑ `rico:affectsOrAffected`: the person who died; no RiC-O deceased part |
| `remembered` | `pc:part_remembered` ⊑ `rico:affectsOrAffected`: the person remembered, without asserting another death |
| `engagement` | `pc:site_event_engagement`, a `rico:EventType`: a life-event kind still awaiting this batch |
| `memorial` | `pc:site_event_memorial`, a `rico:EventType`: commemorations of either interval |
| `supplied` | `pc:site_name_supplied`, local concept; names use `rico:AgentName` via `hasOrHadAgentName`: marks our description, not print |

Also present the `fact_source` correction to `rico:isEvidencedBy`. For the batch,
**not implemented now**: deprecate released `parenthood`, replaced by `parent_of`
to the described child (`hasChild` via `ChildRelation`); remap `grandparent_of`
and `great_grandparent_of` to `hasDescendant` via `DescendanceRelation`, retaining
their distinct local meanings and all released ids.

## Tests and boundaries

| rule | source and a real refusal |
|---|---|
| 5 | RiC-O: Family ⊑ Group, Group disjoint Person; refuse an id in both collections |
| 6 | Local narrowing of RiC-O Event → Thing to our Person parts; refuse missing/person-in-wrong-collection references, including a family |
| 7 | RiC-CM's single Event Type, mapped by RiC-O `hasEventType`; refuse a direct proposed kind, missing proposal, or an issue copy of kind/name |
| 8 | Local: every part exists, has an explained Event → Person subproperty and fits the kind; refuse a wedding baby or a doctor part |
| 9 | RiC-CM R070/R072: refuse the same baby in two births, or the deceased in two deaths; memorials remain allowed |
| 10 | RiC-O date property domains/ranges, with local ISO validation and qualifier rules; refuse impossible dates, unprinted normalization, fallback bounds or a later-issue fallback |
| 13 | Local: refuse a supplied name as printed, plural/unspecified child count, absent designation mention, birth fact or parental evidence |
| evidence | RiC-O `isEvidencedBy` domain/range and `hasChild` chain/endpoints; local citation checks refuse missing pieces, false quotes and notice-derived inverse/duplicate rows |

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
`hasDescendant`, `DescendanceRelation`, `Identifier`, `IdentifierType`. Their
kinds, domains, ranges, hierarchy, disjointness and child property chain are read
from the pins. Claim only “mapped to RiC-O 1.1 as EHRI 0.2.0 imports it, with these
rules tested”.

4b must change `site_writer._life_events`, `_event_faults`, `site_people` merging,
hand-made/preservation/carry paths and generated site-next shapes. 4c must change
the projection, public validation, data-to-view adapters, event/person pages and
their fixtures. `content-unit`, `enrichment`, production names/dates and
`life-event.schema.ts`'s live `LifeEventSchema` stay unchanged. Site-next is an
intentional breaking shape; old site-next data must be rebuilt before publication.

The [verification record](2026-10-23-one-life-event-verification.json) gives the
failing-before/passing-after counts, gate results, exact consumer commands and
every affected consumer path. All runnable schema gates pass; `scan` needs the
missing gitleaks 8.24.3. Consumer failures are the expected 4b/4c migration work,
not a reason to publish these files early. Review this design and commit the
schema branch before starting 4b; vocabulary approval remains the end-of-round batch.
