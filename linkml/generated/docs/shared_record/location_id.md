---
search:
  boost: 5.0
---

# Slot: location_id 


_Where the event happened, by the place's id._



<div data-search-exclude markdown="1">



URI: [pc:location_id](https://pruzhany.org/ns/sourced-entities#location_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedEvent](SharedEvent.md) | One life event, once for each happening across every issue (a birth, a wedding, a death, a memorial and so on): its kind, its main people and their parts, its dates and its place. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [SharedEvent](SharedEvent.md) |
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
| self | pc:location_id |
| native | pc:location_id |




## LinkML Source

<details>
```yaml
name: location_id
description: Where the event happened, by the place's id.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: SharedEvent
domain_of:
- SharedEvent
range: NonBlankText

```
</details></div>
