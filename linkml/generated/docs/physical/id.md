---
search:
  boost: 5.0
---

# Slot: id 


_Impresso's canonical page identifier; for example FABLE-1900-01-01-a-p0001._



<div data-search-exclude markdown="1">



URI: [pc:id](https://pruzhany.org/ns/sourced-entities#id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalPage](PhysicalPage.md) | One Impresso page file, with its picture metadata and physical text hierarchy. Impresso allows unknown properties at every object level; no such properties are defined here. Exactly one image key and at least one timestamp key must be present. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PhysicalPage](PhysicalPage.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalPage](PhysicalPage.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,2}-p[0-9]{4}$` |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json id, with its exact pattern. |
| alto | Page/@ID after ensuring the ALTO XML ID lexical constraints. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:id |
| native | pc:id |




## LinkML Source

<details>
```yaml
name: id
annotations:
  impresso:
    tag: impresso
    value: page.schema.json id, with its exact pattern.
  alto:
    tag: alto
    value: Page/@ID after ensuring the ALTO XML ID lexical constraints.
description: Impresso's canonical page identifier; for example FABLE-1900-01-01-a-p0001.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalPage
domain_of:
- PhysicalPage
range: string
required: true
pattern: ^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,2}-p[0-9]{4}$

```
</details></div>
