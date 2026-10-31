---
search:
  boost: 5.0
---

# Slot: publication_date 


_Date of publication of issue or broadcast to which the content item belongs to in yyyy-mm-dd format._



<div data-search-exclude markdown="1">



URI: [pc:publication_date](https://pruzhany.org/ns/sourced-entities#publication_date)
Alias: d

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


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.d |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:publication_date |
| native | pc:publication_date |




## LinkML Source

<details>
```yaml
name: publication_date
annotations:
  impresso:
    tag: impresso
    value: content.d
description: Date of publication of issue or broadcast to which the content item belongs
  to in yyyy-mm-dd format.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
alias: d
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: string
pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$

```
</details></div>
