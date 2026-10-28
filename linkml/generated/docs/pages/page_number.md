---
search:
  boost: 5.0
---

# Slot: page_number 


_The page's number within the issue, from 1._



<div data-search-exclude markdown="1">



URI: [pc:page_number](https://pruzhany.org/ns/sourced-entities#page_number)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Page](Page.md) | One printed page of the issue: its picture, its size and its regions of print. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
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
| self | pc:page_number |
| native | pc:page_number |




## LinkML Source

<details>
```yaml
name: page_number
description: The page's number within the issue, from 1.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
owner: Page
domain_of:
- Page
range: integer
required: true

```
</details></div>
