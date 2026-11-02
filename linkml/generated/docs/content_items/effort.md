---
search:
  boost: 5.0
---

# Slot: effort 


_How hard the model was told to think, in its service's own word, such as low._



<div data-search-exclude markdown="1">



URI: [pc:effort](https://pruzhany.org/ns/sourced-entities#effort)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SummaryAuthorship](SummaryAuthorship.md) | Who wrote a summary, always a model, on which day, how hard it was told to think, and whether a person has checked the summary against the English. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
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
| self | pc:effort |
| native | pc:effort |




## LinkML Source

<details>
```yaml
name: effort
description: How hard the model was told to think, in its service's own word, such
  as low.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: SummaryAuthorship
domain_of:
- SummaryAuthorship
range: NonBlankText
required: true

```
</details></div>
