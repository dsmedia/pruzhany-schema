# The fates list of the Pruzhany record

Everyone printed in the paper whose fate the record knows, with where and when, the archives' records about them, how their age is known and whether they were children, and the list's counts and notes.

URI: https://pruzhany.org/ns/fates_list

Name: pruzhany_fates_list



## Classes

| Class | Description |
| --- | --- |
| [Attribution](Attribution.md) | Who made or allowed something, on what day, with an optional note. |
| [Authorship](Authorship.md) | Who wrote a supplied title, a translation or a check of one, a person or a model, and on which day. |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |
| [CitedTextBasis](CitedTextBasis.md) | The exact source words of a citation or source title. The containing citation's locator or source description locates them; printed addresses are optional, and when supplied remain nonempty real image-and-box witnesses. |
| [CitedTranslation](CitedTranslation.md) | English of a citation's quote or a source title, located by its containing record. Reuses Translation's English, attribution and check contract without requiring an image and box for a book page or archive record. |
| [ContentItemBlockRef](ContentItemBlockRef.md) | The regions of one page that a content item or a section heading covers, in reading order. |
| [CrossReference](CrossReference.md) | A link from one content item to another in the same issue, with how sure it is and why. |
| [EnglishCheck](EnglishCheck.md) | A later, separate check of one English field against one exact reading of the printed text, bound to both and to the judgement kept by their digests. |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |
| [FactQualifiers](FactQualifiers.md) | More about a fact, as named texts: how many children a notice names, how a statement is supported and the like. |
| [Fate](Fate.md) | What became of a person in the Holocaust, as far as the record shows, the facts it rests on and its review. |
| [FatesList](FatesList.md) | The fates list: its people, its counts and its notes. |
| [FatesListAge](FatesListAge.md) | How a person's age is known, and whether it marks a child. |
| [FatesListArchiveCount](FatesListArchiveCount.md) | How many people an archive's database names, and how many of them with an address. |
| [FatesListCounts](FatesListCounts.md) | The list's counts. |
| [FatesListDate](FatesListDate.md) | A normalized date: its start, how precise it is and, for a range, its end. |
| [FatesListFateDetail](FatesListFateDetail.md) | Where or when one of the person's own fate statements, or the death event it names, places the fate. |
| [FatesListOutsideRecord](FatesListOutsideRecord.md) | A record an archive holds about the person: the archive, the database it is in, the record's type and id as the archive gives them, and its own address where the record has one. |
| [FatesListPerson](FatesListPerson.md) | One person on the list: who, the fate, where the paper first prints them, where and when the fate is placed, the archives' records about them and how their age is known. |
| [FatesListPiece](FatesListPiece.md) | A published piece of an edition of the paper. |
| [Mention](Mention.md) | The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention. |
| [Name](Name.md) | One name of a person, a family, an organisation or a place, of one kind (printed, birth, married, supplied and so on), in one script. A person's, a family's and an organisation's names are agent names and a place's are place names (vocabulary/ site-content.json, bindings agent_name and place_name), so the class itself names no single term. |
| [PrintedAddress](PrintedAddress.md) | Where some printed words stand: the page picture, a box on it in the picture's own pixels, and the words read in that box. |
| [PrintedTitle](PrintedTitle.md) | A title as printed in the paper: its words and where each line of them stands. |
| [Review](Review.md) | Whether a person has reviewed a statement, who and on what day. |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |
| [SourcedDate](SourcedDate.md) | A date a source gives: a normalized start (and end, for a range) with how precise it is, or the words as printed with their calendar, or both. |
| [SourceDerivation](SourceDerivation.md) | The record a source we hold was made from, and how: a copy or a transcription of it. |
| [SuppliedTitle](SuppliedTitle.md) | A title supplied in English for a content item or section, with what it was made from, who made it and, where one was made, its later check. |
| [TextBasis](TextBasis.md) | The exact text a translation or supplied title was made from, and where it is printed, kept even after the text is read again. |
| [TitleCheck](TitleCheck.md) | A check of a supplied title's English. |
| [Translation](Translation.md) | An English translation of exact source words, with the exact text it was made from, who made it and, where one was made, its later check. |
| [TranslationCheck](TranslationCheck.md) | A check of a translation's English. |



