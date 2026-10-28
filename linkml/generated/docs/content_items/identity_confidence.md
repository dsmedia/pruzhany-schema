---
search:
  boost: 5.0
---

# Slot: identity_confidence 


_How sure it is that the statement is about this person._



<div data-search-exclude markdown="1">



URI: [pc:identity_confidence](https://pruzhany.org/ns/sourced-entities#identity_confidence)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Confidence](Confidence.md) |
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


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:identity_confidence |
| native | pc:identity_confidence |




## LinkML Source

<details>
```yaml
name: identity_confidence
description: How sure it is that the statement is about this person.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: Fact
domain_of:
- Fact
range: Confidence
required: true

```
</details></div>
