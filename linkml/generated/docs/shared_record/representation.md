---
search:
  boost: 5.0
---

# Slot: representation 


_The form the statement is kept in: structured, prose or an image path._



<div data-search-exclude markdown="1">



URI: [pc:site_fact_representation](https://pruzhany.org/ns/sourced-entities#site_fact_representation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedFact](SharedFact.md) | One source's statement as the shared record keeps it: a fact with its subject, its form and its evidence located on the printed page where the site writer found it. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SharedFactRepresentation](SharedFactRepresentation.md) |
| Domain Of | [SharedFact](SharedFact.md) |
| Slot URI | [pc:site_fact_representation](https://pruzhany.org/ns/sourced-entities#site_fact_representation) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SharedFact](SharedFact.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:site_fact_representation |
| native | pc:representation |




## LinkML Source

<details>
```yaml
name: representation
description: 'The form the statement is kept in: structured, prose or an image path.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
slot_uri: pc:site_fact_representation
owner: SharedFact
domain_of:
- SharedFact
range: SharedFactRepresentation
required: true

```
</details></div>
