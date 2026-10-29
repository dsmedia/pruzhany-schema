---
search:
  boost: 5.0
---

# Slot: tokens 


_OCR tokens in line order; Impresso permits an empty list._



<div data-search-exclude markdown="1">



URI: [pc:tokens](https://pruzhany.org/ns/sourced-entities#tokens)
Alias: t

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalLine](PhysicalLine.md) | One line with a box and ordered OCR tokens. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalWord](PhysicalWord.md) |
| Domain Of | [PhysicalLine](PhysicalLine.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalLine](PhysicalLine.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json r[].p[].l[].t. |
| alto | TextLine/String, with SP or HYP as appropriate for spacing and hyphenation. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:tokens |
| native | pc:tokens |




## LinkML Source

<details>
```yaml
name: tokens
annotations:
  impresso:
    tag: impresso
    value: page.schema.json r[].p[].l[].t.
  alto:
    tag: alto
    value: TextLine/String, with SP or HYP as appropriate for spacing and hyphenation.
description: OCR tokens in line order; Impresso permits an empty list.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
alias: t
owner: PhysicalLine
domain_of:
- PhysicalLine
range: PhysicalWord
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
