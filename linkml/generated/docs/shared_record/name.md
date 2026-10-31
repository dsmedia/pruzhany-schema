---
search:
  boost: 5.0
---

# Slot: name 

<div data-search-exclude markdown="1">



URI: [pc:name](https://pruzhany.org/ns/sourced-entities#name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedPerson](SharedPerson.md) | One person of the record, across every issue: their id, the name shown, every name they are known by, their gender, what became of them, their portrait and evidenced identifiers. |  no  |
| [SharedFamily](SharedFamily.md) | One family of the record: its id, the name shown and its names. |  no  |
| [Holder](Holder.md) | Who holds a source: an institution, a family or a private person, with its outside identifiers and its web host. A private holder's name is never published. |  no  |
| [SharedPlace](SharedPlace.md) | One place of the record: its names, its kind, the place it lies in, its coordinates and its outside identifiers. |  no  |
| [SharedOrganization](SharedOrganization.md) | One organisation of the record: its id, the name shown, its names and evidenced identifiers; its offices and members are sourced facts. |  no  |
| [SharedEvent](SharedEvent.md) | One life event, once for each happening across every issue (a birth, a wedding, a death, a memorial and so on): its kind, its main people and their parts, its dates and its place. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SharedPerson](SharedPerson.md), [SharedFamily](SharedFamily.md), [Holder](Holder.md), [SharedPlace](SharedPlace.md), [SharedOrganization](SharedOrganization.md), [SharedEvent](SharedEvent.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:name |
| native | pc:name |




## LinkML Source

<details>
```yaml
name: name
domain_of:
- SharedPerson
- SharedFamily
- Holder
- SharedPlace
- SharedOrganization
- SharedEvent
range: string

```
</details></div>
