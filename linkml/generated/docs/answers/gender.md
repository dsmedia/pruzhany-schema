---
search:
  boost: 5.0
---

# Slot: Gender (gender) 


_The gender field in the Person response._



<div data-search-exclude markdown="1">



URI: [pc:gender](https://pruzhany.org/ns/sourced-entities#gender)
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


<details>
<summary>Additional Constraints</summary>
**Must Be One Of:** male, female, unknown

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
| self | pc:gender |
| native | pc:gender |




## LinkML Source

<details>
```yaml
name: gender
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The gender field in the Person response.
title: Gender
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: WriteEnglishPerson
domain_of:
- WriteEnglishPerson
range: string
required: true
equals_string_in:
- male
- female
- unknown

```
</details></div>
