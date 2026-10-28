---
search:
  boost: 5.0
---

# Slot: rests_on 


_The facts the outcome rests on, by their ids in the record._



<div data-search-exclude markdown="1">



URI: [pc:rests_on](https://pruzhany.org/ns/sourced-entities#rests_on)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fate](Fate.md) | What became of a person in the Holocaust, as far as the record shows, the facts it rests on and its review. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Fate](Fate.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fate](Fate.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:rests_on |
| native | pc:rests_on |




## LinkML Source

<details>
```yaml
name: rests_on
description: The facts the outcome rests on, by their ids in the record.
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
owner: Fate
domain_of:
- Fate
range: string
required: true
multivalued: true

```
</details></div>
