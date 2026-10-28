---
search:
  boost: 5.0
---

# Slot: blocks 


_The regions of print on the page._



<div data-search-exclude markdown="1">



URI: [pc:blocks](https://pruzhany.org/ns/sourced-entities#blocks)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Page](Page.md) | One printed page of the issue: its picture, its size and its regions of print. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Block](Block.md) |
| Domain Of | [Page](Page.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Page](Page.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | The page file's regions (r). |




### Schema Source


* from schema: https://pruzhany.org/ns/pages




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:blocks |
| native | pc:blocks |




## LinkML Source

<details>
```yaml
name: blocks
annotations:
  impresso:
    tag: impresso
    value: The page file's regions (r).
description: The regions of print on the page.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
owner: Page
domain_of:
- Page
range: Block
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
