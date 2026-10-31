---
search:
  boost: 5.0
---

# Slot: judgement_id 


_The kept judgement, by an id without spaces followed by the field it judged, :title or :text._



<div data-search-exclude markdown="1">



URI: [pc:judgement_id](https://pruzhany.org/ns/sourced-entities#judgement_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnglishCheck](EnglishCheck.md) | A later, separate check of one English field against one exact reading of the printed text, bound to both and to the judgement kept by their digests. |  no  |
| [TitleCheck](TitleCheck.md) | A check of a supplied title's English. |  yes  |
| [TranslationCheck](TranslationCheck.md) | A check of a translation's English. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [EnglishCheck](EnglishCheck.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EnglishCheck](EnglishCheck.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[^\s\u0085\uFEFF]+:(title|text)$(?![\s\S])` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:judgement_id |
| native | pc:judgement_id |




## LinkML Source

<details>
```yaml
name: judgement_id
description: The kept judgement, by an id without spaces followed by the field it
  judged, :title or :text.
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: EnglishCheck
domain_of:
- EnglishCheck
range: string
required: true
pattern: ^[^\s\u0085\uFEFF]+:(title|text)$(?![\s\S])

```
</details></div>
