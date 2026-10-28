---
search:
  boost: 5.0
---

# Slot: wkd_id 


_The person's Wikidata id, where one is linked._



<div data-search-exclude markdown="1">



URI: [pc:wkd_id](https://pruzhany.org/ns/sourced-entities#wkd_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mention](Mention.md) | The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Mention](Mention.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Mention](Mention.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/sourced_entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:wkd_id |
| native | pc:wkd_id |




## LinkML Source

<details>
```yaml
name: wkd_id
description: The person's Wikidata id, where one is linked.
from_schema: https://pruzhany.org/ns/sourced_entities
rank: 1000
owner: Mention
domain_of:
- Mention
range: string

```
</details></div>
