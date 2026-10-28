---
search:
  boost: 5.0
---

# Slot: relationship 


_What kind of link it is, in words._



<div data-search-exclude markdown="1">



URI: [pc:relationship](https://pruzhany.org/ns/sourced-entities#relationship)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CrossReference](CrossReference.md) | A link from one content item to another in the same issue, with how sure it is and why. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CrossReference](CrossReference.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CrossReference](CrossReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:relationship |
| native | pc:relationship |




## LinkML Source

<details>
```yaml
name: relationship
description: What kind of link it is, in words.
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
owner: CrossReference
domain_of:
- CrossReference
range: string
required: true

```
</details></div>
