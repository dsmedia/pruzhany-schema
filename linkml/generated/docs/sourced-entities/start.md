---
search:
  boost: 5.0
---

# Slot: start 


_The date's start, as far as it is known: YYYY, YYYY-MM or YYYY-MM-DD._



<div data-search-exclude markdown="1">



URI: [pc:start](https://pruzhany.org/ns/sourced-entities#start)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SourcedDate](SourcedDate.md) | A date a source gives: a normalized start (and end, for a range) with how precise it is, or the words as printed with their calendar, or both. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IsoYearMonthOrDay](IsoYearMonthOrDay.md) |
| Domain Of | [SourcedDate](SourcedDate.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SourcedDate](SourcedDate.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/sourced_entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:start |
| native | pc:start |




## LinkML Source

<details>
```yaml
name: start
description: 'The date''s start, as far as it is known: YYYY, YYYY-MM or YYYY-MM-DD.'
from_schema: https://pruzhany.org/ns/sourced_entities
rank: 1000
owner: SourcedDate
domain_of:
- SourcedDate
range: IsoYearMonthOrDay

```
</details></div>
