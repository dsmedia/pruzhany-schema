---
search:
  boost: 5.0
---

# Slot: tp 


_content item type (e.g. 'ar' for article, 'ad' for advertisement)_



<div data-search-exclude markdown="1">



URI: [pc:tp](https://pruzhany.org/ns/sourced-entities#tp)
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
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.tp |
| nullable | True |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:tp |
| native | pc:tp |




## LinkML Source

<details>
```yaml
name: tp
annotations:
  impresso:
    tag: impresso
    value: content.tp
  nullable:
    tag: nullable
    value: true
description: content item type (e.g. 'ar' for article, 'ad' for advertisement)
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: string
required: true

```
</details></div>
