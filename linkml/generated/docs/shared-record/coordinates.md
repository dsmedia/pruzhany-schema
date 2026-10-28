---
search:
  boost: 5.0
---

# Slot: coordinates 


_Where it lies: latitude then longitude, in degrees._



<div data-search-exclude markdown="1">



URI: [rico:geographicalCoordinates](https://www.ica.org/standards/RiC/ontology#geographicalCoordinates)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedPlace](SharedPlace.md) | One place of the record: its names, its kind, the place it lies in, its coordinates and its outside identifiers. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Coordinate](Coordinate.md) |
| Domain Of | [SharedPlace](SharedPlace.md) |
| Slot URI | [rico:geographicalCoordinates](https://www.ica.org/standards/RiC/ontology#geographicalCoordinates) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 2 |
| Maximum Cardinality | 2 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SharedPlace](SharedPlace.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:geographicalCoordinates |
| native | pc:coordinates |




## LinkML Source

<details>
```yaml
name: coordinates
description: 'Where it lies: latitude then longitude, in degrees.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
slot_uri: rico:geographicalCoordinates
owner: SharedPlace
domain_of:
- SharedPlace
range: Coordinate
multivalued: true
minimum_cardinality: 2
maximum_cardinality: 2

```
</details></div>
