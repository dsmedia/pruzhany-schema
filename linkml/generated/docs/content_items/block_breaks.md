---
search:
  boost: 5.0
---

# Slot: block_breaks 


_Where each region's text begins in the full text, counted in Unicode code points._



<div data-search-exclude markdown="1">



URI: [pc:block_breaks](https://pruzhany.org/ns/sourced-entities#block_breaks)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItem](ContentItem.md) | One article, notice, greeting or advertisement of the issue: its kind, its titles, its text and English, the regions it is printed in and what it names. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonNegativeInteger](NonNegativeInteger.md) |
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



### Annotations

| property | value |
| --- | --- |
| impresso | The text offsets of page regions (rb). |




### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:block_breaks |
| native | pc:block_breaks |
| related | pc:site_site_copy |




## LinkML Source

<details>
```yaml
name: block_breaks
annotations:
  impresso:
    tag: impresso
    value: The text offsets of page regions (rb).
description: Where each region's text begins in the full text, counted in Unicode
  code points.
from_schema: https://pruzhany.org/ns/content_items
related_mappings:
- pc:site_site_copy
rank: 1000
owner: ContentItem
domain_of:
- ContentItem
range: NonNegativeInteger
required: true
multivalued: true

```
</details></div>
