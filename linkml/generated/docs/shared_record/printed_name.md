---
search:
  boost: 5.0
---

# Slot: printed_name 


_The name as printed._



<div data-search-exclude markdown="1">



URI: [pc:printed_name](https://pruzhany.org/ns/sourced-entities#printed_name)
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


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:printed_name |
| native | pc:printed_name |




## LinkML Source

<details>
```yaml
name: printed_name
description: The name as printed.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: Mention
domain_of:
- Mention
range: NonBlankText
required: true

```
</details></div>
