---
search:
  boost: 5.0
---

# Slot: cdt 


_Legacy JSON creation timestamp; Impresso validates a string without a date format._



<div data-search-exclude markdown="1">



URI: [pc:cdt](https://pruzhany.org/ns/sourced-entities#cdt)
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
| impresso | page.schema.json cdt. |
| alto | Processing/processingStep/processingDateTime only if that step created this file; a JSON file timestamp is not necessarily an OCR processing time. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:cdt |
| native | pc:cdt |




## LinkML Source

<details>
```yaml
name: cdt
annotations:
  impresso:
    tag: impresso
    value: page.schema.json cdt.
  alto:
    tag: alto
    value: Processing/processingStep/processingDateTime only if that step created
      this file; a JSON file timestamp is not necessarily an OCR processing time.
description: Legacy JSON creation timestamp; Impresso validates a string without a
  date format.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalPage
domain_of:
- PhysicalPage
range: string

```
</details></div>
