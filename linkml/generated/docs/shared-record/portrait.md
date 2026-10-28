---
search:
  boost: 5.0
---

# Slot: portrait 


_The reviewed picture and region the person's page shows._



<div data-search-exclude markdown="1">



URI: [pc:media_portrait](https://pruzhany.org/ns/sourced-entities#media_portrait)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedPerson](SharedPerson.md) | One person of the record, across every issue: their id, the name shown, every name they are known by, their gender, what became of them, and their portrait. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MediaPortrait](MediaPortrait.md) |
| Domain Of | [SharedPerson](SharedPerson.md) |
| Slot URI | [pc:media_portrait](https://pruzhany.org/ns/sourced-entities#media_portrait) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SharedPerson](SharedPerson.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:media_portrait |
| native | pc:portrait |




## LinkML Source

<details>
```yaml
name: portrait
description: The reviewed picture and region the person's page shows.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
slot_uri: pc:media_portrait
owner: SharedPerson
domain_of:
- SharedPerson
range: MediaPortrait
inlined: true

```
</details></div>
