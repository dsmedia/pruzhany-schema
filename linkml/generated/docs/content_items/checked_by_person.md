---
search:
  boost: 5.0
---

# Slot: checked_by_person 


_Whether a person has checked the summary against the English; false until one has._



<div data-search-exclude markdown="1">



URI: [pc:checked_by_person](https://pruzhany.org/ns/sourced-entities#checked_by_person)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SummaryAuthorship](SummaryAuthorship.md) | Who wrote a summary, always a model, on which day, how hard it was told to think, and whether a person has checked the summary against the English. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [SummaryAuthorship](SummaryAuthorship.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SummaryAuthorship](SummaryAuthorship.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:checked_by_person |
| native | pc:checked_by_person |




## LinkML Source

<details>
```yaml
name: checked_by_person
description: Whether a person has checked the summary against the English; false until
  one has.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: SummaryAuthorship
domain_of:
- SummaryAuthorship
range: boolean
required: true

```
</details></div>
