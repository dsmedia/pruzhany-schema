---
search:
  boost: 5.0
---

# Slot: section_part_of 


_Content-item ids grouped by this section-heading region. The list may be absent or null; Impresso also permits null members and empty lists._



<div data-search-exclude markdown="1">



URI: [pc:section_part_of](https://pruzhany.org/ns/sourced-entities#section_part_of)
Alias: section_pOf

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
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalRegion](PhysicalRegion.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| nullable | True |
| nullable_items | True |
| impresso | page.schema.json r[].section_pOf. |
| alto | No direct ALTO equivalent for a section's semantic content-item membership. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:section_part_of |
| native | pc:section_part_of |




## LinkML Source

<details>
```yaml
name: section_part_of
annotations:
  nullable:
    tag: nullable
    value: true
  nullable_items:
    tag: nullable_items
    value: true
  impresso:
    tag: impresso
    value: page.schema.json r[].section_pOf.
  alto:
    tag: alto
    value: No direct ALTO equivalent for a section's semantic content-item membership.
description: Content-item ids grouped by this section-heading region. The list may
  be absent or null; Impresso also permits null members and empty lists.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
alias: section_pOf
owner: PhysicalRegion
domain_of:
- PhysicalRegion
range: string
multivalued: true

```
</details></div>
