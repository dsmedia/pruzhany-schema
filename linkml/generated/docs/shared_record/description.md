---
search:
  boost: 5.0
---

# Slot: description 


_A short description in words._



<div data-search-exclude markdown="1">



URI: [pc:description](https://pruzhany.org/ns/sourced-entities#description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedEvent](SharedEvent.md) | One life event, once for each happening across every issue (a birth, a wedding, a death, a memorial and so on): its kind, its main people and their parts, its dates and its place. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SharedEvent](SharedEvent.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SharedEvent](SharedEvent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:description |
| native | pc:description |




## LinkML Source

<details>
```yaml
name: description
description: A short description in words.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: SharedEvent
domain_of:
- SharedEvent
range: string

```
</details></div>
