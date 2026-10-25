# The proposed site files beside the old shapes

> Historical design note, 2026-10-24: the owner approved the switch to four issue documents and one shared record; the old persisted models described below are retired (see [current contracts](../../README.md#current-site-files)).

> Release update, 2026-10-25: the owner approved the subtypes and subjects as
> proposed (steps decision 164, item 1), released as site-content 1.0.0. Title
> types remain proposed. The contracts accept the existing 0.1.0 stamp and the
> released 1.0.0 stamp; new writers use 1.0.0. See the [release record](2026-10-25-site-content-release.md).

The existing schemas, enums and exports keep their meanings. These new exports
are for the later site-writer/site switch. No data is migrated or published here.
The four issue documents hold pages, content items and sections, mentions, and
life events. The shared record is a separate file read by all issues.

| File (Zod; Pydantic twin) | New shapes |
| --- | --- |
| `site-common.schema.ts`; `site_common.py` | PrintedAddress, TextBasis, Authorship, PrintedTitle, SuppliedTitle, Translation, ContentItemBlockRef |
| `content-item.schema.ts`; `content_item.py` | ContentItem, PrintedSection, ContentItemsData |
| `shared-record.schema.ts`; `shared_record.py` | SharedFact, SourcedRelation, SharedPerson, SharedFamily, SharedPlace, SharedOrganization, SharedEvent, SharedRecord |
| `site-issue.schema.ts`; `site_issue.py` | IssueMention, IssueMentionsData, ContentItemRef, IssueLifeEvent, IssueLifeEventsData, SiteIssue, SiteArchive |

`ContentItemsData` records the proposed site vocabulary version `0.1.0`.
`SharedRecord` records its shape version `1` and the unchanged sourced-entity
vocabulary `1.0.0`. Proposal status is exported by the site vocabulary; parsing a
proposed concept does not approve or release it.

## Printed words, names and translation

A printed title is optional on a content item and required on a section. Its
text is exactly its addressed words, joined by newlines; a supplied title never
fills that field. Both map through `rico:hasOrHadTitle` to `rico:Title`, with
`rico:textualValue` and `rico:hasTitleType`. The two local title type concepts are
instances of `rico:TitleType` and `skos:Concept`.

A supplied title is required on a content item but optional (omitted or null) on
a printed section. The writer omits a section's supplied title when its members'
English heading answers disagree or are missing; the printed title remains required.

Supplied titles and translations are separate English values with authorship
(`kind: person | model`, `by`, `on`, optional note). Each has a `based_on` value:
the exact `source_text` and one or more printed addresses. An address is the
picture's storage name or URI, a box in that picture's native pixels, and the
text read there. It does not depend on a content item's changing number.
`content_item_id` on a mention is the current join derived from that address.
The twins share the common attributed-English fields; neither translation nor
supplied title inherits from the other.

`IssueMention` requires an explicit `address_grain: words | regions` and a
`printed_name` field. With `words`, the name is nonblank and must occur exactly
in the address texts joined by newlines, as before; each address is within one
of its content item's regions and its text occurs in that region's transcription.
With `regions`, `printed_name` must be null: this person is named somewhere in
the addressed regions, but the printed words have not been located. Null is
required rather than omission so a producer must deliberately record that
limitation; an accidentally missing name does not weaken validation. The grain
is explicit so consumers can distinguish these links without inferring precision
from text or boxes. The proposed site shape's writers must now supply it even
for located names; the released `Mention` shape is unchanged.

For a region mention, `SiteIssue` requires every address to equal one of the
content item's own regions: the same image URI, all four box coordinates and
the complete, unnormalised transcription. A crop, substring, section heading or
another item's region fails. One or more whole regions may be addressed; these
need not exhaust a multi-region item. A writer that knows only the old item link
uses all of that item's regions. `IssueMention` alone can check the grain/name
pair; validating it through `SiteIssue` is required to check region ownership
and equality across the files. The addresses remain the evidence and
`content_item_id` remains their derived join, never the sole anchor.

Old source text is retained after a rereading. `textBasisMatches` /
`text_basis_matches` compares it without normalisation; consumers must withhold
or mark a translation or supplied title whose basis no longer matches. Finding
the address again after a new page reading is the site writer's responsibility.
The schema does not generate titles or certify their editorial distinctness.

## Physical references and sections

The page file stays unchanged: it already has the picture, dimensions, region
boxes and transcriptions, and a nullable `unit_id`. That field points to the new
content item when the region belongs to one; it is null for a section heading.
`heading_blocks` on the section identifies those heading regions. No new page
field is needed. `PrintedSection` avoids colliding with the old `Section`, which
continues to mean a side-list group.
Field names retain `block` because that is the site's existing word for a region.

`SiteIssue` checks the four documents together: dates, unique identifiers,
reciprocal section membership, region ownership, printed addresses, mention and
life-event references. Every region has exactly one owner. `page_blocks` and
`heading_blocks` are in reading order. The page transcriptions retain the printed
line breaks; `full_text` is a site copy assembled from those lines and the program's
recorded broken-word joins.

**Text rule:** `full_text` must match the referenced regions in order at the starts
given by `block_breaks`, allowing only LF preserved or replaced by one space and
line-ending `-`/`־` words joined with that sign retained or removed, with a word
joined across regions placed wholly in the following segment and exactly two LFs
between nonempty segments (the exact legacy blank-line join is also accepted).

`block_breaks` supplies one ordered Unicode code-point start per region, beginning
at zero; a single region accepts either `[]` or `[0]`. The exact legacy join must
have those same region starts, including when a transcription is empty. A carried
first half also removes its preceding space or LF from the earlier segment;
other spaces, punctuation and letters cannot change or move between regions.
For example, regions `A co-` and `operative opens.` may yield
`A\n\ncooperative opens.` with starts `[0, 3]`: the first half is carried forward,
so comparing each segment independently with its region would reject valid text.
The check recognises possible joins; only the writer, which has `find_broken`'s
marks, can certify which joins were recorded. It neither normalises the stored
text nor chooses a join. Hand-made issues that preserve the transcriptions and
join regions by blank lines remain valid with the corresponding starts.

Section headings are excluded from the content items' text. No `category` or
person copies are accepted in the new shapes.
These integrity checks are the site's data rules and the minimum checks for its writer.

`SiteArchive` is an in-memory validation value, not another persisted file. It
joins issues to the shared record, checking persons, places, organisations and
events. `IssueLifeEvent` keeps today's names, dates, descriptions and principal
ids; only its content references become `content_items`. Principals refer to
shared persons. Mention roles remain the released roles, with one or more roles
per occurrence. A signer's role belongs to the mention, not the event's principals.

An issue life event needs no duplicate in the shared record. A content item's
`event_id` may resolve to that issue's life event or to a shared event. `SharedEvent`
remains for the reused production facts' `event_id`, required by
`event_participation`, and for content references to those research events.
The shared `events` list may be empty. If the same event is also described in an
issue, its type must agree with the shared description.

## Keeping the hand-written research

`SharedFact` extends the production `Fact` with `subject_id`, optional `family_id`,
and `representation: structured | prose | image`. It reuses the fact vocabulary,
sources, citations, confidence, status, review and attribution without copying
their definitions. Facts may describe a person, family, place, organisation,
event or relation. Fate must rest on that person's own facts. Source identifiers
and all structured references resolve inside the shared record; place parents
are acyclic. Family membership can be a sourced `membership` fact with `family_id`.

| Existing hand-written field | Preservation in the shared record |
| --- | --- |
| `biographical_narratives` | `other` fact, proposed type `biographical_narrative`, representation `prose`, exact markdown in `value`; original writer retained in qualifiers/attribution |
| `ghetto_role` | `ghetto_role`, or ordinary `office` / `membership` when supported by the source |
| `partisan_activity` | `partisan_service` or membership, unit in `value`, rank/alias/alternate unit in qualifiers; unreviewed activities prose kept as a separate prose fact |
| `headshot_path` | `other`, proposed type `headshot`, representation `image`, exact path in `value` |
| `proposed_relationships` | `SourcedRelation`, reusing `kinship` and released directional relationship types, or `other` / `proposed_type` for an unreleased or ambiguous type; unresolved hints stay in `related_name` without inventing a person |
| `birth_location` | `birth` fact with `place_id`, or source wording in `value` until the place is identified; no date invented |
| `additional_details` | Recognised sourced facts when justified; otherwise exact unreviewed prose under `other` with the original label in qualifiers |

Every such fact or relation requires a citation with a locator and attribution.
An ambiguous relation label is preserved verbatim in `proposed_type`; it must not
be silently narrowed to a released kinship term. Its evidence stays in `value`
or its citation, and its original writer can be retained in qualifiers.
When no underlying historical source was recorded, cite the preserved research
document and its field/record locator as the source of that text. A tool name is
authorship, not historical evidence. Import attribution records the import day;
it must not pretend to know when undated prose was originally written.

Standing uses the existing separate claim and review fields. In the new record,
a proposal is retained as `status: accepted` with pending review; acceptance is
distinguished by approved review, with who and when. Doubt uses `disputed`;
rejection uses `rejected`. This is a reading of the two fields together, not a new
value added to the released status enum. Existing consumers retain their current
interpretation. `shown` on a relation retains permission to show a relative and
does not imply death or fate.

Unreviewed biographies and additional-detail prose keep `representation: prose`
and pending review. `isUnreviewedProse` / `is_unreviewed_prose` identifies them even
when the claim status is accepted. **Do not flatten them into ordinary accepted
facts in the current site's projection:** it treats accepted facts as publishable
without consulting review. The later shared-record projection must withhold
unreviewed prose and preserve the site's living-person presumption. This ticket
adds storage and validation only; it grants no new publication permission.

## Mappings and checks

The pinned lists under `standards/` were read before mapping. Persons, families,
organisations and source/content record resources use EHRI classes. Places use
the specific EHRI city/region/country class where applicable, otherwise RiC-O
Place. Life events use RiC-O Event. Relations use the existing relationship
type's qualification class, not an unconditional historical triple.

Subtypes are local SKOS concepts typed `rico:DocumentaryFormType`. Subjects are
local SKOS concepts because the pinned ontologies supply a subject predicate,
not controlled identifiers for what these content items are about. Title types, printed addresses, text
bases, translation, authorship, mention occurrences, shared-file grouping,
fact subjects/representations, standing, display permission and site copies have declared local
terms with one-line reasons. `vocabulary/site-content.json` records these
mappings; `site-content.profile.ttl` declares the proposed, unreleased concepts.
The released `profile.ttl` is unchanged. Both profiles and all their mappings are
checked against the pinned ontology files, which are untouched.

Mention address grain maps to the declared local property
`pc:site_mention_address_grain`, with literal values `words` and `regions`.
EHRI 0.2.0 has no term for this distinction (its `Region` is a geographic place),
and its RiC-O version, 1.1, has no term distinguishing located name words from
whole printed regions. The mapping therefore stays in the proposed site profile,
beside the existing local mention and printed-address terms.

`bin/verify contract` compares the twins and runs shared fictional fixtures,
including invalid references and pending research. JSON Schema alone cannot
express the semantic refinements; producers must use the runtime validators.
When serialising reused Pydantic pages, preserve omitted fields with
`model_dump(mode='json', exclude_unset=True)`: the old Block's default null
confidence differs from its Zod twin's optional number, and is unchanged here.

The private approval inventory accounts for all 338 category values: 140 carry a
form, 144 a heading, 112 a subject and 38 an unresolved part
(10,493 / 2,644 / 3,516 / 629 content items). These counts overlap: 95 category
values, used by 2,579 content items, carry more than one route. Each value appears
once, with every applicable route recorded separately.
These are proposed routes for labels, not automatic assignments to every content
item bearing them. Null, individual titles, event labels, unclear headings and
structural labels needing a parent decision are retained in the unresolved list.

A retained private script checks the 44 people's specified hand-written fields;
its run validated 102 facts and 113 relations in this shape. The original values were
retained exactly, all reviews stayed pending, and no migration file was written.
It reconstructs all 213 original field values and prints counts per person and
in total; the command is in the private approval sheet.
The committed contract fixtures remain entirely fictional.
