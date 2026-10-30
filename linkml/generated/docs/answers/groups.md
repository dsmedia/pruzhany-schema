---
search:
  boost: 5.0
---

# Slot: Groups (groups) 


_The groups field in the Answer response._



<div data-search-exclude markdown="1">



URI: [pc:groups](https://pruzhany.org/ns/sourced-entities#groups)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [JoinPeopleAnswer](JoinPeopleAnswer.md) | The groups of names that are one person; a name in no group is a person of its own. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [JoinPeopleGroup](JoinPeopleGroup.md) |
| Domain Of | [JoinPeopleAnswer](JoinPeopleAnswer.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [JoinPeopleAnswer](JoinPeopleAnswer.md) |












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
| self | pc:groups |
| native | pc:groups |




## LinkML Source

<details>
```yaml
name: groups
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The groups field in the Answer response.
title: Groups
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: JoinPeopleAnswer
domain_of:
- JoinPeopleAnswer
range: JoinPeopleGroup
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
