---
search:
  boost: 5.0
---

# Slot: issue_date 


_The issue's date, written YYYY-MM-DD._



<div data-search-exclude markdown="1">



URI: [pc:issue_date](https://pruzhany.org/ns/sourced-entities#issue_date)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItemsData](ContentItemsData.md) | One issue's content items document: the issue's date, the vocabulary version its values are from, its content items and its printed sections. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IsoDay](IsoDay.md) |
| Domain Of | [ContentItemsData](ContentItemsData.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ContentItemsData](ContentItemsData.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:issue_date |
| native | pc:issue_date |




## LinkML Source

<details>
```yaml
name: issue_date
description: The issue's date, written YYYY-MM-DD.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: ContentItemsData
domain_of:
- ContentItemsData
range: IsoDay
required: true

```
</details></div>
