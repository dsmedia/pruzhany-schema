---
search:
  boost: 5.0
---

# Slot: counts 


_The list's counts, so that a page never counts for itself._



<div data-search-exclude markdown="1">



URI: [pc:counts](https://pruzhany.org/ns/sourced-entities#counts)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesList](FatesList.md) | The fates list: its people, its counts and its notes. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FatesListCounts](FatesListCounts.md) |
| Domain Of | [FatesList](FatesList.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FatesList](FatesList.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/fates_list




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:counts |
| native | pc:counts |




## LinkML Source

<details>
```yaml
name: counts
description: The list's counts, so that a page never counts for itself.
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
owner: FatesList
domain_of:
- FatesList
range: FatesListCounts
required: true
inlined: true

```
</details></div>
