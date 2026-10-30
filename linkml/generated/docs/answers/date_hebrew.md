---
search:
  boost: 5.0
---

# Slot: Date Hebrew (date_hebrew) 


_The date_hebrew field in the LifeEvent response._



<div data-search-exclude markdown="1">



URI: [pc:date_hebrew](https://pruzhany.org/ns/sourced-entities#date_hebrew)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WriteEnglishLifeEvent](WriteEnglishLifeEvent.md) | The one family event a piece announces, greets or mourns. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [WriteEnglishLifeEvent](WriteEnglishLifeEvent.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [WriteEnglishLifeEvent](WriteEnglishLifeEvent.md) |












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
| self | pc:date_hebrew |
| native | pc:date_hebrew |




## LinkML Source

<details>
```yaml
name: date_hebrew
annotations:
  nullable:
    tag: nullable
    value: true
  description_in_wire:
    tag: description_in_wire
    value: false
description: The date_hebrew field in the LifeEvent response.
title: Date Hebrew
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: WriteEnglishLifeEvent
domain_of:
- WriteEnglishLifeEvent
range: string
required: true

```
</details></div>
