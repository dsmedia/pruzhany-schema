# Impresso rebuilt paper content item external contract

External Impresso wire contract. Every published field is described; no stored field is added. Unknown object properties remain allowed. Annotations preserve JSON unions and nulls independently of requiredness; native LinkML validation alone is not the oracle.

URI: https://pruzhany.org/ns/impresso_contentitem

Name: pruzhany_impresso_contentitem



## Classes

| Class | Description |
| --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |
| [ImpressoContentSection](ImpressoContentSection.md) | A section title grouping this content item with others. |
| [ImpressoRebuiltPage](ImpressoRebuiltPage.md) | The rebuilt tokens and region boxes for one physical page of this content item. |
| [ImpressoRebuiltToken](ImpressoRebuiltToken.md) | The rebuilt tokens and region boxes for one physical page of this content item.t[]. |



## Slots

| Slot | Description |
| --- | --- |
| [cc](cc.md) | True if image box coordinates are known to be correct (eg. have been checked, converted or rescaled), False otherwise |
| [composing_ci_ids](composing_ci_ids.md) | A section title grouping this content item with others.composing_ci_ids. |
| [consolidated](consolidated.md) | True if the issue this CI comes from was consolidated, meaning it contains additional language identification and ocrqa information. |
| [consolidated_ocrqa](consolidated_ocrqa.md) | Estimated OCR quality, between 0 and 1. May be null if there is no text or not enough text to compute an estimate. |
| [consolidated_reocr_applied](consolidated_reocr_applied.md) | True if the CI's text went through the re-OCRisation process. |
| [coordinates](coordinates.md) | Coordinates of token relative to page. |
| [ft](ft.md) | The rebuilt full text. |
| [id](id.md) | The unique identifier for a content item (CI), (e.g. GDL-1900-01-02-a-i0001, or SOC_CJ-1940-07-22-a-i0001) |
| [is_exact_date](is_exact_date.md) | False if the date assigned to the issue is known to be inexact or approximated, True or undefined otherwise. |
| [lb](lb.md) | text offsets of physical line breaks (relative to 'ft' field) |
| [length](length.md) | token length |
| [lg](lg.md) | Language of the content item's text, expressed as a two-letter ISO 639-1 language code. |
| [lg_original](lg_original.md) | Language of the content item in the original OCR/OLR. Only defined if the content-item was consolidated. |
| [media_title_variant](media_title_variant.md) | Variant title of the media title this CI is from (mainly in the case of BL newspapers). The field is present only when a meaningful variant title is available. |
| [olr](olr.md) | True if optical layout recognition was applied to the issue/bulletin this content item originates from. |
| [page_number](page_number.md) | page number |
| [pb](pb.md) | text offsets of physical paragraph breaks (relative to 'ft' field) |
| [pp](pp.md) | Array of physical page numbers spanned by the content item, based on the issue pagination as extracted from the OCR. |
| [ppreb](ppreb.md) | List of rebuilt pages |
| [publication_date](publication_date.md) | Date of publication of issue or broadcast to which the content item belongs to in yyyy-mm-dd format. |
| [rb](rb.md) | text offsets of page regions (relative to 'ft' field) |
| [rc](rc.md) | Radio channel, if applicable (st=='radio_broadcast') and is known. |
| [regions](regions.md) | List of region coordinates. |
| [ro](ro.md) | Reading order index of the content item, for the table of contents view on the interface. If not defined, the CI number (after 'i' in the ID) should be used. |
| [rp](rp.md) | Radio program, if applicable (st=='radio_broadcast') and is known. |
| [section_id](section_id.md) | A section title grouping this content item with others.section_id. |
| [section_title](section_title.md) | A section title grouping this content item with others. |
| [sm](sm.md) | The medium in which the source media this content item belongs to was originally produced. For printed documents, this relates to the physical paper support. |
| [st](st.md) | The type of media source to which this content item belongs. Must be a value from the impresso-essentials.utils SourceType enum. |
| [start](start.md) | offset start (relative to ft field) |
| [title](title.md) | Content-item title. |
| [title_text](title_text.md) | Content-item title (deprecated). |
| [tokens](tokens.md) | List of tokens |
| [tp](tp.md) | content item type (e.g. 'ar' for article, 'ad' for advertisement) |
| [ts](ts.md) | timestamp of creation of the JSON file (in '%Y-%m-%dT%H:%M:%SZ' format e.g. '2018-09-18T08:00:08Z') |


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
