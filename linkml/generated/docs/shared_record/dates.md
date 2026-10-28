---
search:
  boost: 5.0
---

# Slot: dates 


_The event's dates: as printed (in either calendar), or the first report's day, or the preferred record statement's._



<div data-search-exclude markdown="1">



URI: [pc:dates](https://pruzhany.org/ns/sourced-entities#dates)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedEvent](SharedEvent.md) | One life event, once for each happening across every issue (a birth, a wedding, a death, a memorial and so on): its kind, its main people and their parts, its dates and its place. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LifeEventDate](LifeEventDate.md) |
| Domain Of | [SharedEvent](SharedEvent.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
| Minimum Cardinality | 1 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SharedEvent](SharedEvent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:dates |
| native | pc:dates |




## LinkML Source

<details>
```yaml
name: dates
description: 'The event''s dates: as printed (in either calendar), or the first report''s
  day, or the preferred record statement''s.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: SharedEvent
domain_of:
- SharedEvent
range: LifeEventDate
required: true
multivalued: true
inlined: true
inlined_as_list: true
minimum_cardinality: 1

```
</details></div>
