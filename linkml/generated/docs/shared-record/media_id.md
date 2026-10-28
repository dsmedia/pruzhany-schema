---
search:
  boost: 5.0
---

# Slot: media_id 


_The medium, by its id in the record's media._



<div data-search-exclude markdown="1">



URI: [pc:media_id](https://pruzhany.org/ns/sourced-entities#media_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaPortrait](MediaPortrait.md) | The picture a person's page shows as their portrait: a reviewed medium and the region of it to show. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [MediaPortrait](MediaPortrait.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaPortrait](MediaPortrait.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:media_id |
| native | pc:media_id |




## LinkML Source

<details>
```yaml
name: media_id
description: The medium, by its id in the record's media.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: MediaPortrait
domain_of:
- MediaPortrait
range: NonBlankText
required: true

```
</details></div>
