---
search:
  boost: 5.0
---

# Slot: type 

<div data-search-exclude markdown="1">



URI: [pc:type](https://pruzhany.org/ns/sourced-entities#type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedFact](SharedFact.md) | One source's statement as the shared record keeps it: a fact with its subject, its form and its evidence located on the printed page where the site writer found it. |  no  |
| [SourcedRelation](SourcedRelation.md) | One source's statement that a person is related to another, from the subject to the relative, of a released kinship type, or of type other with a proposed type. |  no  |
| [SharedPlace](SharedPlace.md) | One place of the record: its names, its kind, the place it lies in, its coordinates and its outside identifiers. |  no  |
| [SharedEvent](SharedEvent.md) | One life event, once for each happening across every issue (a birth, a wedding, a death, a memorial and so on): its kind, its main people and their parts, its dates and its place. |  no  |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SourcedRelation](SourcedRelation.md), [SharedPlace](SharedPlace.md), [SharedEvent](SharedEvent.md), [Fact](Fact.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:type |
| native | pc:type |




## LinkML Source

<details>
```yaml
name: type
domain_of:
- SourcedRelation
- SharedPlace
- SharedEvent
- Fact
range: string

```
</details></div>
