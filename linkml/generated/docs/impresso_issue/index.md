# Impresso canonical issue external contract

External Impresso wire contract. Every published field is described; no stored field is added. Unknown object properties remain allowed. Annotations preserve JSON unions and nulls independently of requiredness; native LinkML validation alone is not the oracle.

URI: https://pruzhany.org/ns/impresso_issue

Name: pruzhany_impresso_issue



## Classes

| Class | Description |
| --- | --- |
| [ImpressoIssue](ImpressoIssue.md) | Logical representation of the contents of a canonical issue (newspaper or broadcast). |
| [ImpressoIssueItem](ImpressoIssueItem.md) | A content item (e.g. article, advertisement, radio broadcast, etc.) |
| [ImpressoIssueSection](ImpressoIssueSection.md) | A section title grouping content items, with its original OCR components. |
| [ImpressoLegacy](ImpressoLegacy.md) | Legacy sections or components of the content item in the original OCR/OLR. They are meant to enable the reassignation of Impresso CIs (and enrichments) to the original OCR/OLR files. |
| [ImpressoLegacyPart](ImpressoLegacyPart.md) | One original OCR component retained for tracing a content item back to its source. |
| [ImpressoMetadata](ImpressoMetadata.md) | Metadata for an entry in the canonical issue, including its page or audio references. |
| [ImpressoStyle](ImpressoStyle.md) | One text style from the original OCR, identified locally within the issue. |



## Slots

