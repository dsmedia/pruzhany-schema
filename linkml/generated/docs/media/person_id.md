---
search:
  boost: 5.0
---

# Slot: person_id 


_The person shown, by the person's id; null for a person not identified._



<div data-search-exclude markdown="1">



URI: [pc:person_id](https://pruzhany.org/ns/sourced-entities#person_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaDepicted](MediaDepicted.md) | One person a picture shows, identified or not, where in the picture, and on whose identification. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [MediaDepicted](MediaDepicted.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaDepicted](MediaDepicted.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:person_id |
| native | pc:person_id |




## LinkML Source

<details>
```yaml
name: person_id
description: The person shown, by the person's id; null for a person not identified.
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: MediaDepicted
domain_of:
- MediaDepicted
range: NonBlankText

```
</details></div>
