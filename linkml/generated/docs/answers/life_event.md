---
search:
  boost: 5.0
---

# Slot: life_event 


_The life_event field in the AnsweredPiece response._



<div data-search-exclude markdown="1">



URI: [pc:life_event](https://pruzhany.org/ns/sourced-entities#life_event)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WriteEnglishAnsweredPiece](WriteEnglishAnsweredPiece.md) | A piece of the answer, with the number it was sent under. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [WriteEnglishLifeEvent](WriteEnglishLifeEvent.md) |
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
| nullable | True |
| description_in_wire | False |




### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:life_event |
| native | pc:life_event |




## LinkML Source

<details>
```yaml
name: life_event
annotations:
  nullable:
    tag: nullable
    value: true
  description_in_wire:
    tag: description_in_wire
    value: false
description: The life_event field in the AnsweredPiece response.
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: WriteEnglishAnsweredPiece
domain_of:
- WriteEnglishAnsweredPiece
range: WriteEnglishLifeEvent
required: true
inlined: true

```
</details></div>
