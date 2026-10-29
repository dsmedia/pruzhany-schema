---
search:
  boost: 5.0
---

# Slot: hy 


_Whether this token is the first part of a hyphenated word, including the hyphen. Readers assume false when absent; the schema inserts no default._



<div data-search-exclude markdown="1">



URI: [pc:hy](https://pruzhany.org/ns/sourced-entities#hy)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalWord](PhysicalWord.md) | One OCR token (a word or word part), with its own box and surface text. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [PhysicalWord](PhysicalWord.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalWord](PhysicalWord.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json r[].p[].l[].t[].hy. |
| alto | String/@SUBS_TYPE HypPart1; an export must handle a trailing HYP consistently. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:hy |
| native | pc:hy |




## LinkML Source

<details>
```yaml
name: hy
annotations:
  impresso:
    tag: impresso
    value: page.schema.json r[].p[].l[].t[].hy.
  alto:
    tag: alto
    value: String/@SUBS_TYPE HypPart1; an export must handle a trailing HYP consistently.
description: Whether this token is the first part of a hyphenated word, including
  the hyphen. Readers assume false when absent; the schema inserts no default.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalWord
domain_of:
- PhysicalWord
range: boolean

```
</details></div>
