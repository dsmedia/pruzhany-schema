---
search:
  boost: 5.0
---

# Slot: font 


_Font name_



<div data-search-exclude markdown="1">



URI: [pc:font](https://pruzhany.org/ns/sourced-entities#font)
Alias: f

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoStyle](ImpressoStyle.md) | One text style from the original OCR, identified locally within the issue. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoStyle](ImpressoStyle.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoStyle](ImpressoStyle.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.s[].f |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:font |
| native | pc:font |




## LinkML Source

<details>
```yaml
name: font
annotations:
  impresso:
    tag: impresso
    value: issue.s[].f
description: Font name
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
alias: f
owner: ImpressoStyle
domain_of:
- ImpressoStyle
range: string

```
</details></div>
