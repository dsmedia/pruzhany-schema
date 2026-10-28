---
search:
  boost: 5.0
---

# Slot: end_date 


_The day the event ended, where it lasted more than a day._



<div data-search-exclude markdown="1">



URI: [pc:end_date](https://pruzhany.org/ns/sourced-entities#end_date)
Alias: endDate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HistoricalEvent](HistoricalEvent.md) | An event in the world outside the town, such as Kristallnacht, on a day or over a span of days. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IsoDay](IsoDay.md) |
| Domain Of | [HistoricalEvent](HistoricalEvent.md) |
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
| self | pc:end_date |
| native | pc:end_date |




## LinkML Source

<details>
```yaml
name: end_date
description: The day the event ended, where it lasted more than a day.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
alias: endDate
owner: HistoricalEvent
domain_of:
- HistoricalEvent
range: IsoDay

```
</details></div>
