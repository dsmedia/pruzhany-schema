# The mentions document of a Pruzhany issue

One issue's mentions: each place a content item names a person of the shared record, with the printed words or regions where the name stands and the person's roles there.

URI: https://pruzhany.org/ns/mentions

Name: pruzhany_mentions



## Classes

| Class | Description |
| --- | --- |
| [Attribution](Attribution.md) | Who made or allowed something, on what day, with an optional note. |
| [Authorship](Authorship.md) | Who wrote a supplied title, a translation or a check of one, a person or a model, and on which day. |
| [CitedTextBasis](CitedTextBasis.md) | The exact source words of a citation or source title. The containing citation's locator or source description locates them; printed addresses are optional, and when supplied remain nonempty real image-and-box witnesses. |
| [CitedTranslation](CitedTranslation.md) | English of a citation's quote or a source title, located by its containing record. Reuses Translation's English, attribution and check contract without requiring an image and box for a book page or archive record. |
| [ContentItemBlockRef](ContentItemBlockRef.md) | The regions of one page that a content item or a section heading covers, in reading order. |
| [CrossReference](CrossReference.md) | A link from one content item to another in the same issue, with how sure it is and why. |
| [EnglishCheck](EnglishCheck.md) | A later, separate check of one English field against one exact reading of the printed text, bound to both and to the judgement kept by their digests. |
| [IssueMention](IssueMention.md) | A person of the shared record named in a content item, pinned to the printed words of the name or to whole regions, with the person's roles there. A mention alone does not say the content item is about the person. |
| [IssueMentionsData](IssueMentionsData.md) | One issue's mentions document: the issue's date and its mentions. |
| [PrintedAddress](PrintedAddress.md) | Where some printed words stand: the page picture, a box on it in the picture's own pixels, and the words read in that box. |
| [PrintedTitle](PrintedTitle.md) | A title as printed in the paper: its words and where each line of them stands. |
| [SuppliedTitle](SuppliedTitle.md) | A title supplied in English for a content item or section, with what it was made from, who made it and, where one was made, its later check. |
| [TextBasis](TextBasis.md) | The exact text a translation or supplied title was made from, and where it is printed, kept even after the text is read again. |
| [TitleCheck](TitleCheck.md) | A check of a supplied title's English. |
| [Translation](Translation.md) | An English translation of exact source words, with the exact text it was made from, who made it and, where one was made, its later check. |
| [TranslationCheck](TranslationCheck.md) | A check of a translation's English. |



## Slots

