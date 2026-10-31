---
search:
  boost: 5.0
---

# Slot: section_title 


_A section title grouping this content item with others._



<div data-search-exclude markdown="1">



URI: [pc:section_title](https://pruzhany.org/ns/sourced-entities#section_title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImpressoContentSection](ImpressoContentSection.md) |
| Domain Of | [ImpressoContentItem](ImpressoContentItem.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.section_title |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:section_title |
| native | pc:section_title |




## LinkML Source

<details>
```yaml
name: section_title
annotations:
  impresso:
    tag: impresso
    value: content.section_title
description: A section title grouping this content item with others.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: ImpressoContentSection
inlined: true

```
</details></div>
