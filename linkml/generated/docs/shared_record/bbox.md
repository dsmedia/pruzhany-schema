---
search:
  boost: 5.0
---

# Slot: bbox 


_The box on the picture: left, top, width and height, in the picture's pixels._



<div data-search-exclude markdown="1">



URI: [pc:bbox](https://pruzhany.org/ns/sourced-entities#bbox)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PrintedAddress](PrintedAddress.md) | Where some printed words stand: the page picture, a box on it in the picture's own pixels, and the words read in that box. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonNegativeNumber](NonNegativeNumber.md) |
| Domain Of | [PrintedAddress](PrintedAddress.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
| Minimum Cardinality | 4 |
| Maximum Cardinality | 4 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PrintedAddress](PrintedAddress.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:bbox |
| native | pc:bbox |




## LinkML Source

<details>
```yaml
name: bbox
description: 'The box on the picture: left, top, width and height, in the picture''s
  pixels.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: PrintedAddress
domain_of:
- PrintedAddress
range: NonNegativeNumber
required: true
multivalued: true
minimum_cardinality: 4
maximum_cardinality: 4

```
</details></div>
