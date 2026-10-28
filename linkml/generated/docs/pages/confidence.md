---
search:
  boost: 5.0
---

# Slot: confidence 


_How sure the reading is, from 0 to 1, where it was recorded._



<div data-search-exclude markdown="1">



URI: [pc:confidence](https://pruzhany.org/ns/sourced-entities#confidence)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Block](Block.md) | One region of print on a page, its box and the words read in it, belonging to one content item, or to no item when it is a section heading. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [Block](Block.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Block](Block.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/pages




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:confidence |
| native | pc:confidence |




## LinkML Source

<details>
```yaml
name: confidence
description: How sure the reading is, from 0 to 1, where it was recorded.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
owner: Block
domain_of:
- Block
range: float

```
</details></div>
