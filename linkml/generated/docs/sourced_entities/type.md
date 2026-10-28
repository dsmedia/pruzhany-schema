---
search:
  boost: 5.0
---

# Slot: type 


_What the statement is about: a birth, a death, a residence, an occupation and so on._



<div data-search-exclude markdown="1">



URI: [pc:type](https://pruzhany.org/ns/sourced-entities#type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FactTypes](FactTypes.md) |
| Domain Of | [Fact](Fact.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fact](Fact.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/sourced_entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:type |
| native | pc:type |




## LinkML Source

<details>
```yaml
name: type
description: 'What the statement is about: a birth, a death, a residence, an occupation
  and so on.'
from_schema: https://pruzhany.org/ns/sourced_entities
rank: 1000
owner: Fact
domain_of:
- Fact
range: FactTypes
required: true

```
</details></div>
