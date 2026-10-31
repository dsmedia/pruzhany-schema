---
search:
  boost: 5.0
---

# Slot: ppreb 


_List of rebuilt pages_



<div data-search-exclude markdown="1">



URI: [pc:ppreb](https://pruzhany.org/ns/sourced-entities#ppreb)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImpressoRebuiltPage](ImpressoRebuiltPage.md) |
| Domain Of | [ImpressoContentItem](ImpressoContentItem.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.ppreb |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:ppreb |
| native | pc:ppreb |




## LinkML Source

<details>
```yaml
name: ppreb
annotations:
  impresso:
    tag: impresso
    value: content.ppreb
description: List of rebuilt pages
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: ImpressoRebuiltPage
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
