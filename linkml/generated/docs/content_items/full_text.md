---
search:
  boost: 5.0
---

# Slot: full_text 


_The content item's printed text, a copy made for the site from the lines of its regions._



<div data-search-exclude markdown="1">



URI: [pc:full_text](https://pruzhany.org/ns/sourced-entities#full_text)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItem](ContentItem.md) | One article, notice, greeting or advertisement of the issue: its kind, its titles, its text and English, the regions it is printed in and what it names. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ContentItem](ContentItem.md) |
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
| impresso | The content item's rebuilt full text (ft). |




### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:full_text |
| native | pc:full_text |
| related | pc:site_site_copy |




## LinkML Source

<details>
```yaml
name: full_text
annotations:
  impresso:
    tag: impresso
    value: The content item's rebuilt full text (ft).
description: The content item's printed text, a copy made for the site from the lines
  of its regions.
from_schema: https://pruzhany.org/ns/content_items
related_mappings:
- pc:site_site_copy
rank: 1000
owner: ContentItem
domain_of:
- ContentItem
range: string
required: true

```
</details></div>
