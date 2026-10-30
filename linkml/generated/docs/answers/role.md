---
search:
  boost: 5.0
---

# Slot: Role (role) 


_What the person is in this piece, in a few words._



<div data-search-exclude markdown="1">



URI: [pc:role](https://pruzhany.org/ns/sourced-entities#role)
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





### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:role |
| native | pc:role |




## LinkML Source

<details>
```yaml
name: role
description: What the person is in this piece, in a few words.
title: Role
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: WriteEnglishPerson
domain_of:
- WriteEnglishPerson
range: string
required: true

```
</details></div>
