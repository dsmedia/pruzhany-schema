---
search:
  boost: 5.0
---

# Slot: names 

<div data-search-exclude markdown="1">



URI: [pc:names](https://pruzhany.org/ns/sourced-entities#names)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedPerson](SharedPerson.md) | One person of the record, across every issue: their id, the name shown, every name they are known by, their gender, what became of them, their portrait and evidenced identifiers. |  no  |
| [SharedFamily](SharedFamily.md) | One family of the record: its id, the name shown and its names. |  no  |
| [SharedPlace](SharedPlace.md) | One place of the record: its names, its kind, the place it lies in, its coordinates and its outside identifiers. |  no  |
| [SharedOrganization](SharedOrganization.md) | One organisation of the record: its id, the name shown, its names and evidenced identifiers; its offices and members are sourced facts. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SharedPerson](SharedPerson.md), [SharedFamily](SharedFamily.md), [SharedPlace](SharedPlace.md), [SharedOrganization](SharedOrganization.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:names |
| native | pc:names |




## LinkML Source

<details>
```yaml
name: names
domain_of:
- SharedPerson
- SharedFamily
- SharedPlace
- SharedOrganization
range: string

```
</details></div>
