---
search:
  boost: 5.0
---

# Slot: printed_name 

<div data-search-exclude markdown="1">



URI: [pc:printed_name](https://pruzhany.org/ns/sourced-entities#printed_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListPerson](FatesListPerson.md) | One person on the list: who, the fate, where the paper first prints them, where and when the fate is placed, the archives' records about them and how their age is known. |  no  |
| [Mention](Mention.md) | The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FatesListPerson](FatesListPerson.md), [Mention](Mention.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:printed_name |
| native | pc:printed_name |




## LinkML Source

<details>
```yaml
name: printed_name
domain_of:
- FatesListPerson
- Mention
range: string

```
</details></div>
