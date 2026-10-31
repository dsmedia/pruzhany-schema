---
search:
  boost: 5.0
---

# Slot: rgb 


_Color of the text (in RGB)._



<div data-search-exclude markdown="1">



URI: [pc:rgb](https://pruzhany.org/ns/sourced-entities#rgb)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoStyle](ImpressoStyle.md) | One text style from the original OCR, identified locally within the issue. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [ImpressoStyle](ImpressoStyle.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 3 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoStyle](ImpressoStyle.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.s[].rgb |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:rgb |
| native | pc:rgb |




## LinkML Source

<details>
```yaml
name: rgb
annotations:
  impresso:
    tag: impresso
    value: issue.s[].rgb
description: Color of the text (in RGB).
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoStyle
domain_of:
- ImpressoStyle
range: integer
multivalued: true
minimum_cardinality: 3

```
</details></div>
