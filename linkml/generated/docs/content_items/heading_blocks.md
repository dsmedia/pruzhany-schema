---
search:
  boost: 5.0
---

# Slot: heading_blocks 


_The regions the heading is printed in, page by page._



<div data-search-exclude markdown="1">



URI: [pc:heading_blocks](https://pruzhany.org/ns/sourced-entities#heading_blocks)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PrintedSection](PrintedSection.md) | A printed heading and the content items that stand beneath it, such as the title "What is heard in town?" over the town's news. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ContentItemBlockRef](ContentItemBlockRef.md) |
| Domain Of | [PrintedSection](PrintedSection.md) |
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





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:heading_blocks |
| native | pc:heading_blocks |




## LinkML Source

<details>
```yaml
name: heading_blocks
description: The regions the heading is printed in, page by page.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: PrintedSection
domain_of:
- PrintedSection
range: ContentItemBlockRef
required: true
multivalued: true
inlined: true
inlined_as_list: true
minimum_cardinality: 1

```
</details></div>
