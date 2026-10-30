---
search:
  boost: 5.0
---

# Slot: Number (number) 


_The number field in the AnsweredPiece response._



<div data-search-exclude markdown="1">



URI: [pc:number](https://pruzhany.org/ns/sourced-entities#number)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WriteEnglishAnsweredPiece](WriteEnglishAnsweredPiece.md) | A piece of the answer, with the number it was sent under. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [WriteEnglishAnsweredPiece](WriteEnglishAnsweredPiece.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [WriteEnglishAnsweredPiece](WriteEnglishAnsweredPiece.md) |












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
| self | pc:number |
| native | pc:number |




## LinkML Source

<details>
```yaml
name: number
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The number field in the AnsweredPiece response.
title: Number
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: WriteEnglishAnsweredPiece
domain_of:
- WriteEnglishAnsweredPiece
range: integer
required: true

```
</details></div>
