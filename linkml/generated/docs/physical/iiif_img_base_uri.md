---
search:
  boost: 5.0
---

# Slot: iiif_img_base_uri 


_Base IIIF image URI without a suffix; Impresso validates plain text, not URI syntax._



<div data-search-exclude markdown="1">



URI: [pc:iiif_img_base_uri](https://pruzhany.org/ns/sourced-entities#iiif_img_base_uri)
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
| impresso | page.schema.json iiif_img_base_uri. |
| alto | Description/sourceImageInformation/fileName can identify the source picture; an image-service base URI needs an export policy to select the actual image. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:iiif_img_base_uri |
| native | pc:iiif_img_base_uri |




## LinkML Source

<details>
```yaml
name: iiif_img_base_uri
annotations:
  impresso:
    tag: impresso
    value: page.schema.json iiif_img_base_uri.
  alto:
    tag: alto
    value: Description/sourceImageInformation/fileName can identify the source picture;
      an image-service base URI needs an export policy to select the actual image.
description: Base IIIF image URI without a suffix; Impresso validates plain text,
  not URI syntax.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalPage
domain_of:
- PhysicalPage
range: string

```
</details></div>
