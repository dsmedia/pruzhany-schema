---
search:
  boost: 5.0
---

# Slot: person_ids 


_The people the permission covers, by their ids; each must be shown in the medium._



<div data-search-exclude markdown="1">



URI: [pc:person_ids](https://pruzhany.org/ns/sourced-entities#person_ids)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaConsentScope](MediaConsentScope.md) | What a permission covers: the use, the people shown, and whether people not identified are covered. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [MediaConsentScope](MediaConsentScope.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaConsentScope](MediaConsentScope.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:person_ids |
| native | pc:person_ids |




## LinkML Source

<details>
```yaml
name: person_ids
description: The people the permission covers, by their ids; each must be shown in
  the medium.
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: MediaConsentScope
domain_of:
- MediaConsentScope
range: NonBlankText
required: true
multivalued: true

```
</details></div>
