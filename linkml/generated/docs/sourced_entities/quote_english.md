---
search:
  boost: 5.0
---

# Slot: quote_english 


_English of exactly quote, with based_on.source_text equal to that field's exact bytes and attribution naming the kept English or its person or model._



<div data-search-exclude markdown="1">



URI: [pc:quote_english](https://pruzhany.org/ns/sourced-entities#quote_english)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CitedTranslation](CitedTranslation.md) |
| Domain Of | [Citation](Citation.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Citation](Citation.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| english_of | quote |




### Schema Source


* from schema: https://pruzhany.org/ns/sourced_entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:quote_english |
| native | pc:quote_english |
| exact | pc:site_translation |




## LinkML Source

<details>
```yaml
name: quote_english
annotations:
  english_of:
    tag: english_of
    value: quote
description: English of exactly quote, with based_on.source_text equal to that field's
  exact bytes and attribution naming the kept English or its person or model.
from_schema: https://pruzhany.org/ns/sourced_entities
exact_mappings:
- pc:site_translation
rank: 1000
owner: Citation
domain_of:
- Citation
range: CitedTranslation
inlined: true

```
</details></div>
