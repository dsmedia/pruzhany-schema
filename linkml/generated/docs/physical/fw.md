---
search:
  boost: 5.0
---

# Slot: fw 


_Facsimile width in pixels; present together with fh, with no bound in Impresso._



<div data-search-exclude markdown="1">



URI: [pc:fw](https://pruzhany.org/ns/sourced-entities#fw)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalPage](PhysicalPage.md) | One Impresso page file, with its picture metadata and physical text hierarchy. Impresso allows unknown properties at every object level; no such properties are defined here. Exactly one image key and at least one timestamp key must be present. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [PhysicalPage](PhysicalPage.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalPage](PhysicalPage.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json fw. |
| alto | Page/@WIDTH with MeasurementUnit pixel. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:fw |
| native | pc:fw |




## LinkML Source

<details>
```yaml
name: fw
annotations:
  impresso:
    tag: impresso
    value: page.schema.json fw.
  alto:
    tag: alto
    value: Page/@WIDTH with MeasurementUnit pixel.
description: Facsimile width in pixels; present together with fh, with no bound in
  Impresso.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalPage
domain_of:
- PhysicalPage
range: integer

```
</details></div>
