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
| [Translation](Translation.md) | An English translation of exact source words, with the exact text it was made from, who made it and, where one was made, its later check. |  no  |
| [CitedTranslation](CitedTranslation.md) | English of a citation's quote or a source title, located by its containing record. Reuses Translation's English, attribution and check contract without requiring an image and box for a book page or archive record. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SuppliedTitle](SuppliedTitle.md), [Translation](Translation.md) |










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
range: string

```
</details></div>
