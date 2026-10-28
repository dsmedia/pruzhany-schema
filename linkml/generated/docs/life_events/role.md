---
search:
  boost: 5.0
---

# Slot: role 


_The part the content item plays for the event, not any person's role._



<div data-search-exclude markdown="1">



URI: [pc:role](https://pruzhany.org/ns/sourced-entities#role)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItemRef](ContentItemRef.md) | A content item that prints a life event, and the part it plays: the announcement itself, a greeting, a condolence, a mention or an advertisement. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ContentUnitRoles](ContentUnitRoles.md) |
| Domain Of | [ContentItemRef](ContentItemRef.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ContentItemRef](ContentItemRef.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/life_events




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:role |
| native | pc:role |




## LinkML Source

<details>
```yaml
name: role
description: The part the content item plays for the event, not any person's role.
from_schema: https://pruzhany.org/ns/life_events
rank: 1000
owner: ContentItemRef
domain_of:
- ContentItemRef
range: ContentUnitRoles
required: true

```
</details></div>
