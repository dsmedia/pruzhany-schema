---
search:
  boost: 5.0
---

# Slot: attribution 

<div data-search-exclude markdown="1">



URI: [pc:attribution](https://pruzhany.org/ns/sourced-entities#attribution)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnglishCheck](EnglishCheck.md) | A later, separate check of one English field against one exact reading of the printed text, bound to both and to the judgement kept by their digests. |  no  |
| [TitleCheck](TitleCheck.md) | A check of a supplied title's English. |  no  |
| [TranslationCheck](TranslationCheck.md) | A check of a translation's English. |  no  |
| [SuppliedTitle](SuppliedTitle.md) | A title supplied in English for a content item or section, with what it was made from, who made it and, where one was made, its later check. |  no  |
| [Translation](Translation.md) | An English translation of exact source words, with the exact text it was made from, who made it and, where one was made, its later check. |  no  |
| [CitedTranslation](CitedTranslation.md) | English of a citation's quote or a source title, located by its containing record. Reuses Translation's English, attribution and check contract without requiring an image and box for a book page or archive record. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [EnglishCheck](EnglishCheck.md), [SuppliedTitle](SuppliedTitle.md), [Translation](Translation.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:attribution |
| native | pc:attribution |




## LinkML Source

<details>
```yaml
name: attribution
domain_of:
- EnglishCheck
- SuppliedTitle
- Translation
range: string

```
</details></div>
