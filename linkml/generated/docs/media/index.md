# Media of the Pruzhany record

Photographs, documents, sound and film beside a person: each held or linked copy of a registered source, what it shows and says, who reviewed and cleared it, and where its private master and its served copies are.

URI: https://pruzhany.org/ns/media

Name: pruzhany_media



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
| [PrintedAddress](PrintedAddress.md) | Where some printed words stand: the page picture, a box on it in the picture's own pixels, and the words read in that box. |
| [PrintedTitle](PrintedTitle.md) | A title as printed in the paper: its words and where each line of them stands. |
| [PublicMedia](PublicMedia.md) | One held or linked copy of a registered source (a photograph, document, recording or film), as the public may see it: what it is, what it shows and says, its review, its terms and its served copies. |
| [SuppliedTitle](SuppliedTitle.md) | A title supplied in English for a content item or section, with what it was made from, who made it and, where one was made, its later check. |
| [TextBasis](TextBasis.md) | The exact text a translation or supplied title was made from, and where it is printed, kept even after the text is read again. |
| [TitleCheck](TitleCheck.md) | A check of a supplied title's English. |
| [Translation](Translation.md) | An English translation of exact source words, with the exact text it was made from, who made it and, where one was made, its later check. |
| [TranslationCheck](TranslationCheck.md) | A check of a translation's English. |



## Slots

