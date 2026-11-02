---
search:
  boost: 5.0
---

# Slot: newspaper 


_The paper this content item belongs to, by its id in the source register._



<div data-search-exclude markdown="1">



URI: [pc:site_newspaper](https://pruzhany.org/ns/sourced-entities#site_newspaper)
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
| Slot URI | [pc:site_newspaper](https://pruzhany.org/ns/sourced-entities#site_newspaper) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ContentItem](ContentItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | The media alias carried by Impresso's canonical id. The pinned schemas have no separate media-alias property; site_newspaper keeps the source register id. |




### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:site_newspaper |
| native | pc:newspaper |




## LinkML Source

<details>
```yaml
name: newspaper
annotations:
  impresso:
    tag: impresso
    value: The media alias carried by Impresso's canonical id. The pinned schemas
      have no separate media-alias property; site_newspaper keeps the source register
      id.
description: The paper this content item belongs to, by its id in the source register.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
slot_uri: pc:site_newspaper
owner: ContentItem
domain_of:
- ContentItem
range: NonBlankText
required: true

```
</details></div>
