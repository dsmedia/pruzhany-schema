---
search:
  boost: 5.0
---

# Slot: location_ids 


_The places the content item names, by their ids in the shared record._



<div data-search-exclude markdown="1">



URI: [pc:location_ids](https://pruzhany.org/ns/sourced-entities#location_ids)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItem](ContentItem.md) | One article, notice, greeting or advertisement of the issue: its kind, its titles, its text and English, the regions it is printed in and what it names. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
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
| self | pc:location_ids |
| native | pc:location_ids |




## LinkML Source

<details>
```yaml
name: location_ids
description: The places the content item names, by their ids in the shared record.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: ContentItem
domain_of:
- ContentItem
range: NonBlankText
required: true
multivalued: true

```
</details></div>
