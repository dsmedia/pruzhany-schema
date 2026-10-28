---
search:
  boost: 5.0
---

# Slot: unit_id 


_The content item the region belongs to, by its id; null for a region that is a section's heading._



<div data-search-exclude markdown="1">



URI: [pc:unit_id](https://pruzhany.org/ns/sourced-entities#unit_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Block](Block.md) | One region of print on a page, its box and the words read in it, belonging to one content item, or to no item when it is a section heading. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Block](Block.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Block](Block.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | The content item a region belongs to (r[].pOf). |




### Schema Source


* from schema: https://pruzhany.org/ns/pages




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:unit_id |
| native | pc:unit_id |




## LinkML Source

<details>
```yaml
name: unit_id
annotations:
  impresso:
    tag: impresso
    value: The content item a region belongs to (r[].pOf).
description: The content item the region belongs to, by its id; null for a region
  that is a section's heading.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
owner: Block
domain_of:
- Block
range: string

```
</details></div>
