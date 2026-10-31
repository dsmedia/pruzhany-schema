---
search:
  boost: 5.0
---

# Slot: coordinates 


_Coordinates of token relative to page._



<div data-search-exclude markdown="1">



URI: [pc:coordinates](https://pruzhany.org/ns/sourced-entities#coordinates)
Alias: c

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoRebuiltToken](ImpressoRebuiltToken.md) | The rebuilt tokens and region boxes for one physical page of this content item.t[]. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [ImpressoRebuiltToken](ImpressoRebuiltToken.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 4 |
| Maximum Cardinality | 4 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoRebuiltToken](ImpressoRebuiltToken.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.ppreb[].t[].c |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:coordinates |
| native | pc:coordinates |




## LinkML Source

<details>
```yaml
name: coordinates
annotations:
  impresso:
    tag: impresso
    value: content.ppreb[].t[].c
description: Coordinates of token relative to page.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
alias: c
owner: ImpressoRebuiltToken
domain_of:
- ImpressoRebuiltToken
range: integer
multivalued: true
minimum_cardinality: 4
maximum_cardinality: 4

```
</details></div>
