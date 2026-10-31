---
search:
  boost: 5.0
---

# Slot: regions 


_List of region coordinates._



<div data-search-exclude markdown="1">



URI: [pc:regions](https://pruzhany.org/ns/sourced-entities#regions)
Alias: r

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


<details>
<summary>Advanced Properties</summary>
**Array Configuration:**

- **Dimensions:** DimensionExpression({'minimum_cardinality': 0}) x DimensionExpression({'maximum_cardinality': 4, 'minimum_cardinality': 4})

</details>











## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.ppreb[].r |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:regions |
| native | pc:regions |




## LinkML Source

<details>
```yaml
name: regions
annotations:
  impresso:
    tag: impresso
    value: content.ppreb[].r
description: List of region coordinates.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
alias: r
owner: ImpressoRebuiltPage
domain_of:
- ImpressoRebuiltPage
range: integer
array:
  dimensions:
  - minimum_cardinality: 0
  - maximum_cardinality: 4
    minimum_cardinality: 4

```
</details></div>
