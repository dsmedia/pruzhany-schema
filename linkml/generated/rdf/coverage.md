# Public RDF view coverage

Generated from the LinkML model index and `rdf-profile.yaml`. Every model and field has an explicit export or omission decision. This is the project’s public-view profile, not EHRI ingestion conformance.

Literal formats are checked with an enabled JSON Schema FormatChecker as well as SHACL patterns. RDF lists are checked for structure, order, length and position; arbitrary list cycles are rejected by the runtime before SHACL. Scalar and list constraints come from generated field shapes; position bounds come from the existing Zod tuple contract, cited in the profile.

## Attribution

A public view of Attribution; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `by` | `https://pruzhany.org/ns/sourced-entities#export_Attribution_by` |
| `on` | `https://pruzhany.org/ns/sourced-entities#export_Attribution_on` |
| `note` | Omitted: Absent from this final public view; never recover it from private storage. |


## Citation

A public view of Citation; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `source_id` | `https://pruzhany.org/ns/sourced-entities#export_Citation_source_id` |
| `record_id` | `https://pruzhany.org/ns/sourced-entities#export_Citation_record_id` |
| `page` | `https://pruzhany.org/ns/sourced-entities#export_Citation_page` |
| `scan` | `https://pruzhany.org/ns/sourced-entities#export_Citation_scan` |
| `time` | `https://pruzhany.org/ns/sourced-entities#export_Citation_time` |
| `edition_date` | `https://pruzhany.org/ns/sourced-entities#export_Citation_edition_date` |
| `unit_id` | `https://pruzhany.org/ns/sourced-entities#export_Citation_unit_id` |
| `url` | `https://pruzhany.org/ns/sourced-entities#export_Citation_url` |
| `quote` | `https://pruzhany.org/ns/sourced-entities#export_Citation_quote` |
| `accessed` | `https://pruzhany.org/ns/sourced-entities#export_Citation_accessed` |
| `locator` | Omitted: Absent from this final public view; never recover it from private storage. |
| `note` | Omitted: Absent from this final public view; never recover it from private storage. |
| `public_note` | Omitted: Absent from this final public view; never recover it from private storage. |
| `quote_language` | Omitted: Absent from this final public view; never recover it from private storage. |
| `record_type` | Omitted: Absent from this final public view; never recover it from private storage. |
| `reference_code` | Omitted: Absent from this final public view; never recover it from private storage. |
| `via` | Omitted: Absent from this final public view; never recover it from private storage. |
| `quote_english` | Omitted: Staged English and its attribution remain private until the site publication projection explicitly supports them. |


## LifeEventDate

A public view of LifeEventDate; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `printed` | `https://www.ica.org/standards/RiC/ontology#expressedDate` |
| `printed_calendar` | `https://pruzhany.org/ns/sourced-entities#export_LifeEventDate_printed_calendar` |
| `start` | `https://www.ica.org/standards/RiC/ontology#normalizedDateValue` |
| `qualifier` | `https://www.ica.org/standards/RiC/ontology#dateQualifier` |
| `reported_in` | `https://pruzhany.org/ns/sourced-entities#export_LifeEventDate_reported_in` |
| `record_fact_id` | `https://pruzhany.org/ns/sourced-entities#export_LifeEventDate_record_fact_id` |


## LifeEventMainPerson

A public view of LifeEventMainPerson; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `person_id` | `https://pruzhany.org/ns/sourced-entities#export_LifeEventMainPerson_person_id` |
| `part` | `https://pruzhany.org/ns/sourced-entities#export_LifeEventMainPerson_part` |


## PlaceIdentifier

A public view of PlaceIdentifier; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `source_id` | `https://pruzhany.org/ns/sourced-entities#export_PlaceIdentifier_source_id` |
| `value` | `https://pruzhany.org/ns/sourced-entities#export_PlaceIdentifier_value` |
| `url` | `https://pruzhany.org/ns/sourced-entities#export_PlaceIdentifier_url` |
| `accessed` | `https://pruzhany.org/ns/sourced-entities#export_PlaceIdentifier_accessed` |
| `attribution` | Omitted: Absent from this final public view; never recover it from private storage. |
| `type` | Omitted: Not yet carried by the final public site projection; keep this sourced shared-record field private until that projection is deliberately extended. |


## PrintedAddress

A public view of PrintedAddress; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `image_uri` | `https://pruzhany.org/ns/sourced-entities#export_PrintedAddress_image_uri` |
| `bbox` | `https://pruzhany.org/ns/sourced-entities#export_PrintedAddress_bbox` |
| `text` | `https://pruzhany.org/ns/sourced-entities#export_PrintedAddress_text` |


