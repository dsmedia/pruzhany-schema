---
search:
  boost: 5.0
---

# Slot: english_sha256 

<div data-search-exclude markdown="1">



URI: [pc:english_sha256](https://pruzhany.org/ns/sourced-entities#english_sha256)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SummaryBasis](SummaryBasis.md) | The exact English a summary was written from, by its digest, so that a summary of an English since changed can be told apart from a current one. |  no  |
| [EnglishCheck](EnglishCheck.md) | A later, separate check of one English field against one exact reading of the printed text, bound to both and to the judgement kept by their digests. |  no  |
| [TitleCheck](TitleCheck.md) | A check of a supplied title's English. |  no  |
| [TranslationCheck](TranslationCheck.md) | A check of a translation's English. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SummaryBasis](SummaryBasis.md), [EnglishCheck](EnglishCheck.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:english_sha256 |
| native | pc:english_sha256 |




## LinkML Source

<details>
```yaml
name: english_sha256
domain_of:
- SummaryBasis
- EnglishCheck
range: string

```
</details></div>
