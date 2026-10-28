---
search:
  boost: 5.0
---

# Slot: related_person_id 


_For kinship: the relative, by the person's id in the record._



<div data-search-exclude markdown="1">



URI: [pc:related_person_id](https://pruzhany.org/ns/sourced-entities#related_person_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [Fact](Fact.md) |
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
| self | pc:related_person_id |
| native | pc:related_person_id |




## LinkML Source

<details>
```yaml
name: related_person_id
description: 'For kinship: the relative, by the person''s id in the record.'
from_schema: https://pruzhany.org/ns/sourced_entities
rank: 1000
owner: Fact
domain_of:
- Fact
range: NonBlankText

```
</details></div>