## Review

A public view of Review; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `state` | `https://pruzhany.org/ns/sourced-entities#export_Review_state` |
| `by` | `https://pruzhany.org/ns/sourced-entities#export_Review_by` |
| `on` | `https://pruzhany.org/ns/sourced-entities#export_Review_on` |


## SharedEvent

A public view of SharedEvent; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `id` | `https://pruzhany.org/ns/sourced-entities#export_SharedEvent_id` |
| `name` | `http://www.w3.org/2000/01/rdf-schema#label` |
| `type` | `https://pruzhany.org/ns/sourced-entities#export_SharedEvent_type` |
| `proposed_type` | `https://pruzhany.org/ns/sourced-entities#export_SharedEvent_proposed_type` |
| `location_id` | `https://pruzhany.org/ns/sourced-entities#export_SharedEvent_location_id` |
| `main_people` | `https://pruzhany.org/ns/sourced-entities#export_SharedEvent_main_people` |
| `dates` | `https://pruzhany.org/ns/sourced-entities#export_SharedEvent_dates` |
| `evidence_basis` | `https://pruzhany.org/ns/sourced-entities#export_SharedEvent_evidence_basis` |
| `description` | Omitted: Absent from this final public view; never recover it from private storage. |


## SharedFact

A public view of SharedFact; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `id` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_id` |
| `subject_id` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#subject` |
| `type` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_type` |
| `proposed_type` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_proposed_type` |
| `value` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_value` |
| `place_id` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_place_id` |
| `organization_id` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_organization_id` |
| `event_id` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_event_id` |
| `related_person_id` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_related_person_id` |
| `relationship_type` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_relationship_type` |
| `related_name` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_related_name` |
| `holocaust_related` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_holocaust_related` |
| `evidence_confidence` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_evidence_confidence` |
| `identity_confidence` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_identity_confidence` |
| `status` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_status` |
| `date` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_date` |
| `qualifiers` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_qualifiers` |
| `citations` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_citations` |
| `review` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_review` |
| `attribution` | `https://pruzhany.org/ns/sourced-entities#export_SharedFact_attribution` |
| `family_id` | Omitted: Absent from this final public view; never recover it from private storage. |
| `representation` | Omitted: Absent from this final public view; never recover it from private storage. |


## SharedOrganization

A public view of SharedOrganization; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `id` | `https://pruzhany.org/ns/sourced-entities#export_SharedOrganization_id` |
| `name` | `http://www.w3.org/2000/01/rdf-schema#label` |
| `names` | Omitted: Absent from this final public view; never recover it from private storage. |
| `identifiers` | Omitted: Not yet carried by the final public site projection; keep this sourced shared-record field private until that projection is deliberately extended. |


## SharedPerson

A public view of SharedPerson; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `id` | `https://pruzhany.org/ns/sourced-entities#export_SharedPerson_id` |
| `name` | `http://www.w3.org/2000/01/rdf-schema#label` |
| `gender` | `https://pruzhany.org/ns/sourced-entities#export_SharedPerson_gender` |
| `fate` | Omitted: Absent from this final public view; never recover it from private storage. |
| `names` | Omitted: Absent from this final public view; never recover it from private storage. |
| `portrait` | Omitted: Absent from this final public view; never recover it from private storage. |
| `identifiers` | Omitted: Not yet carried by the final public site projection; keep this sourced shared-record field private until that projection is deliberately extended. |


## SharedPlace

A public view of SharedPlace; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `id` | `https://pruzhany.org/ns/sourced-entities#export_SharedPlace_id` |
| `name` | `http://www.w3.org/2000/01/rdf-schema#label` |
| `type` | `https://pruzhany.org/ns/sourced-entities#export_SharedPlace_type` |
| `coordinates` | `https://pruzhany.org/ns/sourced-entities#export_SharedPlace_coordinates` |
| `parent_id` | `https://pruzhany.org/ns/sourced-entities#export_SharedPlace_parent_id` |
| `identifiers` | `https://pruzhany.org/ns/sourced-entities#export_SharedPlace_identifiers` |
| `names` | Omitted: Absent from this final public view; never recover it from private storage. |

Public optional field `type`: Some final person-detail files publish only a place identifier and name.

## Source

