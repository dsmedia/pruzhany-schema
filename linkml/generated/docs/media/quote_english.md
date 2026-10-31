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
| [MediaFamilyWords](MediaFamilyWords.md) | The family's own words about a medium, quoted from a registered source with the page or part they are on: a public part of a citation, with no private note. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CitedTranslation](CitedTranslation.md) |
| Domain Of | [MediaFamilyWords](MediaFamilyWords.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaFamilyWords](MediaFamilyWords.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| english_of | quote |




### Schema Source


* from schema: https://pruzhany.org/ns/media




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
from_schema: https://pruzhany.org/ns/media
exact_mappings:
- pc:site_translation
rank: 1000
owner: MediaFamilyWords
domain_of:
- MediaFamilyWords
range: CitedTranslation
inlined: true

```
</details></div>
