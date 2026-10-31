---
search:
  boost: 5.0
---

# Slot: target_id 


_The id of the content item linked to._



<div data-search-exclude markdown="1">



URI: [pc:target_id](https://pruzhany.org/ns/sourced-entities#target_id)
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


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:target_id |
| native | pc:target_id |




## LinkML Source

<details>
```yaml
name: target_id
description: The id of the content item linked to.
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: CrossReference
domain_of:
- CrossReference
range: string
required: true

```
</details></div>
