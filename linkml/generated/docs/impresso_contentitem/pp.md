---
search:
  boost: 5.0
---

# Slot: pp 


_Array of physical page numbers spanned by the content item, based on the issue pagination as extracted from the OCR._



<div data-search-exclude markdown="1">



URI: [pc:pp](https://pruzhany.org/ns/sourced-entities#pp)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [ImpressoContentItem](ImpressoContentItem.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 1 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.pp |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:pp |
| native | pc:pp |




## LinkML Source

<details>
```yaml
name: pp
annotations:
  impresso:
    tag: impresso
    value: content.pp
description: Array of physical page numbers spanned by the content item, based on
  the issue pagination as extracted from the OCR.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: double
multivalued: true
minimum_cardinality: 1

```
</details></div>
