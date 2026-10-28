# The shared record of the Pruzhany record

One store, across every issue, of the persons, families, places, organisations and life events the paper names, the sources and holders cited, the sourced facts and relations about them, and the media beside them.

URI: https://pruzhany.org/ns/shared_record

Name: pruzhany_shared_record



## Classes

| Class | Description |
| --- | --- |
| [Attribution](Attribution.md) | Who made or allowed something, on what day, with an optional note. |
| [Authorship](Authorship.md) | Who wrote a supplied title, a translation or a check of one, a person or a model, and on which day. |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |
| [ContentItemBlockRef](ContentItemBlockRef.md) | The regions of one page that a content item or a section heading covers, in reading order. |
| [CrossReference](CrossReference.md) | A link from one content item to another in the same issue, with how sure it is and why. |
| [EnglishCheck](EnglishCheck.md) | A later, separate check of one English field against one exact reading of the printed text, bound to both and to the judgement kept by their digests. |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |
| [FactQualifiers](FactQualifiers.md) | More about a fact, as named texts: how many children a notice names, how a statement is supported and the like. |
| [Fate](Fate.md) | What became of a person in the Holocaust, as far as the record shows, the facts it rests on and its review. |
| [Holder](Holder.md) | Who holds a source: an institution, a family or a private person, with its outside identifiers and its web host. A private holder's name is never published. |
| [LifeEventDate](LifeEventDate.md) | One date of a life event: the words printed with their calendar, or, where no date is printed, the day of the first issue that reported it, or the preferred record statement's date for a death known from records alone. |
| [LifeEventMainPerson](LifeEventMainPerson.md) | One main person of a life event and their part in it (the baby, a parent, the bride, the groom, the boy, the one who died, the one remembered); each part means a declared local subproperty of rico:affectsOrAffected or rico:hasOrHadParticipant (EventParts). |
| [Media](Media.md) | One held or linked copy of a registered source, as the shared record keeps it: all that the public may see, with the private master file and the private permission besides. |
| [MediaConsent](MediaConsent.md) | The private record of the permission to show a medium: its basis, who gave it by role, what it covers, the document that holds it and any withdrawal. Never public. |
| [MediaConsentScope](MediaConsentScope.md) | What a permission covers: the use, the people shown, and whether people not identified are covered. |
| [MediaDecision](MediaDecision.md) | A review or a clearance: whose role made it (the owner or the project) and on what day. |
| [MediaDepicted](MediaDepicted.md) | One person a picture shows, identified or not, where in the picture, and on whose identification. |
| [MediaDerivative](MediaDerivative.md) | One served copy of a picture: a WebP file at one of the exported widths, named by the master's digest, made by resizing alone. |
| [MediaFamilyWords](MediaFamilyWords.md) | The family's own words about a medium, quoted from a registered source with the page or part they are on: a public part of a citation, with no private note. |
| [MediaFixity](MediaFixity.md) | A dated check that a master file still has its digest. |
| [MediaMaster](MediaMaster.md) | Where a medium's private master file is kept: its bucket, its key named by its digest, its digest, its type, its size and its last check. Never public. |
| [MediaPortrait](MediaPortrait.md) | The picture a person's page shows as their portrait: a reviewed medium and the region of it to show. |
| [MediaRegion](MediaRegion.md) | A rectangle in a medium's master picture, in its own pixels after orientation. |
| [MediaText](MediaText.md) | Words about or on a medium (a caption, a description for screen readers, an inscription, a transcript), their language and their review. |
| [MediaWithdrawal](MediaWithdrawal.md) | That a medium was withdrawn from the site, on what day and why; its record stays. |
| [Mention](Mention.md) | The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention. |
| [Name](Name.md) | One name of a person, a family, an organisation or a place, of one kind (printed, birth, married, supplied and so on), in one script. A person's, a family's and an organisation's names are agent names and a place's are place names (vocabulary/ site-content.json, bindings agent_name and place_name), so the class itself names no single term. |
| [PlaceIdentifier](PlaceIdentifier.md) | One outside identifier of a place or a holder, read on its authority's own pages and carried only on that evidence, never from a match of names. |
| [PrintedAddress](PrintedAddress.md) | Where some printed words stand: the page picture, a box on it in the picture's own pixels, and the words read in that box. |
| [PrintedTitle](PrintedTitle.md) | A title as printed in the paper: its words and where each line of them stands. |
| [PublicMedia](PublicMedia.md) | One held or linked copy of a registered source (a photograph, document, recording or film), as the public may see it: what it is, what it shows and says, its review, its terms and its served copies. |
| [Review](Review.md) | Whether a person has reviewed a statement, who and on what day. |
| [SharedEvent](SharedEvent.md) | One life event, once for each happening across every issue (a birth, a wedding, a death, a memorial and so on): its kind, its main people and their parts, its dates and its place. |
| [SharedFact](SharedFact.md) | One source's statement as the shared record keeps it: a fact with its subject, its form and its evidence located on the printed page where the site writer found it. |
| [SharedFamily](SharedFamily.md) | One family of the record: its id, the name shown and its names. |
| [SharedName](SharedName.md) | One name of a person in the shared record, with its evidence located on the printed page where the site writer found it. |
| [SharedOrganization](SharedOrganization.md) | One organisation of the record: its id, the name shown and its names; its offices and members are sourced facts. |
| [SharedPerson](SharedPerson.md) | One person of the record, across every issue: their id, the name shown, every name they are known by, their gender, what became of them, and their portrait. |
| [SharedPlace](SharedPlace.md) | One place of the record: its names, its kind, the place it lies in, its coordinates and its outside identifiers. |
| [SharedRecord](SharedRecord.md) | The shared record whole: its version, the vocabulary version it uses, and every person, family, place, organisation, event, source, holder, fact, relation and medium. |
| [SiteCitation](SiteCitation.md) | A citation as the shared record keeps it: an older one as it was written, or one the site writer locates on the printed page, with the addresses of the words it quotes. |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |
| [SourcedDate](SourcedDate.md) | A date a source gives: a normalized start (and end, for a range) with how precise it is, or the words as printed with their calendar, or both. |
| [SourceDerivation](SourceDerivation.md) | The record a source we hold was made from, and how: a copy or a transcription of it. |
| [SourcedRelation](SourcedRelation.md) | One source's statement that a person is related to another, from the subject to the relative, of a released kinship type, or of type other with a proposed type. |
| [SuppliedTitle](SuppliedTitle.md) | A title supplied in English for a content item or section, with what it was made from, who made it and, where one was made, its later check. |
| [TextBasis](TextBasis.md) | The exact text a translation or supplied title was made from, and where it is printed, kept even after the text is read again. |
| [TitleCheck](TitleCheck.md) | A check of a supplied title's English. |
| [Translation](Translation.md) | An English translation of a content item's printed text, with the exact text it was made from, who made it and, where one was made, its later check. |
| [TranslationCheck](TranslationCheck.md) | A check of a translation's English. |



