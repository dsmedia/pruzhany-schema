---
search:
  boost: 5.0
---

# Slot: consolidated_lg 


_Computed language of the content item. Only defined if `consolidated==True`._



<div data-search-exclude markdown="1">



URI: [pc:consolidated_lg](https://pruzhany.org/ns/sourced-entities#consolidated_lg)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoMetadata](ImpressoMetadata.md) | Metadata for an entry in the canonical issue, including its page or audio references. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoMetadata](ImpressoMetadata.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoMetadata](ImpressoMetadata.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[a-z]{2,3}$` |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.metadata.consolidated_lg |
| nullable | True |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:consolidated_lg |
| native | pc:consolidated_lg |




## LinkML Source

<details>
```yaml
name: consolidated_lg
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.consolidated_lg
  nullable:
    tag: nullable
    value: true
description: Computed language of the content item. Only defined if `consolidated==True`.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: string
pattern: ^[a-z]{2,3}$

```
</details></div>
