---
search:
  boost: 5.0
---

# Slot: derived_from 


_For a copy or a transcription we hold: the original it was made from, and how._



<div data-search-exclude markdown="1">



URI: [pc:derived_from](https://pruzhany.org/ns/sourced-entities#derived_from)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SourceDerivation](SourceDerivation.md) |
| Domain Of | [Source](Source.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 1 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Source](Source.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/sourced_entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:derived_from |
| native | pc:derived_from |




## LinkML Source

<details>
```yaml
name: derived_from
description: 'For a copy or a transcription we hold: the original it was made from,
  and how.'
from_schema: https://pruzhany.org/ns/sourced_entities
rank: 1000
owner: Source
domain_of:
- Source
range: SourceDerivation
multivalued: true
inlined: true
inlined_as_list: true
minimum_cardinality: 1

```
</details></div>
