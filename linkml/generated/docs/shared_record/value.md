---
search:
  boost: 5.0
---

# Slot: value 

<div data-search-exclude markdown="1">



URI: [pc:value](https://pruzhany.org/ns/sourced-entities#value)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedName](SharedName.md) | One name of a person in the shared record, with its evidence located on the printed page where the site writer found it. |  no  |
| [SharedFact](SharedFact.md) | One source's statement as the shared record keeps it: a fact with its subject, its form and its evidence located on the printed page where the site writer found it. |  no  |
| [SourcedRelation](SourcedRelation.md) | One source's statement that a person is related to another, from the subject to the relative, of a released kinship type, or of type other with a proposed type. |  no  |
| [PlaceIdentifier](PlaceIdentifier.md) | One identifier of a person, organisation, place or holder, carried only on evidence, never from a match of names. Outside ids are read on their authority's own pages; merged local ids cite the registered source of the adjudicated merge. |  no  |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |
| [Name](Name.md) | One name of a person, a family, an organisation or a place, of one kind (printed, birth, married, supplied and so on), in one script. A person's, a family's and an organisation's names are agent names and a place's are place names (vocabulary/ site-content.json, bindings agent_name and place_name), so the class itself names no single term. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PlaceIdentifier](PlaceIdentifier.md), [Fact](Fact.md), [Name](Name.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:value |
| native | pc:value |




## LinkML Source

<details>
```yaml
name: value
domain_of:
- PlaceIdentifier
- Fact
- Name
range: string

```
</details></div>
