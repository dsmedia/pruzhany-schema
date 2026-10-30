---
search:
  boost: 5.0
---

# Slot: Date Gregorian (date_gregorian) 


_YYYY-MM-DD, only as printed._



<div data-search-exclude markdown="1">



URI: [pc:date_gregorian](https://pruzhany.org/ns/sourced-entities#date_gregorian)
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




### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:date_gregorian |
| native | pc:date_gregorian |




## LinkML Source

<details>
```yaml
name: date_gregorian
annotations:
  nullable:
    tag: nullable
    value: true
description: YYYY-MM-DD, only as printed.
title: Date Gregorian
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: WriteEnglishLifeEvent
domain_of:
- WriteEnglishLifeEvent
range: string
required: true

```
</details></div>
