---
search:
  boost: 5.0
---

# Slot: consolidated_reocr_applied 


_True if the CI's text went through the re-OCRisation process. Only defined if `consolidated==True`._



<div data-search-exclude markdown="1">



URI: [pc:consolidated_reocr_applied](https://pruzhany.org/ns/sourced-entities#consolidated_reocr_applied)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoMetadata](ImpressoMetadata.md) | Metadata for an entry in the canonical issue, including its page or audio references. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [ImpressoMetadata](ImpressoMetadata.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoMetadata](ImpressoMetadata.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.metadata.consolidated_reocr_applied |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:consolidated_reocr_applied |
| native | pc:consolidated_reocr_applied |




## LinkML Source

<details>
```yaml
name: consolidated_reocr_applied
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.consolidated_reocr_applied
description: True if the CI's text went through the re-OCRisation process. Only defined
  if `consolidated==True`.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: boolean

```
</details></div>
