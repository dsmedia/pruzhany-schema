---
search:
  boost: 5.0
---

# Slot: Running Head (running_head) 


_The running_head field in the Answer response._



<div data-search-exclude markdown="1">



URI: [pc:running_head](https://pruzhany.org/ns/sourced-entities#running_head)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FindItemsAnswer](FindItemsAnswer.md) | The page's items in reading order, the headings over several items, the running head. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
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
| default_empty_list | True |
| description_in_wire | False |




### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:running_head |
| native | pc:running_head |




## LinkML Source

<details>
```yaml
name: running_head
annotations:
  default_empty_list:
    tag: default_empty_list
    value: true
  description_in_wire:
    tag: description_in_wire
    value: false
description: The running_head field in the Answer response.
title: Running Head
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: FindItemsAnswer
domain_of:
- FindItemsAnswer
range: integer
required: true
multivalued: true

```
</details></div>
