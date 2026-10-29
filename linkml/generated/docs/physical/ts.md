---
search:
  boost: 5.0
---

# Slot: ts 


_JSON creation timestamp, intended as YYYY-MM-DDTHH:MM:SSZ; Impresso imposes no format constraint. At least one of ts and cdt is present; both are allowed._



<div data-search-exclude markdown="1">



URI: [pc:ts](https://pruzhany.org/ns/sourced-entities#ts)
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
| impresso | page.schema.json ts. |
| alto | Processing/processingStep/processingDateTime only for the corresponding creation step, with export-time conversion if needed. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:ts |
| native | pc:ts |




## LinkML Source

<details>
```yaml
name: ts
annotations:
  impresso:
    tag: impresso
    value: page.schema.json ts.
  alto:
    tag: alto
    value: Processing/processingStep/processingDateTime only for the corresponding
      creation step, with export-time conversion if needed.
description: JSON creation timestamp, intended as YYYY-MM-DDTHH:MM:SSZ; Impresso imposes
  no format constraint. At least one of ts and cdt is present; both are allowed.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalPage
domain_of:
- PhysicalPage
range: string

```
</details></div>
