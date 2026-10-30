---
search:
  boost: 5.0
---

# Slot: Lives In (lives_in) 


_The town the piece says the person lives in._



<div data-search-exclude markdown="1">



URI: [pc:lives_in](https://pruzhany.org/ns/sourced-entities#lives_in)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WriteEnglishPerson](WriteEnglishPerson.md) | A person a piece names. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [WriteEnglishPerson](WriteEnglishPerson.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [WriteEnglishPerson](WriteEnglishPerson.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| nullable | True |




### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:lives_in |
| native | pc:lives_in |




## LinkML Source

<details>
```yaml
name: lives_in
annotations:
  nullable:
    tag: nullable
    value: true
description: The town the piece says the person lives in.
title: Lives In
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: WriteEnglishPerson
domain_of:
- WriteEnglishPerson
range: string
required: true

```
</details></div>
