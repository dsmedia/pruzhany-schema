# The Pruzhany data dictionary

This is the guide to the data behind the Pruzhany newspaper: its pages and pieces, the people and events it names, and the evidence for what we say about them.

LinkML defines the kinds and fields below and generates the Python models. The website’s Zod validators and the retained Python checks still enforce the rules about evidence, dates, relationships and publication. Passing a schema checks the form of a record, not whether a reading or historical claim is correct. Identity, trust, rights and release readiness have their own requirements in the record catalog.

The four issue documents, the editions catalog and the shared record each have a generated JSON Schema. The shared record is checked after its 256 storage shards have been joined. Stored identifiers and file shapes are unchanged.

“Required” in the tables means required by LinkML. Some runtime validators require a key while accepting null; those differences are listed under “Validator responsibilities”. An optional LinkML field generally also accepts null. Value ranges named in the tables are defined in “Types and vocabularies”. Mappings describe alignment with the pinned EHRI and RiC-O terms; they do not claim EHRI acceptance.

Definition fingerprint: `cb039975038866654737b5729cd33d3975ea4f53b121291dc3b8325a5d82f35b`.

## What the Pruzhany issue documents share

### Authorship

Who wrote a supplied title, a translation or a check of one, a person or a model, and on which day.

Meaning: pc:site_authorship (exact mappings).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `by` | Who made it or allowed it: a person, a session or a program. | NonBlankText | Yes | No direct mapping recorded |
| `kind` | Whether a person or a model wrote it. | AuthorshipKind | Yes | No direct mapping recorded |
| `note` | A note on how or why. | string | No | No direct mapping recorded |
| `on` | The day it was made or allowed. | IsoDay | Yes | No direct mapping recorded |

Source: `linkml/schema/site_common.yaml`.

### ContentItemBlockRef

The regions of one page that a content item or a section heading covers, in reading order.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `block_ids` | The regions on that page, by their ids in the pages document, in reading order. | list of NonBlankText; minimum items: 1 | Yes | No direct mapping recorded |
| `page_id` | The page, by its id in the pages document. | NonBlankText | Yes | No direct mapping recorded |

Source: `linkml/schema/site_common.yaml`.

### CrossReference

A link from one content item to another in the same issue, with how sure it is and why.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `confidence` | How sure the link is, from 0 to 1. | float | Yes | No direct mapping recorded |
| `evidence` | What shows the link, in words. | string | Yes | No direct mapping recorded |
| `relationship` | What kind of link it is, in words. | string | Yes | No direct mapping recorded |
| `target_id` | The id of the content item linked to. | string | Yes | No direct mapping recorded |

Source: `linkml/schema/site_common.yaml`.

### EnglishCheck

A later, separate check of one English field against one exact reading of the printed text, bound to both and to the judgement kept by their digests.

