---
search:
  boost: 5.0
---

# Slot: styles 


_The text style as defined in the OCR output. _

_Each style consists of:_

_ - a name (`id`)_

_ - a type-face (`f`)_

_ - a font-size (`fs`)_

_ - a color (`rgb`)._



<div data-search-exclude markdown="1">



URI: [pc:styles](https://pruzhany.org/ns/sourced-entities#styles)
Alias: s

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoIssue](ImpressoIssue.md) | Logical representation of the contents of a canonical issue (newspaper or broadcast). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImpressoStyle](ImpressoStyle.md) |
| Domain Of | [ImpressoIssue](ImpressoIssue.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoIssue](ImpressoIssue.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.s |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:styles |
| native | pc:styles |




## LinkML Source

<details>
```yaml
name: styles
annotations:
  impresso:
    tag: impresso
    value: issue.s
description: "The text style as defined in the OCR output. \nEach style consists of:\n\
  \ - a name (`id`)\n - a type-face (`f`)\n - a font-size (`fs`)\n - a color (`rgb`)."
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
alias: s
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: ImpressoStyle
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
