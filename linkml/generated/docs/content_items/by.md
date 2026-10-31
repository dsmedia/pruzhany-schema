---
search:
  boost: 5.0
---

# Slot: by 


_Who made it or allowed it: a person, a session or a program._



<div data-search-exclude markdown="1">



URI: [pc:by](https://pruzhany.org/ns/sourced-entities#by)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Attribution](Attribution.md) | Who made or allowed something, on what day, with an optional note. |  no  |
| [Authorship](Authorship.md) | Who wrote a supplied title, a translation or a check of one, a person or a model, and on which day. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [Attribution](Attribution.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Attribution](Attribution.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:by |
| native | pc:by |




## LinkML Source

<details>
```yaml
name: by
description: 'Who made it or allowed it: a person, a session or a program.'
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: Attribution
domain_of:
- Attribution
range: NonBlankText
required: true

```
</details></div>
