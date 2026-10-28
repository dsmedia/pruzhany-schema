---
search:
  boost: 5.0
---

# Slot: pages 


_The issue's pages._



<div data-search-exclude markdown="1">



URI: [pc:pages](https://pruzhany.org/ns/sourced-entities#pages)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PagesData](PagesData.md) | One issue's pages document: the issue's date and its pages in order. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Page](Page.md) |
| Domain Of | [PagesData](PagesData.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


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
| self | pc:pages |
| native | pc:pages |




## LinkML Source

<details>
```yaml
name: pages
description: The issue's pages.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
owner: PagesData
domain_of:
- PagesData
range: Page
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
