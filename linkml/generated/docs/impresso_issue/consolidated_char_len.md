---
search:
  boost: 5.0
---

# Slot: consolidated_char_len 


_Character count of the consolidated text for the content item. May be null if there is no text. Only defined if `consolidated==True`._



<div data-search-exclude markdown="1">



URI: [pc:consolidated_char_len](https://pruzhany.org/ns/sourced-entities#consolidated_char_len)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoMetadata](ImpressoMetadata.md) | Metadata for an entry in the canonical issue, including its page or audio references. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [ImpressoMetadata](ImpressoMetadata.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoMetadata](ImpressoMetadata.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.metadata.consolidated_char_len |
| nullable | True |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:consolidated_char_len |
| native | pc:consolidated_char_len |




## LinkML Source

<details>
```yaml
name: consolidated_char_len
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.consolidated_char_len
  nullable:
    tag: nullable
    value: true
description: Character count of the consolidated text for the content item. May be
  null if there is no text. Only defined if `consolidated==True`.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: integer
minimum_value: 0

```
</details></div>
