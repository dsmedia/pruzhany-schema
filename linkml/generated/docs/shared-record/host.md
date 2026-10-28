---
search:
  boost: 5.0
---

# Slot: host 

<div data-search-exclude markdown="1">



URI: [pc:host](https://pruzhany.org/ns/sourced-entities#host)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Holder](Holder.md) | Who holds a source: an institution, a family or a private person, with its outside identifiers and its web host. A private holder's name is never published. |  no  |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Holder](Holder.md), [Source](Source.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:host |
| native | pc:host |




## LinkML Source

<details>
```yaml
name: host
domain_of:
- Holder
- Source
range: string

```
</details></div>
