---
search:
  boost: 5.0
---

# Slot: lg 


_Language of the content item._



<div data-search-exclude markdown="1">



URI: [pc:lg](https://pruzhany.org/ns/sourced-entities#lg)
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
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoMetadata](ImpressoMetadata.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.metadata.lg |
| nullable | True |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:lg |
| native | pc:lg |




## LinkML Source

<details>
```yaml
name: lg
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.lg
  nullable:
    tag: nullable
    value: true
description: Language of the content item.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: string
required: true

```
</details></div>
