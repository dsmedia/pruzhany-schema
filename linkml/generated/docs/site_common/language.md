---
search:
  boost: 5.0
---

# Slot: language 

<div data-search-exclude markdown="1">



URI: [pc:language](https://pruzhany.org/ns/sourced-entities#language)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SuppliedTitle](SuppliedTitle.md) | A title supplied in English for a content item or section, with what it was made from, who made it and, where one was made, its later check. |  no  |
| [Translation](Translation.md) | An English translation of a content item's printed text, with the exact text it was made from, who made it and, where one was made, its later check. |  no  |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SuppliedTitle](SuppliedTitle.md), [Translation](Translation.md), [Source](Source.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:language |
| native | pc:language |




## LinkML Source

<details>
```yaml
name: language
domain_of:
- SuppliedTitle
- Translation
- Source
range: string

```
</details></div>