## Slots

| Slot | Description |
| --- | --- |
| [accessed](accessed.md) | The day a person read the record. |
| [addresses](addresses.md) | Where that text is printed, one address a line or patch. |
| [age](age.md) | How the person's age is known; absent where the record gives no age. |
| [announced](announced.md) | The earliest published piece that announced the person's birth. |
| [archive](archive.md) | The archive's name, as the shared record's holder gives it. |
| [attribution](attribution.md) | Who checked it, and on which day. |
| [author](author.md) | Who wrote the source: an institution, never a member of its staff. |
| [based_on](based_on.md) | The exact printed text the title was made from, and where it is printed. |
| [bbox](bbox.md) | The box on the picture: left, top, width and height, in the picture's pixels. |
| [birth_year](birth_year.md) | The one year of birth the person's own records give. |
| [birth_year_known](birth_year_known.md) | The people whose own records give one year of birth, children or not. |
| [birth_years](birth_years.md) | The years of birth that disagree, in order. |
| [birth_years_disagree](birth_years_disagree.md) | The people whose own records give years of birth that disagree. |
| [block_ids](block_ids.md) | The regions on that page, by their ids in the pages document, in reading order. |
| [by](by.md) | Who made it or allowed it: a person, a session or a program. |
| [checked_against](checked_against.md) | A later check of this title against the reading, where one was made. |
| [child](child.md) | True for a child: one year of birth of 1925 or later, or a birth the paper announced. |
| [children](children.md) | The people marked as children. |
| [children_by_announcement](children_by_announcement.md) | The children marked because the paper announced their birth. |
| [children_by_birth_year](children_by_birth_year.md) | The children marked by one year of birth of 1925 or later. |
| [citations](citations.md) | The evidence: where in which sources the statement is found. |
| [collection](collection.md) | The database's title, as the shared record's source gives it. |
| [confidence](confidence.md) | How sure the fate is: confirmed or probable. |
| [content_item_id](content_item_id.md) | The piece's id, such as cu-1938-12-16-i0105, with another paper's lowercase code after cu- for any paper but the first, such as cu-abcd-1938-12-16-i0105. |
| [counts](counts.md) | The list's counts, so that a page never counts for itself. |
| [date](date.md) | The date, as the record holds it structured; its printed words are never carried. |
| [dated](dated.md) | The record's own date, apart from when it was published or consulted. |
| [derived_from](derived_from.md) | For a copy or a transcription we hold: the original it was made from, and how. |
| [edition_date](edition_date.md) | The edition's day, written YYYY-MM-DD. |
| [editor](editor.md) | Who edited the source. |
| [end](end.md) | The end of a range of dates, written as the start is. |
| [english_sha256](english_sha256.md) | The SHA-256 digest of the checked English field's exact UTF-8 bytes. |
| [event_id](event_id.md) | The life event the statement concerns, by its id in the record. |
| [evidence](evidence.md) | What shows the link, in words. |
| [evidence_confidence](evidence_confidence.md) | How sure the evidence makes the statement. |
| [fact_ids](fact_ids.md) | The shared record's birth statements that give the year. |
| [fate_details](fate_details.md) | Where and when the person's own death, survival and deportation statements place the fate, as the record holds them structured. |
| [first_mention](first_mention.md) | The earliest published piece that prints the person. |
| [function](function.md) | A function printed with the name. |
| [holder_id](holder_id.md) | Who holds the source, by its id in the record's holders. |
| [holocaust_related](holocaust_related.md) | True when the statement concerns the Holocaust. |
| [host](host.md) | The web host the source's records are served from, without www: every address cited from it is on that host or a subdomain of it. |
| [id](id.md) | The source's id in the record, which citations name. |
| [identity_confidence](identity_confidence.md) | How sure it is that the statement is about this person. |
| [image_uri](image_uri.md) | The page picture the box is on, by its name or address. |
| [inferred](inferred.md) | True when the date was worked out rather than read. |
| [judgement_id](judgement_id.md) | The kept judgement, by an id without spaces followed by the field it judged, :title or :text. |
| [judgement_sha256](judgement_sha256.md) | The SHA-256 digest of the kept judgement file's exact bytes. |
| [kind](kind.md) | The kind of statement: death, survival or deportation. |
| [known_by](known_by.md) | How the age is known: one year of birth, a birth the paper announced, or years that disagree. |
| [lang](lang.md) | Its language, as a language tag such as yi or en. |
| [language](language.md) | The title's language, always English (en). |
| [locator](locator.md) | An internal pointer into the project's files; never published and never a holder's record number. |
| [made_by](made_by.md) | Who made the source, as a category (family, studio, institution, perpetrator, unknown); never its creator. |
| [name](name.md) | The person's name as the site shows it. |
| [no_age](no_age.md) | The people with no age in the record; they are not marked as children. |
| [note](note.md) | A note on how or why. |
| [notes](notes.md) | What the counts count, in plain English, the people with no age among them. |
| [on](on.md) | The day it was made or allowed. |
| [organization_id](organization_id.md) | The organisation the statement concerns, by its id in the record. |
| [outcome](outcome.md) | The record's fate: perished or survived. |
| [outside_records](outside_records.md) | The archives' records about the person that the record cites. |
| [page](page.md) | The page, folio or entry cited. |
| [page_id](page_id.md) | The page, by its id in the pages document. |
| [people](people.md) | Everyone printed in the paper whose fate the record knows, by name as shown. |
| [people_with_address](people_with_address.md) | The people with at least one of its records at the record's own address. |
| [perished_confirmed](perished_confirmed.md) | The people who perished. |
| [perished_probable](perished_probable.md) | The people who probably perished. |
| [person_id](person_id.md) | The person's id in the shared record; the site's person page has this address. |
| [place_id](place_id.md) | The place's id in the shared record. |
| [place_name](place_name.md) | The place's name in the shared record. |
| [precision](precision.md) | How much of the date is known: year, month, day or range. |
| [printed](printed.md) | The date's words as the source prints or writes them. |
| [printed_calendar](printed_calendar.md) | The calendar of the printed words. |
| [printed_name](printed_name.md) | The person's name in Yiddish as the paper prints it, where the record has it. |
| [private](private.md) | True when the document itself is never shown. |
| [proposed_type](proposed_type.md) | For a statement of type other: the type proposed for it, awaiting the owner's approval. |
| [public_note](public_note.md) | Our reviewed words for the page about this evidence, apart from the record's quote. |
| [published](published.md) | When or where the source was published, as written. |
| [qualifiers](qualifiers.md) | More about the statement, as named texts. |
| [quote](quote.md) | The record's own words, exactly. |
| [quote_condition](quote_condition.md) | The owner's condition on the cleared quotes: shown only where no other record says the same. |
| [quote_english](quote_english.md) | English of exactly quote, with based_on.source_text equal to that field's exact bytes and attribution naming the kept English or its person or model. |
| [quote_language](quote_language.md) | The quote's language, where it is not the source's (a translation). |
| [quotes_cleared](quotes_cleared.md) | Who allowed quotes from this private document to be published, and on what day. |
| [reading_id](reading_id.md) | The reading of the printed text that the English was checked against. |
| [reading_sha256](reading_sha256.md) | The SHA-256 digest of that reading's exact UTF-8 bytes. |
| [record_id](record_id.md) | The archive's id for the record. |
| [record_type](record_type.md) | The record's type as the archive names it, from the record's citations, such as Page of Testimony; absent where they name none. |
| [reference_code](reference_code.md) | The holder's own reference for the record, as the holder writes it. |
| [related_name](related_name.md) | For kinship: the relative's name, where the relative has no person of their own. |
| [related_person_id](related_person_id.md) | For kinship: the relative, by the person's id in the record. |
| [relation](relation.md) | Whether this source is a copy or a transcription of the original. |
| [relationship](relationship.md) | What kind of link it is, in words. |
| [relationship_type](relationship_type.md) | For kinship: how the relative is related, from the subject to the relative. |
| [repository](repository.md) | The old free-text holder, read for one release; holder_id replaces it. |
| [rests_on](rests_on.md) | The facts the outcome rests on, by their ids in the record. |
| [review](review.md) | Whether a person has reviewed the statement. |
| [role](role.md) | The person's role in the piece. |
| [scan](scan.md) | The scan or image cited. |
| [script](script.md) | The script it is written in, as a four-letter ISO 15924 code such as Hebr or Latn. |
| [short_name](short_name.md) | A short name the site shows for the source. |
| [source_id](source_id.md) | The archive's database as the shared record's source id, such as yad-vashem. |
| [source_text](source_text.md) | The text used, exactly, never normalised or replaced by a later reading. |
| [start](start.md) | The date's start, as far as it is known: YYYY, YYYY-MM or YYYY-MM-DD. |
| [state](state.md) | Pending, or approved by a reviewer. |
| [status](status.md) | The statement's standing: proposed, accepted, disputed or rejected. |
| [subjects](subjects.md) | The persons, places or events the source shows or speaks of, by their ids. |
| [summary](summary.md) | A short summary in words. |
| [survived_confirmed](survived_confirmed.md) | The people who survived. |
| [survived_probable](survived_probable.md) | The people who probably survived. |
| [target_id](target_id.md) | The id of the content item linked to. |
| [text](text.md) | The words read in the box, exactly as read; empty for a patch with no readable line. |
| [time](time.md) | The time in a recording. |
| [title](title.md) | The source's title. |
| [title_english](title_english.md) | English of exactly title, with based_on.source_text equal to that field's exact bytes and attribution naming the kept English or its person or model. |
| [type](type.md) | What the statement is about: a birth, a death, a residence, an occupation and so on. |
| [unit_id](unit_id.md) | The piece of the paper cited, by its content item id. |
| [url](url.md) | The record's own address at the archive, never a scan or file address; absent where the record has none. |
| [url_pattern](url_pattern.md) | How an address of one of the source's records is formed. |
| [value](value.md) | The statement's words or value, such as an occupation. |
| [via](via.md) | The one source actually read, a copy or a transcription of the original, by its id. |
| [with_date](with_date.md) | The people whose fate the record dates. |
| [with_place](with_place.md) | The people whose fate the record places somewhere. |
| [wkd_id](wkd_id.md) | The person's Wikidata id, where one is linked. |
| [work_id](work_id.md) | The id of the work in the project's files; never published where it is a file name. |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AgeKnownBy](AgeKnownBy.md) | How a person's age is known. |
| [AuthorshipKind](AuthorshipKind.md) | Whether a person or a program wrote a supplied title or a translation. |
| [CitationRemarkKinds](CitationRemarkKinds.md) | Citation remark kinds: the values of citation_remark_kinds in vocabulary/sourced-entities.json, version 1.3.0. |
| [ClaimStatus](ClaimStatus.md) | Claim status: the values of claim_status in vocabulary/sourced-entities.json, version 1.3.0. |
| [CompatibilityEventTypes](CompatibilityEventTypes.md) | Compatibility event types: the values of compatibility_event_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [Confidence](Confidence.md) | Confidence: the values of confidence in vocabulary/sourced-entities.json, version 1.3.0. |
| [ContentItemSubtypes](ContentItemSubtypes.md) | Content item subtypes: the values of content_item_subtypes in vocabulary/site-content.json, version 1.3.0. |
| [ContentUnitRoles](ContentUnitRoles.md) | Content unit roles: the values of content_unit_roles in vocabulary/sourced-entities.json, version 1.3.0. |
| [EventParts](EventParts.md) | Event parts: the values of event_parts in vocabulary/sourced-entities.json, version 1.3.0. |
| [EventTypes](EventTypes.md) | Event types: the values of event_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [ExternalSourceTypes](ExternalSourceTypes.md) | External source types: the values of external_source_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [FactTypes](FactTypes.md) | Fact types: the values of fact_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [FateDetailKind](FateDetailKind.md) | The kind of statement a fate detail comes from: a death, a survival or a deportation. |
| [FateOutcomes](FateOutcomes.md) | Fate outcomes: the values of fate_outcomes in vocabulary/sourced-entities.json, version 1.3.0. |
| [FatesListConfidence](FatesListConfidence.md) | How sure the fate is: the shared record's confidences confirmed and probable. |
| [FatesListOutcome](FatesListOutcome.md) | The fates the list holds: the shared record's fate outcomes perished and survived. |
| [Gender](Gender.md) | Gender: the values of gender in vocabulary/sourced-entities.json, version 1.3.0. |
| [HolocaustFateTypes](HolocaustFateTypes.md) | Holocaust fate types: the values of holocaust_fate_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [IdentifierTypes](IdentifierTypes.md) | Identifier types approved in ADR 0001 and linked-data ticket 03. |
| [ImpressoTypes](ImpressoTypes.md) | Impresso types: the content-item types of Impresso as vocabulary/site-content.json, version 1.3.0, lists them in impresso_types. Impresso defines them in a JSON Schema, not an ontology, so they carry no meaning here. |
| [LifeEventTypes](LifeEventTypes.md) | Life event types: the values of life_event_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [LocationTypes](LocationTypes.md) | Location types: the values of location_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [MentionRoles](MentionRoles.md) | Mention roles: the values of mention_roles in vocabulary/sourced-entities.json, version 1.3.0. |
| [NameKinds](NameKinds.md) | Name kinds: the values of name_kinds in vocabulary/sourced-entities.json, version 1.3.0. |
| [PrintedCalendar](PrintedCalendar.md) | The calendar a date was printed or written in. |
| [ReadingStatusValue](ReadingStatusValue.md) | Reading states: the values of a content item's reading_status, from vocabulary/reading-status.json, whose entry reading_status describes the field: Optional per-field reading provenance. Null is unrecorded. A session check may cover particular words only. |
| [RelationshipTypes](RelationshipTypes.md) | Relationship types: the values of relationship_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [ReviewStates](ReviewStates.md) | Review states: the values of review_states in vocabulary/sourced-entities.json, version 1.3.0. |
| [SourcedDatePrecision](SourcedDatePrecision.md) | How much of a sourced date is known: its year, its month, its day, or a range. |
| [SourceDerivationRelation](SourceDerivationRelation.md) | How a source we hold was made from another: a copy of it, or a transcription of it. |
| [SourceKinds](SourceKinds.md) | Source kinds: the values of source_kinds in vocabulary/sourced-entities.json, version 1.3.0. |
| [SourceMadeBy](SourceMadeBy.md) | Who made a source, as a category: never an agent, so never its creator. |
| [SourceQuoteCondition](SourceQuoteCondition.md) | The owner's condition on a private source's cleared quotes. |
| [Subjects](Subjects.md) | Subjects: the values of subjects in vocabulary/site-content.json, version 1.3.0. |
| [TitleTypes](TitleTypes.md) | Title types: the values of title_types in vocabulary/site-content.json, version 1.3.0. |


## Types

| Type | Description |
| --- | --- |
| [ArchiveAddress](ArchiveAddress.md) | A record's address at its archive: it begins https:// and holds no white space. A pattern alone, as the twins' address checks say it, without LinkML's uri format. |
| [BirthYear](BirthYear.md) | A year of birth, from 1800 to 2100. |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal specification |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [HostName](HostName.md) | A lowercase internet host name with at least one dot, such as collections.yadvashem.org. |
| [HttpsUri](HttpsUri.md) | A web address that begins https:// and holds no white space, as the Pydantic twin's pattern says; the Zod twin asks for a URL whose protocol is https. |
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