A public view of Source; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `id` | `https://pruzhany.org/ns/sourced-entities#export_Source_id` |
| `kind` | `https://pruzhany.org/ns/sourced-entities#export_Source_kind` |
| `title` | `http://www.w3.org/2000/01/rdf-schema#label` |
| `work_id` | `https://pruzhany.org/ns/sourced-entities#export_Source_work_id` |
| `author` | `https://pruzhany.org/ns/sourced-entities#export_Source_author` |
| `editor` | `https://pruzhany.org/ns/sourced-entities#export_Source_editor` |
| `published` | `https://pruzhany.org/ns/sourced-entities#export_Source_published` |
| `repository` | `https://pruzhany.org/ns/sourced-entities#export_Source_repository` |
| `url_pattern` | `https://pruzhany.org/ns/sourced-entities#export_Source_url_pattern` |
| `host` | `https://pruzhany.org/ns/sourced-entities#export_Source_host` |
| `dated` | Omitted: Absent from this final public view; never recover it from private storage. |
| `derived_from` | Omitted: Absent from this final public view; never recover it from private storage. |
| `holder_id` | Omitted: Absent from this final public view; never recover it from private storage. |
| `language` | Omitted: Absent from this final public view; never recover it from private storage. |
| `made_by` | Omitted: Absent from this final public view; never recover it from private storage. |
| `private` | Omitted: Absent from this final public view; never recover it from private storage. |
| `quote_condition` | Omitted: Absent from this final public view; never recover it from private storage. |
| `quotes_cleared` | Omitted: Absent from this final public view; never recover it from private storage. |
| `reference_code` | Omitted: Absent from this final public view; never recover it from private storage. |
| `short_name` | Omitted: Absent from this final public view; never recover it from private storage. |
| `subjects` | Omitted: Absent from this final public view; never recover it from private storage. |
| `title_english` | Omitted: Staged English and its attribution remain private until the site publication projection explicitly supports them. |


## SourcedDate

A public view of SourcedDate; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `start` | `https://www.ica.org/standards/RiC/ontology#normalizedDateValue` |
| `end` | `https://pruzhany.org/ns/sourced-entities#export_SourcedDate_end` |
| `precision` | `https://pruzhany.org/ns/sourced-entities#export_SourcedDate_precision` |
| `printed` | `https://www.ica.org/standards/RiC/ontology#expressedDate` |
| `printed_calendar` | `https://pruzhany.org/ns/sourced-entities#export_SourcedDate_printed_calendar` |
| `inferred` | `https://pruzhany.org/ns/sourced-entities#export_SourcedDate_inferred` |


## SourcedRelation

A public view of SourcedRelation; source-scoped values are retained without asserting an unqualified historical relationship.

| Field | Export predicate or omission |
|---|---|
| `subject_id` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#subject` |
| `related_person_id` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#object` |
| `relationship_type` | `https://pruzhany.org/ns/sourced-entities#export_SourcedRelation_relationship_type` |
| `review` | `https://pruzhany.org/ns/sourced-entities#export_SourcedRelation_review` |
| `attribution` | Omitted: Absent from this final public view; never recover it from private storage. |
| `citations` | Omitted: Absent from this final public view; never recover it from private storage. |
| `date` | Omitted: Absent from this final public view; never recover it from private storage. |
| `event_id` | Omitted: Absent from this final public view; never recover it from private storage. |
| `evidence_confidence` | Omitted: Absent from this final public view; never recover it from private storage. |
| `family_id` | Omitted: Absent from this final public view; never recover it from private storage. |
| `holocaust_related` | Omitted: Absent from this final public view; never recover it from private storage. |
| `id` | Omitted: Absent from this final public view; never recover it from private storage. |
| `identity_confidence` | Omitted: Absent from this final public view; never recover it from private storage. |
| `organization_id` | Omitted: Absent from this final public view; never recover it from private storage. |
| `place_id` | Omitted: Absent from this final public view; never recover it from private storage. |
| `proposed_type` | Omitted: Absent from this final public view; never recover it from private storage. |
| `qualifiers` | Omitted: Absent from this final public view; never recover it from private storage. |
| `related_name` | Omitted: Absent from this final public view; never recover it from private storage. |
| `shown` | Omitted: Absent from this final public view; never recover it from private storage. |
| `status` | Omitted: Absent from this final public view; never recover it from private storage. |
| `type` | Omitted: Absent from this final public view; never recover it from private storage. |
| `value` | Omitted: Absent from this final public view; never recover it from private storage. |

