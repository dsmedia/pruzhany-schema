---
search:
  boost: 5.0
---

# Slot: nf 


_Normalized dehyphenated form on the latter part or parts of a hyphenated word._



<div data-search-exclude markdown="1">



URI: [pc:nf](https://pruzhany.org/ns/sourced-entities#nf)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalWord](PhysicalWord.md) | One OCR token (a word or word part), with its own box and surface text. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PhysicalWord](PhysicalWord.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalWord](PhysicalWord.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json r[].p[].l[].t[].nf. |
| alto | String/@SUBS_CONTENT with SUBS_TYPE HypPart2 for the latter part. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:nf |
| native | pc:nf |




## LinkML Source

<details>
```yaml
name: nf
annotations:
  impresso:
    tag: impresso
    value: page.schema.json r[].p[].l[].t[].nf.
  alto:
    tag: alto
    value: String/@SUBS_CONTENT with SUBS_TYPE HypPart2 for the latter part.
description: Normalized dehyphenated form on the latter part or parts of a hyphenated
  word.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalWord
domain_of:
- PhysicalWord
range: string

```
</details></div>
