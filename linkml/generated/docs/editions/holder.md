---
search:
  boost: 5.0
---

# Slot: holder 


_The name of the institution holding the pages the pictures were made from._



<div data-search-exclude markdown="1">



URI: [pc:picture_holder_name](https://pruzhany.org/ns/sourced-entities#picture_holder_name)
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
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [PictureSource](PictureSource.md) |
| Slot URI | [pc:picture_holder_name](https://pruzhany.org/ns/sourced-entities#picture_holder_name) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


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
| self | pc:picture_holder_name |
| native | pc:holder |
| close | rico:hasOrHadHolder |




## LinkML Source

<details>
```yaml
name: holder
description: The name of the institution holding the pages the pictures were made
  from.
from_schema: https://pruzhany.org/ns/editions
close_mappings:
- rico:hasOrHadHolder
rank: 1000
slot_uri: pc:picture_holder_name
owner: PictureSource
domain_of:
- PictureSource
range: NonBlankText
required: true

```
</details></div>
