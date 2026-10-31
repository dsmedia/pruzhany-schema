---
search:
  boost: 5.0
---

# Slot: consolidated_ocrqa 


_Estimated OCR quality, between 0 and 1. May be null if there is no text or not enough text to compute an estimate. Only defined if `consolidated==True`._



<div data-search-exclude markdown="1">



URI: [pc:consolidated_ocrqa](https://pruzhany.org/ns/sourced-entities#consolidated_ocrqa)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoMetadata](ImpressoMetadata.md) | Metadata for an entry in the canonical issue, including its page or audio references. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [ImpressoMetadata](ImpressoMetadata.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoMetadata](ImpressoMetadata.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |
| Maximum Value | 1 |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.metadata.consolidated_ocrqa |
| nullable | True |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:consolidated_ocrqa |
| native | pc:consolidated_ocrqa |




## LinkML Source

<details>
```yaml
name: consolidated_ocrqa
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.consolidated_ocrqa
  nullable:
    tag: nullable
    value: true
description: Estimated OCR quality, between 0 and 1. May be null if there is no text
  or not enough text to compute an estimate. Only defined if `consolidated==True`.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: double
minimum_value: 0
maximum_value: 1

```
</details></div>
