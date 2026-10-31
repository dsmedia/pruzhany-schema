---
search:
  boost: 5.0
---

# Slot: page_id 


_The page, by its id in the pages document._



<div data-search-exclude markdown="1">



URI: [pc:page_id](https://pruzhany.org/ns/sourced-entities#page_id)
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


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ContentItemBlockRef](ContentItemBlockRef.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/sourced_entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:page_id |
| native | pc:page_id |




## LinkML Source

<details>
```yaml
name: page_id
description: The page, by its id in the pages document.
from_schema: https://pruzhany.org/ns/sourced_entities
rank: 1000
owner: ContentItemBlockRef
domain_of:
- ContentItemBlockRef
range: NonBlankText
required: true

```
</details></div>
