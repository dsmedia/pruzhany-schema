---
search:
  boost: 5.0
---

# Slot: rights 


_The rights statement for the pictures, as text._



<div data-search-exclude markdown="1">



URI: [rico:conditionsOfUse](https://www.ica.org/standards/RiC/ontology#conditionsOfUse)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PictureSource](PictureSource.md) | The credit for pictures made from a holding: its holder's name, a separate access service or collection, the shelf mark and a link. Shared by a newspaper's default credit and a page whose picture comes from elsewhere. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [PictureSource](PictureSource.md) |
| Slot URI | [rico:conditionsOfUse](https://www.ica.org/standards/RiC/ontology#conditionsOfUse) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PictureSource](PictureSource.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/picture_source




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:conditionsOfUse |
| native | pc:rights |




## LinkML Source

<details>
```yaml
name: rights
description: The rights statement for the pictures, as text.
from_schema: https://pruzhany.org/ns/picture_source
rank: 1000
slot_uri: rico:conditionsOfUse
owner: PictureSource
domain_of:
- PictureSource
range: NonBlankText

```
</details></div>
