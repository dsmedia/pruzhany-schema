---
search:
  boost: 5.0
---

# Slot: fs 


_Font size_



<div data-search-exclude markdown="1">



URI: [pc:fs](https://pruzhany.org/ns/sourced-entities#fs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoStyle](ImpressoStyle.md) | One text style from the original OCR, identified locally within the issue. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [ImpressoStyle](ImpressoStyle.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoStyle](ImpressoStyle.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.s[].fs |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:fs |
| native | pc:fs |




## LinkML Source

<details>
```yaml
name: fs
annotations:
  impresso:
    tag: impresso
    value: issue.s[].fs
description: Font size
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoStyle
domain_of:
- ImpressoStyle
range: double

```
</details></div>