Meaning: rico:Activity (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `attribution` | Who checked it, and on which day. | Authorship | Yes | No direct mapping recorded |
| `english_sha256` | The SHA-256 digest of the checked English field's exact UTF-8 bytes. | Sha256Hex | Yes | pc:site_english_sha256 (slot uri) |
| `judgement_id` | The kept judgement, by an id without spaces followed by the field it judged, :title or :text. | string; pattern: ^[^\s\u0085\uFEFF]+:(title\|text)$(?![\s\S]) | Yes | No direct mapping recorded |
| `judgement_sha256` | The SHA-256 digest of the kept judgement file's exact bytes. | Sha256Hex | Yes | pc:site_judgement_sha256 (slot uri) |
| `reading_id` | The reading of the printed text that the English was checked against. | NonBlankText | Yes | No direct mapping recorded |
| `reading_sha256` | The SHA-256 digest of that reading's exact UTF-8 bytes. | Sha256Hex | Yes | pc:site_reading_sha256 (slot uri) |

Source: `linkml/schema/site_common.yaml`.

### PrintedAddress

Where some printed words stand: the page picture, a box on it in the picture's own pixels, and the words read in that box.

Meaning: pc:site_printed_address (exact mappings).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `bbox` | The box on the picture: left, top, width and height, in the picture's pixels. | list of NonNegativeNumber; minimum items: 4; maximum items: 4 | Yes | No direct mapping recorded |
| `image_uri` | The page picture the box is on, by its name or address. | NonBlankText | Yes | No direct mapping recorded |
| `text` | The words read in the box, exactly as read; empty for a patch with no readable line. | string | Yes | No direct mapping recorded |

Source: `linkml/schema/site_common.yaml`.

### PrintedTitle

A title as printed in the paper: its words and where each line of them stands.

Meaning: rico:Title (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `addresses` | Where each line of the title is printed, in order. | list of PrintedAddress; minimum items: 1 | Yes | No direct mapping recorded |
| `text` | The printed words, its lines joined by line breaks. | NonBlankText | Yes | rico:textualValue (slot uri) |

Source: `linkml/schema/site_common.yaml`.

### SuppliedTitle

A title supplied in English for a content item or section, with what it was made from, who made it and, where one was made, its later check.

Meaning: rico:Title (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `attribution` | Who wrote the title, and on which day. | Authorship | Yes | No direct mapping recorded |
| `based_on` | The exact printed text the title was made from, and where it is printed. | TextBasis | Yes | No direct mapping recorded |
| `checked_against` | A later check of this title against the reading, where one was made. | TitleCheck | No | pc:site_checked_against_text (exact mappings) |
| `language` | The title's language, always English (en). | string; fixed value: en | Yes | No direct mapping recorded |
| `text` | The English title. | NonBlankText | Yes | rico:textualValue (slot uri) |

Source: `linkml/schema/site_common.yaml`.

### TextBasis

The exact text a translation or supplied title was made from, and where it is printed, kept even after the text is read again.

Meaning: pc:site_text_basis (exact mappings).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `addresses` | Where that text is printed, one address a line or patch. | list of PrintedAddress; minimum items: 1 | Yes | No direct mapping recorded |
| `source_text` | The text used, exactly, never normalised or replaced by a later reading. | string | Yes | No direct mapping recorded |

Source: `linkml/schema/site_common.yaml`.

### TitleCheck

A check of a supplied title's English.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `attribution` | Who checked it, and on which day. | Authorship | Yes | No direct mapping recorded |
| `english_sha256` | The SHA-256 digest of the checked English field's exact UTF-8 bytes. | Sha256Hex | Yes | pc:site_english_sha256 (slot uri) |
| `judgement_id` | The kept judgement, by an id without spaces followed by the field it judged, :title or :text. | string; pattern: ^[^\s\u0085\uFEFF]+:title$(?![\s\S]) | Yes | No direct mapping recorded |
| `judgement_sha256` | The SHA-256 digest of the kept judgement file's exact bytes. | Sha256Hex | Yes | pc:site_judgement_sha256 (slot uri) |
| `reading_id` | The reading of the printed text that the English was checked against. | NonBlankText | Yes | No direct mapping recorded |
| `reading_sha256` | The SHA-256 digest of that reading's exact UTF-8 bytes. | Sha256Hex | Yes | pc:site_reading_sha256 (slot uri) |

Source: `linkml/schema/site_common.yaml`.

### Translation

An English translation of a content item's printed text, with the exact text it was made from, who made it and, where one was made, its later check.

Meaning: pc:site_translation (exact mappings).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `attribution` | Who translated it, and on which day. | Authorship | Yes | No direct mapping recorded |
| `based_on` | The exact printed text translated, and where it is printed. | TextBasis | Yes | No direct mapping recorded |
| `checked_against` | A later check of this translation against the reading, where one was made. | TranslationCheck | No | pc:site_checked_against_text (exact mappings) |
| `language` | The translation's language, always English (en). | string; fixed value: en | Yes | No direct mapping recorded |
| `text` | The English text. | NonBlankText | Yes | No direct mapping recorded |

Source: `linkml/schema/site_common.yaml`.

### TranslationCheck

A check of a translation's English.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `attribution` | Who checked it, and on which day. | Authorship | Yes | No direct mapping recorded |
| `english_sha256` | The SHA-256 digest of the checked English field's exact UTF-8 bytes. | Sha256Hex | Yes | pc:site_english_sha256 (slot uri) |
| `judgement_id` | The kept judgement, by an id without spaces followed by the field it judged, :title or :text. | string; pattern: ^[^\s\u0085\uFEFF]+:text$(?![\s\S]) | Yes | No direct mapping recorded |
| `judgement_sha256` | The SHA-256 digest of the kept judgement file's exact bytes. | Sha256Hex | Yes | pc:site_judgement_sha256 (slot uri) |
| `reading_id` | The reading of the printed text that the English was checked against. | NonBlankText | Yes | No direct mapping recorded |
| `reading_sha256` | The SHA-256 digest of that reading's exact UTF-8 bytes. | Sha256Hex | Yes | pc:site_reading_sha256 (slot uri) |

Source: `linkml/schema/site_common.yaml`.

## The pages document of a Pruzhany issue

### Block

One region of print on a page, its box and the words read in it, belonging to one content item, or to no item when it is a section heading.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `bbox` | The region's box on the page picture: left, top, width and height, in the picture's pixels. | list of NonNegativeInteger; minimum items: 4; maximum items: 4 | Yes | No direct mapping recorded |
| `confidence` | How sure the reading is, from 0 to 1, where it was recorded. | float | No | No direct mapping recorded |
| `id` | The region's id, such as blk-p4-001. | string | Yes | No direct mapping recorded |
| `image_crop` | A picture of the region alone, by its path, where one was made. | string | No | No direct mapping recorded |
| `transcription` | The words read in the region, its lines separated by line breaks. | string | Yes | No direct mapping recorded |
| `unit_id` | The content item the region belongs to, by its id; null for a region that is a section's heading. | string | No | No direct mapping recorded |

Source: `linkml/schema/pages.yaml`.

### Page

One printed page of the issue: its picture, its size and its regions of print.

Meaning: schema:CreativeWork (close mappings).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `blocks` | The regions of print on the page. | list of Block | Yes | No direct mapping recorded |
| `dimensions` | The picture's width and height, in its pixels. | list of integer; minimum items: 2; maximum items: 2 | Yes | No direct mapping recorded |
| `id` | The page's id, such as page-1938-12-16-4. | string | Yes | No direct mapping recorded |
| `image_uri` | The page's picture, by its name or address. | string | Yes | No direct mapping recorded |
| `issue_date` | The date of the issue the page belongs to, written YYYY-MM-DD. | string | Yes | No direct mapping recorded |
| `page_number` | The page's number within the issue, from 1. | integer | Yes | No direct mapping recorded |

Source: `linkml/schema/pages.yaml`.

### PagesData

One issue's pages document: the issue's date and its pages in order.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `edition_date` | The issue's date, written YYYY-MM-DD. | string | Yes | No direct mapping recorded |
| `pages` | The issue's pages. | list of Page | Yes | No direct mapping recorded |

Source: `linkml/schema/pages.yaml`.

## The content items document of a Pruzhany issue

### ContentItem

One article, notice, greeting or advertisement of the issue: its kind, its titles, its text and English, the regions it is printed in and what it names.

Meaning: ehri:RecordResource (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `block_breaks` | Where each region's text begins in the full text, counted in Unicode code points. | list of NonNegativeInteger | Yes | pc:site_site_copy (related mappings) |
| `cross_references` | Links from this content item to others in the issue. | list of CrossReference | Yes | No direct mapping recorded |
| `event_id` | The life event the content item prints, by the event's id, where it prints one. | NonBlankText | No | No direct mapping recorded |
| `full_text` | The content item's printed text, a copy made for the site from the lines of its regions. | string | Yes | pc:site_site_copy (related mappings) |
| `id` | The content item's id within the issue. | NonBlankText | Yes | No direct mapping recorded |
| `location_ids` | The places the content item names, by their ids in the shared record. | list of NonBlankText | Yes | No direct mapping recorded |
| `organization_ids` | The organisations the content item names, by their ids in the shared record. | list of NonBlankText | Yes | No direct mapping recorded |
| `page_blocks` | The regions the content item is printed in, page by page, in reading order. | list of ContentItemBlockRef; minimum items: 1 | Yes | pc:site_site_copy (related mappings) |
| `printed_title` | The title as printed above the content item, where it has one. | PrintedTitle | No | rico:hasOrHadTitle (slot uri) |
| `reading_status` | How far the text and the English have been checked; left out or null where it is not recorded. | ReadingStatus | No | pc:site_reading_status (exact mappings) |
| `section_id` | The printed section the content item stands under, by the section's id, where it stands under one. | NonBlankText | No | No direct mapping recorded |
| `subject_ids` | What the content item is about, as subjects of the site-content vocabulary. | list of Subjects | Yes | rico:hasOrHadSubject (slot uri) |
| `subtype` | The narrower form the content item takes within its kind, such as a wedding greeting within advertisements, where one is known. | ContentItemSubtypes | No | rico:hasDocumentaryFormType (slot uri) |
| `supplied_title` | A title in English supplied for the content item. | SuppliedTitle | Yes | rico:hasOrHadTitle (slot uri) |
| `translation` | The content item's text in English, where it has been translated. | Translation | No | No direct mapping recorded |
| `type` | The content item's kind, one of Impresso's content item types. | ImpressoTypes | Yes | No direct mapping recorded |

Source: `linkml/schema/content_items.yaml`.

### ContentItemsData

One issue's content items document: the issue's date, the vocabulary version its values are from, its content items and its printed sections.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `content_items` | The issue's content items. | list of ContentItem | Yes | No direct mapping recorded |
| `issue_date` | The issue's date, written YYYY-MM-DD. | IsoDay | Yes | No direct mapping recorded |
| `sections` | The issue's printed sections. | list of PrintedSection | Yes | No direct mapping recorded |
| `vocabulary_version` | The version of the site-content vocabulary whose values the document uses: one of the versions the current vocabulary accepts as compatible. | string; pattern: ^(0\.1\.0\|1\.0\.0)$(?![\s\S]) | Yes | No direct mapping recorded |

Source: `linkml/schema/content_items.yaml`.

### PrintedSection

A printed heading and the content items that stand beneath it, such as the title "What is heard in town?" over the town's news.

Meaning: ehri:RecordSet (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `content_item_ids` | The content items beneath the heading, by their ids. | list of NonBlankText; minimum items: 1 | Yes | rico:includesOrIncluded (slot uri) |
| `heading_blocks` | The regions the heading is printed in, page by page. | list of ContentItemBlockRef; minimum items: 1 | Yes | No direct mapping recorded |
| `id` | The section's id within the issue. | NonBlankText | Yes | No direct mapping recorded |
| `printed_title` | The heading as printed. | PrintedTitle | Yes | rico:hasOrHadTitle (slot uri) |
| `supplied_title` | A title in English supplied for the heading, where one was made. | SuppliedTitle | No | rico:hasOrHadTitle (slot uri) |

Source: `linkml/schema/content_items.yaml`.

### ReadingStatus

How far a content item's text and its English have been checked, each recorded on its own; null for either means it is not recorded, not that it was reviewed.

Meaning: pc:site_reading_status (exact mappings).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `english` | How far the English has been checked; null where not recorded. | ReadingStatusValue | No | No direct mapping recorded |
| `text` | How far the printed text has been checked; null where not recorded. | ReadingStatusValue | No | No direct mapping recorded |

Source: `linkml/schema/content_items.yaml`.

## The mentions document of a Pruzhany issue

### IssueMention

A person of the shared record named in a content item, pinned to the printed words of the name or to whole regions, with the person's roles there. A mention alone does not say the content item is about the person.

Meaning: pc:site_mention (exact mappings).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `address_grain` | Whether the mention is pinned to the name's words or only to whole regions. | AddressGrain | Yes | pc:site_mention_address_grain (slot uri) |
| `addresses` | Where the name stands: the words of the name, or the whole regions it is in. | list of PrintedAddress; minimum items: 1 | Yes | No direct mapping recorded |
| `content_item_id` | The content item the name stands in, by its id in the content items document. | NonBlankText | Yes | No direct mapping recorded |
| `function` | The person's occupation or part in the content item, in a few words, such as bride, mourner or well-wisher. | string | No | No direct mapping recorded |
| `id` | The mention's id within the issue. | NonBlankText | Yes | No direct mapping recorded |
| `person_id` | The person named, by their id in the shared record. | NonBlankText | Yes | No direct mapping recorded |
| `printed_name` | The name as printed, found at the mention's addresses; null when the mention is pinned only to whole regions. | NonBlankText | No | No direct mapping recorded |
| `roles` | The person's roles in the content item, such as the deceased or a mourner. | list of MentionRoles; minimum items: 1 | Yes | No direct mapping recorded |
| `title` | An honorific printed with the name, such as Rabbi or Dr., where one is kept. | string | No | No direct mapping recorded |
| `wkd_id` | The person's Wikidata id, where one is known. | string | No | No direct mapping recorded |

Source: `linkml/schema/mentions.yaml`.

### IssueMentionsData

One issue's mentions document: the issue's date and its mentions.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `issue_date` | The issue's date, written YYYY-MM-DD. | IsoDay | Yes | No direct mapping recorded |
| `mentions` | The issue's mentions. | list of IssueMention | Yes | No direct mapping recorded |

Source: `linkml/schema/mentions.yaml`.

## The life events document of a Pruzhany issue

### ContentItemRef

A content item that prints a life event, and the part it plays: the announcement itself, a greeting, a condolence, a mention or an advertisement.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `content_item_id` | The content item, by its id in the content items document. | NonBlankText | Yes | No direct mapping recorded |
| `role` | The part the content item plays for the event, not any person's role. | ContentUnitRoles | Yes | No direct mapping recorded |

Source: `linkml/schema/life_events.yaml`.

### IssueLifeEvent

A life event of the shared record as this issue prints it: the content items that print it, each with its part.

Meaning: rico:Event (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `content_items` | The content items of the issue that print the event. | list of ContentItemRef; minimum items: 1 | Yes | No direct mapping recorded |
| `id` | The life event, by its id in the shared record. | NonBlankText | Yes | No direct mapping recorded |

Source: `linkml/schema/life_events.yaml`.

### IssueLifeEventsData

One issue's life events document: the issue's date and the life events it prints.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `issue_date` | The issue's date, written YYYY-MM-DD. | IsoDay | Yes | No direct mapping recorded |
| `life_events` | The life events the issue prints. | list of IssueLifeEvent | Yes | No direct mapping recorded |

Source: `linkml/schema/life_events.yaml`.

## The catalog of Pruzhany editions

### Edition

One edition of the paper: its date in the common calendar and in the Hebrew one, and the holiday it falls on, if any.

Meaning: schema:PublicationIssue (close mappings).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `date` | The edition's date, written YYYY-MM-DD. | IsoDay | Yes | No direct mapping recorded |
| `hebrewDate` | The edition's date in the Hebrew calendar, written in Hebrew letters. | string | Yes | No direct mapping recorded |
| `hebrewMonth` | The Hebrew month, by its number from 1 to 13, counted from Nisan. | integer; minimum: 1; maximum: 13 | Yes | No direct mapping recorded |
| `hebrewYear` | The Hebrew year, such as 5699. | integer; minimum: -9007199254740991; maximum: 9007199254740991 | Yes | No direct mapping recorded |
| `holiday` | The holiday the edition falls on or near, where there is one. | string | No | No direct mapping recorded |

Source: `linkml/schema/editions.yaml`.

### EditionsCatalog

The catalog of editions: every edition, the holidays and historical events beside them, and the dates available on the site.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `availableDates` | The dates of the editions whose pages are on the site. | list of IsoDay | Yes | No direct mapping recorded |
| `editions` | Every edition of the paper, with its Hebrew date. | list of Edition | Yes | No direct mapping recorded |
| `historicalEvents` | Events in the world outside the town that the calendar marks. | list of HistoricalEvent | Yes | No direct mapping recorded |
| `holidays` | The Jewish holidays of the paper's years. | list of Holiday | Yes | No direct mapping recorded |

Source: `linkml/schema/editions.yaml`.

### HistoricalEvent

An event in the world outside the town, such as Kristallnacht, on a day or over a span of days.

Meaning: rico:Event (close mappings).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `date` | The day the event began, written YYYY-MM-DD. | IsoDay | Yes | No direct mapping recorded |
| `description` | What happened, in a sentence or two. | string | Yes | No direct mapping recorded |
| `endDate` | The day the event ended, where it lasted more than a day. | IsoDay | No | No direct mapping recorded |
| `name` | The event's name in English. | string | Yes | No direct mapping recorded |

Source: `linkml/schema/editions.yaml`.

### Holiday

A Jewish holiday on a given day.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `date` | The holiday's day, written YYYY-MM-DD. | IsoDay | Yes | No direct mapping recorded |
| `hebrewName` | The holiday's name in Hebrew letters, where it is given. | string | No | No direct mapping recorded |
| `name` | The holiday's name in Latin letters, such as Purim or Pesach. | string | Yes | No direct mapping recorded |

Source: `linkml/schema/editions.yaml`.

## The sourced entities of the Pruzhany record

### Attribution

Who made or allowed something, on what day, with an optional note.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `by` | Who made it or allowed it: a person, a session or a program. | NonBlankText | Yes | No direct mapping recorded |
| `note` | A note on how or why. | string | No | No direct mapping recorded |
| `on` | The day it was made or allowed. | IsoDay | Yes | No direct mapping recorded |

Source: `linkml/schema/sourced_entities.yaml`.

### Citation

Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `accessed` | The day a person read the record. | IsoDay | No | No direct mapping recorded |
| `edition_date` | The day of the paper's issue cited, written YYYY-MM-DD. | string | No | No direct mapping recorded |
| `locator` | An internal pointer into the project's files; never published and never a holder's record number. | NonBlankText | No | pc:site_citation_locator (slot uri) |
| `note` | Our private note on the evidence; never published. | string | No | No direct mapping recorded |
| `page` | The page, folio or entry cited. | string | No | No direct mapping recorded |
| `public_note` | Our reviewed words for the page about this evidence, apart from the record's quote. | NonBlankText | No | pc:site_citation_public_note (slot uri) |
| `quote` | The record's own words, exactly. | string | No | No direct mapping recorded |
| `quote_language` | The quote's language, where it is not the source's (a translation). | LanguageTag | No | rico:hasOrHadLanguage (slot uri) |
| `record_id` | The holder's own number for the record, such as a Yad Vashem record number. | string | No | rico:hasOrHadIdentifier (slot uri) |
| `record_type` | The holder's own type of the record, such as Page of Testimony. | NonBlankText | No | rico:hasDocumentaryFormType (slot uri) |
| `reference_code` | The holder's reference of the document cited, where the source is a set of many. | NonBlankText | No | rico:hasOrHadIdentifier (slot uri) |
| `scan` | The scan or image cited. | string | No | No direct mapping recorded |
| `source_id` | The record the statement rests on (the original where it is known), by its id in the record's sources. | NonBlankText | Yes | rico:isEvidencedBy (slot uri) |
| `time` | The time in a recording. | string | No | No direct mapping recorded |
| `unit_id` | The piece of the paper cited, by its content item id. | string | No | No direct mapping recorded |
| `url` | The record's web address. | HttpsUri | No | No direct mapping recorded |
| `via` | The one source actually read, a copy or a transcription of the original, by its id. | NonBlankText | No | No direct mapping recorded |

Source: `linkml/schema/sourced_entities.yaml`.

### Fact

One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes).

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `attribution` | Who recorded the statement, and on what day. | Attribution | Yes | No direct mapping recorded |
| `citations` | The evidence: where in which sources the statement is found. | list of Citation; minimum items: 1 | Yes | No direct mapping recorded |
| `date` | When, as the source gives it. | SourcedDate | No | No direct mapping recorded |
| `event_id` | The life event the statement concerns, by its id in the record. | NonBlankText | No | No direct mapping recorded |
| `evidence_confidence` | How sure the evidence makes the statement. | Confidence | Yes | rico:relationCertainty (slot uri) |
| `holocaust_related` | True when the statement concerns the Holocaust. | boolean | No | No direct mapping recorded |
| `id` | The fact's id in the record. | NonBlankText | Yes | No direct mapping recorded |
| `identity_confidence` | How sure it is that the statement is about this person. | Confidence | Yes | No direct mapping recorded |
| `organization_id` | The organisation the statement concerns, by its id in the record. | NonBlankText | No | No direct mapping recorded |
| `place_id` | Where, by the place's id in the record. | NonBlankText | No | No direct mapping recorded |
| `proposed_type` | For a statement of type other: the type proposed for it, awaiting the owner's approval. | NonBlankText | No | No direct mapping recorded |
| `qualifiers` | More about the statement, as named texts. | FactQualifiers | No | No direct mapping recorded |
| `related_name` | For kinship: the relative's name, where the relative has no person of their own. | NonBlankText | No | No direct mapping recorded |
| `related_person_id` | For kinship: the relative, by the person's id in the record. | NonBlankText | No | No direct mapping recorded |
| `relationship_type` | For kinship: how the relative is related, from the subject to the relative. | RelationshipTypes | No | No direct mapping recorded |
| `review` | Whether a person has reviewed the statement. | Review | Yes | pc:site_standing (related mappings) |
| `status` | The statement's standing: proposed, accepted, disputed or rejected. | ClaimStatus | Yes | pc:site_standing (related mappings) |
| `type` | What the statement is about: a birth, a death, a residence, an occupation and so on. | FactTypes | Yes | No direct mapping recorded |
| `value` | The statement's words or value, such as an occupation. | NonBlankText | No | No direct mapping recorded |

Source: `linkml/schema/sourced_entities.yaml`.

### FactQualifiers

More about a fact, as named texts: how many children a notice names, how a statement is supported and the like.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| Arbitrary keys | A dictionary of named text values | string values | No fixed keys | No direct mapping recorded |

Source: `linkml/schema/sourced_entities.yaml`.

### Fate

What became of a person in the Holocaust, as far as the record shows, the facts it rests on and its review.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `confidence` | How sure the outcome is. | Confidence | Yes | No direct mapping recorded |
| `outcome` | What became of the person: unknown, perished, survived, died before, or not applicable. | FateOutcomes | Yes | No direct mapping recorded |
| `rests_on` | The facts the outcome rests on, by their ids in the record. | list of string | Yes | No direct mapping recorded |
| `review` | Whether a person has reviewed the outcome. | Review | Yes | No direct mapping recorded |
| `summary` | A short summary in words. | string | No | No direct mapping recorded |

Source: `linkml/schema/sourced_entities.yaml`.

### Mention

The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `function` | A function printed with the name. | string | No | No direct mapping recorded |
| `id` | The mention's id. | NonBlankText | Yes | No direct mapping recorded |
| `person_id` | The person mentioned, by the person's id. | NonBlankText | Yes | No direct mapping recorded |
| `printed_name` | The name as printed. | NonBlankText | Yes | No direct mapping recorded |
| `role` | The person's role in the piece. | MentionRoles | No | No direct mapping recorded |
| `title` | A title printed with the name. | string | No | No direct mapping recorded |
| `unit_id` | The piece of the paper the person is mentioned in, by its id. | NonBlankText | Yes | No direct mapping recorded |
| `wkd_id` | The person's Wikidata id, where one is linked. | string | No | No direct mapping recorded |

Source: `linkml/schema/sourced_entities.yaml`.

### Name

One name of a person, a family, an organisation or a place, of one kind (printed, birth, married, supplied and so on), in one script. A person's, a family's and an organisation's names are agent names and a place's are place names (vocabulary/ site-content.json, bindings agent_name and place_name), so the class itself names no single term.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `attribution` | For a supplied name only: who wrote the description, and on what day. | Attribution | No | No direct mapping recorded |
| `citations` | Where the name is found. | list of Citation | No | No direct mapping recorded |
| `kind` | What kind of name it is: printed, birth, married, supplied and so on. | NameKinds | Yes | No direct mapping recorded |
| `lang` | Its language, as a language tag such as yi or en. | SimpleLanguageTag | No | No direct mapping recorded |
| `script` | The script it is written in, as a four-letter ISO 15924 code such as Hebr or Latn. | ScriptCode | Yes | No direct mapping recorded |
| `value` | The name, as written. | NonBlankText | Yes | No direct mapping recorded |

Source: `linkml/schema/sourced_entities.yaml`.

### Review

Whether a person has reviewed a statement, who and on what day.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `by` | Who reviewed it. | NonBlankText | No | No direct mapping recorded |
| `on` | The day it was reviewed. | IsoDay | No | No direct mapping recorded |
| `state` | Pending, or approved by a reviewer. | ReviewStates | Yes | No direct mapping recorded |

Source: `linkml/schema/sourced_entities.yaml`.

### Source

A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id.

Meaning: ehri:RecordResource (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `author` | Who wrote the source: an institution, never a member of its staff. | string | No | rico:hasCreator (slot uri) |
| `dated` | The record's own date, apart from when it was published or consulted. | SourcedDate | No | rico:hasCreationDate (slot uri) |
| `derived_from` | For a copy or a transcription we hold: the original it was made from, and how. | list of SourceDerivation; minimum items: 1 | No | No direct mapping recorded |
| `editor` | Who edited the source. | string | No | No direct mapping recorded |
| `holder_id` | Who holds the source, by its id in the record's holders. | NonBlankText | No | rico:hasOrHadHolder (slot uri) |
| `host` | The web host the source's records are served from, without www: every address cited from it is on that host or a subdomain of it. | HostName | No | pc:site_source_host (slot uri) |
| `id` | The source's id in the record, which citations name. | NonBlankText | Yes | No direct mapping recorded |
| `kind` | What kind of source it is: a book, a memorial book, an archive's database, the paper and so on. | SourceKinds | Yes | No direct mapping recorded |
| `language` | The languages of the record, as BCP 47 tags. | list of LanguageTag; minimum items: 1 | No | rico:hasOrHadLanguage (slot uri) |
| `made_by` | Who made the source, as a category (family, studio, institution, perpetrator, unknown); never its creator. | SourceMadeBy | No | pc:source_made_by (slot uri) |
| `private` | True when the document itself is never shown. | boolean | No | pc:site_source_privacy (related mappings) |
| `published` | When or where the source was published, as written. | string | No | No direct mapping recorded |
| `quote_condition` | The owner's condition on the cleared quotes: shown only where no other record says the same. | SourceQuoteCondition | No | pc:site_source_quote_condition (slot uri) |
| `quotes_cleared` | Who allowed quotes from this private document to be published, and on what day. | Attribution | No | pc:site_source_privacy (related mappings) |
| `reference_code` | The holder's own reference for the record, as the holder writes it. | NonBlankText | No | rico:hasOrHadIdentifier (slot uri) |
| `repository` | The old free-text holder, read for one release; holder_id replaces it. | string | No | No direct mapping recorded |
| `short_name` | A short name the site shows for the source. | NonBlankText | No | pc:site_source_display (slot uri) |
| `subjects` | The persons, places or events the source shows or speaks of, by their ids. | list of NonBlankText; minimum items: 1 | No | rico:hasOrHadSubject (slot uri) |
| `title` | The source's title. | NonBlankText | Yes | No direct mapping recorded |
| `url_pattern` | How an address of one of the source's records is formed. | string | No | No direct mapping recorded |
| `work_id` | The id of the work in the project's files; never published where it is a file name. | string | No | No direct mapping recorded |

Source: `linkml/schema/sourced_entities.yaml`.

### SourceDerivation

The record a source we hold was made from, and how: a copy or a transcription of it.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `relation` | Whether this source is a copy or a transcription of the original. | SourceDerivationRelation | Yes | No direct mapping recorded |
| `source_id` | The original source, by its id in the record's sources. | NonBlankText | Yes | No direct mapping recorded |

Source: `linkml/schema/sourced_entities.yaml`.

### SourcedDate

A date a source gives: a normalized start (and end, for a range) with how precise it is, or the words as printed with their calendar, or both.

Meaning: rico:Date (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `end` | The end of a range of dates, written as the start is. | IsoYearMonthOrDay | No | No direct mapping recorded |
| `inferred` | True when the date was worked out rather than read. | boolean | No | No direct mapping recorded |
| `precision` | How much of the date is known: year, month, day or range. | SourcedDatePrecision | No | No direct mapping recorded |
| `printed` | The date's words as the source prints or writes them. | NonBlankText | No | rico:expressedDate (slot uri) |
| `printed_calendar` | The calendar of the printed words. | PrintedCalendar | No | No direct mapping recorded |
| `start` | The date's start, as far as it is known: YYYY, YYYY-MM or YYYY-MM-DD. | IsoYearMonthOrDay | No | No direct mapping recorded |

Source: `linkml/schema/sourced_entities.yaml`.

## Media of the Pruzhany record

### Media

One held or linked copy of a registered source, as the shared record keeps it: all that the public may see, with the private master file and the private permission besides.

Meaning: rico:Instantiation (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `alt` | The description for screen readers of what is visible; required for images and documents. | MediaText | No | pc:media_alt (slot uri) |
| `caption` | The caption the site shows, with its language and review. | MediaText | Yes | pc:media_caption (slot uri) |
| `cleared` | Who cleared the medium for the site, by role, and on what day. | MediaDecision | No | pc:media_clearance (slot uri) |
| `conditions_of_access` | The holder's terms of access, as written. | NonBlankText | No | rico:conditionsOfAccess (slot uri) |
| `conditions_of_use` | The holder's terms of use, as written, with no permission inferred from them. | NonBlankText | No | rico:conditionsOfUse (slot uri) |
| `consent` | The private record of the permission to show the medium; never public. | MediaConsent | No | pc:media_consent (slot uri) |
| `credit` | The holder's or the family's credit, as they word it. | NonBlankText | Yes | pc:media_credit (slot uri) |
| `depicted` | The people the picture shows, identified or not, and where. | list of MediaDepicted | Yes | pc:media_depicted (slot uri) |
| `derived` | The served copies of the picture, one for each exported width. | list of MediaDerivative; minimum items: 1 | No | pc:media_derived (slot uri) |
| `duration` | The master's length in seconds, for sound and film. | NonNegativeNumber | No | pc:media_duration (slot uri) |
| `family_words` | The family's words about the medium, quoted from a source. | MediaFamilyWords | No | pc:media_family_words (slot uri) |
| `height` | The master's height in pixels, after orientation. | PositiveInteger | No | rico:height (slot uri) |
| `id` | The medium's id: lowercase letters and digits in parts joined by hyphens. | string; pattern: ^[a-z0-9]+(?:-[a-z0-9]+)*$(?![\s\S]) | Yes | No direct mapping recorded |
| `inscription` | The object's own words, such as writing on the back of a photograph. | MediaText | No | pc:media_inscription (slot uri) |
| `kind` | What the medium is: image, audio, video or document. | MediaKind | Yes | rico:hasRepresentationType (slot uri) |
| `link` | For sound or film: the page on the holder's own host where it can be heard or seen. | string; pattern: ^https://[a-z0-9]+(?:[.-][a-z0-9]+)*(?:/[^\s\\]*)?$(?![\s\S]) | No | pc:media_link (slot uri) |
| `master` | Where the private master file is kept; never public. | MediaMaster | No | pc:media_master (slot uri) |
| `rights` | The rights statement or licence that applies, by its address; when absent, copyright not evaluated. | string; one of: ['http://rightsstatements.org/vocab/InC/1.0/', 'http://rightsstatements.org/vocab/InC-OW-EU/1.0/', 'http://rightsstatements.org/vocab/InC-EDU/1.0/', 'http://rightsstatements.org/vocab/InC-NC/1.0/', 'http://rightsstatements.org/vocab/InC-RUU/1.0/', 'http://rightsstatements.org/vocab/NoC-CR/1.0/', 'http://rightsstatements.org/vocab/NoC-NC/1.0/', 'http://rightsstatements.org/vocab/NoC-OKLR/1.0/', 'http://rightsstatements.org/vocab/NoC-US/1.0/', 'http://rightsstatements.org/vocab/CNE/1.0/', 'http://rightsstatements.org/vocab/UND/1.0/', 'http://rightsstatements.org/vocab/NKC/1.0/', 'https://creativecommons.org/licenses/by/4.0/', 'https://creativecommons.org/licenses/by-sa/4.0/', 'https://creativecommons.org/licenses/by-nd/4.0/', 'https://creativecommons.org/licenses/by-nc/4.0/', 'https://creativecommons.org/licenses/by-nc-sa/4.0/', 'https://creativecommons.org/licenses/by-nc-nd/4.0/', 'https://creativecommons.org/publicdomain/zero/1.0/', 'https://creativecommons.org/publicdomain/mark/1.0/'] | No | pc:media_rights (slot uri) |
| `shows_unidentified` | True when the picture shows people not identified. | boolean | Yes | pc:media_shows_unidentified (slot uri) |
| `source_id` | The source this medium is a copy of, by its id; never the person shown. | NonBlankText | Yes | rico:isOrWasInstantiationOf (slot uri) |
| `transcript` | A document's full text; required for documents. | MediaText | No | pc:media_transcript (slot uri) |
| `width` | The master's width in pixels, after orientation. | PositiveInteger | No | rico:width (slot uri) |
| `withdrawn` | That the medium was withdrawn, on what day and why. | MediaWithdrawal | No | pc:media_withdrawn (slot uri) |

Source: `linkml/schema/media.yaml`.

### MediaConsent

The private record of the permission to show a medium: its basis, who gave it by role, what it covers, the document that holds it and any withdrawal. Never public.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `basis` | What the permission rests on: an institution's terms, the holder's licence, the family's permission, the public domain, or the owner's family papers. | string; one of: ['institution-terms', 'holder-licence', 'family-permission', 'public-domain', 'owner-family-papers'] | Yes | No direct mapping recorded |
| `granted_by` | Who gave the permission, by role; never a person's name. | MediaGrantedBy | Yes | No direct mapping recorded |
| `ref` | The private reference of the document that holds the permission. | NonBlankText | Yes | No direct mapping recorded |
| `scope` | What the permission covers. | MediaConsentScope | Yes | No direct mapping recorded |
| `withdrawn_on` | The day the permission was withdrawn. | IsoDay | No | No direct mapping recorded |

Source: `linkml/schema/media.yaml`.

### MediaConsentScope

What a permission covers: the use, the people shown, and whether people not identified are covered.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `person_ids` | The people the permission covers, by their ids; each must be shown in the medium. | list of NonBlankText | Yes | No direct mapping recorded |
| `unidentified` | True when the permission also covers people shown and not identified. | boolean | Yes | No direct mapping recorded |
| `use` | The use allowed: shown on the site, or shown and downloaded. | string; one of: ['site', 'site+download'] | Yes | No direct mapping recorded |

Source: `linkml/schema/media.yaml`.

### MediaDecision

A review or a clearance: whose role made it (the owner or the project) and on what day.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `on` | The day of the decision. | IsoDay | Yes | No direct mapping recorded |
| `role` | Who decided, by role: the owner or the project; never a person's name. | MediaDecisionRole | Yes | No direct mapping recorded |

Source: `linkml/schema/media.yaml`.

### MediaDepicted

One person a picture shows, identified or not, where in the picture, and on whose identification.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `identified_by` | What identifies the person: the family, a record, or the picture's inscription. | MediaIdentifiedBy | Yes | No direct mapping recorded |
| `person_id` | The person shown, by the person's id; null for a person not identified. | NonBlankText | No | No direct mapping recorded |
| `region` | Where in the picture the person is. | MediaRegion | Yes | No direct mapping recorded |

Source: `linkml/schema/media.yaml`.

### MediaDerivative

One served copy of a picture: a WebP file at one of the exported widths, named by the master's digest, made by resizing alone.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `height` | The copy's actual height in pixels. | PositiveInteger | Yes | No direct mapping recorded |
| `process` | How the copy was made: resizing alone. | string; fixed value: resize | Yes | No direct mapping recorded |
| `url` | The copy's address, ending in its nominal width (zod/media-widths.json). | string; pattern: ^https://pictures\.pruzhanychronicles\.org/media/[0-9a-f]{64}-w(?:100\|400\|800\|1200)\.webp$(?![\s\S]) | Yes | No direct mapping recorded |
| `width` | The copy's actual width in pixels. | PositiveInteger | Yes | No direct mapping recorded |

Source: `linkml/schema/media.yaml`.

### MediaFamilyWords

The family's own words about a medium, quoted from a registered source with the page or part they are on: a public part of a citation, with no private note.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `page` | The page or recorded part the words are on. | NonBlankText | Yes | No direct mapping recorded |
| `quote` | The words, exactly. | NonBlankText | Yes | No direct mapping recorded |
| `quote_language` | Their language, as a BCP 47 tag. | LanguageTag | Yes | No direct mapping recorded |
| `source_id` | The source the words are quoted from, by its id in the record's sources. | NonBlankText | Yes | No direct mapping recorded |

Source: `linkml/schema/media.yaml`.

### MediaFixity

A dated check that a master file still has its digest.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `on` | The day of the check. | IsoDay | Yes | No direct mapping recorded |
| `sha256` | The SHA-256 digest found on that day. | Sha256Hex | Yes | No direct mapping recorded |

Source: `linkml/schema/media.yaml`.

### MediaMaster

Where a medium's private master file is kept: its bucket, its key named by its digest, its digest, its type, its size and its last check. Never public.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `bucket` | The private storage bucket, apart from the page pictures' bucket. | string; pattern: ^[a-z0-9][a-z0-9-]{1,61}[a-z0-9]$(?![\s\S]) | Yes | No direct mapping recorded |
| `bytes` | The file's size in bytes. | PositiveInteger | Yes | No direct mapping recorded |
| `checked` | The last dated check of the file's digest. | MediaFixity | No | No direct mapping recorded |
| `key` | The file's key in the bucket, whose last part is its SHA-256 digest. | string; pattern: ^(?:[a-z0-9_-]+/)*[0-9a-f]{64}$(?![\s\S]) | Yes | No direct mapping recorded |
| `mime` | The file's media type, such as image/tiff. | string; pattern: ^(?:image\|audio\|video\|application)/[a-z0-9][a-z0-9.+-]*$(?![\s\S]) | Yes | No direct mapping recorded |
| `sha256` | The SHA-256 digest of the file. | Sha256Hex | Yes | No direct mapping recorded |

Source: `linkml/schema/media.yaml`.

### MediaPortrait

The picture a person's page shows as their portrait: a reviewed medium and the region of it to show.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `media_id` | The medium, by its id in the record's media. | NonBlankText | Yes | No direct mapping recorded |
| `region` | The part of the picture to show, in its master pixels. | MediaRegion | Yes | No direct mapping recorded |
| `reviewed` | Who chose the portrait, by role, and on what day. | MediaDecision | Yes | No direct mapping recorded |

Source: `linkml/schema/media.yaml`.

### MediaRegion

A rectangle in a medium's master picture, in its own pixels after orientation.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `h` | The height, in pixels. | PositiveInteger | Yes | No direct mapping recorded |
| `w` | The width, in pixels. | PositiveInteger | Yes | No direct mapping recorded |
| `x` | The left edge, in pixels from the picture's left. | NonNegativeInteger | Yes | No direct mapping recorded |
| `y` | The top edge, in pixels from the picture's top. | NonNegativeInteger | Yes | No direct mapping recorded |

Source: `linkml/schema/media.yaml`.

### MediaText

Words about or on a medium (a caption, a description for screen readers, an inscription, a transcript), their language and their review.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `lang` | Their language, as a BCP 47 tag. | LanguageTag | Yes | No direct mapping recorded |
| `reviewed` | Who reviewed the words, by role, and on what day. | MediaDecision | No | No direct mapping recorded |
| `text` | The words. | NonBlankText | Yes | No direct mapping recorded |

Source: `linkml/schema/media.yaml`.

### MediaWithdrawal

That a medium was withdrawn from the site, on what day and why; its record stays.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `on` | The day it was withdrawn. | IsoDay | Yes | No direct mapping recorded |
| `reason` | Why: at the family's or the holder's request, or for an error. | MediaWithdrawalReason | Yes | No direct mapping recorded |

Source: `linkml/schema/media.yaml`.

### PublicMedia

One held or linked copy of a registered source (a photograph, document, recording or film), as the public may see it: what it is, what it shows and says, its review, its terms and its served copies.

Meaning: rico:Instantiation (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `alt` | The description for screen readers of what is visible; required for images and documents. | MediaText | No | pc:media_alt (slot uri) |
| `caption` | The caption the site shows, with its language and review. | MediaText | Yes | pc:media_caption (slot uri) |
| `cleared` | Who cleared the medium for the site, by role, and on what day. | MediaDecision | No | pc:media_clearance (slot uri) |
| `conditions_of_access` | The holder's terms of access, as written. | NonBlankText | No | rico:conditionsOfAccess (slot uri) |
| `conditions_of_use` | The holder's terms of use, as written, with no permission inferred from them. | NonBlankText | No | rico:conditionsOfUse (slot uri) |
| `credit` | The holder's or the family's credit, as they word it. | NonBlankText | Yes | pc:media_credit (slot uri) |
| `depicted` | The people the picture shows, identified or not, and where. | list of MediaDepicted | Yes | pc:media_depicted (slot uri) |
| `derived` | The served copies of the picture, one for each exported width. | list of MediaDerivative; minimum items: 1 | No | pc:media_derived (slot uri) |
| `duration` | The master's length in seconds, for sound and film. | NonNegativeNumber | No | pc:media_duration (slot uri) |
| `family_words` | The family's words about the medium, quoted from a source. | MediaFamilyWords | No | pc:media_family_words (slot uri) |
| `height` | The master's height in pixels, after orientation. | PositiveInteger | No | rico:height (slot uri) |
| `id` | The medium's id: lowercase letters and digits in parts joined by hyphens. | string; pattern: ^[a-z0-9]+(?:-[a-z0-9]+)*$(?![\s\S]) | Yes | No direct mapping recorded |
| `inscription` | The object's own words, such as writing on the back of a photograph. | MediaText | No | pc:media_inscription (slot uri) |
| `kind` | What the medium is: image, audio, video or document. | MediaKind | Yes | rico:hasRepresentationType (slot uri) |
| `link` | For sound or film: the page on the holder's own host where it can be heard or seen. | string; pattern: ^https://[a-z0-9]+(?:[.-][a-z0-9]+)*(?:/[^\s\\]*)?$(?![\s\S]) | No | pc:media_link (slot uri) |
| `rights` | The rights statement or licence that applies, by its address; when absent, copyright not evaluated. | string; one of: ['http://rightsstatements.org/vocab/InC/1.0/', 'http://rightsstatements.org/vocab/InC-OW-EU/1.0/', 'http://rightsstatements.org/vocab/InC-EDU/1.0/', 'http://rightsstatements.org/vocab/InC-NC/1.0/', 'http://rightsstatements.org/vocab/InC-RUU/1.0/', 'http://rightsstatements.org/vocab/NoC-CR/1.0/', 'http://rightsstatements.org/vocab/NoC-NC/1.0/', 'http://rightsstatements.org/vocab/NoC-OKLR/1.0/', 'http://rightsstatements.org/vocab/NoC-US/1.0/', 'http://rightsstatements.org/vocab/CNE/1.0/', 'http://rightsstatements.org/vocab/UND/1.0/', 'http://rightsstatements.org/vocab/NKC/1.0/', 'https://creativecommons.org/licenses/by/4.0/', 'https://creativecommons.org/licenses/by-sa/4.0/', 'https://creativecommons.org/licenses/by-nd/4.0/', 'https://creativecommons.org/licenses/by-nc/4.0/', 'https://creativecommons.org/licenses/by-nc-sa/4.0/', 'https://creativecommons.org/licenses/by-nc-nd/4.0/', 'https://creativecommons.org/publicdomain/zero/1.0/', 'https://creativecommons.org/publicdomain/mark/1.0/'] | No | pc:media_rights (slot uri) |
| `shows_unidentified` | True when the picture shows people not identified. | boolean | Yes | pc:media_shows_unidentified (slot uri) |
| `source_id` | The source this medium is a copy of, by its id; never the person shown. | NonBlankText | Yes | rico:isOrWasInstantiationOf (slot uri) |
| `transcript` | A document's full text; required for documents. | MediaText | No | pc:media_transcript (slot uri) |
| `width` | The master's width in pixels, after orientation. | PositiveInteger | No | rico:width (slot uri) |
| `withdrawn` | That the medium was withdrawn, on what day and why. | MediaWithdrawal | No | pc:media_withdrawn (slot uri) |

Source: `linkml/schema/media.yaml`.

## The shared record of the Pruzhany record

### Holder

Who holds a source: an institution, a family or a private person, with its outside identifiers and its web host. A private holder's name is never published.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `host` | The holder's web host, without www. | HostName | No | No direct mapping recorded |
| `id` | The holder's id, which sources name. | NonBlankText | Yes | No direct mapping recorded |
| `identifiers` | The holder's outside identifiers, each with its evidence: EHRI's institution id first. | list of PlaceIdentifier; minimum items: 1 | No | rico:hasOrHadIdentifier (slot uri) |
| `kind` | An institution, a family or a private person. | HolderKind | Yes | No direct mapping recorded |
| `name` | The holder's name. | NonBlankText | Yes | rico:hasOrHadName (slot uri) |
| `short_name` | The name the site shows. | NonBlankText | No | rico:hasOrHadName (slot uri) |

Source: `linkml/schema/shared_record.yaml`.

### LifeEventDate

One date of a life event: the words printed with their calendar, or, where no date is printed, the day of the first issue that reported it, or the preferred record statement's date for a death known from records alone.

Meaning: rico:Date (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `printed` | The date's words as printed. | NonBlankText | No | rico:expressedDate (slot uri) |
| `printed_calendar` | The calendar the date was printed in. | PrintedCalendar | No | rico:expressedDate (related mappings) |
| `qualifier` | reported_in: the day is the first issue's that reported the event, not the day it happened. | string; fixed value: reported_in | No | rico:dateQualifier (slot uri) |
| `record_fact_id` | For a death known from records: the accepted death fact whose date and place describe it, by the fact's id. | NonBlankText | No | pc:site_event_record_date (slot uri) |
| `reported_in` | The day of the first issue that reported the event, where no date is printed. | IsoDay | No | No direct mapping recorded |
| `start` | The printed date normalized, for a date printed in the Gregorian calendar only. | IsoYearMonthOrDay | No | rico:normalizedDateValue (slot uri) |

Source: `linkml/schema/shared_record.yaml`.

### LifeEventMainPerson

One main person of a life event and their part in it (the baby, a parent, the bride, the groom, the boy, the one who died, the one remembered); each part means a declared local subproperty of rico:affectsOrAffected or rico:hasOrHadParticipant (EventParts).

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `part` | The person's part in the event. | EventParts | Yes | No direct mapping recorded |
| `person_id` | The person, by the person's id in the record. | NonBlankText | Yes | No direct mapping recorded |

Source: `linkml/schema/shared_record.yaml`.

### PlaceIdentifier

One outside identifier of a place or a holder, read on its authority's own pages and carried only on that evidence, never from a match of names.

Meaning: rico:Identifier (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `accessed` | The day it was read on its authority's own pages. | IsoDay | Yes | pc:site_identifier_reading (related mappings) |
| `attribution` | Who added it, and on what day. | Attribution | Yes | pc:site_identifier_reading (related mappings) |
| `source_id` | The authority the identifier comes from, a registered source, by its id. | NonBlankText | Yes | rico:hasIdentifierType (slot uri) |
| `url` | The identifier's page on the authority's host. | HttpsUri | No | No direct mapping recorded |
| `value` | The identifier as its authority writes it. | NonBlankText | Yes | rico:textualValue (slot uri) |

Source: `linkml/schema/shared_record.yaml`.

### SharedEvent

One life event, once for each happening across every issue (a birth, a wedding, a death, a memorial and so on): its kind, its main people and their parts, its dates and its place.

Meaning: rico:Event (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `dates` | The event's dates: as printed (in either calendar), or the first report's day, or the preferred record statement's. | list of LifeEventDate; minimum items: 1 | Yes | No direct mapping recorded |
| `description` | A short description in words. | string | No | No direct mapping recorded |
| `evidence_basis` | records_only: a death known from records alone, which no issue prints. | string; fixed value: records_only | No | pc:site_event_evidence_basis (slot uri) |
| `id` | The event's id, which each issue's life events name. | NonBlankText | Yes | No direct mapping recorded |
| `location_id` | Where the event happened, by the place's id. | NonBlankText | No | No direct mapping recorded |
| `main_people` | The people the event is about, each with their part; empty while unresolved. | list of LifeEventMainPerson | Yes | rico:hasOrHadParticipant (slot uri) |
| `name` | The event's name. | NonBlankText | Yes | No direct mapping recorded |
| `proposed_type` | For an event of kind other: the kind proposed for it, awaiting the owner's approval. | NonBlankText | No | No direct mapping recorded |
| `type` | The one kind of the event. | EventTypes | Yes | rico:hasEventType (slot uri) |

Source: `linkml/schema/shared_record.yaml`.

### SharedFact

One source's statement as the shared record keeps it: a fact with its subject, its form and its evidence located on the printed page where the site writer found it.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `attribution` | Who recorded the statement, and on what day. | Attribution | Yes | No direct mapping recorded |
| `citations` | The evidence: where in which sources the statement is found. | list of SiteCitation; minimum items: 1 | Yes | No direct mapping recorded |
| `date` | When, as the source gives it. | SourcedDate | No | No direct mapping recorded |
| `event_id` | The life event the statement concerns, by its id in the record. | NonBlankText | No | No direct mapping recorded |
| `evidence_confidence` | How sure the evidence makes the statement. | Confidence | Yes | rico:relationCertainty (slot uri) |
| `family_id` | The family the statement concerns, by its id; on a membership fact, the family the person belongs to. | NonBlankText | No | rico:isOrWasMemberOf (slot uri); via rico:MembershipRelation |
| `holocaust_related` | True when the statement concerns the Holocaust. | boolean | No | No direct mapping recorded |
| `id` | The fact's id in the record. | NonBlankText | Yes | No direct mapping recorded |
| `identity_confidence` | How sure it is that the statement is about this person. | Confidence | Yes | No direct mapping recorded |
| `organization_id` | The organisation the statement concerns, by its id in the record. | NonBlankText | No | No direct mapping recorded |
| `place_id` | Where, by the place's id in the record. | NonBlankText | No | No direct mapping recorded |
| `proposed_type` | For a statement of type other: the type proposed for it, awaiting the owner's approval. | NonBlankText | No | No direct mapping recorded |
| `qualifiers` | More about the statement, as named texts. | FactQualifiers | No | No direct mapping recorded |
| `related_name` | For kinship: the relative's name, where the relative has no person of their own. | NonBlankText | No | No direct mapping recorded |
| `related_person_id` | For kinship: the relative, by the person's id in the record. | NonBlankText | No | No direct mapping recorded |
| `relationship_type` | For kinship: how the relative is related, from the subject to the relative. | RelationshipTypes | No | No direct mapping recorded |
| `representation` | The form the statement is kept in: structured, prose or an image path. | SharedFactRepresentation | Yes | pc:site_fact_representation (slot uri) |
| `review` | Whether a person has reviewed the statement. | Review | Yes | pc:site_standing (related mappings) |
| `status` | The statement's standing: proposed, accepted, disputed or rejected. | ClaimStatus | Yes | pc:site_standing (related mappings) |
| `subject_id` | Whose statement it is: a person, a family, a place, an organisation, an event or a relation, by its id. | NonBlankText | Yes | pc:site_fact_subject (slot uri) |
| `type` | What the statement is about: a birth, a death, a residence, an occupation and so on. | FactTypes | Yes | No direct mapping recorded |
| `value` | The statement's words or value, such as an occupation. | NonBlankText | No | No direct mapping recorded |

Source: `linkml/schema/shared_record.yaml`.

### SharedFamily

One family of the record: its id, the name shown and its names.

Meaning: ehri:Family (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `id` | The family's id. | NonBlankText | Yes | No direct mapping recorded |
| `name` | The name the site shows. | NonBlankText | Yes | No direct mapping recorded |
| `names` | The family's names. | list of Name | Yes | No direct mapping recorded |

Source: `linkml/schema/shared_record.yaml`.

### SharedName

One name of a person in the shared record, with its evidence located on the printed page where the site writer found it.

Meaning: rico:AgentName (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `attribution` | For a supplied name only: who wrote the description, and on what day. | Attribution | No | No direct mapping recorded |
| `citations` | Where the name is found. | list of SiteCitation | No | No direct mapping recorded |
| `kind` | What kind of name it is: printed, birth, married, supplied and so on. | NameKinds | Yes | No direct mapping recorded |
| `lang` | Its language, as a language tag such as yi or en. | SimpleLanguageTag | No | No direct mapping recorded |
| `script` | The script it is written in, as a four-letter ISO 15924 code such as Hebr or Latn. | ScriptCode | Yes | No direct mapping recorded |
| `value` | The name, as written. | NonBlankText | Yes | No direct mapping recorded |

Source: `linkml/schema/shared_record.yaml`.

### SharedOrganization

One organisation of the record: its id, the name shown and its names; its offices and members are sourced facts.

Meaning: ehri:CorporateBody (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `id` | The organisation's id. | NonBlankText | Yes | No direct mapping recorded |
| `name` | The name the site shows. | NonBlankText | Yes | No direct mapping recorded |
| `names` | The organisation's names. | list of Name | Yes | No direct mapping recorded |

Source: `linkml/schema/shared_record.yaml`.

### SharedPerson

One person of the record, across every issue: their id, the name shown, every name they are known by, their gender, what became of them, and their portrait.

Meaning: ehri:Person (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `fate` | What became of the person in the Holocaust, as far as the record shows. | Fate | No | No direct mapping recorded |
| `gender` | The person's gender, or unknown. | Gender | Yes | No direct mapping recorded |
| `id` | The person's id, kept for ever: never renamed, reused or deleted. | NonBlankText | Yes | No direct mapping recorded |
| `name` | The name the site shows. | NonBlankText | Yes | No direct mapping recorded |
| `names` | Every name the person is known by, printed or supplied, with where it is found. | list of SharedName | Yes | rico:hasOrHadAgentName (slot uri) |
| `portrait` | The reviewed picture and region the person's page shows. | MediaPortrait | No | pc:media_portrait (slot uri) |

Source: `linkml/schema/shared_record.yaml`.

### SharedPlace

One place of the record: its names, its kind, the place it lies in, its coordinates and its outside identifiers.

Meaning: rico:Place (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `coordinates` | Where it lies: latitude then longitude, in degrees. | list of Coordinate; minimum items: 2; maximum items: 2 | No | rico:geographicalCoordinates (slot uri) |
| `id` | The place's id. | NonBlankText | Yes | No direct mapping recorded |
| `identifiers` | The place's outside identifiers, each with its evidence. | list of PlaceIdentifier; minimum items: 1 | No | rico:hasOrHadIdentifier (slot uri) |
| `name` | The name the site shows. | NonBlankText | Yes | No direct mapping recorded |
| `names` | The place's names. | list of Name | Yes | No direct mapping recorded |
| `parent_id` | The place it lies in, by its id. | NonBlankText | No | rico:isOrWasPartOf (slot uri) |
| `type` | What kind of place it is: a city, a town, a street, a camp and so on. | LocationTypes | Yes | No direct mapping recorded |

Source: `linkml/schema/shared_record.yaml`.

### SharedRecord

The shared record whole: its version, the vocabulary version it uses, and every person, family, place, organisation, event, source, holder, fact, relation and medium.

Meaning: pc:site_shared_record (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `events` | Every life event, once for each happening. | list of SharedEvent | Yes | No direct mapping recorded |
| `facts` | Every sourced fact. | list of SharedFact | Yes | No direct mapping recorded |
| `families` | Every family. | list of SharedFamily | Yes | No direct mapping recorded |
| `holders` | Every holder of a source. | list of Holder | No | No direct mapping recorded |
| `media` | Every medium held or linked beside a person. | list of Media | No | No direct mapping recorded |
| `organizations` | Every organisation. | list of SharedOrganization | Yes | No direct mapping recorded |
| `persons` | Every person. | list of SharedPerson | Yes | No direct mapping recorded |
| `places` | Every place. | list of SharedPlace | Yes | No direct mapping recorded |
| `relations` | Every sourced relation between people. | list of SourcedRelation | Yes | No direct mapping recorded |
| `sources` | Every registered source. | list of Source | Yes | No direct mapping recorded |
| `version` | The version of the record's shape. | string; fixed value: 1 | Yes | No direct mapping recorded |
| `vocabulary_version` | The version of the sourced-entities vocabulary the record uses. | string; fixed value: 1.3.0 | Yes | No direct mapping recorded |

Source: `linkml/schema/shared_record.yaml`.

### SiteCitation

A citation as the shared record keeps it: an older one as it was written, or one the site writer locates on the printed page, with the addresses of the words it quotes.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `accessed` | The day a person read the record. | IsoDay | No | No direct mapping recorded |
| `addresses` | Where on the page pictures the quoted words are printed. | list of PrintedAddress; minimum items: 1 | No | No direct mapping recorded |
| `edition_date` | The day of the paper's issue cited, written YYYY-MM-DD. | string | No | No direct mapping recorded |
| `locator` | An internal pointer into the project's files; never published and never a holder's record number. | NonBlankText | No | pc:site_citation_locator (slot uri) |
| `note` | Our private note on the evidence; never published. | string | No | No direct mapping recorded |
| `page` | The page, folio or entry cited. | string | No | No direct mapping recorded |
| `public_note` | Our reviewed words for the page about this evidence, apart from the record's quote. | NonBlankText | No | pc:site_citation_public_note (slot uri) |
| `quote` | The record's own words, exactly. | string | No | No direct mapping recorded |
| `quote_language` | The quote's language, where it is not the source's (a translation). | LanguageTag | No | rico:hasOrHadLanguage (slot uri) |
| `record_id` | The holder's own number for the record, such as a Yad Vashem record number. | string | No | rico:hasOrHadIdentifier (slot uri) |
| `record_type` | The holder's own type of the record, such as Page of Testimony. | NonBlankText | No | rico:hasDocumentaryFormType (slot uri) |
| `reference_code` | The holder's reference of the document cited, where the source is a set of many. | NonBlankText | No | rico:hasOrHadIdentifier (slot uri) |
| `scan` | The scan or image cited. | string | No | No direct mapping recorded |
| `source_id` | The record the statement rests on (the original where it is known), by its id in the record's sources. | NonBlankText | Yes | rico:isEvidencedBy (slot uri) |
| `time` | The time in a recording. | string | No | No direct mapping recorded |
| `unit_id` | The piece of the paper cited, by its content item id. | string | No | No direct mapping recorded |
| `url` | The record's web address. | HttpsUri | No | No direct mapping recorded |
| `via` | The one source actually read, a copy or a transcription of the original, by its id. | NonBlankText | No | No direct mapping recorded |

Source: `linkml/schema/shared_record.yaml`.

### SourcedRelation

One source's statement that a person is related to another, from the subject to the relative, of a released kinship type, or of type other with a proposed type.

Meaning: rico:Relation (class uri).

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `attribution` | Who recorded the statement, and on what day. | Attribution | Yes | No direct mapping recorded |
| `citations` | The evidence: where in which sources the relation is found. | list of SiteCitation; minimum items: 1 | Yes | No direct mapping recorded |
| `date` | When, as the source gives it. | SourcedDate | No | No direct mapping recorded |
| `event_id` | The life event the statement concerns, by its id in the record. | NonBlankText | No | No direct mapping recorded |
| `evidence_confidence` | How sure the evidence makes the statement. | Confidence | Yes | rico:relationCertainty (slot uri) |
| `family_id` | The family the relation concerns, by its id. | NonBlankText | No | No direct mapping recorded |
| `holocaust_related` | True when the statement concerns the Holocaust. | boolean | No | No direct mapping recorded |
| `id` | The fact's id in the record. | NonBlankText | Yes | No direct mapping recorded |
| `identity_confidence` | How sure it is that the statement is about this person. | Confidence | Yes | No direct mapping recorded |
| `organization_id` | The organisation the statement concerns, by its id in the record. | NonBlankText | No | No direct mapping recorded |
| `place_id` | Where, by the place's id in the record. | NonBlankText | No | No direct mapping recorded |
| `proposed_type` | For a statement of type other: the type proposed for it, awaiting the owner's approval. | NonBlankText | No | No direct mapping recorded |
| `qualifiers` | More about the statement, as named texts. | FactQualifiers | No | No direct mapping recorded |
| `related_name` | For kinship: the relative's name, where the relative has no person of their own. | NonBlankText | No | No direct mapping recorded |
| `related_person_id` | For kinship: the relative, by the person's id in the record. | NonBlankText | No | No direct mapping recorded |
| `relationship_type` | For kinship: how the relative is related, from the subject to the relative. | RelationshipTypes | No | No direct mapping recorded |
| `review` | Whether a person has reviewed the statement. | Review | Yes | pc:site_standing (related mappings) |
| `shown` | Who allowed the relative to be shown on the person's page, and on what day; never evidence of a death. | Attribution | No | pc:site_display_permission (slot uri) |
| `status` | The statement's standing: proposed, accepted, disputed or rejected. | ClaimStatus | Yes | pc:site_standing (related mappings) |
| `subject_id` | The person the relation goes from, by the person's id. | NonBlankText | Yes | pc:site_fact_subject (slot uri) |
| `type` | kinship for a released relationship type; other, with a proposed type, for one not yet released. | FactTypes; one of: ['kinship', 'other'] | Yes | No direct mapping recorded |
| `value` | The statement's words or value, such as an occupation. | NonBlankText | No | No direct mapping recorded |

Source: `linkml/schema/shared_record.yaml`.

## Shared compatibility shapes of the Pruzhany record

### ExternalReference

A reference to a record in an outside database or resource, such as a page of testimony at Yad Vashem.

Meaning: No direct mapping recorded.

| Field | What it holds | Value | Required | Standard mapping |
| --- | --- | --- | --- | --- |
| `notes` | Notes on the record. | string | No | No direct mapping recorded |
| `record_id` | The record's identifier in that database. | string | No | No direct mapping recorded |
| `source` | The database or resource, by name, such as yad_vashem or jri_poland. | string | Yes | No direct mapping recorded |
| `url` | The record's address; null for a citation of evidence that was looked for and not found. | string | No | No direct mapping recorded |
| `verified` | True when a person has reviewed and confirmed the reference. | boolean | No | No direct mapping recorded |

Source: `linkml/schema/shared.yaml`.

## Types and vocabularies

### HostName

A lowercase internet host name with at least one dot, such as collections.yadvashem.org.

string; pattern: ^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$

### IsoDay

A calendar day written YYYY-MM-DD, such as 1938-12-16.

string; pattern: ^\d{4}-\d{2}-\d{2}$

### IsoYearMonthOrDay

A year, a month or a day, as far as it is known: YYYY, YYYY-MM or YYYY-MM-DD.

string; pattern: ^\d{4}(-\d{2}(-\d{2})?)?$

### LanguageTag

A BCP 47 language tag, by the pattern in vocabulary/citation-requirements.json.

string; pattern: ^(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}){0,3}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}\|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}\|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?\|[A-Za-z]{4,8}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}\|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}\|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?\|[xX](?:-[A-Za-z0-9]{1,8})+\|[eE][nN]-[gG][bB]-[oO][eE][dD]\|[iI]-(?:[aA][mM][iI]\|[bB][nN][nN]\|[dD][eE][fF][aA][uU][lL][tT]\|[eE][nN][oO][cC][hH][iI][aA][nN]\|[hH][aA][kK]\|[kK][lL][iI][nN][gG][oO][nN]\|[lL][uU][xX]\|[mM][iI][nN][gG][oO]\|[nN][aA][vV][aA][jJ][oO]\|[pP][wW][nN]\|[tT][aA][oO]\|[tT][aA][yY]\|[tT][sS][uU])\|[sS][gG][nN]-(?:[bB][eE]-[fF][rR]\|[bB][eE]-[nN][lL]\|[cC][hH]-[dD][eE])\|[aA][rR][tT]-[lL][oO][jJ][bB][aA][nN]\|[cC][eE][lL]-[gG][aA][uU][lL][iI][sS][hH]\|[nN][oO]-[bB][oO][kK]\|[nN][oO]-[nN][yY][nN]\|[zZ][hH]-[gG][uU][oO][yY][uU]\|[zZ][hH]-[hH][aA][kK][kK][aA]\|[zZ][hH]-[mM][iI][nN]\|[zZ][hH]-[mM][iI][nN]-[nN][aA][nN]\|[zZ][hH]-[xX][iI][aA][nN][gG])$

### NonBlankText

Text with at least one character that is not white space.

string; pattern: \S

### NonNegativeInteger

A whole number from 0 to 9007199254740991, the largest integer JavaScript holds exactly. As the range of a multivalued slot it bounds each item, not the list.

integer; minimum: 0; maximum: 9007199254740991

### NonNegativeNumber

A number at least 0, such as each of the four numbers of a box on a page picture; the shapes bound the box's width and height above 0, which known-looser.yaml records.

float; minimum: 0

### PositiveInteger

A whole number from 1 to 9007199254740991; the shapes say above 0, which for a whole number is the same.

integer; minimum: 1; maximum: 9007199254740991

### ScriptCode

A four-letter ISO 15924 script code, such as Hebr or Latn.

string; pattern: ^[A-Za-z]{4}$

### Sha256Hex

A SHA-256 digest: exactly 64 lowercase hexadecimal digits and nothing after them. Some shapes write the pattern without its last part and add a length of 64, which says the same; LinkML has no length of a string, hence the last part.

string; pattern: ^[0-9a-f]{64}$(?![\s\S])

### SimpleLanguageTag

A language tag in its simple form, letters then hyphenated parts, such as yi or yi-Latn.

string; pattern: ^[A-Za-z]{2,8}(-[A-Za-z0-9]{1,8})*$

### CitationRemarkKinds

Citation remark kinds: the values of citation_remark_kinds in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `private_source_remark` | Private citation remark about the record giver; never published. | pc:citation_remark_kinds_private_source_remark (meaning) |

### ClaimStatus

Claim status: the values of claim_status in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `proposed` | An assertion put forward and not yet accepted, disputed or rejected; never published. | pc:claim_status_proposed (meaning) |
| `accepted` | An assertion retained as accepted; this alone does not authorize publication. | pc:claim_status_accepted (meaning) |
| `disputed` | An assertion retained with an unresolved challenge. | pc:claim_status_disputed (meaning) |
| `rejected` | An assertion retained as rejected so it is not silently reintroduced. | pc:claim_status_rejected (meaning) |

### CompatibilityEventTypes

Compatibility event types: the values of compatibility_event_types in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `wedding` | Compatibility value wedding: preserved unchanged from production event types. | pc:event_types_wedding (meaning) |
| `birth` | Compatibility value birth: preserved unchanged from production event types. | pc:event_types_birth (meaning) |
| `death` | Compatibility value death: preserved unchanged from production event types. | pc:event_types_death (meaning) |
| `bar_mitzvah` | Compatibility value bar_mitzvah: preserved unchanged from production event types. | pc:event_types_bar_mitzvah (meaning) |
| `celebration` | Compatibility value celebration: preserved unchanged from production event types. | pc:event_types_celebration (meaning) |
| `community_event` | Compatibility value community_event: preserved unchanged from production event types. | pc:event_types_community_event (meaning) |
| `holocaust_event` | Compatibility value holocaust_event: preserved unchanged from production event types. | pc:event_types_holocaust_event (meaning) |
| `other` | Compatibility value other: preserved unchanged from production event types. | pc:event_types_other (meaning) |

### Confidence

Confidence: the values of confidence in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `confirmed` | The cited evidence directly supports the assertion at the confirmed level; separate from identity confidence and editorial approval. | pc:confidence_confirmed (meaning) |
| `probable` | The evidence supports the assertion with remaining uncertainty. | pc:confidence_probable (meaning) |
| `possible` | The evidence permits the assertion but does not establish it as probable. | pc:confidence_possible (meaning) |

### ContentItemSubtypes

Content item subtypes: the values of content_item_subtypes in vocabulary/site-content.json, version 1.0.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `wedding_greeting` | A greeting to a couple on their wedding. | pc:subtype_wedding_greeting (meaning) |
| `engagement_greeting` | A greeting on an engagement. | pc:subtype_engagement_greeting (meaning) |
| `birth_greeting` | A greeting on the birth of a child. | pc:subtype_birth_greeting (meaning) |
| `bar_mitzvah_greeting` | A greeting on a bar mitzvah. | pc:subtype_bar_mitzvah_greeting (meaning) |
| `new_year_greeting` | A greeting for the New Year. | pc:subtype_new_year_greeting (meaning) |
| `departure_greeting` | Good wishes on departure or settlement elsewhere. | pc:subtype_departure_greeting (meaning) |
| `greeting` | A greeting whose occasion is not specified by a narrower form. | pc:subtype_greeting (meaning) |
| `thanks` | A public expression of thanks or acknowledgement. | pc:subtype_thanks (meaning) |
| `meeting_notice` | A notice inviting people to a meeting. | pc:subtype_meeting_notice (meaning) |
| `announcement` | A public announcement without a narrower established form. | pc:subtype_announcement (meaning) |
| `appeal` | A public request for support, contributions or participation. | pc:subtype_appeal (meaning) |
| `commercial_advertisement` | An advertisement for goods, services or premises. | pc:subtype_commercial_advertisement (meaning) |
| `condolence` | An expression of sympathy to mourners. | pc:subtype_condolence (meaning) |
| `memorial_notice` | A notice commemorating someone who has died. | pc:subtype_memorial_notice (meaning) |
| `death_announcement` | An announcement of a death or funeral. | pc:subtype_death_announcement (meaning) |
| `editorial` | An editorial statement by the newspaper. | pc:subtype_editorial (meaning) |
| `opinion` | An argument or commentary expressing a view. | pc:subtype_opinion (meaning) |
| `letter` | A letter printed for readers, including letters to the editor. | pc:subtype_letter (meaning) |
| `poem` | A composition in verse. | pc:subtype_poem (meaning) |
| `sketch` | A short literary sketch. | pc:subtype_sketch (meaning) |
| `humour` | A joke or short humorous composition. | pc:subtype_humour (meaning) |

### ContentUnitRoles

Content unit roles: the values of content_unit_roles in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `primary_announcement` | Compatibility value primary_announcement: preserved unchanged from production content unit roles. | pc:content_unit_roles_primary_announcement (meaning) |
| `congratulation` | Compatibility value congratulation: preserved unchanged from production content unit roles. | pc:content_unit_roles_congratulation (meaning) |
| `condolence` | A notice of sympathy sent to the mourners by friends or a society; a response to a death as a congratulation is to a wedding or birth. | pc:content_unit_roles_condolence (meaning) |
| `mention` | Compatibility value mention: preserved unchanged from production content unit roles. | pc:content_unit_roles_mention (meaning) |
| `advertisement` | Compatibility value advertisement: preserved unchanged from production content unit roles. | pc:content_unit_roles_advertisement (meaning) |

### EventParts

Event parts: the values of event_parts in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `baby` | The baby at a birth. | pc:part_baby (meaning) |
| `parent` | The parent at a birth. | pc:part_parent (meaning) |
| `bride` | The bride at an engagement or a wedding. | pc:part_bride (meaning) |
| `groom` | The groom at an engagement or a wedding. | pc:part_groom (meaning) |
| `boy` | The boy at his bar mitzvah. | pc:part_boy (meaning) |
| `deceased` | The person who died, at a death. | pc:part_deceased (meaning) |
| `remembered` | The person remembered, at a memorial. | pc:part_remembered (meaning) |

### EventTypes

Event types: the values of event_types in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `engagement` | An engagement event; participation uses event_participation with a mention role. | pc:event_types_engagement (meaning) |
| `wedding` | Compatibility value wedding: preserved unchanged from production event types. | pc:event_types_wedding (meaning) |
| `birth` | Compatibility value birth: preserved unchanged from production event types. | pc:event_types_birth (meaning) |
| `death` | Compatibility value death: preserved unchanged from production event types. | pc:event_types_death (meaning) |
| `bar_mitzvah` | Compatibility value bar_mitzvah: preserved unchanged from production event types. | pc:event_types_bar_mitzvah (meaning) |
| `celebration` | Compatibility value celebration: preserved unchanged from production event types. | pc:event_types_celebration (meaning) |
| `community_event` | Compatibility value community_event: preserved unchanged from production event types. | pc:event_types_community_event (meaning) |
| `holocaust_event` | Compatibility value holocaust_event: preserved unchanged from production event types. | pc:event_types_holocaust_event (meaning) |
| `other` | Compatibility value other: preserved unchanged from production event types. | pc:event_types_other (meaning) |
| `memorial` | One commemoration of a deceased person, including annual and 30-day memorials. A remembrance is never the death itself. | pc:site_event_memorial (meaning) |

### ExternalSourceTypes

External source types: the values of external_source_types in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `arolsen_archives` | International Center on Nazi Persecution. Contains records of Holocaust victims. | pc:external_source_types_arolsen_archives (meaning) |
| `familysearch` | Genealogical records including Polish vital records. | pc:external_source_types_familysearch (meaning) |
| `findagrave` | Cemetery and burial records. | pc:external_source_types_findagrave (meaning) |
| `geni` | Collaborative family tree platform. | pc:external_source_types_geni (meaning) |
| `jewishgen` | Jewish genealogical research. Contains Yizkor books, vital records, and community data. | pc:external_source_types_jewishgen (meaning) |
| `jri_poland` | Jewish Records Indexing - Poland. Contains indexed vital records. | pc:external_source_types_jri_poland (meaning) |
| `wikipedia` | General reference for locations and events. | pc:external_source_types_wikipedia (meaning) |
| `yad_vashem` | World Holocaust Remembrance Center. Contains Pages of Testimony and victim database. | pc:external_source_types_yad_vashem (meaning) |

### FactTypes

Fact types: the values of fact_types in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `birth` | A sourced birth date; a birth place uses rico:hasBirthPlace independently, including when no date is known. | rico:hasBirthDate (meaning) |
| `death` | A sourced death date; a death place uses rico:hasDeathPlace independently, including when no date is known. | rico:hasDeathDate (meaning) |
| `residence` | Residence in a place at a specified time. | rico:hasOrHadLocation (meaning) |
| `occupation` | An occupation, optionally bounded in time. | rico:hasOrHadOccupationOfType (meaning) |
| `office` | Holding a Position at a time; person occupiesOrOccupied the position, qualified through PositionHoldingRelation. | rico:occupiesOrOccupied (meaning); via rico:PositionHoldingRelation |
| `membership` | A person isOrWasMemberOf a group, inverse of group hasOrHadMember, qualified through MembershipRelation. | rico:isOrWasMemberOf (meaning); via rico:MembershipRelation |
| `education` | School attendance or education at a specified time. | pc:fact_types_education (meaning) |
| `emigration` | A dated departure to live elsewhere; establishes neither death nor survival. | pc:fact_types_emigration (meaning) |
| `survival` | Evidence that a person was alive at a specified time. | pc:fact_types_survival (meaning) |
| `parenthood` | Parenthood of an unnamed child without inventing a person node; claims naming a relative use kinship, and links between identified people use relationships. Deprecated in 1.2.0: represent the child as a person and link each parent by parent_of. | pc:fact_types_parenthood (meaning) |
| `ghetto_role` | A sourced ghetto activity not expressible as membership or office; use membership or office whenever those fit. | pc:fact_types_ghetto_role (meaning) |
| `partisan_service` | A sourced partisan activity beyond membership or office; use membership or office whenever those fit. | pc:fact_types_partisan_service (meaning) |
| `deportation` | A sourced forced removal at a date and place; event participation may link its event. | pc:fact_types_deportation (meaning) |
| `burial` | A sourced interment, optionally dated and placed; distinct from death. | pc:fact_types_burial (meaning) |
| `commemoration` | A sourced act of remembrance; event participation may link its event. | pc:fact_types_commemoration (meaning) |
| `event_participation` | Taking part in an event with an explicit mention role; weddings are events, not marriage facts. | rico:isOrWasParticipantIn (meaning) |
| `other` | An assertion awaiting an owner-approved type; requires a nonempty proposed_type. | pc:fact_types_other (meaning) |
| `kinship` | A source's statement that the person is related, in a stated way, to a named person who need not be identified | rico:hasFamilyAssociationWith (meaning); via rico:FamilyRelation |

### FateOutcomes

Fate outcomes: the values of fate_outcomes in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `unknown` | Compatibility value unknown: preserved unchanged from production fate outcomes. | pc:fate_outcomes_unknown (meaning) |
| `perished` | Compatibility value perished: preserved unchanged from production fate outcomes. How sure the conclusion is lives in the fate's separate confidence; the site's legacy likely_* values are derived from outcome plus confidence. | pc:fate_outcomes_perished (meaning) |
| `survived` | Compatibility value survived: preserved unchanged from production fate outcomes. How sure the conclusion is lives in the fate's separate confidence; the site's legacy likely_* values are derived from outcome plus confidence. | pc:fate_outcomes_survived (meaning) |
| `died_before` | Compatibility value died_before: preserved unchanged from production fate outcomes. | pc:fate_outcomes_died_before (meaning) |
| `not_applicable` | Compatibility value not_applicable: preserved unchanged from production fate outcomes. | pc:fate_outcomes_not_applicable (meaning) |

### Gender

Gender: the values of gender in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `male` | Compatibility value male: preserved unchanged from production gender. | pc:gender_male (meaning) |
| `female` | Compatibility value female: preserved unchanged from production gender. | pc:gender_female (meaning) |
| `unknown` | Compatibility value unknown: preserved unchanged from production gender. | pc:gender_unknown (meaning) |

### HolocaustFateTypes

Holocaust fate types: the values of holocaust_fate_types in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `unknown` | Fate during Holocaust is not known | pc:holocaust_fate_types_unknown (meaning) |
| `perished` | Confirmed killed during Holocaust | pc:holocaust_fate_types_perished (meaning) |
| `likely_perished` | Living in area that was later destroyed, presumed perished | pc:holocaust_fate_types_likely_perished (meaning) |
| `survived` | Confirmed survived the Holocaust | pc:holocaust_fate_types_survived (meaning) |
| `likely_survived` | Living outside Nazi-occupied areas at time of publication | pc:holocaust_fate_types_likely_survived (meaning) |
| `died_before` | Died before the Holocaust began | pc:holocaust_fate_types_died_before (meaning) |
| `not_applicable` | Non-Jewish individual | pc:holocaust_fate_types_not_applicable (meaning) |

### ImpressoTypes

Impresso types: the content-item types of Impresso as vocabulary/site-content.json, version 1.0.0, lists them in impresso_types. Impresso defines them in a JSON Schema, not an ontology, so they carry no meaning here.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `article` | The Impresso type article. | No direct mapping recorded |
| `ad` | The Impresso type ad. | No direct mapping recorded |
| `image` | The Impresso type image. | No direct mapping recorded |
| `table` | The Impresso type table. | No direct mapping recorded |
| `death_notice` | The Impresso type death_notice. | No direct mapping recorded |
| `weather` | The Impresso type weather. | No direct mapping recorded |
| `page` | The Impresso type page. | No direct mapping recorded |
| `radio_bulletin` | The Impresso type radio_bulletin. | No direct mapping recorded |
| `radio_broadcast_episode` | The Impresso type radio_broadcast_episode. | No direct mapping recorded |
| `chronicle` | The Impresso type chronicle. | No direct mapping recorded |
| `chapter` | The Impresso type chapter. | No direct mapping recorded |
| `discussion` | The Impresso type discussion. | No direct mapping recorded |
| `entertainment` | The Impresso type entertainment. | No direct mapping recorded |

### LifeEventTypes

Life event types: the values of life_event_types in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `wedding` | Compatibility value wedding: preserved unchanged from production life event types. | pc:life_event_types_wedding (meaning) |
| `birth` | Compatibility value birth: preserved unchanged from production life event types. | pc:life_event_types_birth (meaning) |
| `death` | Compatibility value death: preserved unchanged from production life event types. | pc:life_event_types_death (meaning) |
| `bar_mitzvah` | Compatibility value bar_mitzvah: preserved unchanged from production life event types. | pc:life_event_types_bar_mitzvah (meaning) |
| `celebration` | Compatibility value celebration: preserved unchanged from production life event types. | pc:life_event_types_celebration (meaning) |
| `community_event` | Compatibility value community_event: preserved unchanged from production life event types. | pc:life_event_types_community_event (meaning) |
| `other` | Compatibility value other: preserved unchanged from production life event types. | pc:life_event_types_other (meaning) |

### LocationTypes

Location types: the values of location_types in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `city` | Compatibility value city: preserved unchanged from production location types. | ehri:City (meaning) |
| `town` | Compatibility value town: preserved unchanged from production location types. | pc:location_types_town (meaning) |
| `village` | Compatibility value village: preserved unchanged from production location types. | pc:location_types_village (meaning) |
| `shtetl` | Compatibility value shtetl: preserved unchanged from production location types. | pc:location_types_shtetl (meaning) |
| `street` | Compatibility value street: preserved unchanged from production location types. | pc:location_types_street (meaning) |
| `address` | Compatibility value address: preserved unchanged from production location types. | pc:location_types_address (meaning) |
| `landmark` | Compatibility value landmark: preserved unchanged from production location types. | pc:location_types_landmark (meaning) |
| `country` | Compatibility value country: preserved unchanged from production location types. | ehri:Country (meaning) |
| `region` | Compatibility value region: preserved unchanged from production location types. | ehri:Region (meaning) |
| `district` | Compatibility value district: preserved unchanged from production location types. | pc:location_types_district (meaning) |
| `ghetto` | Compatibility value ghetto: preserved unchanged from production location types. | pc:location_types_ghetto (meaning) |
| `camp` | Compatibility value camp: preserved unchanged from production location types. | pc:location_types_camp (meaning) |
| `massacre_site` | Compatibility value massacre_site: preserved unchanged from production location types. | pc:location_types_massacre_site (meaning) |
| `deportation_point` | Compatibility value deportation_point: preserved unchanged from production location types. | pc:location_types_deportation_point (meaning) |
| `forest` | Compatibility value forest: preserved unchanged from production location types. | pc:location_types_forest (meaning) |

### MentionRoles

Mention roles: the values of mention_roles in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `subject` | The person whom the source passage concerns. | pc:mention_roles_subject (meaning) |
| `deceased` | The person whose death the passage concerns; a mention role alone is not death evidence. | pc:mention_roles_deceased (meaning) |
| `honoree` | The person being honored or congratulated. | pc:mention_roles_honoree (meaning) |
| `signer` | A person signing the item. | pc:mention_roles_signer (meaning) |
| `mourner` | A person identified as mourning. | pc:mention_roles_mourner (meaning) |
| `advertiser` | A person placing or represented by an advertisement. | pc:mention_roles_advertiser (meaning) |
| `author` | The author identified by a byline or attribution. | pc:mention_roles_author (meaning) |
| `office_holder` | A person named in an official capacity; an office fact requires its own evidence. | pc:mention_roles_office_holder (meaning) |
| `donor` | A person identified as a donor. | pc:mention_roles_donor (meaning) |
| `named` | A person named without a more specific established role. | pc:mention_roles_named (meaning) |
| `betrothed` | A person identified as engaged to marry. | pc:mention_roles_betrothed (meaning) |
| `parent` | A participant identified as a parent; a named parent-child link belongs in relationships. | pc:mention_roles_parent (meaning) |

### NameKinds

Name kinds: the values of name_kinds in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `printed` | A name exactly as printed in a source. | pc:name_kinds_printed (meaning) |
| `birth` | A name used at birth, including a maiden name. | pc:name_kinds_birth (meaning) |
| `married` | A name used following marriage. | pc:name_kinds_married (meaning) |
| `later` | A name used later in life, without assuming the reason for its adoption. | pc:name_kinds_later (meaning) |
| `nickname` | A familiar or informal name. | pc:name_kinds_nickname (meaning) |
| `alias` | An alternative assumed name. | pc:name_kinds_alias (meaning) |
| `religious` | A name used in religious life. | pc:name_kinds_religious (meaning) |
| `spelling` | An alternative spelling of a name, without asserting a different identity. | pc:name_kinds_spelling (meaning) |
| `supplied` | An attributed description used to name a person whom the source does not name. | pc:site_name_supplied (meaning) |

### ReadingStatusValue

Reading states: the values of a content item's reading_status, from vocabulary/reading-status.json, whose entry reading_status describes the field: Optional per-field reading provenance. Null is unrecorded. A session check may cover particular words only.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `machine` | A machine reading without a recorded qualifying check. | pc:site_reading_machine (meaning) |
| `session_checked` | An AI session checked or corrected the field, possibly particular words only. | pc:site_reading_session_checked (meaning) |
| `person_corrected` | A recorded human author corrected the field; AI drafts and approvals alone do not qualify. | pc:site_reading_person_corrected (meaning) |

### RelationshipTypes

Relationship types: the values of relationship_types in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `child_in_law` | The subject is child in law of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasFamilyAssociationWith (meaning); via rico:FamilyRelation |
| `child_of` | The subject is child of of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:isChildOf (meaning); via rico:ChildRelation |
| `colleague` | The subject is colleague of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:isAgentAssociatedWithAgent (meaning); via rico:AgentToAgentRelation |
| `cousin` | The subject is cousin of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasFamilyAssociationWith (meaning); via rico:FamilyRelation |
| `family_member` | The subject is family member of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasFamilyAssociationWith (meaning); via rico:FamilyRelation |
| `friend` | The subject is friend of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:isAgentAssociatedWithAgent (meaning); via rico:AgentToAgentRelation |
| `grandchild_of` | The subject is grandchild of the related person; direction is descendant to ascendant. The vocabulary ID retains the exact generation; RiC-O DescendanceRelation covers descent across any number of intermediate persons. | rico:hasAncestor (meaning); via rico:DescendanceRelation |
| `grandparent_of` | The subject is grandparent of the related person; direction is ascendant to descendant. The vocabulary ID retains the exact generation; RiC-O DescendanceRelation covers descent across any number of intermediate persons. | rico:hasDescendant (meaning); via rico:DescendanceRelation |
| `in_law` | The subject is in law of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasFamilyAssociationWith (meaning); via rico:FamilyRelation |
| `nephew_niece_of` | The subject is nephew niece of of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasFamilyAssociationWith (meaning); via rico:FamilyRelation |
| `parent_in_law` | The subject is parent in law of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasFamilyAssociationWith (meaning); via rico:FamilyRelation |
| `parent_of` | The subject is parent of of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasChild (meaning); via rico:ChildRelation |
| `sibling` | The subject is sibling of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasSibling (meaning); via rico:SiblingRelation |
| `sibling_in_law` | The subject is sibling in law of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasFamilyAssociationWith (meaning); via rico:FamilyRelation |
| `spouse` | The subject is spouse of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasOrHadSpouse (meaning); via rico:SpouseRelation |
| `student_of` | The subject is student of of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasOrHadTeacher (meaning); via rico:TeachingRelation |
| `teacher_of` | The subject is teacher of of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasOrHadStudent (meaning); via rico:TeachingRelation |
| `uncle_aunt_of` | The subject is uncle aunt of of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | rico:hasFamilyAssociationWith (meaning); via rico:FamilyRelation |
| `great_grandparent_of` | The subject is great-grandparent of the related person; direction is ascendant to descendant. The vocabulary ID retains the exact generation; RiC-O DescendanceRelation covers descent across any number of intermediate persons. | rico:hasDescendant (meaning); via rico:DescendanceRelation |
| `great_grandchild_of` | The subject is great-grandchild of the related person; direction is descendant to ascendant. The vocabulary ID retains the exact generation; RiC-O DescendanceRelation covers descent across any number of intermediate persons. | rico:hasAncestor (meaning); via rico:DescendanceRelation |

### ReviewStates

Review states: the values of review_states in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `pending` | Awaiting human editorial approval. | pc:review_states_pending (meaning) |
| `approved` | Human editorial review has approved the item; publication remains subject to downstream privacy rules. | pc:review_states_approved (meaning) |

### SourceKinds

Source kinds: the values of source_kinds in vocabulary/sourced-entities.json, version 1.3.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `archive_database` | Archive database source kinds category. | pc:source_kinds_archive_database (meaning) |
| `book` | Book source kinds category. | pc:source_kinds_book (meaning) |
| `memorial_book` | Memorial book source kinds category. | pc:source_kinds_memorial_book (meaning) |
| `oral_history` | Oral history source kinds category. | pc:source_kinds_oral_history (meaning) |
| `memoir` | Memoir source kinds category. | pc:source_kinds_memoir (meaning) |
| `photograph` | Photograph source kinds category. | pc:source_kinds_photograph (meaning) |
| `press` | Press source kinds category. | pc:source_kinds_press (meaning) |
| `family_document` | Family document source kinds category. | pc:source_kinds_family_document (meaning) |
| `web_page` | Web page source kinds category. | pc:source_kinds_web_page (meaning) |
| `the_paper` | The paper source kinds category. | pc:source_kinds_the_paper (meaning) |

### Subjects

Subjects: the values of subjects in vocabulary/site-content.json, version 1.0.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `education` | Education, schools and learning. | pc:subject_education (meaning) |
| `culture` | Cultural activity and institutions. | pc:subject_culture (meaning) |
| `health` | Health, medicine and hygiene. | pc:subject_health (meaning) |
| `palestine` | Life and developments in Palestine. | pc:subject_palestine (meaning) |
| `jewish_world` | Jewish communities beyond the immediate locality. | pc:subject_jewish_world (meaning) |
| `literature` | Literary works and literary life. | pc:subject_literature (meaning) |
| `sport` | Sport and sporting associations. | pc:subject_sport (meaning) |
| `economy` | Trade, work and economic conditions. | pc:subject_economy (meaning) |
| `community_affairs` | Local and regional communal life. | pc:subject_community_affairs (meaning) |
| `zionism` | Zionist activity, institutions and campaigns. | pc:subject_zionism (meaning) |
| `international_affairs` | News of the wider world. | pc:subject_international_affairs (meaning) |

### TitleTypes

Title types: the values of title_types in vocabulary/site-content.json, version 1.0.0.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `printed` | The printed words naming a content item or a section. | pc:title_type_printed (meaning) |
| `supplied` | An attributed English name pinned to the text it was made from. | pc:title_type_supplied (meaning) |

### AuthorshipKind

Whether a person or a program wrote a supplied title or a translation.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `person` | A person wrote it. | No direct mapping recorded |
| `model` | A language model wrote it. | No direct mapping recorded |

### AddressGrain

How a mention is pinned to the page: to the words of the printed name, or only to whole regions where the words are not located.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `words` | The mention is pinned to the printed name's words. | No direct mapping recorded |
| `regions` | The mention is pinned to whole regions of print; its printed name is not located. | No direct mapping recorded |

### HttpsUri

A web address that begins https:// and holds no white space, as the Pydantic twin's pattern says; the Zod twin asks for a URL whose protocol is https.

uri; pattern: ^https://[^\s/?#]+[^\s]*$

### PrintedCalendar

The calendar a date was printed or written in.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `gregorian` | The Gregorian calendar. | No direct mapping recorded |
| `hebrew` | The Hebrew calendar; its words are kept as printed and never converted. | No direct mapping recorded |

### SourceDerivationRelation

How a source we hold was made from another: a copy of it, or a transcription of it.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `copy` | A copy of the original record. | ehri:isCopyOf (meaning) |
| `transcription` | A transcription of the original record, which describes it and is not a copy of it. | rico:describesOrDescribed (meaning) |

### SourceMadeBy

Who made a source, as a category: never an agent, so never its creator.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `family` | The family. | No direct mapping recorded |
| `studio` | A photographer's studio. | No direct mapping recorded |
| `institution` | An institution. | No direct mapping recorded |
| `perpetrator` | The perpetrators. | No direct mapping recorded |
| `unknown` | Not known. | No direct mapping recorded |

### SourceQuoteCondition

The owner's condition on a private source's cleared quotes.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `unique_information` | A quote is shown only where no other record states the same (the owner's word of 24 October 2026). | No direct mapping recorded |

### SourcedDatePrecision

How much of a sourced date is known: its year, its month, its day, or a range.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `year` | Only the year is known; the start is written YYYY. | No direct mapping recorded |
| `month` | The year and month are known; the start is written YYYY-MM. | No direct mapping recorded |
| `day` | The day is known; the start is written YYYY-MM-DD. | No direct mapping recorded |
| `range` | The date lies between a start and an end. | No direct mapping recorded |

### MediaDecisionRole

Whose role made a decision about a medium.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `owner` | The owner. | No direct mapping recorded |
| `project` | The project. | No direct mapping recorded |

### MediaGrantedBy

Who gave the permission to show a medium, by role; never a person's name.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `owner` | The owner. | No direct mapping recorded |
| `family` | The family. | No direct mapping recorded |
| `holder` | The holder. | No direct mapping recorded |
| `institution` | An institution. | No direct mapping recorded |

### MediaIdentifiedBy

What identifies a person shown in a picture.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `family` | The family. | No direct mapping recorded |
| `record` | A record. | No direct mapping recorded |
| `inscription` | The picture's own inscription. | No direct mapping recorded |

### MediaKind

What a medium is: an image, a sound recording, a film or a document.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `image` | A still picture, such as a photograph. | pc:media_image (meaning) |
| `audio` | A sound recording. | pc:media_audio (meaning) |
| `video` | A film or video. | pc:media_video (meaning) |
| `document` | A document, with its transcript. | pc:media_document (meaning) |

### MediaWithdrawalReason

Why a medium was withdrawn.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `family` | At the family's request. | No direct mapping recorded |
| `holder` | At the holder's request. | No direct mapping recorded |
| `error` | For an error. | No direct mapping recorded |

### Coordinate

One coordinate of a place, in degrees from -180 to 180. The twins bound the latitude, the first, to -90 to 90; a bound by position in a list cannot be said here (known-looser.yaml).

float; minimum: -180; maximum: 180

### HolderKind

What kind of holder keeps a source.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `institution` | An institution, such as an archive or a library. | ehri:Institution (meaning) |
| `family` | A family holding papers. | ehri:Family (meaning) |
| `private` | A private person holding papers; the name is never published. | rico:Person (meaning) |

### SharedFactRepresentation

The form a fact is kept in: a structured statement, retained prose, or an image path.

| Value | Meaning | Standard mapping |
| --- | --- | --- |
| `structured` | A structured statement of a released type. | No direct mapping recorded |
| `prose` | Retained prose, kept as other with a proposed type until it is reviewed. | No direct mapping recorded |
| `image` | An image path, kept as other with a proposed type. | No direct mapping recorded |

## Validator responsibilities

The following measured differences are checked by `record compare linkml`. Its report must exercise every listed place, accept every real document and pass the bundled Zod archive and catalog checks. The generated Python models also validate every document and the complete archive. Python-specific API adjustments are recorded in `linkml/python-compatibility.json`, each with synthetic witnesses; retained rules still check dates, uniqueness and agreement between records.

### Required key nullable

Present-and-null is a distinction LinkML's data model does not make.

LinkML has no null apart from absence. A required slot must hold a value, and its JSON Schema refuses null; an optional slot may be left out, and its JSON Schema accepts null. The twins require these keys while permitting null values, so the definition marks them optional to retain that nullable shape, and its JSON Schema accepts a document that leaves the key out. value_presence PRESENT makes gen-json-schema put the key in required and still allow null, but the metamodel says PRESENT has "the same effect as required=true" (status unstable) and the Pydantic validation plugin ignores it, so it is not used.

Enforced by:

- zod/page.schema.ts: Block.unit_id is z.string().nullable(), not optional
- zod/content-item.schema.ts: ReadingStatus.text and .english are nullable, not optional
- zod/site-issue.schema.ts: IssueMention.printed_name is nullable, not optional
- zod/media.schema.ts: MediaDepicted.person_id is nullable, not optional
- pydantic/page.py, pydantic/content_item.py, pydantic/site_issue.py, pydantic/media.py: the same fields typed X \| None with no default
- pruzhany-steps: the bundled Zod validator (schemas/site-next/validate-archive.js), before site_writer installs a document

Exact places:

- `schemas/site/pages.schema.json#/properties/pages/items/properties/blocks/items/properties/unit_id`
- `schemas/site-next/content-items.schema.json#/properties/content_items/items/properties/reading_status/anyOf/0/properties/text`
- `schemas/site-next/content-items.schema.json#/properties/content_items/items/properties/reading_status/anyOf/0/properties/english`
- `schemas/site-next/mentions.schema.json#/properties/mentions/items/properties/printed_name`
- `schemas/site-next/shared-record.schema.json#/properties/media/anyOf/0/items/properties/depicted/items/properties/person_id`

### Optional key not nullable

Present-and-null is a distinction LinkML's data model does not make.

gen-json-schema gives every optional slot a null branch (its --include-null, the default). --no-include-null is one switch for a whole schema and would refuse the null that the 248 optional keys which do allow it accept, so the definition keeps the default and its JSON Schema accepts null here. An optional slot with equals_string needs no entry: const refuses null by itself; so does equals_string_in, which the house style uses for a list of values the naming rule refuses or that are addresses (media rights), and whose enum refuses null too.

Enforced by:

- zod/editions.schema.ts: Edition.holiday, Holiday.hebrewName and HistoricalEvent.endDate are optional, not nullable; measured by record compare linkml on the catalog and synthetic fixtures
- zod/page.schema.ts: Block.confidence is z.number().optional()
- zod/site-common.schema.ts: checked_against is .optional(), not nullable
- zod/shared-record.schema.ts: SharedRecord.holders is z.array(...).optional()
- pydantic/site_common.py: checked_against refuses null in a field validator (check_is_not_null)
- pydantic/shared_record.py: holders has a default and no None; Block.confidence in pydantic/page.py accepts null, so only Zod refuses it
- pruzhany-steps: the bundled Zod validator (schemas/site-next/validate-archive.js), before site_writer installs a document

Exact places:

- `schemas/site/editions.schema.json#/properties/editions/items/properties/holiday`
- `schemas/site/editions.schema.json#/properties/holidays/items/properties/hebrewName`
- `schemas/site/editions.schema.json#/properties/historicalEvents/items/properties/endDate`
- `schemas/site/pages.schema.json#/properties/pages/items/properties/blocks/items/properties/confidence`
- `schemas/site-next/content-items.schema.json#/properties/content_items/items/properties/supplied_title/properties/checked_against`
- `schemas/site-next/content-items.schema.json#/properties/content_items/items/properties/translation/anyOf/0/properties/checked_against`
- `schemas/site-next/content-items.schema.json#/properties/sections/items/properties/supplied_title/anyOf/0/properties/checked_against`
- `schemas/site-next/shared-record.schema.json#/properties/holders`

### Position wise bounds

LinkML has no constraint by position within a list, which is what JSON Schema's prefixItems is.

A multivalued slot has one range and one bound for every item. The definition bounds each of a box's four numbers at least 0 (NonNegativeNumber), so it accepts a width or a height of 0, and each coordinate from -180 to 180, so it accepts a latitude beyond 90. A class with named parts would hold every bound but change the stored shape of a box and of coordinates, which the plan rules out (section 10).

Enforced by:

- zod/site-common.schema.ts: pixelBox, a z.tuple of nonnegative, nonnegative, positive, positive
- zod/shared-record.schema.ts: Place.coordinates, a z.tuple of min(-90).max(90) and min(-180).max(180)
- pydantic/site_common.py: PrintedAddress.bbox, a tuple with ge=0, ge=0, gt=0, gt=0
- pydantic/shared_record.py: Place.coordinates, a tuple with ge=-90, le=90 and ge=-180, le=180
- pruzhany-steps: the bundled Zod validator (schemas/site-next/validate-archive.js), before site_writer installs a document

Exact places:

- `schemas/site-next/content-items.schema.json#/properties/content_items/items/properties/printed_title/anyOf/0/properties/addresses/items/properties/bbox`
- `schemas/site-next/content-items.schema.json#/properties/content_items/items/properties/supplied_title/properties/based_on/properties/addresses/items/properties/bbox`
- `schemas/site-next/content-items.schema.json#/properties/content_items/items/properties/translation/anyOf/0/properties/based_on/properties/addresses/items/properties/bbox`
- `schemas/site-next/content-items.schema.json#/properties/sections/items/properties/printed_title/properties/addresses/items/properties/bbox`
- `schemas/site-next/content-items.schema.json#/properties/sections/items/properties/supplied_title/anyOf/0/properties/based_on/properties/addresses/items/properties/bbox`
- `schemas/site-next/mentions.schema.json#/properties/mentions/items/properties/addresses/items/properties/bbox`
- `schemas/site-next/shared-record.schema.json#/properties/persons/items/properties/names/items/properties/citations/anyOf/0/items/properties/addresses/anyOf/0/items/properties/bbox`
- `schemas/site-next/shared-record.schema.json#/properties/places/items/properties/coordinates/anyOf/0`
- `schemas/site-next/shared-record.schema.json#/properties/facts/items/properties/citations/items/properties/addresses/anyOf/0/items/properties/bbox`
- `schemas/site-next/shared-record.schema.json#/properties/relations/items/properties/citations/items/properties/addresses/anyOf/0/items/properties/bbox`

### Exclusive minimum on a number

LinkML's bounds are inclusive only.

minimum_value is inclusive and metamodel 1.12.0 has no exclusive bound, so the definition says at least 0 and accepts a duration of 0. none_of with equals_number 0 does refuse 0 in the generated JSON Schema (minimum 0 and not const 0), but the generator then drops the null branch the export allows on this optional key (measured), so it is not used. A whole number above 0 needs no entry: minimum_value 1 says the same (PositiveInteger).

Enforced by:

- zod/media.schema.ts: Media.duration is z.number().positive().nullish()
- pydantic/media.py: Media.duration is Field(gt=0) or None
- pruzhany-steps: the bundled Zod validator (schemas/site-next/validate-archive.js), before site_writer installs a document

Exact places:

- `schemas/site-next/shared-record.schema.json#/properties/media/anyOf/0/items/properties/duration/anyOf/0`

The complete refinement inventory is in `linkml/checks/documents.yaml` and `linkml/checks/record.yaml`. Rules about uniqueness, agreement between files, citation content and identity remain with the validators and record rule catalog.

## Requirements still planned

These are requirements recorded by the project, not extra fields accepted by the schemas. Existing family records, word boxes and corrections are not being declared absent; the gaps below describe what remains to complete their contracts.

### Stable line and word identifiers

Lines and word boxes already exist in rebuilt Impresso editions. Their stable identifiers and redirect or tombstone behavior remain to be defined.

Source: `steps:docs/record/end-state.md:204` — “ids exist for pages, blocks, pieces and people, but not for lines and words”.

### Trust recorded for each word

Record a word's own check level, so correcting it does not mark the entire line or piece as checked. Existing piece-level checks remain useful evidence.

Source: `steps:docs/record/end-state.md:60` — “Correcting a word marks that word as person-checked, not its line or piece.”.

### Evidence for joins and non-joins

Make existing identity decisions complete and consistent, retaining evidence, attribution and date for joins and decisions that two records are different. Uncertain identity remains an allowed outcome.

Source: `steps:docs/record/end-state.md:97` — “Joins and "these are different" rulings are both recorded, each with its evidence, who made it and when.”.

### Family relationships supported by evidence

Family records already have a shape. Complete the evidence and reconstruction of their relationships where the sources allow it; no target count is imposed.

Source: `steps:docs/record/end-state.md:239` — “Families are reconstructed where evidence allows, with no count target.”.

### Works and typed organizations

Define works and finish organization typing, resolving local entities and recording outside links or explicit lack of a link for world entities.

Source: `steps:docs/record/end-state.md:242` — “Organizations and works:** typed; local ones resolved; world ones linked or marked unlinkable.”.
