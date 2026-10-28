---
search:
  boost: 5.0
---

# Slot: citations 

<div data-search-exclude markdown="1">



URI: [pc:citations](https://pruzhany.org/ns/sourced-entities#citations)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedName](SharedName.md) | One name of a person in the shared record, with its evidence located on the printed page where the site writer found it. |  no  |
| [SharedFact](SharedFact.md) | One source's statement as the shared record keeps it: a fact with its subject, its form and its evidence located on the printed page where the site writer found it. |  no  |
| [SourcedRelation](SourcedRelation.md) | One source's statement that a person is related to another, from the subject to the relative, of a released kinship type, or of type other with a proposed type. |  no  |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |
| [Name](Name.md) | One name of a person, a family, an organisation or a place, of one kind (printed, birth, married, supplied and so on), in one script. A person's, a family's and an organisation's names are agent names and a place's are place names (vocabulary/ site-content.json, bindings agent_name and place_name), so the class itself names no single term. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SharedName](SharedName.md), [SharedFact](SharedFact.md), [SourcedRelation](SourcedRelation.md), [Fact](Fact.md), [Name](Name.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:citations |
| native | pc:citations |




## LinkML Source

<details>
```yaml
name: citations
domain_of:
- SharedName
- SharedFact
- SourcedRelation
- Fact
- Name
range: string

```
</details></div>
