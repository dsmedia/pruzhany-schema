---
search:
  boost: 5.0
---

# Slot: vocabulary_version 


_The version of the site-content vocabulary whose values the document uses: one of the versions the current vocabulary accepts as compatible._



<div data-search-exclude markdown="1">



URI: [pc:vocabulary_version](https://pruzhany.org/ns/sourced-entities#vocabulary_version)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItemsData](ContentItemsData.md) | One issue's content items document: the issue's date, the vocabulary version its values are from, its content items and its printed sections. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ContentItemsData](ContentItemsData.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ContentItemsData](ContentItemsData.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^(0\.1\.0|1\.0\.0)$(?![\s\S])` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:vocabulary_version |
| native | pc:vocabulary_version |




## LinkML Source

<details>
```yaml
name: vocabulary_version
description: 'The version of the site-content vocabulary whose values the document
  uses: one of the versions the current vocabulary accepts as compatible.'
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: ContentItemsData
domain_of:
- ContentItemsData
range: string
required: true
pattern: ^(0\.1\.0|1\.0\.0)$(?![\s\S])

```
</details></div>
