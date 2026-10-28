---
search:
  boost: 5.0
---

# Slot: sections 


_The issue's printed sections._



<div data-search-exclude markdown="1">



URI: [pc:sections](https://pruzhany.org/ns/sourced-entities#sections)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItemsData](ContentItemsData.md) | One issue's content items document: the issue's date, the vocabulary version its values are from, its content items and its printed sections. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PrintedSection](PrintedSection.md) |
| Domain Of | [ContentItemsData](ContentItemsData.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ContentItemsData](ContentItemsData.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:sections |
| native | pc:sections |




## LinkML Source

<details>
```yaml
name: sections
description: The issue's printed sections.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: ContentItemsData
domain_of:
- ContentItemsData
range: PrintedSection
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
