---
search:
  boost: 5.0
---

# Slot: rights_url 


_The address where the rights statement was read._



<div data-search-exclude markdown="1">



URI: [pc:picture_rights_url](https://pruzhany.org/ns/sourced-entities#picture_rights_url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PictureSource](PictureSource.md) | The credit for pictures made from a holding: its holder's name, a separate access service or collection, the shelf mark and a link. Shared by a newspaper's default credit and a page whose picture comes from elsewhere. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [PictureSource](PictureSource.md) |
| Slot URI | [pc:picture_rights_url](https://pruzhany.org/ns/sourced-entities#picture_rights_url) |
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
| self | pc:picture_rights_url |
| native | pc:rights_url |




## LinkML Source

<details>
```yaml
name: rights_url
description: The address where the rights statement was read.
from_schema: https://pruzhany.org/ns/picture_source
rank: 1000
slot_uri: pc:picture_rights_url
owner: PictureSource
domain_of:
- PictureSource
range: uri

```
</details></div>
