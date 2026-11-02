---
search:
  boost: 5.0
---

# Slot: based_on 

<div data-search-exclude markdown="1">



URI: [pc:based_on](https://pruzhany.org/ns/sourced-entities#based_on)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Summary](Summary.md) | A short summary in English of a content item, written from its English translation, with the digest of the exact English it was written from and who wrote it. |  no  |
| [SuppliedTitle](SuppliedTitle.md) | A title supplied in English for a content item or section, with what it was made from, who made it and, where one was made, its later check. |  no  |
| [Translation](Translation.md) | An English translation of exact source words, with the exact text it was made from, who made it and, where one was made, its later check. |  no  |
| [CitedTranslation](CitedTranslation.md) | English of a citation's quote or a source title, located by its containing record. Reuses Translation's English, attribution and check contract without requiring an image and box for a book page or archive record. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Summary](Summary.md), [SuppliedTitle](SuppliedTitle.md), [Translation](Translation.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:based_on |
| native | pc:based_on |




## LinkML Source

<details>
```yaml
name: based_on
domain_of:
- Summary
- SuppliedTitle
- Translation
range: string

```
</details></div>
