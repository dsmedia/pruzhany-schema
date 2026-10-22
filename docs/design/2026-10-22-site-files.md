# The proposed site files beside the old shapes

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

Supplied titles and translations are separate English values with authorship
(`kind: person | model`, `by`, `on`, optional note). Each has a `based_on` value:
the exact `source_text` and one or more printed addresses. An address is the
picture's storage name or URI, a box in that picture's native pixels, and the
text read there. It does not depend on a content item's changing number.
`content_item_id` on a mention is the current join derived from that address.

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

`SiteIssue` checks the four documents together: dates, unique identifiers,
reciprocal section membership, region ownership, printed addresses, mention and
life-event references. Every region has exactly one owner. `page_blocks` and
`heading_blocks` are in reading order. In the new file, `full_text` is a site copy
of the referenced block transcriptions joined by two newlines. The writer builds
those transcriptions from the physical source's lines first. `block_breaks` are
ordered Unicode code-point offsets. Section headings are excluded from the
content items' text. No `category` or person copies are accepted in the new shapes.

`SiteArchive` is an in-memory validation value, not another persisted file. It
joins issues to the shared record, checking persons, places, organisations and
events. `IssueLifeEvent` keeps today's names, dates, descriptions and principal
ids; only its content references become `content_items`. Principals refer to
shared persons. Mention roles remain the released roles, with one or more roles
per occurrence. A signer's role belongs to the mention, not the event's principals.

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
not this newspaper's topic identifiers. Title types, printed addresses, text
bases, translation, authorship, mention occurrences, shared-file grouping,
fact subjects/representations, standing, display permission and site copies have declared local
terms with one-line reasons. `vocabulary/site-content.json` records these
mappings; `profile.ttl` declares the concepts. Pinned ontology files are untouched.

`bin/verify contract` compares the twins and runs shared fictional fixtures,
including invalid references and pending research. JSON Schema alone cannot
express the semantic refinements; producers must use the runtime validators.
When serialising reused Pydantic pages, preserve omitted fields with
`model_dump(mode='json', exclude_unset=True)`: the old Block's default null
confidence differs from its Zod twin's optional number, and is unchanged here.

The private approval inventory accounts for all 338 category values: 139 form,
143 heading, 18 subject, 38 unresolved (10,492 / 2,641 / 940 / 629 content items).
These are proposed routes for labels, not automatic assignments to every content
item bearing them. Null, individual titles, event labels, unclear headings and
structural labels needing a parent decision are retained in the unresolved list.

A read-only preservation check of the 44 people's specified hand-written fields
validated 102 facts and 113 relations in this shape. The original values were
retained exactly, all reviews stayed pending, and no migration file was written.
The committed contract fixtures remain entirely fictional.
