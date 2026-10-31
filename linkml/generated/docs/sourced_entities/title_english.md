---
search:
  boost: 5.0
---

# Slot: title_english 


_English of exactly title, with based_on.source_text equal to that field's exact bytes and attribution naming the kept English or its person or model._



<div data-search-exclude markdown="1">



URI: [pc:title_english](https://pruzhany.org/ns/sourced-entities#title_english)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CitedTranslation](CitedTranslation.md) |
| Domain Of | [Source](Source.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Source](Source.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| english_of | title |




### Schema Source


* from schema: https://pruzhany.org/ns/sourced_entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:title_english |
| native | pc:title_english |
| exact | pc:site_translation |




## LinkML Source

<details>
```yaml
name: title_english
annotations:
  english_of:
    tag: english_of
    value: title
description: English of exactly title, with based_on.source_text equal to that field's
  exact bytes and attribution naming the kept English or its person or model.
from_schema: https://pruzhany.org/ns/sourced_entities
exact_mappings:
- pc:site_translation
rank: 1000
owner: Source
domain_of:
- Source
range: CitedTranslation
inlined: true

```
</details></div>
