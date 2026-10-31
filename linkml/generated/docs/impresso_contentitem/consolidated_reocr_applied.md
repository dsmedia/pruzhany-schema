---
search:
  boost: 5.0
---

# Slot: consolidated_reocr_applied 


_True if the CI's text went through the re-OCRisation process._



<div data-search-exclude markdown="1">



URI: [pc:consolidated_reocr_applied](https://pruzhany.org/ns/sourced-entities#consolidated_reocr_applied)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [ImpressoContentItem](ImpressoContentItem.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.consolidated_reocr_applied |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




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
    value: content.consolidated_reocr_applied
description: True if the CI's text went through the re-OCRisation process.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: boolean

```
</details></div>
