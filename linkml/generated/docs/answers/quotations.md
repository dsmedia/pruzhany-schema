---
search:
  boost: 5.0
---

# Slot: Quotations (quotations) 


_The quotations field in the Answer response._



<div data-search-exclude markdown="1">



URI: [pc:quotations](https://pruzhany.org/ns/sourced-entities#quotations)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuoteEnglishAnswer](QuoteEnglishAnswer.md) | The answer about a batch of quotations: every quotation it was sent, by its number. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [QuoteEnglishQuotedEnglish](QuoteEnglishQuotedEnglish.md) |
| Domain Of | [QuoteEnglishAnswer](QuoteEnglishAnswer.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [QuoteEnglishAnswer](QuoteEnglishAnswer.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_in_wire | False |




### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:quotations |
| native | pc:quotations |




## LinkML Source

<details>
```yaml
name: quotations
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The quotations field in the Answer response.
title: Quotations
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: QuoteEnglishAnswer
domain_of:
- QuoteEnglishAnswer
range: QuoteEnglishQuotedEnglish
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
