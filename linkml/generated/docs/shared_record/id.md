---
search:
  boost: 5.0
---

# Slot: id 

<div data-search-exclude markdown="1">



URI: [pc:id](https://pruzhany.org/ns/sourced-entities#id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedFact](SharedFact.md) | One source's statement as the shared record keeps it: a fact with its subject, its form and its evidence located on the printed page where the site writer found it. |  no  |
| [SourcedRelation](SourcedRelation.md) | One source's statement that a person is related to another, from the subject to the relative, of a released kinship type, or of type other with a proposed type. |  no  |
| [SharedPerson](SharedPerson.md) | One person of the record, across every issue: their id, the name shown, every name they are known by, their gender, what became of them, and their portrait. |  no  |
| [SharedFamily](SharedFamily.md) | One family of the record: its id, the name shown and its names. |  no  |
| [Holder](Holder.md) | Who holds a source: an institution, a family or a private person, with its outside identifiers and its web host. A private holder's name is never published. |  no  |
| [SharedPlace](SharedPlace.md) | One place of the record: its names, its kind, the place it lies in, its coordinates and its outside identifiers. |  no  |
| [SharedOrganization](SharedOrganization.md) | One organisation of the record: its id, the name shown and its names; its offices and members are sourced facts. |  no  |
| [SharedEvent](SharedEvent.md) | One life event, once for each happening across every issue (a birth, a wedding, a death, a memorial and so on): its kind, its main people and their parts, its dates and its place. |  no  |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |
| [Mention](Mention.md) | The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention. |  no  |
| [PublicMedia](PublicMedia.md) | One held or linked copy of a registered source (a photograph, document, recording or film), as the public may see it: what it is, what it shows and says, its review, its terms and its served copies. |  no  |
| [Media](Media.md) | One held or linked copy of a registered source, as the shared record keeps it: all that the public may see, with the private master file and the private permission besides. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SharedPerson](SharedPerson.md), [SharedFamily](SharedFamily.md), [Holder](Holder.md), [SharedPlace](SharedPlace.md), [SharedOrganization](SharedOrganization.md), [SharedEvent](SharedEvent.md), [Source](Source.md), [Fact](Fact.md), [Mention](Mention.md), [PublicMedia](PublicMedia.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:id |
| native | pc:id |




## LinkML Source

<details>
```yaml
name: id
domain_of:
- SharedPerson
- SharedFamily
- Holder
- SharedPlace
- SharedOrganization
- SharedEvent
- Source
- Fact
- Mention
- PublicMedia
range: string

```
</details></div>
