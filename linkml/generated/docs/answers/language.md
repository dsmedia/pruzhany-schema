---
search:
  boost: 5.0
---

# Slot: Language (language) 


_The language field in the AnswerItem response._



<div data-search-exclude markdown="1">



URI: [pc:language](https://pruzhany.org/ns/sourced-entities#language)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FindItemsAnswerItem](FindItemsAnswerItem.md) | One item as the model gives it: its parts in order, its kind, language and headline. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FindItemsAnswerItem](FindItemsAnswerItem.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FindItemsAnswerItem](FindItemsAnswerItem.md) |


<details>
<summary>Additional Constraints</summary>
**Must Be One Of:** yi, he, pl

</details>











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
| self | pc:language |
| native | pc:language |




## LinkML Source

<details>
```yaml
name: language
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The language field in the AnswerItem response.
title: Language
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: FindItemsAnswerItem
domain_of:
- FindItemsAnswerItem
range: string
required: true
equals_string_in:
- yi
- he
- pl

```
</details></div>
