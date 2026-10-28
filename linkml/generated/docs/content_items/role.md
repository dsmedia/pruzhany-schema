---
search:
  boost: 5.0
---

# Slot: role 


_The person's role in the piece._



<div data-search-exclude markdown="1">



URI: [pc:role](https://pruzhany.org/ns/sourced-entities#role)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mention](Mention.md) | The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MentionRoles](MentionRoles.md) |
| Domain Of | [Mention](Mention.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Mention](Mention.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:role |
| native | pc:role |




## LinkML Source

<details>
```yaml
name: role
description: The person's role in the piece.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: Mention
domain_of:
- Mention
range: MentionRoles

```
</details></div>
