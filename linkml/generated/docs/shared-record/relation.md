---
search:
  boost: 5.0
---

# Slot: relation 


_Whether this source is a copy or a transcription of the original._



<div data-search-exclude markdown="1">



URI: [pc:relation](https://pruzhany.org/ns/sourced-entities#relation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SourceDerivation](SourceDerivation.md) | The record a source we hold was made from, and how: a copy or a transcription of it. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SourceDerivationRelation](SourceDerivationRelation.md) |
| Domain Of | [SourceDerivation](SourceDerivation.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SourceDerivation](SourceDerivation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:relation |
| native | pc:relation |




## LinkML Source

<details>
```yaml
name: relation
description: Whether this source is a copy or a transcription of the original.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: SourceDerivation
domain_of:
- SourceDerivation
range: SourceDerivationRelation
required: true

```
</details></div>
