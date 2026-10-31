---
search:
  boost: 5.0
---

# Slot: reading_id 


_The reading of the printed text that the English was checked against._



<div data-search-exclude markdown="1">



URI: [pc:reading_id](https://pruzhany.org/ns/sourced-entities#reading_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnglishCheck](EnglishCheck.md) | A later, separate check of one English field against one exact reading of the printed text, bound to both and to the judgement kept by their digests. |  no  |
| [TitleCheck](TitleCheck.md) | A check of a supplied title's English. |  no  |
| [TranslationCheck](TranslationCheck.md) | A check of a translation's English. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [EnglishCheck](EnglishCheck.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EnglishCheck](EnglishCheck.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/sourced_entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:reading_id |
| native | pc:reading_id |




## LinkML Source

<details>
```yaml
name: reading_id
description: The reading of the printed text that the English was checked against.
from_schema: https://pruzhany.org/ns/sourced_entities
rank: 1000
owner: EnglishCheck
domain_of:
- EnglishCheck
range: NonBlankText
required: true

```
</details></div>
