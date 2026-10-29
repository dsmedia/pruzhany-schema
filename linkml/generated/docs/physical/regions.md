---
search:
  boost: 5.0
---

# Slot: regions 


_Regions in page order; an empty list is accepted by Impresso._



<div data-search-exclude markdown="1">



URI: [pc:regions](https://pruzhany.org/ns/sourced-entities#regions)
Alias: r

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalPage](PhysicalPage.md) | One Impresso page file, with its picture metadata and physical text hierarchy. Impresso allows unknown properties at every object level; no such properties are defined here. Exactly one image key and at least one timestamp key must be present. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalRegion](PhysicalRegion.md) |
| Domain Of | [PhysicalPage](PhysicalPage.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalPage](PhysicalPage.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json r. |
| alto | Page/PrintSpace/TextBlock in order; this module adds no ALTO ReadingOrder field. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:regions |
| native | pc:regions |




## LinkML Source

<details>
```yaml
name: regions
annotations:
  impresso:
    tag: impresso
    value: page.schema.json r.
  alto:
    tag: alto
    value: Page/PrintSpace/TextBlock in order; this module adds no ALTO ReadingOrder
      field.
description: Regions in page order; an empty list is accepted by Impresso.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
alias: r
owner: PhysicalPage
domain_of:
- PhysicalPage
range: PhysicalRegion
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
