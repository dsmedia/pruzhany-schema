---
search:
  boost: 5.0
---

# Slot: Likely (likely) 


_The likely field in the Doubt response._



<div data-search-exclude markdown="1">



URI: [pc:likely](https://pruzhany.org/ns/sourced-entities#likely)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WriteEnglishDoubt](WriteEnglishDoubt.md) | A word or short phrase the model believes the machine misread. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [WriteEnglishDoubt](WriteEnglishDoubt.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [WriteEnglishDoubt](WriteEnglishDoubt.md) |












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
| self | pc:likely |
| native | pc:likely |




## LinkML Source

<details>
```yaml
name: likely
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The likely field in the Doubt response.
title: Likely
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: WriteEnglishDoubt
domain_of:
- WriteEnglishDoubt
range: string
required: true

```
</details></div>
