---
search:
  boost: 5.0
---

# Slot: Parts (parts) 


_The parts field in the AnswerItem response._



<div data-search-exclude markdown="1">



URI: [pc:parts](https://pruzhany.org/ns/sourced-entities#parts)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FindItemsAnswerItem](FindItemsAnswerItem.md) | One item as the model gives it: its parts in order, its kind, language and headline. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [FindItemsAnswerItem](FindItemsAnswerItem.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FindItemsAnswerItem](FindItemsAnswerItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_in_wire | False |




### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:parts |
| native | pc:parts |




## LinkML Source

<details>
```yaml
name: parts
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The parts field in the AnswerItem response.
title: Parts
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: FindItemsAnswerItem
domain_of:
- FindItemsAnswerItem
range: integer
required: true
multivalued: true

```
</details></div>
