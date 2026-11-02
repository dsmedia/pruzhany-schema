---
search:
  boost: 5.0
---

# Slot: route 


_The name of the service or collection readers reach the pages through, when it differs from the holder itself._



<div data-search-exclude markdown="1">



URI: [pc:picture_access_route](https://pruzhany.org/ns/sourced-entities#picture_access_route)
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
| Slot URI | [pc:picture_access_route](https://pruzhany.org/ns/sourced-entities#picture_access_route) |
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
| self | pc:picture_access_route |
| native | pc:route |




## LinkML Source

<details>
```yaml
name: route
description: The name of the service or collection readers reach the pages through,
  when it differs from the holder itself.
from_schema: https://pruzhany.org/ns/picture_source
rank: 1000
slot_uri: pc:picture_access_route
owner: PictureSource
domain_of:
- PictureSource
range: NonBlankText

```
</details></div>
