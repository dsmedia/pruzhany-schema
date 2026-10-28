---
search:
  boost: 5.0
---

# Slot: historical_events 


_Events in the world outside the town that the calendar marks._



<div data-search-exclude markdown="1">



URI: [pc:historical_events](https://pruzhany.org/ns/sourced-entities#historical_events)
Alias: historicalEvents

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EditionsCatalog](EditionsCatalog.md) | The catalog of editions: every edition, the holidays and historical events beside them, and the dates available on the site. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [HistoricalEvent](HistoricalEvent.md) |
| Domain Of | [EditionsCatalog](EditionsCatalog.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EditionsCatalog](EditionsCatalog.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:historical_events |
| native | pc:historical_events |




## LinkML Source

<details>
```yaml
name: historical_events
description: Events in the world outside the town that the calendar marks.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
alias: historicalEvents
owner: EditionsCatalog
domain_of:
- EditionsCatalog
range: HistoricalEvent
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
