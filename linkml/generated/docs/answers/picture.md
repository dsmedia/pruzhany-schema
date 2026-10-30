---
search:
  boost: 5.0
---

# Slot: Picture (picture) 


_The picture field in the Line response._



<div data-search-exclude markdown="1">



URI: [pc:picture](https://pruzhany.org/ns/sourced-entities#picture)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReadLatinLine](ReadLatinLine.md) | One picture as the model answers for it: the picture's number and the text printed in it. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [ReadLatinLine](ReadLatinLine.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ReadLatinLine](ReadLatinLine.md) |












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
| self | pc:picture |
| native | pc:picture |




## LinkML Source

<details>
```yaml
name: picture
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The picture field in the Line response.
title: Picture
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: ReadLatinLine
domain_of:
- ReadLatinLine
range: integer
required: true

```
</details></div>
