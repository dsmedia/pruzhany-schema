---
search:
  boost: 5.0
---

# Slot: block_ids 


_The regions on that page, by their ids in the pages document, in reading order._



<div data-search-exclude markdown="1">



URI: [pc:block_ids](https://pruzhany.org/ns/sourced-entities#block_ids)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItemBlockRef](ContentItemBlockRef.md) | The regions of one page that a content item or a section heading covers, in reading order. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [ContentItemBlockRef](ContentItemBlockRef.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
| Minimum Cardinality | 1 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ContentItemBlockRef](ContentItemBlockRef.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:block_ids |
| native | pc:block_ids |




## LinkML Source

<details>
```yaml
name: block_ids
description: The regions on that page, by their ids in the pages document, in reading
  order.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
owner: ContentItemBlockRef
domain_of:
- ContentItemBlockRef
range: NonBlankText
required: true
multivalued: true
minimum_cardinality: 1

```
</details></div>
