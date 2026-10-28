---
search:
  boost: 5.0
---

# Slot: reported_in 


_The day of the first issue that reported the event, where no date is printed._



<div data-search-exclude markdown="1">



URI: [pc:reported_in](https://pruzhany.org/ns/sourced-entities#reported_in)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LifeEventDate](LifeEventDate.md) | One date of a life event: the words printed with their calendar, or, where no date is printed, the day of the first issue that reported it, or the preferred record statement's date for a death known from records alone. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IsoDay](IsoDay.md) |
| Domain Of | [LifeEventDate](LifeEventDate.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [LifeEventDate](LifeEventDate.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:reported_in |
| native | pc:reported_in |




## LinkML Source

<details>
```yaml
name: reported_in
description: The day of the first issue that reported the event, where no date is
  printed.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: LifeEventDate
domain_of:
- LifeEventDate
range: IsoDay

```
</details></div>
