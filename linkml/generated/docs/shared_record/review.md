---
search:
  boost: 5.0
---

# Slot: review 

<div data-search-exclude markdown="1">



URI: [pc:review](https://pruzhany.org/ns/sourced-entities#review)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedFact](SharedFact.md) | One source's statement as the shared record keeps it: a fact with its subject, its form and its evidence located on the printed page where the site writer found it. |  no  |
| [SourcedRelation](SourcedRelation.md) | One source's statement that a person is related to another, from the subject to the relative, of a released kinship type, or of type other with a proposed type. |  no  |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |
| [Fate](Fate.md) | What became of a person in the Holocaust, as far as the record shows, the facts it rests on and its review. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Fact](Fact.md), [Fate](Fate.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:review |
| native | pc:review |




## LinkML Source

<details>
```yaml
name: review
domain_of:
- Fact
- Fate
range: string

```
</details></div>
