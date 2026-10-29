# The physical page in Impresso's stored format

The physical layer is a page picture and its ordered regions, paragraphs, lines and words, with boxes in that picture's pixels. This module describes every field in Impresso's page schema, including deprecated fields; it adds no stored field. The semantic content items remain separate. Computed identifiers name positions in the last written segmentation: region <page id>-r<RRR>, where RRR is its 1-based place in r; line <region id>-l<LLL>, where LLL counts lines across all the region's paragraphs in order; word <line id>-w<WWW>, where WWW is its 1-based place in t. Each suffix is three zero-padded digits, from 001 to 999; an identifier producer must refuse any count above 999. These ids are computed, never stored in the Impresso page file. Identical segmentation gives identical ids; changed segmentation may put another word at the same id. Identity lifecycle work (record-book-two ticket 05) must handle matching, tombstones and redirects across such changes. The 999 limit is an identifier-production rule, not an Impresso shape constraint.

URI: https://pruzhany.org/ns/physical

Name: pruzhany_physical



## Classes

| Class | Description |
| --- | --- |
| [PhysicalLine](PhysicalLine.md) | One line with a box and ordered OCR tokens. |
| [PhysicalPage](PhysicalPage.md) | One Impresso page file, with its picture metadata and physical text hierarchy. Impresso allows unknown properties at every object level; no such properties are defined here. Exactly one image key and at least one timestamp key must be present. |
| [PhysicalParagraph](PhysicalParagraph.md) | One ordered group of lines in a region, optionally with its own box; no computed id is assigned to paragraphs by this contract. |
| [PhysicalRegion](PhysicalRegion.md) | One region of the page, with a box, ordered paragraphs and optional semantic links. |
| [PhysicalWord](PhysicalWord.md) | One OCR token (a word or word part), with its own box and surface text. |



## Slots

| Slot | Description |
| --- | --- |
| [cc](cc.md) | Whether legacy coordinates were converted or rescaled to the IIIF picture frame. |
| [cdt](cdt.md) | Legacy JSON creation timestamp; Impresso validates a string without a date format. |
| [fh](fh.md) | Facsimile height in pixels; present together with fw, with no bound in Impresso. |
| [fw](fw.md) | Facsimile width in pixels; present together with fh, with no bound in Impresso. |
| [gn](gn.md) | Glue next: true means no following whitespace. When absent readers assume false; the schema inserts no default. |
| [hy](hy.md) | Whether this token is the first part of a hyphenated word, including the hyphen. Readers assume false when absent; the schema inserts no default. |
| [id](id.md) | Impresso's canonical page identifier; for example FABLE-1900-01-01-a-p0001. |
| [iiif](iiif.md) | Deprecated IIIF manifest URI, retained for compatibility; Impresso validates plain text, not URI syntax. Exactly one of this and iiif_img_base_uri is present. |
| [iiif_img_base_uri](iiif_img_base_uri.md) | Base IIIF image URI without a suffix; Impresso validates plain text, not URI syntax. |
| [lines](lines.md) | Lines in paragraph order, including an empty list if stored that way. |
| [nf](nf.md) | Normalized dehyphenated form on the latter part or parts of a hyphenated word. |
| [paragraphs](paragraphs.md) | Paragraphs in region order; Impresso permits zero, one or several. |
| [part_of](part_of.md) | Canonical content-item id, absent or null when no item is assigned. |
| [physical_box](physical_box.md) | A box [x, y, width, height] in pixels of this page's picture, with origin at its upper left. Impresso requires exactly four integers, without a nonnegative or positive bound. It is an array, not an object with invented coordinate fields. |
| [regions](regions.md) | Regions in page order; an empty list is accepted by Impresso. |
| [section_part_of](section_part_of.md) | Content-item ids grouped by this section-heading region. The list may be absent or null; Impresso also permits null members and empty lists. |
| [sm](sm.md) | Original source medium; present together with st. |
| [st](st.md) | Media source type; present together with sm. Newspaper requires print; radio_broadcast requires typescript. |
| [style](style.md) | Style id in the separate issue file's s list; no style fields are added here. |
| [tokens](tokens.md) | OCR tokens in line order; Impresso permits an empty list. |
| [ts](ts.md) | JSON creation timestamp, intended as YYYY-MM-DDTHH:MM:SSZ; Impresso imposes no format constraint. At least one of ts and cdt is present; both are allowed. |
| [tx](tx.md) | Token surface text, including empty text if stored that way. |


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
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model. |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model. |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular day |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