Public required field `related_person_id`: A displayed confirmed relationship has two known public endpoints.
Public required field `relationship_type`: The displayed direction must be explicit.

## Models outside this view

- `Authorship`: Outside the public shared-record export; this layer keeps its current format.
- `Block`: Outside the public shared-record export; this layer keeps its current format.
- `ContentItem`: Outside the public shared-record export; this layer keeps its current format.
- `ContentItemBlockRef`: Outside the public shared-record export; this layer keeps its current format.
- `ContentItemRef`: Outside the public shared-record export; this layer keeps its current format.
- `ContentItemsData`: Outside the public shared-record export; this layer keeps its current format.
- `CrossReference`: Outside the public shared-record export; this layer keeps its current format.
- `Edition`: Outside the public shared-record export; this layer keeps its current format.
- `EditionsCatalog`: Outside the public shared-record export; this layer keeps its current format.
- `EnglishCheck`: Outside the public shared-record export; this layer keeps its current format.
- `ExternalReference`: Outside the public shared-record export; this layer keeps its current format.
- `Fact`: Outside the public shared-record export; this layer keeps its current format.
- `FactQualifiers`: Outside the public shared-record export; this layer keeps its current format.
- `Fate`: Outside the public shared-record export; this layer keeps its current format.
- `HistoricalEvent`: Outside the public shared-record export; this layer keeps its current format.
- `Holder`: Outside the public shared-record export; this layer keeps its current format.
- `Holiday`: Outside the public shared-record export; this layer keeps its current format.
- `IssueLifeEvent`: Outside the public shared-record export; this layer keeps its current format.
- `IssueLifeEventsData`: Outside the public shared-record export; this layer keeps its current format.
- `IssueMention`: Outside the public shared-record export; this layer keeps its current format.
- `IssueMentionsData`: Outside the public shared-record export; this layer keeps its current format.
- `Media`: Outside the public shared-record export; this layer keeps its current format.
- `MediaConsent`: Outside the public shared-record export; this layer keeps its current format.
- `MediaConsentScope`: Outside the public shared-record export; this layer keeps its current format.
- `MediaDecision`: Outside the public shared-record export; this layer keeps its current format.
- `MediaDepicted`: Outside the public shared-record export; this layer keeps its current format.
- `MediaDerivative`: Outside the public shared-record export; this layer keeps its current format.
- `MediaFamilyWords`: Outside the public shared-record export; this layer keeps its current format.
- `MediaFixity`: Outside the public shared-record export; this layer keeps its current format.
- `MediaMaster`: Outside the public shared-record export; this layer keeps its current format.
- `MediaPortrait`: Outside the public shared-record export; this layer keeps its current format.
- `MediaRegion`: Outside the public shared-record export; this layer keeps its current format.
- `MediaText`: Outside the public shared-record export; this layer keeps its current format.
- `MediaWithdrawal`: Outside the public shared-record export; this layer keeps its current format.
- `Mention`: Outside the public shared-record export; this layer keeps its current format.
- `Name`: Outside the public shared-record export; this layer keeps its current format.
- `Page`: Outside the public shared-record export; this layer keeps its current format.
- `PagesData`: Outside the public shared-record export; this layer keeps its current format.
- `PrintedSection`: Outside the public shared-record export; this layer keeps its current format.
- `PrintedTitle`: Outside the public shared-record export; this layer keeps its current format.
- `PublicMedia`: Outside the public shared-record export; this layer keeps its current format.
- `ReadingStatus`: Outside the public shared-record export; this layer keeps its current format.
- `SharedFamily`: Outside the public shared-record export; this layer keeps its current format.
- `SharedName`: Outside the public shared-record export; this layer keeps its current format.
- `SharedRecord`: Outside the public shared-record export; this layer keeps its current format.
- `SiteCitation`: Outside the public shared-record export; this layer keeps its current format.
- `SourceDerivation`: Outside the public shared-record export; this layer keeps its current format.
- `SuppliedTitle`: Outside the public shared-record export; this layer keeps its current format.
- `TextBasis`: Outside the public shared-record export; this layer keeps its current format.
- `TitleCheck`: Outside the public shared-record export; this layer keeps its current format.
- `Translation`: Outside the public shared-record export; this layer keeps its current format.
- `TranslationCheck`: Outside the public shared-record export; this layer keeps its current format.
- `CitedTextBasis`: Outside the public shared-record export; citation/source English requires an explicit publication projection.
- `CitedTranslation`: Outside the public shared-record export; citation/source English requires an explicit publication projection.
