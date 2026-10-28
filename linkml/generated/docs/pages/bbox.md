---
search:
  boost: 5.0
---

# Slot: bbox 


_The region's box on the page picture: left, top, width and height, in the picture's pixels._



<div data-search-exclude markdown="1">



URI: [pc:bbox](https://pruzhany.org/ns/sourced-entities#bbox)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Block](Block.md) | One region of print on a page, its box and the words read in it, belonging to one content item, or to no item when it is a section heading. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonNegativeInteger](NonNegativeInteger.md) |
| Domain Of | [Block](Block.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
| Minimum Cardinality | 4 |
| Maximum Cardinality | 4 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Block](Block.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | The region's coordinates (r[].c). |




### Schema Source


* from schema: https://pruzhany.org/ns/pages




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:bbox |
| native | pc:bbox |




## LinkML Source

<details>
```yaml
name: bbox
annotations:
  impresso:
    tag: impresso
    value: The region's coordinates (r[].c).
description: 'The region''s box on the page picture: left, top, width and height,
  in the picture''s pixels.'
from_schema: https://pruzhany.org/ns/pages
rank: 1000
owner: Block
domain_of:
- Block
range: NonNegativeInteger
required: true
multivalued: true
minimum_cardinality: 4
maximum_cardinality: 4

```
</details></div>
