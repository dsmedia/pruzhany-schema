---
search:
  boost: 5.0
---

# Slot: ts 


_timestamp of creation of the JSON file (in '%Y-%m-%dT%H:%M:%SZ' format e.g. '2018-09-18T08:00:08Z')_



<div data-search-exclude markdown="1">



URI: [pc:ts](https://pruzhany.org/ns/sourced-entities#ts)
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
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$` |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.ts |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:ts |
| native | pc:ts |




## LinkML Source

<details>
```yaml
name: ts
annotations:
  impresso:
    tag: impresso
    value: content.ts
description: timestamp of creation of the JSON file (in '%Y-%m-%dT%H:%M:%SZ' format
  e.g. '2018-09-18T08:00:08Z')
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: string
required: true
pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$

```
</details></div>
