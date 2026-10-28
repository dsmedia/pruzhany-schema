---
search:
  boost: 5.0
---

# Slot: source 


_The database or resource, by name, such as yad_vashem or jri_poland._



<div data-search-exclude markdown="1">



URI: [pc:source](https://pruzhany.org/ns/sourced-entities#source)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExternalReference](ExternalReference.md) | A reference to a record in an outside database or resource, such as a page of testimony at Yad Vashem. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ExternalReference](ExternalReference.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ExternalReference](ExternalReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:source |
| native | pc:source |




## LinkML Source

<details>
```yaml
name: source
description: The database or resource, by name, such as yad_vashem or jri_poland.
from_schema: https://pruzhany.org/ns/shared
rank: 1000
owner: ExternalReference
domain_of:
- ExternalReference
range: string
required: true

```
</details></div>
