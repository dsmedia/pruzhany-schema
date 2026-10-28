---
search:
  boost: 5.0
---

# Slot: dimensions 


_The picture's width and height, in its pixels._



<div data-search-exclude markdown="1">



URI: [pc:dimensions](https://pruzhany.org/ns/sourced-entities#dimensions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Page](Page.md) | One printed page of the issue: its picture, its size and its regions of print. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Page](Page.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
| Minimum Cardinality | 2 |
| Maximum Cardinality | 2 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Page](Page.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | The page file's fw and fh, the width and height of the facsimile. |




### Schema Source


* from schema: https://pruzhany.org/ns/pages




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:dimensions |
| native | pc:dimensions |




## LinkML Source

<details>
```yaml
name: dimensions
annotations:
  impresso:
    tag: impresso
    value: The page file's fw and fh, the width and height of the facsimile.
description: The picture's width and height, in its pixels.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
owner: Page
domain_of:
- Page
range: integer
required: true
multivalued: true
minimum_cardinality: 2
maximum_cardinality: 2

```
</details></div>
