# What the Pruzhany issue documents share

The printed address of words on a page picture, printed and supplied titles, translations, the checks of their English, and the regions a content item covers: the parts the content items and mentions documents share.

URI: https://pruzhany.org/ns/site_common

Name: pruzhany_site_common



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
| [addresses](addresses.md) | Where that text is printed, one address a line or patch. |
| [attribution](attribution.md) | Who checked it, and on which day. |
| [based_on](based_on.md) | The exact printed text the title was made from, and where it is printed. |
| [bbox](bbox.md) | The box on the picture: left, top, width and height, in the picture's pixels. |
| [block_ids](block_ids.md) | The regions on that page, by their ids in the pages document, in reading order. |
| [by](by.md) | Who made it or allowed it: a person, a session or a program. |
| [checked_against](checked_against.md) | A later check of this title against the reading, where one was made. |
| [confidence](confidence.md) | How sure the link is, from 0 to 1. |
| [english_sha256](english_sha256.md) | The SHA-256 digest of the checked English field's exact UTF-8 bytes. |
| [evidence](evidence.md) | What shows the link, in words. |
| [image_uri](image_uri.md) | The page picture the box is on, by its name or address. |
| [judgement_id](judgement_id.md) | The kept judgement, by an id without spaces followed by the field it judged, :title or :text. |
| [judgement_sha256](judgement_sha256.md) | The SHA-256 digest of the kept judgement file's exact bytes. |
| [kind](kind.md) | Whether a person or a model wrote it. |
| [language](language.md) | The title's language, always English (en). |
| [note](note.md) | A note on how or why. |
| [on](on.md) | The day it was made or allowed. |
| [page_id](page_id.md) | The page, by its id in the pages document. |
| [reading_id](reading_id.md) | The reading of the printed text that the English was checked against. |
| [reading_sha256](reading_sha256.md) | The SHA-256 digest of that reading's exact UTF-8 bytes. |
| [relationship](relationship.md) | What kind of link it is, in words. |
| [source_text](source_text.md) | The text used, exactly, never normalised or replaced by a later reading. |
| [target_id](target_id.md) | The id of the content item linked to. |
| [text](text.md) | The words read in the box, exactly as read; empty for a patch with no readable line. |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AuthorshipKind](AuthorshipKind.md) | Whether a person or a program wrote a supplied title or a translation. |


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
