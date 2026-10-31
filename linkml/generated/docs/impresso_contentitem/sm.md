---
search:
  boost: 5.0
---

# Slot: sm 


_The medium in which the source media this content item belongs to was originally produced. For printed documents, this relates to the physical paper support._



<div data-search-exclude markdown="1">



URI: [pc:sm](https://pruzhany.org/ns/sourced-entities#sm)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoContentItem](ImpressoContentItem.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |


<details>
<summary>Additional Constraints</summary>
**Must Be One Of:** print, typescript

</details>











## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.sm |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:sm |
| native | pc:sm |




## LinkML Source

<details>
```yaml
name: sm
annotations:
  impresso:
    tag: impresso
    value: content.sm
description: The medium in which the source media this content item belongs to was
  originally produced. For printed documents, this relates to the physical paper support.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: string
equals_string_in:
- print
- typescript

```
</details></div>
