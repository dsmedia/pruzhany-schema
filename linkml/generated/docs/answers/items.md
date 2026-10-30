---
search:
  boost: 5.0
---

# Slot: Items (items) 


_The items field in the Answer response._



<div data-search-exclude markdown="1">



URI: [pc:items](https://pruzhany.org/ns/sourced-entities#items)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FindItemsAnswer](FindItemsAnswer.md) | The page's items in reading order, the headings over several items, the running head. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FindItemsAnswerItem](FindItemsAnswerItem.md) |
| Domain Of | [FindItemsAnswer](FindItemsAnswer.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FindItemsAnswer](FindItemsAnswer.md) |












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
| self | pc:items |
| native | pc:items |




## LinkML Source

<details>
```yaml
name: items
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The items field in the Answer response.
title: Items
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: FindItemsAnswer
domain_of:
- FindItemsAnswer
range: FindItemsAnswerItem
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
