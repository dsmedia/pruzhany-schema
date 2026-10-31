---
search:
  boost: 5.0
---

# Slot: lg_original 


_Language of the content item in the original OCR/OLR. Only defined if the content-item was consolidated._



<div data-search-exclude markdown="1">



URI: [pc:lg_original](https://pruzhany.org/ns/sourced-entities#lg_original)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoContentItem](ImpressoContentItem.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.lg_original |
| nullable | True |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:lg_original |
| native | pc:lg_original |




## LinkML Source

<details>
```yaml
name: lg_original
annotations:
  impresso:
    tag: impresso
    value: content.lg_original
  nullable:
    tag: nullable
    value: true
description: Language of the content item in the original OCR/OLR. Only defined if
  the content-item was consolidated.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: string

```
</details></div>
