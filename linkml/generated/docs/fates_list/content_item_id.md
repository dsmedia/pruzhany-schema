---
search:
  boost: 5.0
---

# Slot: content_item_id 


_The piece's id, such as cu-1938-12-16-i0105._



<div data-search-exclude markdown="1">



URI: [pc:content_item_id](https://pruzhany.org/ns/sourced-entities#content_item_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListPiece](FatesListPiece.md) | A published piece of an edition of the paper. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FatesListPiece](FatesListPiece.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FatesListPiece](FatesListPiece.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^cu-\d{4}-\d{2}-\d{2}-i\d{4}$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/fates_list




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:content_item_id |
| native | pc:content_item_id |




## LinkML Source

<details>
```yaml
name: content_item_id
description: The piece's id, such as cu-1938-12-16-i0105.
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
owner: FatesListPiece
domain_of:
- FatesListPiece
range: string
required: true
pattern: ^cu-\d{4}-\d{2}-\d{2}-i\d{4}$

```
</details></div>
