---
search:
  boost: 5.0
---

# Slot: gn 


_Glue next: true means no following whitespace. When absent readers assume false; the schema inserts no default._



<div data-search-exclude markdown="1">



URI: [pc:gn](https://pruzhany.org/ns/sourced-entities#gn)
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
| impresso | page.schema.json r[].p[].l[].t[].gn. |
| alto | Omit the intervening SP when true; no equivalent boolean on String. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:gn |
| native | pc:gn |




## LinkML Source

<details>
```yaml
name: gn
annotations:
  impresso:
    tag: impresso
    value: page.schema.json r[].p[].l[].t[].gn.
  alto:
    tag: alto
    value: Omit the intervening SP when true; no equivalent boolean on String.
description: 'Glue next: true means no following whitespace. When absent readers assume
  false; the schema inserts no default.'
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalWord
domain_of:
- PhysicalWord
range: boolean

```
</details></div>
