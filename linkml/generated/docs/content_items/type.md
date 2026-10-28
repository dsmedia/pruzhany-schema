---
search:
  boost: 5.0
---

# Slot: type 


_The content item's kind, one of Impresso's content item types._



<div data-search-exclude markdown="1">



URI: [pc:type](https://pruzhany.org/ns/sourced-entities#type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItem](ContentItem.md) | One article, notice, greeting or advertisement of the issue: its kind, its titles, its text and English, the regions it is printed in and what it names. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImpressoTypes](ImpressoTypes.md) |
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
| impresso | The content item's type (tp). |




### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:type |
| native | pc:type |




## LinkML Source

<details>
```yaml
name: type
annotations:
  impresso:
    tag: impresso
    value: The content item's type (tp).
description: The content item's kind, one of Impresso's content item types.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: ContentItem
domain_of:
- ContentItem
range: ImpressoTypes
required: true

```
</details></div>
