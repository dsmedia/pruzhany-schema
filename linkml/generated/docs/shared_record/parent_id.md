---
search:
  boost: 5.0
---

# Slot: parent_id 


_The place it lies in, by its id._



<div data-search-exclude markdown="1">



URI: [rico:isOrWasPartOf](https://www.ica.org/standards/RiC/ontology#isOrWasPartOf)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedPlace](SharedPlace.md) | One place of the record: its names, its kind, the place it lies in, its coordinates and its outside identifiers. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [SharedPlace](SharedPlace.md) |
| Slot URI | [rico:isOrWasPartOf](https://www.ica.org/standards/RiC/ontology#isOrWasPartOf) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SharedPlace](SharedPlace.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:isOrWasPartOf |
| native | pc:parent_id |




## LinkML Source

<details>
```yaml
name: parent_id
description: The place it lies in, by its id.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
slot_uri: rico:isOrWasPartOf
owner: SharedPlace
domain_of:
- SharedPlace
range: NonBlankText

```
</details></div>
