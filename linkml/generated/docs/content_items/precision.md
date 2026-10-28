---
search:
  boost: 5.0
---

# Slot: precision 


_How much of the date is known: year, month, day or range._



<div data-search-exclude markdown="1">



URI: [pc:precision](https://pruzhany.org/ns/sourced-entities#precision)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SourcedDate](SourcedDate.md) | A date a source gives: a normalized start (and end, for a range) with how precise it is, or the words as printed with their calendar, or both. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SourcedDatePrecision](SourcedDatePrecision.md) |
| Domain Of | [SourcedDate](SourcedDate.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SourcedDate](SourcedDate.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:precision |
| native | pc:precision |




## LinkML Source

<details>
```yaml
name: precision
description: 'How much of the date is known: year, month, day or range.'
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: SourcedDate
domain_of:
- SourcedDate
range: SourcedDatePrecision

```
</details></div>