| Slot | Description |
| --- | --- |
| [addresses](addresses.md) | Where that text is printed, one address a line or patch. |
| [alt](alt.md) | The description for screen readers of what is visible; required for images and documents. |
| [attribution](attribution.md) | Who checked it, and on which day. |
| [based_on](based_on.md) | The exact printed text the title was made from, and where it is printed. |
| [basis](basis.md) | What the permission rests on: an institution's terms, the holder's licence, the family's permission, the public domain, or the owner's family papers. |
| [bbox](bbox.md) | The box on the picture: left, top, width and height, in the picture's pixels. |
| [block_ids](block_ids.md) | The regions on that page, by their ids in the pages document, in reading order. |
| [bucket](bucket.md) | The private storage bucket, apart from the page pictures' bucket. |
| [by](by.md) | Who made it or allowed it: a person, a session or a program. |
| [bytes](bytes.md) | The file's size in bytes. |
| [caption](caption.md) | The caption the site shows, with its language and review. |
| [checked](checked.md) | The last dated check of the file's digest. |
| [checked_against](checked_against.md) | A later check of this title against the reading, where one was made. |
| [cleared](cleared.md) | Who cleared the medium for the site, by role, and on what day. |
| [conditions_of_access](conditions_of_access.md) | The holder's terms of access, as written. |
| [conditions_of_use](conditions_of_use.md) | The holder's terms of use, as written, with no permission inferred from them. |
| [confidence](confidence.md) | How sure the link is, from 0 to 1. |
| [consent](consent.md) | The private record of the permission to show the medium; never public. |
| [credit](credit.md) | The holder's or the family's credit, as they word it. |
| [depicted](depicted.md) | The people the picture shows, identified or not, and where. |
| [derived](derived.md) | The served copies of the picture, one for each exported width. |
| [duration](duration.md) | The master's length in seconds, for sound and film. |
| [english_sha256](english_sha256.md) | The SHA-256 digest of the checked English field's exact UTF-8 bytes. |
| [evidence](evidence.md) | What shows the link, in words. |
| [family_words](family_words.md) | The family's words about the medium, quoted from a source. |
| [granted_by](granted_by.md) | Who gave the permission, by role; never a person's name. |
| [h](h.md) | The height, in pixels. |
| [height](height.md) | The copy's actual height in pixels. |
| [id](id.md) | The medium's id: lowercase letters and digits in parts joined by hyphens. |
| [identified_by](identified_by.md) | What identifies the person: the family, a record, or the picture's inscription. |
| [image_uri](image_uri.md) | The page picture the box is on, by its name or address. |
| [inscription](inscription.md) | The object's own words, such as writing on the back of a photograph. |
| [judgement_id](judgement_id.md) | The kept judgement, by an id without spaces followed by the field it judged, :title or :text. |
| [judgement_sha256](judgement_sha256.md) | The SHA-256 digest of the kept judgement file's exact bytes. |
| [key](key.md) | The file's key in the bucket, whose last part is its SHA-256 digest. |
| [kind](kind.md) | What the medium is: image, audio, video or document. |
| [lang](lang.md) | Their language, as a BCP 47 tag. |
| [language](language.md) | The title's language, always English (en). |
| [link](link.md) | For sound or film: the page on the holder's own host where it can be heard or seen. |
| [master](master.md) | Where the private master file is kept; never public. |
| [media_id](media_id.md) | The medium, by its id in the record's media. |
| [mime](mime.md) | The file's media type, such as image/tiff. |
| [note](note.md) | A note on how or why. |
| [on](on.md) | The day of the decision. |
| [page](page.md) | The page or recorded part the words are on. |
| [page_id](page_id.md) | The page, by its id in the pages document. |
| [person_id](person_id.md) | The person shown, by the person's id; null for a person not identified. |
| [person_ids](person_ids.md) | The people the permission covers, by their ids; each must be shown in the medium. |
| [process](process.md) | How the copy was made: resizing alone. |
| [quote](quote.md) | The words, exactly. |
| [quote_english](quote_english.md) | English of exactly quote, with based_on.source_text equal to that field's exact bytes and attribution naming the kept English or its person or model. |
| [quote_language](quote_language.md) | Their language, as a BCP 47 tag. |
| [reading_id](reading_id.md) | The reading of the printed text that the English was checked against. |
| [reading_sha256](reading_sha256.md) | The SHA-256 digest of that reading's exact UTF-8 bytes. |
| [reason](reason.md) | Why: at the family's or the holder's request, or for an error. |
| [ref](ref.md) | The private reference of the document that holds the permission. |
| [region](region.md) | Where in the picture the person is. |
| [relationship](relationship.md) | What kind of link it is, in words. |
| [reviewed](reviewed.md) | Who reviewed the words, by role, and on what day. |
| [rights](rights.md) | The rights statement or licence that applies, by its address; when absent, copyright not evaluated. |
| [role](role.md) | Who decided, by role: the owner or the project; never a person's name. |
| [scope](scope.md) | What the permission covers. |
| [sha256](sha256.md) | The SHA-256 digest found on that day. |
| [shows_unidentified](shows_unidentified.md) | True when the picture shows people not identified. |
| [source_id](source_id.md) | The source the words are quoted from, by its id in the record's sources. |
| [source_text](source_text.md) | The text used, exactly, never normalised or replaced by a later reading. |
| [target_id](target_id.md) | The id of the content item linked to. |
| [text](text.md) | The words. |
| [transcript](transcript.md) | A document's full text; required for documents. |
| [unidentified](unidentified.md) | True when the permission also covers people shown and not identified. |
| [url](url.md) | The copy's address, ending in its nominal width (zod/media-widths.json). |
| [use](use.md) | The use allowed: shown on the site, or shown and downloaded. |
| [w](w.md) | The width, in pixels. |
| [width](width.md) | The copy's actual width in pixels. |
| [withdrawn](withdrawn.md) | That the medium was withdrawn, on what day and why. |
| [withdrawn_on](withdrawn_on.md) | The day the permission was withdrawn. |
| [x](x.md) | The left edge, in pixels from the picture's left. |
| [y](y.md) | The top edge, in pixels from the picture's top. |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AuthorshipKind](AuthorshipKind.md) | Whether a person or a program wrote a supplied title or a translation. |
| [MediaDecisionRole](MediaDecisionRole.md) | Whose role made a decision about a medium. |
| [MediaGrantedBy](MediaGrantedBy.md) | Who gave the permission to show a medium, by role; never a person's name. |
| [MediaIdentifiedBy](MediaIdentifiedBy.md) | What identifies a person shown in a picture. |
| [MediaKind](MediaKind.md) | What a medium is: an image, a sound recording, a film or a document. |
| [MediaWithdrawalReason](MediaWithdrawalReason.md) | Why a medium was withdrawn. |


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
