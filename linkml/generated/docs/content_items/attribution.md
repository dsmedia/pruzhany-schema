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
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |
| [Name](Name.md) | One name of a person, a family, an organisation or a place, of one kind (printed, birth, married, supplied and so on), in one script. A person's, a family's and an organisation's names are agent names and a place's are place names (vocabulary/ site-content.json, bindings agent_name and place_name), so the class itself names no single term. |  no  |
| [EnglishCheck](EnglishCheck.md) | A later, separate check of one English field against one exact reading of the printed text, bound to both and to the judgement kept by their digests. |  no  |
| [TitleCheck](TitleCheck.md) | A check of a supplied title's English. |  no  |
| [TranslationCheck](TranslationCheck.md) | A check of a translation's English. |  no  |
| [SuppliedTitle](SuppliedTitle.md) | A title supplied in English for a content item or section, with what it was made from, who made it and, where one was made, its later check. |  no  |
| [Translation](Translation.md) | An English translation of a content item's printed text, with the exact text it was made from, who made it and, where one was made, its later check. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Fact](Fact.md), [Name](Name.md), [EnglishCheck](EnglishCheck.md), [SuppliedTitle](SuppliedTitle.md), [Translation](Translation.md) |










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
- Fact
- Name
- EnglishCheck
- SuppliedTitle
- Translation
range: string

```
</details></div>
