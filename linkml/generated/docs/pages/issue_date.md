---
search:
  boost: 5.0
---

# Slot: issue_date 


_The date of the issue the page belongs to, written YYYY-MM-DD._



<div data-search-exclude markdown="1">



URI: [pc:issue_date](https://pruzhany.org/ns/sourced-entities#issue_date)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Page](Page.md) | One printed page of the issue: its picture, its size and its regions of print. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Page](Page.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Page](Page.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/pages




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:issue_date |
| native | pc:issue_date |




## LinkML Source

<details>
```yaml
name: issue_date
description: The date of the issue the page belongs to, written YYYY-MM-DD.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
owner: Page
domain_of:
- Page
range: string
required: true

```
</details></div>
