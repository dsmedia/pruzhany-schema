---
search:
  boost: 5.0
---

# Slot: content_item_ids 


_The content items beneath the heading, by their ids._



<div data-search-exclude markdown="1">



URI: [rico:includesOrIncluded](https://www.ica.org/standards/RiC/ontology#includesOrIncluded)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PrintedSection](PrintedSection.md) | A printed heading and the content items that stand beneath it, such as the title "What is heard in town?" over the town's news. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [PrintedSection](PrintedSection.md) |
| Slot URI | [rico:includesOrIncluded](https://www.ica.org/standards/RiC/ontology#includesOrIncluded) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
| Minimum Cardinality | 1 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PrintedSection](PrintedSection.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | The content items that make up the section (section_title.composing_ci_ids). |




### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:includesOrIncluded |
| native | pc:content_item_ids |




## LinkML Source

<details>
```yaml
name: content_item_ids
annotations:
  impresso:
    tag: impresso
    value: The content items that make up the section (section_title.composing_ci_ids).
description: The content items beneath the heading, by their ids.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
slot_uri: rico:includesOrIncluded
owner: PrintedSection
domain_of:
- PrintedSection
range: NonBlankText
required: true
multivalued: true
minimum_cardinality: 1

```
</details></div>
