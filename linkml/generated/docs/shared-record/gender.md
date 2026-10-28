---
search:
  boost: 5.0
---

# Slot: gender 


_The person's gender, or unknown._



<div data-search-exclude markdown="1">



URI: [pc:gender](https://pruzhany.org/ns/sourced-entities#gender)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedPerson](SharedPerson.md) | One person of the record, across every issue: their id, the name shown, every name they are known by, their gender, what became of them, and their portrait. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Gender](Gender.md) |
| Domain Of | [SharedPerson](SharedPerson.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SharedPerson](SharedPerson.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:gender |
| native | pc:gender |




## LinkML Source

<details>
```yaml
name: gender
description: The person's gender, or unknown.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: SharedPerson
domain_of:
- SharedPerson
range: Gender
required: true

```
</details></div>
