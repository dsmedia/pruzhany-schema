---
search:
  boost: 5.0
---

# Slot: person_id 


_The person mentioned, by the person's id._



<div data-search-exclude markdown="1">



URI: [pc:person_id](https://pruzhany.org/ns/sourced-entities#person_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mention](Mention.md) | The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [Mention](Mention.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Mention](Mention.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:person_id |
| native | pc:person_id |




## LinkML Source

<details>
```yaml
name: person_id
description: The person mentioned, by the person's id.
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
owner: Mention
domain_of:
- Mention
range: NonBlankText
required: true

```
</details></div>
