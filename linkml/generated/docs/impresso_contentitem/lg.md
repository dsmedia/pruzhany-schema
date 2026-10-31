---
search:
  boost: 5.0
---

# Slot: lg 


_Language of the content item's text, expressed as a two-letter ISO 639-1 language code._



<div data-search-exclude markdown="1">



URI: [pc:lg](https://pruzhany.org/ns/sourced-entities#lg)
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
| Regex Pattern | `^[a-z]{2,3}$` |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.lg |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:lg |
| native | pc:lg |




## LinkML Source

<details>
```yaml
name: lg
annotations:
  impresso:
    tag: impresso
    value: content.lg
description: Language of the content item's text, expressed as a two-letter ISO 639-1
  language code.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: string
pattern: ^[a-z]{2,3}$

```
</details></div>
