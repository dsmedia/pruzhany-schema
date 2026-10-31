---
search:
  boost: 5.0
---

# Slot: lg_original 


_Language of the content item in the original OCR/OLR. Only defined if `consolidated==True`._



<div data-search-exclude markdown="1">



URI: [pc:lg_original](https://pruzhany.org/ns/sourced-entities#lg_original)
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












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.metadata.lg_original |
| nullable | True |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:lg_original |
| native | pc:lg_original |




## LinkML Source

<details>
```yaml
name: lg_original
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.lg_original
  nullable:
    tag: nullable
    value: true
description: Language of the content item in the original OCR/OLR. Only defined if
  `consolidated==True`.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: string

```
</details></div>
