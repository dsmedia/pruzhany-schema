---
search:
  boost: 5.0
---

# Slot: Names (names) 


_The numbers of the names that are one person._



<div data-search-exclude markdown="1">



URI: [pc:names](https://pruzhany.org/ns/sourced-entities#names)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [JoinPeopleGroup](JoinPeopleGroup.md) | Names that are one person, and the name the person is given. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [JoinPeopleGroup](JoinPeopleGroup.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [JoinPeopleGroup](JoinPeopleGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:names |
| native | pc:names |




## LinkML Source

<details>
```yaml
name: names
description: The numbers of the names that are one person.
title: Names
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: JoinPeopleGroup
domain_of:
- JoinPeopleGroup
range: integer
required: true
multivalued: true

```
</details></div>
