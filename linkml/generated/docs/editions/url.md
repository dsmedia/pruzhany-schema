---
search:
  boost: 5.0
---

# Slot: url 


_The pages' descriptive page at the holder or access route._



<div data-search-exclude markdown="1">



URI: [pc:holding_object_url](https://pruzhany.org/ns/sourced-entities#holding_object_url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Newspaper](Newspaper.md) | One newspaper in the source register, with its site title, code and default picture credit. A page may supply a different credit through picture_source. |  no  |
| [PictureSource](PictureSource.md) | The credit for pictures made from a holding: its holder's name, a separate access service or collection, the shelf mark and a link. Shared by a newspaper's default credit and a page whose picture comes from elsewhere. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [PictureSource](PictureSource.md) |
| Slot URI | [pc:holding_object_url](https://pruzhany.org/ns/sourced-entities#holding_object_url) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PictureSource](PictureSource.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:holding_object_url |
| native | pc:url |
| close | rdfs:seeAlso |




## LinkML Source

<details>
```yaml
name: url
description: The pages' descriptive page at the holder or access route.
from_schema: https://pruzhany.org/ns/editions
close_mappings:
- rdfs:seeAlso
rank: 1000
slot_uri: pc:holding_object_url
owner: PictureSource
domain_of:
- PictureSource
range: uri

```
</details></div>
