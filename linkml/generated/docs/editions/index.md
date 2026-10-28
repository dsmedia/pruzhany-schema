# The catalog of Pruzhany editions

Every edition of the paper with its Hebrew date, the Jewish holidays and the outside historical events the site's calendar shows, and the dates whose editions are on the site.

URI: https://pruzhany.org/ns/editions

Name: pruzhany_editions



## Classes

| Class | Description |
| --- | --- |
| [Edition](Edition.md) | One edition of the paper: its date in the common calendar and in the Hebrew one, and the holiday it falls on, if any. |
| [EditionsCatalog](EditionsCatalog.md) | The catalog of editions: every edition, the holidays and historical events beside them, and the dates available on the site. |
| [HistoricalEvent](HistoricalEvent.md) | An event in the world outside the town, such as Kristallnacht, on a day or over a span of days. |
| [Holiday](Holiday.md) | A Jewish holiday on a given day. |



## Slots

| Slot | Description |
| --- | --- |
| [available_dates](available_dates.md) | The dates of the editions whose pages are on the site. |
| [date](date.md) | The edition's date, written YYYY-MM-DD. |
| [description](description.md) | What happened, in a sentence or two. |
| [editions](editions.md) | Every edition of the paper, with its Hebrew date. |
| [end_date](end_date.md) | The day the event ended, where it lasted more than a day. |
| [hebrew_date](hebrew_date.md) | The edition's date in the Hebrew calendar, written in Hebrew letters. |
| [hebrew_month](hebrew_month.md) | The Hebrew month, by its number from 1 to 13, counted from Nisan. |
| [hebrew_name](hebrew_name.md) | The holiday's name in Hebrew letters, where it is given. |
| [hebrew_year](hebrew_year.md) | The Hebrew year, such as 5699. |
| [historical_events](historical_events.md) | Events in the world outside the town that the calendar marks. |
| [holiday](holiday.md) | The holiday the edition falls on or near, where there is one. |
| [holidays](holidays.md) | The Jewish holidays of the paper's years. |
| [name](name.md) | The holiday's name in Latin letters, such as Purim or Pesach. |


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
