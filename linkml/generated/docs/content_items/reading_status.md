---
search:
  boost: 5.0
---

# Slot: reading_status 


_How far the text and the English have been checked; left out or null where it is not recorded._



<div data-search-exclude markdown="1">



URI: [pc:reading_status](https://pruzhany.org/ns/sourced-entities#reading_status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItem](ContentItem.md) | One article, notice, greeting or advertisement of the issue: its kind, its titles, its text and English, the regions it is printed in and what it names. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReadingStatus](ReadingStatus.md) |
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
| self | pc:reading_status |
| native | pc:reading_status |
| exact | pc:site_reading_status |




## LinkML Source

<details>
```yaml
name: reading_status
description: How far the text and the English have been checked; left out or null
  where it is not recorded.
from_schema: https://pruzhany.org/ns/content_items
exact_mappings:
- pc:site_reading_status
rank: 1000
owner: ContentItem
domain_of:
- ContentItem
range: ReadingStatus
inlined: true

```
</details></div>
