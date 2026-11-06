---
search:
  boost: 5.0
---

# Slot: heading_item_id 


_The content item that supplies this section's heading, when the heading is an item of its own. It must exist in the same issue, with page_blocks and printed_title equal to this section's heading_blocks and printed_title. No other section may name the same heading item. It is not a member of this section's content_item_ids; the items beneath it retain their section_id._



<div data-search-exclude markdown="1">



URI: [pc:heading_item_id](https://pruzhany.org/ns/sourced-entities#heading_item_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PrintedSection](PrintedSection.md) | A printed heading and the content items that stand beneath it, such as the title "What is heard in town?" over the town's news. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PrintedSection](PrintedSection.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PrintedSection](PrintedSection.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| references | ContentItem.id |




### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:heading_item_id |
| native | pc:heading_item_id |




## LinkML Source

<details>
```yaml
name: heading_item_id
annotations:
  references:
    tag: references
    value: ContentItem.id
description: The content item that supplies this section's heading, when the heading
  is an item of its own. It must exist in the same issue, with page_blocks and printed_title
  equal to this section's heading_blocks and printed_title. No other section may name
  the same heading item. It is not a member of this section's content_item_ids; the
  items beneath it retain their section_id.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: PrintedSection
domain_of:
- PrintedSection
range: string

```
</details></div>
