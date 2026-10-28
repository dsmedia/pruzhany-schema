---
search:
  boost: 5.0
---

# Slot: translation 


_The content item's text in English, where it has been translated._



<div data-search-exclude markdown="1">



URI: [pc:translation](https://pruzhany.org/ns/sourced-entities#translation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItem](ContentItem.md) | One article, notice, greeting or advertisement of the issue: its kind, its titles, its text and English, the regions it is printed in and what it names. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Translation](Translation.md) |
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
| self | pc:translation |
| native | pc:translation |




## LinkML Source

<details>
```yaml
name: translation
description: The content item's text in English, where it has been translated.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: ContentItem
domain_of:
- ContentItem
range: Translation
inlined: true

```
</details></div>
