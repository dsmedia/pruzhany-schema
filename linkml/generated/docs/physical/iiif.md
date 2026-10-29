---
search:
  boost: 5.0
---

# Slot: iiif 


_Deprecated IIIF manifest URI, retained for compatibility; Impresso validates plain text, not URI syntax. Exactly one of this and iiif_img_base_uri is present._



<div data-search-exclude markdown="1">



URI: [pc:iiif](https://pruzhany.org/ns/sourced-entities#iiif)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalPage](PhysicalPage.md) | One Impresso page file, with its picture metadata and physical text hierarchy. Impresso allows unknown properties at every object level; no such properties are defined here. Exactly one image key and at least one timestamp key must be present. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PhysicalPage](PhysicalPage.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalPage](PhysicalPage.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json iiif. |
| alto | No direct equivalent: a manifest is not sourceImageInformation/fileName. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:iiif |
| native | pc:iiif |




## LinkML Source

<details>
```yaml
name: iiif
annotations:
  impresso:
    tag: impresso
    value: page.schema.json iiif.
  alto:
    tag: alto
    value: 'No direct equivalent: a manifest is not sourceImageInformation/fileName.'
description: Deprecated IIIF manifest URI, retained for compatibility; Impresso validates
  plain text, not URI syntax. Exactly one of this and iiif_img_base_uri is present.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalPage
domain_of:
- PhysicalPage
range: string

```
</details></div>
