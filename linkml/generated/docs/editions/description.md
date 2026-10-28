---
search:
  boost: 5.0
---

# Slot: description 


_What happened, in a sentence or two._



<div data-search-exclude markdown="1">



URI: [pc:description](https://pruzhany.org/ns/sourced-entities#description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HistoricalEvent](HistoricalEvent.md) | An event in the world outside the town, such as Kristallnacht, on a day or over a span of days. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [HistoricalEvent](HistoricalEvent.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [HistoricalEvent](HistoricalEvent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:description |
| native | pc:description |




## LinkML Source

<details>
```yaml
name: description
description: What happened, in a sentence or two.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
owner: HistoricalEvent
domain_of:
- HistoricalEvent
range: string
required: true

```
</details></div>
