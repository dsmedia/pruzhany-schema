---
search:
  boost: 5.0
---

# Slot: picture_source 


_The picture's credit when it differs from the paper's catalog entry. Absence means to use that entry; a present credit supplies its own holder and any route, shelf mark, link and rights, rather than merging individual fields._



<div data-search-exclude markdown="1">



URI: [pc:page_picture_source](https://pruzhany.org/ns/sourced-entities#page_picture_source)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Page](Page.md) | One printed page of the issue: its picture, its size and its regions of print. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PictureSource](PictureSource.md) |
| Domain Of | [Page](Page.md) |
| Slot URI | [pc:page_picture_source](https://pruzhany.org/ns/sourced-entities#page_picture_source) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Page](Page.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/pages




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:page_picture_source |
| native | pc:picture_source |




## LinkML Source

<details>
```yaml
name: picture_source
description: The picture's credit when it differs from the paper's catalog entry.
  Absence means to use that entry; a present credit supplies its own holder and any
  route, shelf mark, link and rights, rather than merging individual fields.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
slot_uri: pc:page_picture_source
owner: Page
domain_of:
- Page
range: PictureSource
inlined: true

```
</details></div>
