---
search:
  boost: 5.0
---

# Slot: Title (title) 


_The title field in the AnsweredPiece response._



<div data-search-exclude markdown="1">



URI: [pc:title](https://pruzhany.org/ns/sourced-entities#title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WriteEnglishAnsweredPiece](WriteEnglishAnsweredPiece.md) | A piece of the answer, with the number it was sent under. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | pc:title |
| native | pc:title |




## LinkML Source

<details>
```yaml
name: title
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The title field in the AnsweredPiece response.
title: Title
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: WriteEnglishAnsweredPiece
domain_of:
- WriteEnglishAnsweredPiece
range: string
required: true

```
</details></div>