| Slot | Description |
| --- | --- |
| [address_grain](address_grain.md) | Whether the mention is pinned to the name's words or only to whole regions. |
| [addresses](addresses.md) | Where the name stands: the words of the name, or the whole regions it is in. |
| [attribution](attribution.md) | Who checked it, and on which day. |
| [based_on](based_on.md) | The exact printed text the title was made from, and where it is printed. |
| [bbox](bbox.md) | The box on the picture: left, top, width and height, in the picture's pixels. |
| [block_ids](block_ids.md) | The regions on that page, by their ids in the pages document, in reading order. |
| [by](by.md) | Who made it or allowed it: a person, a session or a program. |
| [checked_against](checked_against.md) | A later check of this title against the reading, where one was made. |
| [confidence](confidence.md) | How sure the link is, from 0 to 1. |
| [content_item_id](content_item_id.md) | The content item the name stands in, by its id in the content items document. |
| [english_sha256](english_sha256.md) | The SHA-256 digest of the checked English field's exact UTF-8 bytes. |
| [evidence](evidence.md) | What shows the link, in words. |
| [function](function.md) | The person's occupation or part in the content item, in a few words, such as bride, mourner or well-wisher. |
| [id](id.md) | The mention's id within the issue. |
| [image_uri](image_uri.md) | The page picture the box is on, by its name or address. |
| [issue_date](issue_date.md) | The issue's date, written YYYY-MM-DD. |
| [judgement_id](judgement_id.md) | The kept judgement, by an id without spaces followed by the field it judged, :title or :text. |
| [judgement_sha256](judgement_sha256.md) | The SHA-256 digest of the kept judgement file's exact bytes. |
| [kind](kind.md) | Whether a person or a model wrote it. |
| [language](language.md) | The title's language, always English (en). |
| [mentions](mentions.md) | The issue's mentions. |
| [note](note.md) | A note on how or why. |
| [on](on.md) | The day it was made or allowed. |
| [page_id](page_id.md) | The page, by its id in the pages document. |
| [person_id](person_id.md) | The person named, by their id in the shared record. |
| [printed_name](printed_name.md) | The name as printed, found at the mention's addresses; null when the mention is pinned only to whole regions. |
| [reading_id](reading_id.md) | The reading of the printed text that the English was checked against. |
| [reading_sha256](reading_sha256.md) | The SHA-256 digest of that reading's exact UTF-8 bytes. |
| [relationship](relationship.md) | What kind of link it is, in words. |
| [roles](roles.md) | The person's roles in the content item, such as the deceased or a mourner. |
| [source_text](source_text.md) | The text used, exactly, never normalised or replaced by a later reading. |
| [target_id](target_id.md) | The id of the content item linked to. |
| [text](text.md) | The words read in the box, exactly as read; empty for a patch with no readable line. |
| [title](title.md) | An honorific printed with the name, such as Rabbi or Dr., where one is kept. |
| [wkd_id](wkd_id.md) | The person's Wikidata id, where one is known. |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AddressGrain](AddressGrain.md) | How a mention is pinned to the page: to the words of the printed name, or only to whole regions where the words are not located. |
| [AuthorshipKind](AuthorshipKind.md) | Whether a person or a program wrote a supplied title or a translation. |
| [CitationRemarkKinds](CitationRemarkKinds.md) | Citation remark kinds: the values of citation_remark_kinds in vocabulary/sourced-entities.json, version 1.3.0. |
| [ClaimStatus](ClaimStatus.md) | Claim status: the values of claim_status in vocabulary/sourced-entities.json, version 1.3.0. |
| [CompatibilityEventTypes](CompatibilityEventTypes.md) | Compatibility event types: the values of compatibility_event_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [Confidence](Confidence.md) | Confidence: the values of confidence in vocabulary/sourced-entities.json, version 1.3.0. |
| [ContentItemSubtypes](ContentItemSubtypes.md) | Content item subtypes: the values of content_item_subtypes in vocabulary/site-content.json, version 1.1.0. |
| [ContentUnitRoles](ContentUnitRoles.md) | Content unit roles: the values of content_unit_roles in vocabulary/sourced-entities.json, version 1.3.0. |
| [EventParts](EventParts.md) | Event parts: the values of event_parts in vocabulary/sourced-entities.json, version 1.3.0. |
| [EventTypes](EventTypes.md) | Event types: the values of event_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [ExternalSourceTypes](ExternalSourceTypes.md) | External source types: the values of external_source_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [FactTypes](FactTypes.md) | Fact types: the values of fact_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [FateOutcomes](FateOutcomes.md) | Fate outcomes: the values of fate_outcomes in vocabulary/sourced-entities.json, version 1.3.0. |
| [Gender](Gender.md) | Gender: the values of gender in vocabulary/sourced-entities.json, version 1.3.0. |
| [HolocaustFateTypes](HolocaustFateTypes.md) | Holocaust fate types: the values of holocaust_fate_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [IdentifierTypes](IdentifierTypes.md) | Identifier types approved in ADR 0001 and linked-data ticket 03. |
| [ImpressoTypes](ImpressoTypes.md) | Impresso types: the content-item types of Impresso as vocabulary/site-content.json, version 1.1.0, lists them in impresso_types. Impresso defines them in a JSON Schema, not an ontology, so they carry no meaning here. |
| [LifeEventTypes](LifeEventTypes.md) | Life event types: the values of life_event_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [LocationTypes](LocationTypes.md) | Location types: the values of location_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [MentionRoles](MentionRoles.md) | Mention roles: the values of mention_roles in vocabulary/sourced-entities.json, version 1.3.0. |
| [NameKinds](NameKinds.md) | Name kinds: the values of name_kinds in vocabulary/sourced-entities.json, version 1.3.0. |
| [ReadingStatusValue](ReadingStatusValue.md) | Reading states: the values of a content item's reading_status, from vocabulary/reading-status.json, whose entry reading_status describes the field: Optional per-field reading provenance. Null is unrecorded. A session check may cover particular words only. |
| [RelationshipTypes](RelationshipTypes.md) | Relationship types: the values of relationship_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [ReviewStates](ReviewStates.md) | Review states: the values of review_states in vocabulary/sourced-entities.json, version 1.3.0. |
| [SourceKinds](SourceKinds.md) | Source kinds: the values of source_kinds in vocabulary/sourced-entities.json, version 1.3.0. |
| [Subjects](Subjects.md) | Subjects: the values of subjects in vocabulary/site-content.json, version 1.1.0. |
| [TitleTypes](TitleTypes.md) | Title types: the values of title_types in vocabulary/site-content.json, version 1.1.0. |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal specification |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [HostName](HostName.md) | A lowercase internet host name with at least one dot, such as collections.yadvashem.org. |
| [Integer](Integer.md) | An integer |
| [IsoDay](IsoDay.md) | A calendar day written YYYY-MM-DD, such as 1938-12-16. |
| [IsoYearMonthOrDay](IsoYearMonthOrDay.md) | A year, a month or a day, as far as it is known: YYYY, YYYY-MM or YYYY-MM-DD. |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. |
| [LanguageTag](LanguageTag.md) | A BCP 47 language tag, by the pattern in vocabulary/citation-requirements.json. |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model. |
| [NonBlankText](NonBlankText.md) | Text with at least one character that is not white space. |
| [NonNegativeInteger](NonNegativeInteger.md) | A whole number from 0 to 9007199254740991, the largest integer JavaScript holds exactly. As the range of a multivalued slot it bounds each item, not the list. |
| [NonNegativeNumber](NonNegativeNumber.md) | A number at least 0, such as each of the four numbers of a box on a page picture; the shapes bound the box's width and height above 0, which known-looser.yaml records. |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model. |
| [PositiveInteger](PositiveInteger.md) | A whole number from 1 to 9007199254740991; the shapes say above 0, which for a whole number is the same. |
| [ScriptCode](ScriptCode.md) | A four-letter ISO 15924 script code, such as Hebr or Latn. |
| [Sha256Hex](Sha256Hex.md) | A SHA-256 digest: exactly 64 lowercase hexadecimal digits and nothing after them. Some shapes write the pattern without its last part and add a length of 64, which says the same; LinkML has no length of a string, hence the last part. |
| [SimpleLanguageTag](SimpleLanguageTag.md) | A language tag in its simple form, letters then hyphenated parts, such as yi or yi-Latn. |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular day |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
