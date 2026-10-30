---
search:
  boost: 5.0
---

# Slot: Pieces (pieces) 


_The pieces field in the Answer response._



<div data-search-exclude markdown="1">



URI: [pc:pieces](https://pruzhany.org/ns/sourced-entities#pieces)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WriteEnglishAnswer](WriteEnglishAnswer.md) | The answer about one page: every piece it was sent, by its number. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [WriteEnglishAnsweredPiece](WriteEnglishAnsweredPiece.md) |
| Domain Of | [WriteEnglishAnswer](WriteEnglishAnswer.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [WriteEnglishAnswer](WriteEnglishAnswer.md) |












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
| self | pc:pieces |
| native | pc:pieces |




## LinkML Source

<details>
```yaml
name: pieces
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The pieces field in the Answer response.
title: Pieces
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: WriteEnglishAnswer
domain_of:
- WriteEnglishAnswer
range: WriteEnglishAnsweredPiece
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
