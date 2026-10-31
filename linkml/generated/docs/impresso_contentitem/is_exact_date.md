---
search:
  boost: 5.0
---

# Slot: is_exact_date 


_False if the date assigned to the issue is known to be inexact or approximated, True or undefined otherwise._



<div data-search-exclude markdown="1">



URI: [pc:is_exact_date](https://pruzhany.org/ns/sourced-entities#is_exact_date)
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
| impresso | content.is_exact_date |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:is_exact_date |
| native | pc:is_exact_date |




## LinkML Source

<details>
```yaml
name: is_exact_date
annotations:
  impresso:
    tag: impresso
    value: content.is_exact_date
description: False if the date assigned to the issue is known to be inexact or approximated,
  True or undefined otherwise.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: boolean

```
</details></div>
