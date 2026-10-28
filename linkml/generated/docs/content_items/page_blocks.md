---
search:
  boost: 5.0
---

# Slot: page_blocks 


_The regions the content item is printed in, page by page, in reading order._



<div data-search-exclude markdown="1">



URI: [pc:page_blocks](https://pruzhany.org/ns/sourced-entities#page_blocks)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItem](ContentItem.md) | One article, notice, greeting or advertisement of the issue: its kind, its titles, its text and English, the regions it is printed in and what it names. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ContentItemBlockRef](ContentItemBlockRef.md) |
| Domain Of | [ContentItem](ContentItem.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
| Minimum Cardinality | 1 |


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
| self | pc:page_blocks |
| native | pc:page_blocks |
| related | pc:site_site_copy |




## LinkML Source

<details>
```yaml
name: page_blocks
description: The regions the content item is printed in, page by page, in reading
  order.
from_schema: https://pruzhany.org/ns/content_items
related_mappings:
- pc:site_site_copy
rank: 1000
owner: ContentItem
domain_of:
- ContentItem
range: ContentItemBlockRef
required: true
multivalued: true
inlined: true
inlined_as_list: true
minimum_cardinality: 1

```
</details></div>
