---
search:
  boost: 5.0
---

# Slot: length 


_token length_



<div data-search-exclude markdown="1">



URI: [pc:length](https://pruzhany.org/ns/sourced-entities#length)
Alias: l

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
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoRebuiltToken](ImpressoRebuiltToken.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.ppreb[].t[].l |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:length |
| native | pc:length |




## LinkML Source

<details>
```yaml
name: length
annotations:
  impresso:
    tag: impresso
    value: content.ppreb[].t[].l
description: token length
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
alias: l
owner: ImpressoRebuiltToken
domain_of:
- ImpressoRebuiltToken
range: integer

```
</details></div>
