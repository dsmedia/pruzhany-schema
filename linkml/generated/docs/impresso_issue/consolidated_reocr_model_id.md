---
search:
  boost: 5.0
---

# Slot: consolidated_reocr_model_id 


_Model ID or name corresponding to the re-OCR process. Only defined if `consolidated==True` and `consolidated_re_ocr_applied==True`._



<div data-search-exclude markdown="1">



URI: [pc:consolidated_reocr_model_id](https://pruzhany.org/ns/sourced-entities#consolidated_reocr_model_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoMetadata](ImpressoMetadata.md) | Metadata for an entry in the canonical issue, including its page or audio references. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoMetadata](ImpressoMetadata.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoMetadata](ImpressoMetadata.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.metadata.consolidated_reocr_model_id |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:consolidated_reocr_model_id |
| native | pc:consolidated_reocr_model_id |




## LinkML Source

<details>
```yaml
name: consolidated_reocr_model_id
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.consolidated_reocr_model_id
description: Model ID or name corresponding to the re-OCR process. Only defined if
  `consolidated==True` and `consolidated_re_ocr_applied==True`.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: string

```
</details></div>
