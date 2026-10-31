---
search:
  boost: 5.0
---

# Slot: english_sha256 


_The SHA-256 digest of the checked English field's exact UTF-8 bytes._



<div data-search-exclude markdown="1">



URI: [pc:site_english_sha256](https://pruzhany.org/ns/sourced-entities#site_english_sha256)
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
| Range | [Sha256Hex](Sha256Hex.md) |
| Domain Of | [EnglishCheck](EnglishCheck.md) |
| Slot URI | [pc:site_english_sha256](https://pruzhany.org/ns/sourced-entities#site_english_sha256) |
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


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:site_english_sha256 |
| native | pc:english_sha256 |




## LinkML Source

<details>
```yaml
name: english_sha256
description: The SHA-256 digest of the checked English field's exact UTF-8 bytes.
from_schema: https://pruzhany.org/ns/media
rank: 1000
slot_uri: pc:site_english_sha256
owner: EnglishCheck
domain_of:
- EnglishCheck
range: Sha256Hex
required: true

```
</details></div>
