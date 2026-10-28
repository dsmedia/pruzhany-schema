---
search:
  boost: 5.0
---

# Slot: roles 


_The person's roles in the content item, such as the deceased or a mourner._



<div data-search-exclude markdown="1">



URI: [pc:roles](https://pruzhany.org/ns/sourced-entities#roles)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IssueMention](IssueMention.md) | A person of the shared record named in a content item, pinned to the printed words of the name or to whole regions, with the person's roles there. A mention alone does not say the content item is about the person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MentionRoles](MentionRoles.md) |
| Domain Of | [IssueMention](IssueMention.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
| Minimum Cardinality | 1 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [IssueMention](IssueMention.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:roles |
| native | pc:roles |




## LinkML Source

<details>
```yaml
name: roles
description: The person's roles in the content item, such as the deceased or a mourner.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
owner: IssueMention
domain_of:
- IssueMention
range: MentionRoles
required: true
multivalued: true
minimum_cardinality: 1

```
</details></div>
