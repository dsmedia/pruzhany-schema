---
search:
  boost: 5.0
---

# Slot: people_with_address 


_The people with at least one of its records at the record's own address._



<div data-search-exclude markdown="1">



URI: [pc:people_with_address](https://pruzhany.org/ns/sourced-entities#people_with_address)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListArchiveCount](FatesListArchiveCount.md) | How many people an archive's database names, and how many of them with an address. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonNegativeInteger](NonNegativeInteger.md) |
| Domain Of | [FatesListArchiveCount](FatesListArchiveCount.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FatesListArchiveCount](FatesListArchiveCount.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/fates_list




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:people_with_address |
| native | pc:people_with_address |




## LinkML Source

<details>
```yaml
name: people_with_address
description: The people with at least one of its records at the record's own address.
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
owner: FatesListArchiveCount
domain_of:
- FatesListArchiveCount
range: NonNegativeInteger
required: true

```
</details></div>
