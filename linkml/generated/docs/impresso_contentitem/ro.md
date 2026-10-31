---
search:
  boost: 5.0
---

# Slot: ro 


_Reading order index of the content item, for the table of contents view on the interface. If not defined, the CI number (after 'i' in the ID) should be used._



<div data-search-exclude markdown="1">



URI: [pc:ro](https://pruzhany.org/ns/sourced-entities#ro)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [ImpressoContentItem](ImpressoContentItem.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.ro |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:ro |
| native | pc:ro |




## LinkML Source

<details>
```yaml
name: ro
annotations:
  impresso:
    tag: impresso
    value: content.ro
description: Reading order index of the content item, for the table of contents view
  on the interface. If not defined, the CI number (after 'i' in the ID) should be
  used.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: integer

```
</details></div>
