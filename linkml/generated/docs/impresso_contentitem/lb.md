---
search:
  boost: 5.0
---

# Slot: lb 


_text offsets of physical line breaks (relative to 'ft' field)_



<div data-search-exclude markdown="1">



URI: [pc:lb](https://pruzhany.org/ns/sourced-entities#lb)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [ImpressoContentItem](ImpressoContentItem.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.lb |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:lb |
| native | pc:lb |




## LinkML Source

<details>
```yaml
name: lb
annotations:
  impresso:
    tag: impresso
    value: content.lb
description: text offsets of physical line breaks (relative to 'ft' field)
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: integer
multivalued: true

```
</details></div>
