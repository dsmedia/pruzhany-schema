---
search:
  boost: 5.0
---

# Slot: edition_date 


_The issue's date, written YYYY-MM-DD._



<div data-search-exclude markdown="1">



URI: [pc:edition_date](https://pruzhany.org/ns/sourced-entities#edition_date)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PagesData](PagesData.md) | One issue's pages document: the issue's date and its pages in order. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PagesData](PagesData.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PagesData](PagesData.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/pages




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:edition_date |
| native | pc:edition_date |




## LinkML Source

<details>
```yaml
name: edition_date
description: The issue's date, written YYYY-MM-DD.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
owner: PagesData
domain_of:
- PagesData
range: string
required: true

```
</details></div>
