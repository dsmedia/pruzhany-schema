---
search:
  boost: 5.0
---

# Slot: Supported (supported) 


_The supported field in the SentenceVerdict response._



<div data-search-exclude markdown="1">



URI: [pc:supported](https://pruzhany.org/ns/sourced-entities#supported)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [JudgeOpeningSentenceVerdict](JudgeOpeningSentenceVerdict.md) | Whether one sentence of the opening, by its number, is supported, and why. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [JudgeOpeningSentenceVerdict](JudgeOpeningSentenceVerdict.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [JudgeOpeningSentenceVerdict](JudgeOpeningSentenceVerdict.md) |












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
| self | pc:supported |
| native | pc:supported |




## LinkML Source

<details>
```yaml
name: supported
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The supported field in the SentenceVerdict response.
title: Supported
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: JudgeOpeningSentenceVerdict
domain_of:
- JudgeOpeningSentenceVerdict
range: boolean
required: true

```
</details></div>
