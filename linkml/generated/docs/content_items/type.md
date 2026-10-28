---
search:
  boost: 5.0
---

# Slot: type 

<div data-search-exclude markdown="1">



URI: [pc:type](https://pruzhany.org/ns/sourced-entities#type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItem](ContentItem.md) | One article, notice, greeting or advertisement of the issue: its kind, its titles, its text and English, the regions it is printed in and what it names. |  no  |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ContentItem](ContentItem.md), [Fact](Fact.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:type |
| native | pc:type |




## LinkML Source

<details>
```yaml
name: type
domain_of:
- ContentItem
- Fact
range: string

```
</details></div>
