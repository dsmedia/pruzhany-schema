---
search:
  boost: 5.0
---

# Slot: cc 


_True if image box coordinates are known to be correct (eg. have been checked, converted or rescaled), False otherwise_



<div data-search-exclude markdown="1">



URI: [pc:cc](https://pruzhany.org/ns/sourced-entities#cc)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [ImpressoContentItem](ImpressoContentItem.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.cc |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:cc |
| native | pc:cc |




## LinkML Source

<details>
```yaml
name: cc
annotations:
  impresso:
    tag: impresso
    value: content.cc
description: True if image box coordinates are known to be correct (eg. have been
  checked, converted or rescaled), False otherwise
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: boolean

```
</details></div>
