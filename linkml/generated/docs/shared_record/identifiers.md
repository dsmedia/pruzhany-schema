---
search:
  boost: 5.0
---

# Slot: identifiers 

<div data-search-exclude markdown="1">



URI: [pc:identifiers](https://pruzhany.org/ns/sourced-entities#identifiers)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Holder](Holder.md) | Who holds a source: an institution, a family or a private person, with its outside identifiers and its web host. A private holder's name is never published. |  no  |
| [SharedPlace](SharedPlace.md) | One place of the record: its names, its kind, the place it lies in, its coordinates and its outside identifiers. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Holder](Holder.md), [SharedPlace](SharedPlace.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:identifiers |
| native | pc:identifiers |




## LinkML Source

<details>
```yaml
name: identifiers
domain_of:
- Holder
- SharedPlace
range: string

```
</details></div>
