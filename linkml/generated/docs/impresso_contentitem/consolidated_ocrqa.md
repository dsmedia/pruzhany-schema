---
search:
  boost: 5.0
---

# Slot: consolidated_ocrqa 


_Estimated OCR quality, between 0 and 1. May be null if there is no text or not enough text to compute an estimate._



<div data-search-exclude markdown="1">



URI: [pc:consolidated_ocrqa](https://pruzhany.org/ns/sourced-entities#consolidated_ocrqa)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [ImpressoContentItem](ImpressoContentItem.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |
| Maximum Value | 1 |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.consolidated_ocrqa |
| nullable | True |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




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
    value: content.consolidated_ocrqa
  nullable:
    tag: nullable
    value: true
description: Estimated OCR quality, between 0 and 1. May be null if there is no text
  or not enough text to compute an estimate.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: double
minimum_value: 0
maximum_value: 1

```
</details></div>
