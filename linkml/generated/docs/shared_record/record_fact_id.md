---
search:
  boost: 5.0
---

# Slot: record_fact_id 


_For a death known from records: the accepted death fact whose date and place describe it, by the fact's id._



<div data-search-exclude markdown="1">



URI: [pc:site_event_record_date](https://pruzhany.org/ns/sourced-entities#site_event_record_date)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LifeEventDate](LifeEventDate.md) | One date of a life event: the words printed with their calendar, or, where no date is printed, the day of the first issue that reported it, or the preferred record statement's date for a death known from records alone. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [LifeEventDate](LifeEventDate.md) |
| Slot URI | [pc:site_event_record_date](https://pruzhany.org/ns/sourced-entities#site_event_record_date) |
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
| self | pc:site_event_record_date |
| native | pc:record_fact_id |




## LinkML Source

<details>
```yaml
name: record_fact_id
description: 'For a death known from records: the accepted death fact whose date and
  place describe it, by the fact''s id.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
slot_uri: pc:site_event_record_date
owner: LifeEventDate
domain_of:
- LifeEventDate
range: NonBlankText

```
</details></div>
