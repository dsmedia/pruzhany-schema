# The pages document of a Pruzhany issue

One issue's pages: each page's picture and size, and the regions of print on it with the words read in each and the content item each belongs to.

URI: https://pruzhany.org/ns/pages

Name: pruzhany_pages



## Classes

| Class | Description |
| --- | --- |
| [Block](Block.md) | One region of print on a page, its box and the words read in it, belonging to one content item, or to no item when it is a section heading. |
| [Page](Page.md) | One printed page of the issue: its picture, its size and its regions of print. |
| [PagesData](PagesData.md) | One issue's pages document: the issue's date and its pages in order. |



## Slots

| Slot | Description |
| --- | --- |
| [bbox](bbox.md) | The region's box on the page picture: left, top, width and height, in the picture's pixels. |
| [blocks](blocks.md) | The regions of print on the page. |
| [confidence](confidence.md) | How sure the reading is, from 0 to 1, where it was recorded. |
| [dimensions](dimensions.md) | The picture's width and height, in its pixels. |
| [edition_date](edition_date.md) | The issue's date, written YYYY-MM-DD. |
| [id](id.md) | The page's id, such as page-1938-12-16-4. |
| [image_crop](image_crop.md) | A picture of the region alone, by its path, where one was made. |
| [image_uri](image_uri.md) | The page's picture, by its name or address. |
| [issue_date](issue_date.md) | The date of the issue the page belongs to, written YYYY-MM-DD. |
| [page_number](page_number.md) | The page's number within the issue, from 1. |
| [pages](pages.md) | The issue's pages. |
| [transcription](transcription.md) | The words read in the region, its lines separated by line breaks. |
| [unit_id](unit_id.md) | The content item the region belongs to, by its id; null for a region that is a section's heading. |


## Enumerations

| Enumeration | Description |
| --- | --- |


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
