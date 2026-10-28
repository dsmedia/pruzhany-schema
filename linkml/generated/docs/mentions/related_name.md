---
search:
  boost: 5.0
---

# Slot: related_name 


_For kinship: the relative's name, where the relative has no person of their own._



<div data-search-exclude markdown="1">



URI: [pc:related_name](https://pruzhany.org/ns/sourced-entities#related_name)
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


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:related_name |
| native | pc:related_name |




## LinkML Source

<details>
```yaml
name: related_name
description: 'For kinship: the relative''s name, where the relative has no person
  of their own.'
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
owner: Fact
domain_of:
- Fact
range: NonBlankText

```
</details></div>
