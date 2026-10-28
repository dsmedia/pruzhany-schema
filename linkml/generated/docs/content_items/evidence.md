---
search:
  boost: 5.0
---

# Slot: evidence 


_What shows the link, in words._



<div data-search-exclude markdown="1">



URI: [pc:evidence](https://pruzhany.org/ns/sourced-entities#evidence)
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


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:evidence |
| native | pc:evidence |




## LinkML Source

<details>
```yaml
name: evidence
description: What shows the link, in words.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: CrossReference
domain_of:
- CrossReference
range: string
required: true

```
</details></div>
