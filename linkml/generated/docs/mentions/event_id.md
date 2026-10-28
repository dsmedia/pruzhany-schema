---
search:
  boost: 5.0
---

# Slot: event_id 


_The life event the statement concerns, by its id in the record._



<div data-search-exclude markdown="1">



URI: [pc:event_id](https://pruzhany.org/ns/sourced-entities#event_id)
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
| self | pc:event_id |
| native | pc:event_id |




## LinkML Source

<details>
```yaml
name: event_id
description: The life event the statement concerns, by its id in the record.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
owner: Fact
domain_of:
- Fact
range: NonBlankText

```
</details></div>
