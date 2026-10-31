---
search:
  boost: 5.0
---

# Slot: tokens 


_List of tokens_



<div data-search-exclude markdown="1">



URI: [pc:tokens](https://pruzhany.org/ns/sourced-entities#tokens)
Alias: t

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoRebuiltPage](ImpressoRebuiltPage.md) | The rebuilt tokens and region boxes for one physical page of this content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImpressoRebuiltToken](ImpressoRebuiltToken.md) |
| Domain Of | [ImpressoRebuiltPage](ImpressoRebuiltPage.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoRebuiltPage](ImpressoRebuiltPage.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.ppreb[].t |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:tokens |
| native | pc:tokens |




## LinkML Source

<details>
```yaml
name: tokens
annotations:
  impresso:
    tag: impresso
    value: content.ppreb[].t
description: List of tokens
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
alias: t
owner: ImpressoRebuiltPage
domain_of:
- ImpressoRebuiltPage
range: ImpressoRebuiltToken
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
