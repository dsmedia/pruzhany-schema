---
search:
  boost: 5.0
---

# Slot: event_id 


_The life event the content item prints, by the event's id, where it prints one._



<div data-search-exclude markdown="1">



URI: [pc:event_id](https://pruzhany.org/ns/sourced-entities#event_id)
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
| self | pc:event_id |
| native | pc:event_id |




## LinkML Source

<details>
```yaml
name: event_id
description: The life event the content item prints, by the event's id, where it prints
  one.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: ContentItem
domain_of:
- ContentItem
range: NonBlankText

```
</details></div>
