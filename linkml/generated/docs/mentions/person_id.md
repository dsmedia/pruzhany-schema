---
search:
  boost: 5.0
---

# Slot: person_id 


_The person named, by their id in the shared record._



<div data-search-exclude markdown="1">



URI: [pc:person_id](https://pruzhany.org/ns/sourced-entities#person_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IssueMention](IssueMention.md) | A person of the shared record named in a content item, pinned to the printed words of the name or to whole regions, with the person's roles there. A mention alone does not say the content item is about the person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [IssueMention](IssueMention.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [IssueMention](IssueMention.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| references | SharedPerson.id |




### Schema Source


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:person_id |
| native | pc:person_id |




## LinkML Source

<details>
```yaml
name: person_id
annotations:
  references:
    tag: references
    value: SharedPerson.id
description: The person named, by their id in the shared record.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
owner: IssueMention
domain_of:
- IssueMention
range: NonBlankText
required: true

```
</details></div>
