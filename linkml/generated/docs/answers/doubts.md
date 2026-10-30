---
search:
  boost: 5.0
---

# Slot: Doubts (doubts) 


_The doubts field in the AnsweredPiece response._



<div data-search-exclude markdown="1">



URI: [pc:doubts](https://pruzhany.org/ns/sourced-entities#doubts)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WriteEnglishAnsweredPiece](WriteEnglishAnsweredPiece.md) | A piece of the answer, with the number it was sent under. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [WriteEnglishDoubt](WriteEnglishDoubt.md) |
| Domain Of | [WriteEnglishAnsweredPiece](WriteEnglishAnsweredPiece.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


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
| self | pc:doubts |
| native | pc:doubts |




## LinkML Source

<details>
```yaml
name: doubts
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The doubts field in the AnsweredPiece response.
title: Doubts
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: WriteEnglishAnsweredPiece
domain_of:
- WriteEnglishAnsweredPiece
range: WriteEnglishDoubt
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
