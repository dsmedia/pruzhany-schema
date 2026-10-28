---
search:
  boost: 5.0
---

# Slot: transcription 


_The words read in the region, its lines separated by line breaks._



<div data-search-exclude markdown="1">



URI: [pc:transcription](https://pruzhany.org/ns/sourced-entities#transcription)
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
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


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
| self | pc:transcription |
| native | pc:transcription |




## LinkML Source

<details>
```yaml
name: transcription
description: The words read in the region, its lines separated by line breaks.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
owner: Block
domain_of:
- Block
range: string
required: true

```
</details></div>
