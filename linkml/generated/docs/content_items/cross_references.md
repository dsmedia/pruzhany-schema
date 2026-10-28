---
search:
  boost: 5.0
---

# Slot: cross_references 


_Links from this content item to others in the issue._



<div data-search-exclude markdown="1">



URI: [pc:cross_references](https://pruzhany.org/ns/sourced-entities#cross_references)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItem](ContentItem.md) | One article, notice, greeting or advertisement of the issue: its kind, its titles, its text and English, the regions it is printed in and what it names. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CrossReference](CrossReference.md) |
| Domain Of | [ContentItem](ContentItem.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ContentItem](ContentItem.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:cross_references |
| native | pc:cross_references |




## LinkML Source

<details>
```yaml
name: cross_references
description: Links from this content item to others in the issue.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: ContentItem
domain_of:
- ContentItem
range: CrossReference
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
