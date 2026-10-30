---
search:
  boost: 5.0
---

# Slot: Minor (minor) 


_True only if the piece shows the person was a child._



<div data-search-exclude markdown="1">



URI: [pc:minor](https://pruzhany.org/ns/sourced-entities#minor)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WriteEnglishPerson](WriteEnglishPerson.md) | A person a piece names. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
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
| self | pc:minor |
| native | pc:minor |




## LinkML Source

<details>
```yaml
name: minor
description: True only if the piece shows the person was a child.
title: Minor
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: WriteEnglishPerson
domain_of:
- WriteEnglishPerson
range: boolean
required: true

```
</details></div>
