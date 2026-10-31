---
search:
  boost: 5.0
---

# Slot: source 


_Source image or OCR/OLR file name._



<div data-search-exclude markdown="1">



URI: [pc:source](https://pruzhany.org/ns/sourced-entities#source)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoLegacy](ImpressoLegacy.md) | Legacy sections or components of the content item in the original OCR/OLR. They are meant to enable the reassignation of Impresso CIs (and enrichments) to the original OCR/OLR files. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoLegacy](ImpressoLegacy.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoLegacy](ImpressoLegacy.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.i[].l.source |
| json_types | string,array |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:source |
| native | pc:source |




## LinkML Source

<details>
```yaml
name: source
annotations:
  impresso:
    tag: impresso
    value: issue.i[].l.source
  json_types:
    tag: json_types
    value: string,array
description: Source image or OCR/OLR file name.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoLegacy
domain_of:
- ImpressoLegacy
range: string

```
</details></div>
