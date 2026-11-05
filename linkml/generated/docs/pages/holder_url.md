---
search:
  boost: 5.0
---

# Slot: holder_url 


_The web address of the institution named in holder: its page for the holding where the source register has one, otherwise its home page._



<div data-search-exclude markdown="1">



URI: [pc:picture_holder_url](https://pruzhany.org/ns/sourced-entities#picture_holder_url)
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
| Slot URI | [pc:picture_holder_url](https://pruzhany.org/ns/sourced-entities#picture_holder_url) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PictureSource](PictureSource.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/pages




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:picture_holder_url |
| native | pc:holder_url |
| close | rdfs:seeAlso |




## LinkML Source

<details>
```yaml
name: holder_url
description: 'The web address of the institution named in holder: its page for the
  holding where the source register has one, otherwise its home page.'
from_schema: https://pruzhany.org/ns/pages
close_mappings:
- rdfs:seeAlso
rank: 1000
slot_uri: pc:picture_holder_url
owner: PictureSource
domain_of:
- PictureSource
range: uri

```
</details></div>
