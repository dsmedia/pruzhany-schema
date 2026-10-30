---
search:
  boost: 5.0
---

# Slot: Certainty (certainty) 


_The certainty field in the Group response._



<div data-search-exclude markdown="1">



URI: [pc:certainty](https://pruzhany.org/ns/sourced-entities#certainty)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [JoinPeopleGroup](JoinPeopleGroup.md) | Names that are one person, and the name the person is given. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [JoinPeopleGroup](JoinPeopleGroup.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [JoinPeopleGroup](JoinPeopleGroup.md) |


<details>
<summary>Additional Constraints</summary>
**Must Be One Of:** certain, likely

</details>











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
| self | pc:certainty |
| native | pc:certainty |




## LinkML Source

<details>
```yaml
name: certainty
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The certainty field in the Group response.
title: Certainty
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: JoinPeopleGroup
domain_of:
- JoinPeopleGroup
range: string
required: true
equals_string_in:
- certain
- likely

```
</details></div>
