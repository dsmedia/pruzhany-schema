---
search:
  boost: 5.0
---

# Slot: image_uri 


_The page's picture, by its name or address._



<div data-search-exclude markdown="1">



URI: [pc:image_uri](https://pruzhany.org/ns/sourced-entities#image_uri)
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
| self | pc:image_uri |
| native | pc:image_uri |




## LinkML Source

<details>
```yaml
name: image_uri
description: The page's picture, by its name or address.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
owner: Page
domain_of:
- Page
range: string
required: true

```
</details></div>
