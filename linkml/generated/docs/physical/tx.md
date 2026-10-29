---
search:
  boost: 5.0
---

# Slot: tx 


_Token surface text, including empty text if stored that way._



<div data-search-exclude markdown="1">



URI: [pc:tx](https://pruzhany.org/ns/sourced-entities#tx)
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
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalWord](PhysicalWord.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json r[].p[].l[].t[].tx. |
| alto | String/@CONTENT. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:tx |
| native | pc:tx |




## LinkML Source

<details>
```yaml
name: tx
annotations:
  impresso:
    tag: impresso
    value: page.schema.json r[].p[].l[].t[].tx.
  alto:
    tag: alto
    value: String/@CONTENT.
description: Token surface text, including empty text if stored that way.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalWord
domain_of:
- PhysicalWord
range: string
required: true

```
</details></div>
