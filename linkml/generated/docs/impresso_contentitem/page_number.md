---
search:
  boost: 5.0
---

# Slot: page_number 


_page number_



<div data-search-exclude markdown="1">



URI: [pc:page_number](https://pruzhany.org/ns/sourced-entities#page_number)
Alias: n

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoRebuiltPage](ImpressoRebuiltPage.md) | The rebuilt tokens and region boxes for one physical page of this content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [ImpressoRebuiltPage](ImpressoRebuiltPage.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoRebuiltPage](ImpressoRebuiltPage.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.ppreb[].n |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:page_number |
| native | pc:page_number |




## LinkML Source

<details>
```yaml
name: page_number
annotations:
  impresso:
    tag: impresso
    value: content.ppreb[].n
description: page number
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
alias: n
owner: ImpressoRebuiltPage
domain_of:
- ImpressoRebuiltPage
range: integer

```
</details></div>
