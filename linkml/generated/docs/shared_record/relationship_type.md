---
search:
  boost: 5.0
---

# Slot: relationship_type 


_For kinship: how the relative is related, from the subject to the relative._



<div data-search-exclude markdown="1">



URI: [pc:relationship_type](https://pruzhany.org/ns/sourced-entities#relationship_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedFact](SharedFact.md) | One source's statement as the shared record keeps it: a fact with its subject, its form and its evidence located on the printed page where the site writer found it. |  no  |
| [SourcedRelation](SourcedRelation.md) | One source's statement that a person is related to another, from the subject to the relative, of a released kinship type, or of type other with a proposed type. |  no  |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RelationshipTypes](RelationshipTypes.md) |
| Domain Of | [Fact](Fact.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fact](Fact.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:relationship_type |
| native | pc:relationship_type |




## LinkML Source

<details>
```yaml
name: relationship_type
description: 'For kinship: how the relative is related, from the subject to the relative.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: Fact
domain_of:
- Fact
range: RelationshipTypes

```
</details></div>
