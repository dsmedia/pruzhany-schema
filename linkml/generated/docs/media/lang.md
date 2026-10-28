---
search:
  boost: 5.0
---

# Slot: lang 


_Their language, as a BCP 47 tag._



<div data-search-exclude markdown="1">



URI: [pc:lang](https://pruzhany.org/ns/sourced-entities#lang)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaText](MediaText.md) | Words about or on a medium (a caption, a description for screen readers, an inscription, a transcript), their language and their review. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LanguageTag](LanguageTag.md) |
| Domain Of | [MediaText](MediaText.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaText](MediaText.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:lang |
| native | pc:lang |




## LinkML Source

<details>
```yaml
name: lang
description: Their language, as a BCP 47 tag.
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: MediaText
domain_of:
- MediaText
range: LanguageTag
required: true

```
</details></div>
