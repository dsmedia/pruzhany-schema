---
search:
  boost: 5.0
---

# Slot: child 


_True for a child: one year of birth of 1925 or later, or a birth the paper announced._



<div data-search-exclude markdown="1">



URI: [pc:fates_list_child](https://pruzhany.org/ns/sourced-entities#fates_list_child)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListAge](FatesListAge.md) | How a person's age is known, and whether it marks a child. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [FatesListAge](FatesListAge.md) |
| Slot URI | [pc:fates_list_child](https://pruzhany.org/ns/sourced-entities#fates_list_child) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FatesListAge](FatesListAge.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/fates_list




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:fates_list_child |
| native | pc:child |




## LinkML Source

<details>
```yaml
name: child
description: 'True for a child: one year of birth of 1925 or later, or a birth the
  paper announced.'
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
slot_uri: pc:fates_list_child
owner: FatesListAge
domain_of:
- FatesListAge
range: boolean
required: true

```
</details></div>
