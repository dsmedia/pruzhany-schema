---
search:
  boost: 5.0
---

# Slot: rc 


_Radio channel, if applicable (st=='radio_broadcast') and is known._



<div data-search-exclude markdown="1">



URI: [pc:rc](https://pruzhany.org/ns/sourced-entities#rc)
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












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.rc |
| nullable | True |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:rc |
| native | pc:rc |




## LinkML Source

<details>
```yaml
name: rc
annotations:
  impresso:
    tag: impresso
    value: content.rc
  nullable:
    tag: nullable
    value: true
description: Radio channel, if applicable (st=='radio_broadcast') and is known.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: string

```
</details></div>