| Slot | Description |
| --- | --- |
| [archival_note](archival_note.md) | Plaintext archival note or description concerning the content item. In case of audio radio broadcasts, this corresponds to the content summary provided with the metadata. The field is present only when a meaningful note is available. |
| [cdt](cdt.md) | Creation date timestamp (of the JSON file). |
| [comp_fileid](comp_fileid.md) | ID of the ALTO file the component comes from. |
| [comp_id](comp_id.md) | ID of the part. |
| [comp_page_no](comp_page_no.md) | Page number of the component. |
| [comp_role](comp_role.md) | Role of the component part (eg. heading, body, etc). |
| [composing_ci_ids](composing_ci_ids.md) | A section title grouping content items, with its original OCR components.composing_ci_ids. |
| [consolidated](consolidated.md) | True if this issue is consolidated, and contains additional language identification and ocrqa information. |
| [consolidated_char_len](consolidated_char_len.md) | Character count of the consolidated text for the content item. May be null if there is no text. Only defined if `consolidated==True`. |
| [consolidated_langident_run_id](consolidated_langident_run_id.md) | Run ID corresponding to the lang ID process used to obtain the `consolidated_language` value. Only defined if `consolidated==True`. |
| [consolidated_lg](consolidated_lg.md) | Computed language of the content item. Only defined if `consolidated==True`. |
| [consolidated_ocrqa](consolidated_ocrqa.md) | Estimated OCR quality, between 0 and 1. May be null if there is no text or not enough text to compute an estimate. Only defined if `consolidated==True`. |
| [consolidated_reocr_applied](consolidated_reocr_applied.md) | True if the CI's text went through the re-OCRisation process. Only defined if `consolidated==True`. |
| [consolidated_reocr_model_id](consolidated_reocr_model_id.md) | Model ID or name corresponding to the re-OCR process. Only defined if `consolidated==True` and `consolidated_re_ocr_applied==True`. |
| [consolidated_reocr_run_id](consolidated_reocr_run_id.md) | Run ID corresponding to the re-OCR process. Only defined if `consolidated==True` and `consolidated_re_ocr_applied==True`. |
| [consolidated_ts_original](consolidated_ts_original.md) | Creation date timestamp (in '%Y-%m-%dT%H:%M:%SZ' format) of the original issue which was consolidated into this object. Only defined if `consolidated==True`. |
| [content_items](content_items.md) | The content item(s) contained in the newspaper/radio_broadcast issue. Upstream places required m on the array, where JSON Schema does not apply it; the entry metadata is therefore optional. |
| [coordinates](coordinates.md) | Coordinates (xywh format or [HPOS, VPOS, WIDTH, HEIGHT]) of image-region corresponding to the content-item depending on its type (if `tp == image`). NOTE: the 'null' option should be removed to prevent tables from having coordinates. |
| [deprecated_language](deprecated_language.md) | Language of the content item (deprecated). |
| [font](font.md) | Font name |
| [fs](fs.md) | Font size |
| [heading_legacy_parts](heading_legacy_parts.md) | A section title grouping content items, with its original OCR components.heading_legacy_parts. |
| [id](id.md) | Canonical ID of the newspaper or radio broadcast issue (e.g. GDL-1900-01-02-a, or SOC_CJ-1940-07-22-a) |
| [iiif_link](iiif_link.md) | IIIF image link, depending on content item type (if `tp == image`). The field is present only when a meaningful link is available. It should follow the format: '{scheme}://{server}/{prefix}/{identifier}/info.json'. |
| [iiif_manifest_uri](iiif_manifest_uri.md) | URI for the issue's manifest in the IIIF Presentation API. The field is present only when a meaningful URI is available. |
| [is_exact_date](is_exact_date.md) | False if the date assigned to the issue is known to be inexact or approximated, True or undefined otherwise. |
| [legacy](legacy.md) | Legacy sections or components of the content item in the original OCR/OLR. They are meant to enable the reassignation of Impresso CIs (and enrichments) to the original OCR/OLR files. |
| [lg](lg.md) | Language of the content item. |
| [lg_original](lg_original.md) | Language of the content item in the original OCR/OLR. Only defined if `consolidated==True`. |
| [media_title_variant](media_title_variant.md) | Variant title of the media title this CI is from (mainly in the case of BL newspapers). The field is present only when a meaningful variant title is available. |
| [metadata](metadata.md) | Metadata about the content item. |
| [notes](notes.md) | Notes. |
| [olr](olr.md) | True if optical layout recognition was applied to the issue/bulletin this content item originates from. |
| [part_of](part_of.md) | Article/content-item to which the image is attached (if `tp == image`). |
| [parts](parts.md) | List of parts of the given section or components. Exact contents can vary, will typically be composed of the metadata at disposal in the OCR/OLR. |
| [pp](pp.md) | Canonical IDs of pages in the issue, without file extension (e.g. GDL-1900-01-02-a-p0004). In the case `sm` is in [`print`, `typescript`]. |
| [provided_metadata](provided_metadata.md) | Minimally preprocessed issue-level metadata included by the provider institution, especially useful for radio data (sm=audio). |
| [rc](rc.md) | Radio channel, if applicable (st=='radio_broadcast'). The field is present only when a meaningful value is available. |
| [rgb](rgb.md) | Color of the text (in RGB). |
| [ro](ro.md) | Reading order index of the content item, for the table of contents view on the interface. If not defined, the CI number (after 'i' in the ID) should be used. |
| [rp](rp.md) | Radio program if applicable (st=='radio_broadcast'). The field is present only when a meaningful program name is available. |
| [rr](rr.md) | Canonical ID of audio record of the issue (in list for consistency), without file extension (e.g. INA-1900-01-02-a-r0004). In the case `sm`==`audio`. |
| [section_id](section_id.md) | A section title grouping content items, with its original OCR components.section_id. |
| [section_title](section_title.md) | A section title grouping content items, with its original OCR components. |
| [sm](sm.md) | Source medium, format in which the media was originally produced. If `tp == radio_broadcast`, this is typically `typescript` or `audio`. |
| [source](source.md) | Source image or OCR/OLR file name. |
| [speakers](speakers.md) | List of speakers (names or IDs based on availabilities) within boradcast. |
| [st](st.md) | Type of media source. Should be a value the impresso-essentials.utils SourceType enum. |
| [styles](styles.md) | The text style as defined in the OCR output. <br>Each style consists of:<br> - a name (`id`)<br> - a type-face (`f`)<br> - a font-size (`fs`)<br> - a color (`rgb`). |
| [title](title.md) | Title of the content item. The field is present only when a meaningful title is available. |
| [title_text](title_text.md) | A section title grouping content items, with its original OCR components.title_text. |
| [tp](tp.md) | Type of the content item. |
| [ts](ts.md) | Creation date timestamp (in '%Y-%m-%dT%H:%M:%SZ' format). If consolidated==True, this is the consolidated timestamp (the original creation timestamp can be found in consolidated_timestamp_original); otherwise it is the original creation timestamp. |
| [var_t](var_t.md) | Deprecated, replaced by `media_title_variant` at issue's top-level. Variant title of the media title this CI is from (only in the case of BL newspapers). The field is present only when a meaningful variant title is available. |


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
