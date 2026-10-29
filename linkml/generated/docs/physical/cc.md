---
search:
  boost: 5.0
---

# Slot: cc 


_Whether legacy coordinates were converted or rescaled to the IIIF picture frame._



<div data-search-exclude markdown="1">



URI: [pc:cc](https://pruzhany.org/ns/sourced-entities#cc)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalPage](PhysicalPage.md) | One Impresso page file, with its picture metadata and physical text hierarchy. Impresso allows unknown properties at every object level; no such properties are defined here. Exactly one image key and at least one timestamp key must be present. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [PhysicalPage](PhysicalPage.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalPage](PhysicalPage.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json cc. |
| alto | No direct flag; an export must resolve coordinates in its MeasurementUnit and source picture frame before writing HPOS, VPOS, WIDTH and HEIGHT. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:cc |
| native | pc:cc |




## LinkML Source

<details>
```yaml
name: cc
annotations:
  impresso:
    tag: impresso
    value: page.schema.json cc.
  alto:
    tag: alto
    value: No direct flag; an export must resolve coordinates in its MeasurementUnit
      and source picture frame before writing HPOS, VPOS, WIDTH and HEIGHT.
description: Whether legacy coordinates were converted or rescaled to the IIIF picture
  frame.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalPage
domain_of:
- PhysicalPage
range: boolean

```
</details></div>
