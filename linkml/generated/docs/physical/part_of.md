---
search:
  boost: 5.0
---

# Slot: part_of 


_Canonical content-item id, absent or null when no item is assigned._



<div data-search-exclude markdown="1">



URI: [pc:part_of](https://pruzhany.org/ns/sourced-entities#part_of)
Alias: pOf

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalRegion](PhysicalRegion.md) | One region of the page, with a box, ordered paragraphs and optional semantic links. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PhysicalRegion](PhysicalRegion.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalRegion](PhysicalRegion.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| nullable | True |
| impresso | page.schema.json r[].pOf. |
| alto | No direct semantic content-item property on TextBlock; linking belongs to a companion logical structure such as METS, outside this module. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:part_of |
| native | pc:part_of |




## LinkML Source

<details>
```yaml
name: part_of
annotations:
  nullable:
    tag: nullable
    value: true
  impresso:
    tag: impresso
    value: page.schema.json r[].pOf.
  alto:
    tag: alto
    value: No direct semantic content-item property on TextBlock; linking belongs
      to a companion logical structure such as METS, outside this module.
description: Canonical content-item id, absent or null when no item is assigned.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
alias: pOf
owner: PhysicalRegion
domain_of:
- PhysicalRegion
range: string

```
</details></div>