## Slots

| Slot | Description |
| --- | --- |
| [accessed](accessed.md) | The day it was read on its authority's own pages. |
| [addresses](addresses.md) | Where on the page pictures the quoted words are printed. |
| [alt](alt.md) | The description for screen readers of what is visible; required for images and documents. |
| [attribution](attribution.md) | Who added it, and on what day. |
| [author](author.md) | Who wrote the source: an institution, never a member of its staff. |
| [based_on](based_on.md) | The exact printed text the title was made from, and where it is printed. |
| [basis](basis.md) | What the permission rests on: an institution's terms, the holder's licence, the family's permission, the public domain, or the owner's family papers. |
| [bbox](bbox.md) | The box on the picture: left, top, width and height, in the picture's pixels. |
| [block_ids](block_ids.md) | The regions on that page, by their ids in the pages document, in reading order. |
| [bucket](bucket.md) | The private storage bucket, apart from the page pictures' bucket. |
| [by](by.md) | Who reviewed it. |
| [bytes](bytes.md) | The file's size in bytes. |
| [caption](caption.md) | The caption the site shows, with its language and review. |
| [checked](checked.md) | The last dated check of the file's digest. |
| [checked_against](checked_against.md) | A later check of this title against the reading, where one was made. |
| [citations](citations.md) | Where the name is found. |
| [cleared](cleared.md) | Who cleared the medium for the site, by role, and on what day. |
| [conditions_of_access](conditions_of_access.md) | The holder's terms of access, as written. |
| [conditions_of_use](conditions_of_use.md) | The holder's terms of use, as written, with no permission inferred from them. |
| [confidence](confidence.md) | How sure the outcome is. |
| [consent](consent.md) | The private record of the permission to show the medium; never public. |
| [coordinates](coordinates.md) | Where it lies: latitude then longitude, in degrees. |
| [credit](credit.md) | The holder's or the family's credit, as they word it. |
| [date](date.md) | When, as the source gives it. |
| [dated](dated.md) | The record's own date, apart from when it was published or consulted. |
| [dates](dates.md) | The event's dates: as printed (in either calendar), or the first report's day, or the preferred record statement's. |
| [depicted](depicted.md) | The people the picture shows, identified or not, and where. |
| [derived](derived.md) | The served copies of the picture, one for each exported width. |
| [derived_from](derived_from.md) | For a copy or a transcription we hold: the original it was made from, and how. |
| [description](description.md) | A short description in words. |
| [duration](duration.md) | The master's length in seconds, for sound and film. |
| [edition_date](edition_date.md) | The day of the paper's issue cited, written YYYY-MM-DD. |
| [editor](editor.md) | Who edited the source. |
| [end](end.md) | The end of a range of dates, written as the start is. |
| [english_sha256](english_sha256.md) | The SHA-256 digest of the checked English field's exact UTF-8 bytes. |
| [event_id](event_id.md) | The life event the statement concerns, by its id in the record. |
| [events](events.md) | Every life event, once for each happening. |
| [evidence](evidence.md) | What shows the link, in words. |
| [evidence_basis](evidence_basis.md) | records_only: a death known from records alone, which no issue prints. |
| [evidence_confidence](evidence_confidence.md) | How sure the evidence makes the statement. |
| [facts](facts.md) | Every sourced fact. |
| [families](families.md) | Every family. |
| [family_id](family_id.md) | The family the statement concerns, by its id; on a membership fact, the family the person belongs to. |
| [family_words](family_words.md) | The family's words about the medium, quoted from a source. |
| [fate](fate.md) | What became of the person in the Holocaust, as far as the record shows. |
| [function](function.md) | A function printed with the name. |
| [gender](gender.md) | The person's gender, or unknown. |
| [granted_by](granted_by.md) | Who gave the permission, by role; never a person's name. |
| [h](h.md) | The height, in pixels. |
| [height](height.md) | The copy's actual height in pixels. |
| [holder_id](holder_id.md) | Who holds the source, by its id in the record's holders. |
| [holders](holders.md) | Every holder of a source. |
| [holocaust_related](holocaust_related.md) | True when the statement concerns the Holocaust. |
| [host](host.md) | The holder's web host, without www. |
| [id](id.md) | The person's id, kept for ever: never renamed, reused or deleted. |
| [identified_by](identified_by.md) | What identifies the person: the family, a record, or the picture's inscription. |
| [identifiers](identifiers.md) | The holder's outside identifiers, each with its evidence: EHRI's institution id first. |
| [identity_confidence](identity_confidence.md) | How sure it is that the statement is about this person. |
| [image_uri](image_uri.md) | The page picture the box is on, by its name or address. |
| [inferred](inferred.md) | True when the date was worked out rather than read. |
| [inscription](inscription.md) | The object's own words, such as writing on the back of a photograph. |
| [judgement_id](judgement_id.md) | The kept judgement, by an id without spaces followed by the field it judged, :title or :text. |
| [judgement_sha256](judgement_sha256.md) | The SHA-256 digest of the kept judgement file's exact bytes. |
| [key](key.md) | The file's key in the bucket, whose last part is its SHA-256 digest. |
| [kind](kind.md) | An institution, a family or a private person. |
| [lang](lang.md) | Its language, as a language tag such as yi or en. |
| [language](language.md) | The languages of the record, as BCP 47 tags. |
| [link](link.md) | For sound or film: the page on the holder's own host where it can be heard or seen. |
| [location_id](location_id.md) | Where the event happened, by the place's id. |
| [locator](locator.md) | An internal pointer into the project's files; never published and never a holder's record number. |
| [made_by](made_by.md) | Who made the source, as a category (family, studio, institution, perpetrator, unknown); never its creator. |
| [main_people](main_people.md) | The people the event is about, each with their part; empty while unresolved. |
| [master](master.md) | Where the private master file is kept; never public. |
| [media](media.md) | Every medium held or linked beside a person. |
| [media_id](media_id.md) | The medium, by its id in the record's media. |
| [mime](mime.md) | The file's media type, such as image/tiff. |
| [name](name.md) | The name the site shows. |
| [names](names.md) | Every name the person is known by, printed or supplied, with where it is found. |
| [note](note.md) | A note on how or why. |
| [on](on.md) | The day it was reviewed. |
| [organization_id](organization_id.md) | The organisation the statement concerns, by its id in the record. |
| [organizations](organizations.md) | Every organisation. |
| [outcome](outcome.md) | What became of the person: unknown, perished, survived, died before, or not applicable. |
| [page](page.md) | The page, folio or entry cited. |
| [page_id](page_id.md) | The page, by its id in the pages document. |
| [parent_id](parent_id.md) | The place it lies in, by its id. |
| [part](part.md) | The person's part in the event. |
| [person_id](person_id.md) | The person, by the person's id in the record. |
| [person_ids](person_ids.md) | The people the permission covers, by their ids; each must be shown in the medium. |
| [persons](persons.md) | Every person. |
| [place_id](place_id.md) | Where, by the place's id in the record. |
| [places](places.md) | Every place. |
| [portrait](portrait.md) | The reviewed picture and region the person's page shows. |
| [precision](precision.md) | How much of the date is known: year, month, day or range. |
| [printed](printed.md) | The date's words as printed. |
| [printed_calendar](printed_calendar.md) | The calendar the date was printed in. |
| [printed_name](printed_name.md) | The name as printed. |
| [private](private.md) | True when the document itself is never shown. |
| [process](process.md) | How the copy was made: resizing alone. |
| [proposed_type](proposed_type.md) | For an event of kind other: the kind proposed for it, awaiting the owner's approval. |
| [public_note](public_note.md) | Our reviewed words for the page about this evidence, apart from the record's quote. |
| [published](published.md) | When or where the source was published, as written. |
| [qualifier](qualifier.md) | reported_in: the day is the first issue's that reported the event, not the day it happened. |
| [qualifiers](qualifiers.md) | More about the statement, as named texts. |
| [quote](quote.md) | The record's own words, exactly. |
| [quote_condition](quote_condition.md) | The owner's condition on the cleared quotes: shown only where no other record says the same. |
| [quote_language](quote_language.md) | The quote's language, where it is not the source's (a translation). |
| [quotes_cleared](quotes_cleared.md) | Who allowed quotes from this private document to be published, and on what day. |
| [reading_id](reading_id.md) | The reading of the printed text that the English was checked against. |
| [reading_sha256](reading_sha256.md) | The SHA-256 digest of that reading's exact UTF-8 bytes. |
| [reason](reason.md) | Why: at the family's or the holder's request, or for an error. |
| [record_fact_id](record_fact_id.md) | For a death known from records: the accepted death fact whose date and place describe it, by the fact's id. |
| [record_id](record_id.md) | The holder's own number for the record, such as a Yad Vashem record number. |
| [record_type](record_type.md) | The holder's own type of the record, such as Page of Testimony. |
| [ref](ref.md) | The private reference of the document that holds the permission. |
| [reference_code](reference_code.md) | The holder's own reference for the record, as the holder writes it. |
| [region](region.md) | Where in the picture the person is. |
| [related_name](related_name.md) | For kinship: the relative's name, where the relative has no person of their own. |
| [related_person_id](related_person_id.md) | For kinship: the relative, by the person's id in the record. |
| [relation](relation.md) | Whether this source is a copy or a transcription of the original. |
| [relations](relations.md) | Every sourced relation between people. |
| [relationship](relationship.md) | What kind of link it is, in words. |
| [relationship_type](relationship_type.md) | For kinship: how the relative is related, from the subject to the relative. |
| [reported_in](reported_in.md) | The day of the first issue that reported the event, where no date is printed. |
| [repository](repository.md) | The old free-text holder, read for one release; holder_id replaces it. |
| [representation](representation.md) | The form the statement is kept in: structured, prose or an image path. |
| [rests_on](rests_on.md) | The facts the outcome rests on, by their ids in the record. |
| [review](review.md) | Whether a person has reviewed the statement. |
| [reviewed](reviewed.md) | Who reviewed the words, by role, and on what day. |
| [rights](rights.md) | The rights statement or licence that applies, by its address; when absent, copyright not evaluated. |
| [role](role.md) | The person's role in the piece. |
| [scan](scan.md) | The scan or image cited. |
| [scope](scope.md) | What the permission covers. |
| [script](script.md) | The script it is written in, as a four-letter ISO 15924 code such as Hebr or Latn. |
| [sha256](sha256.md) | The SHA-256 digest found on that day. |
| [short_name](short_name.md) | The name the site shows. |
| [shown](shown.md) | Who allowed the relative to be shown on the person's page, and on what day; never evidence of a death. |
| [shows_unidentified](shows_unidentified.md) | True when the picture shows people not identified. |
| [source_id](source_id.md) | The authority the identifier comes from, a registered source, by its id. |
| [source_text](source_text.md) | The text used, exactly, never normalised or replaced by a later reading. |
| [sources](sources.md) | Every registered source. |
| [start](start.md) | The printed date normalized, for a date printed in the Gregorian calendar only. |
| [state](state.md) | Pending, or approved by a reviewer. |
| [status](status.md) | The statement's standing: proposed, accepted, disputed or rejected. |
| [subject_id](subject_id.md) | Whose statement it is: a person, a family, a place, an organisation, an event or a relation, by its id. |
| [subjects](subjects.md) | The persons, places or events the source shows or speaks of, by their ids. |
| [summary](summary.md) | A short summary in words. |
| [target_id](target_id.md) | The id of the content item linked to. |
| [text](text.md) | The words. |
| [time](time.md) | The time in a recording. |
| [title](title.md) | The source's title. |
| [transcript](transcript.md) | A document's full text; required for documents. |
| [type](type.md) | kinship for a released relationship type; other, with a proposed type, for one not yet released. |
| [unidentified](unidentified.md) | True when the permission also covers people shown and not identified. |
| [unit_id](unit_id.md) | The piece of the paper cited, by its content item id. |
| [url](url.md) | The identifier's page on the authority's host. |
| [url_pattern](url_pattern.md) | How an address of one of the source's records is formed. |
| [use](use.md) | The use allowed: shown on the site, or shown and downloaded. |
| [value](value.md) | The identifier as its authority writes it. |
| [version](version.md) | The version of the record's shape. |
| [via](via.md) | The one source actually read, a copy or a transcription of the original, by its id. |
| [vocabulary_version](vocabulary_version.md) | The version of the sourced-entities vocabulary the record uses. |
| [w](w.md) | The width, in pixels. |
| [width](width.md) | The copy's actual width in pixels. |
| [withdrawn](withdrawn.md) | That the medium was withdrawn, on what day and why. |
| [withdrawn_on](withdrawn_on.md) | The day the permission was withdrawn. |
| [wkd_id](wkd_id.md) | The person's Wikidata id, where one is linked. |
| [work_id](work_id.md) | The id of the work in the project's files; never published where it is a file name. |
| [x](x.md) | The left edge, in pixels from the picture's left. |
| [y](y.md) | The top edge, in pixels from the picture's top. |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AuthorshipKind](AuthorshipKind.md) | Whether a person or a program wrote a supplied title or a translation. |
| [CitationRemarkKinds](CitationRemarkKinds.md) | Citation remark kinds: the values of citation_remark_kinds in vocabulary/sourced-entities.json, version 1.3.0. |
| [ClaimStatus](ClaimStatus.md) | Claim status: the values of claim_status in vocabulary/sourced-entities.json, version 1.3.0. |
| [CompatibilityEventTypes](CompatibilityEventTypes.md) | Compatibility event types: the values of compatibility_event_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [Confidence](Confidence.md) | Confidence: the values of confidence in vocabulary/sourced-entities.json, version 1.3.0. |
| [ContentItemSubtypes](ContentItemSubtypes.md) | Content item subtypes: the values of content_item_subtypes in vocabulary/site-content.json, version 1.0.0. |
| [ContentUnitRoles](ContentUnitRoles.md) | Content unit roles: the values of content_unit_roles in vocabulary/sourced-entities.json, version 1.3.0. |
| [EventParts](EventParts.md) | Event parts: the values of event_parts in vocabulary/sourced-entities.json, version 1.3.0. |
| [EventTypes](EventTypes.md) | Event types: the values of event_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [ExternalSourceTypes](ExternalSourceTypes.md) | External source types: the values of external_source_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [FactTypes](FactTypes.md) | Fact types: the values of fact_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [FateOutcomes](FateOutcomes.md) | Fate outcomes: the values of fate_outcomes in vocabulary/sourced-entities.json, version 1.3.0. |
| [Gender](Gender.md) | Gender: the values of gender in vocabulary/sourced-entities.json, version 1.3.0. |
| [HolderKind](HolderKind.md) | What kind of holder keeps a source. |
| [HolocaustFateTypes](HolocaustFateTypes.md) | Holocaust fate types: the values of holocaust_fate_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [ImpressoTypes](ImpressoTypes.md) | Impresso types: the content-item types of Impresso as vocabulary/site-content.json, version 1.0.0, lists them in impresso_types. Impresso defines them in a JSON Schema, not an ontology, so they carry no meaning here. |
| [LifeEventTypes](LifeEventTypes.md) | Life event types: the values of life_event_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [LocationTypes](LocationTypes.md) | Location types: the values of location_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [MediaDecisionRole](MediaDecisionRole.md) | Whose role made a decision about a medium. |
| [MediaGrantedBy](MediaGrantedBy.md) | Who gave the permission to show a medium, by role; never a person's name. |
| [MediaIdentifiedBy](MediaIdentifiedBy.md) | What identifies a person shown in a picture. |
| [MediaKind](MediaKind.md) | What a medium is: an image, a sound recording, a film or a document. |
| [MediaWithdrawalReason](MediaWithdrawalReason.md) | Why a medium was withdrawn. |
| [MentionRoles](MentionRoles.md) | Mention roles: the values of mention_roles in vocabulary/sourced-entities.json, version 1.3.0. |
| [NameKinds](NameKinds.md) | Name kinds: the values of name_kinds in vocabulary/sourced-entities.json, version 1.3.0. |
| [PrintedCalendar](PrintedCalendar.md) | The calendar a date was printed or written in. |
| [ReadingStatusValue](ReadingStatusValue.md) | Reading states: the values of a content item's reading_status, from vocabulary/reading-status.json, whose entry reading_status describes the field: Optional per-field reading provenance. Null is unrecorded. A session check may cover particular words only. |
| [RelationshipTypes](RelationshipTypes.md) | Relationship types: the values of relationship_types in vocabulary/sourced-entities.json, version 1.3.0. |
| [ReviewStates](ReviewStates.md) | Review states: the values of review_states in vocabulary/sourced-entities.json, version 1.3.0. |
| [SharedFactRepresentation](SharedFactRepresentation.md) | The form a fact is kept in: a structured statement, retained prose, or an image path. |
| [SourcedDatePrecision](SourcedDatePrecision.md) | How much of a sourced date is known: its year, its month, its day, or a range. |
| [SourceDerivationRelation](SourceDerivationRelation.md) | How a source we hold was made from another: a copy of it, or a transcription of it. |
| [SourceKinds](SourceKinds.md) | Source kinds: the values of source_kinds in vocabulary/sourced-entities.json, version 1.3.0. |
| [SourceMadeBy](SourceMadeBy.md) | Who made a source, as a category: never an agent, so never its creator. |
| [SourceQuoteCondition](SourceQuoteCondition.md) | The owner's condition on a private source's cleared quotes. |
| [Subjects](Subjects.md) | Subjects: the values of subjects in vocabulary/site-content.json, version 1.0.0. |
| [TitleTypes](TitleTypes.md) | Title types: the values of title_types in vocabulary/site-content.json, version 1.0.0. |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Coordinate](Coordinate.md) | One coordinate of a place, in degrees from -180 to 180. The twins bound the latitude, the first, to -90 to 90; a bound by position in a list cannot be said here (known-looser.yaml). |
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
