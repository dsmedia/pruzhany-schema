---
search:
  boost: 5.0
---

# Slot: start 


_offset start (relative to ft field)_



<div data-search-exclude markdown="1">



URI: [pc:start](https://pruzhany.org/ns/sourced-entities#start)
Alias: s

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
| impresso | content.ppreb[].t[].s |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:start |
| native | pc:start |




## LinkML Source

<details>
```yaml
name: start
annotations:
  impresso:
    tag: impresso
    value: content.ppreb[].t[].s
description: offset start (relative to ft field)
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
alias: s
owner: ImpressoRebuiltToken
domain_of:
- ImpressoRebuiltToken
range: integer

```
</details></div>
