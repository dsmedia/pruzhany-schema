---
search:
  boost: 5.0
---

# Slot: parts 


_List of parts of the given section or components. Exact contents can vary, will typically be composed of the metadata at disposal in the OCR/OLR._



<div data-search-exclude markdown="1">



URI: [pc:parts](https://pruzhany.org/ns/sourced-entities#parts)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoLegacy](ImpressoLegacy.md) | Legacy sections or components of the content item in the original OCR/OLR. They are meant to enable the reassignation of Impresso CIs (and enrichments) to the original OCR/OLR files. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImpressoLegacyPart](ImpressoLegacyPart.md) |
| Domain Of | [ImpressoLegacy](ImpressoLegacy.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoLegacy](ImpressoLegacy.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.i[].l.parts |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:parts |
| native | pc:parts |




## LinkML Source

<details>
```yaml
name: parts
annotations:
  impresso:
    tag: impresso
    value: issue.i[].l.parts
description: List of parts of the given section or components. Exact contents can
  vary, will typically be composed of the metadata at disposal in the OCR/OLR.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoLegacy
domain_of:
- ImpressoLegacy
range: ImpressoLegacyPart
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
