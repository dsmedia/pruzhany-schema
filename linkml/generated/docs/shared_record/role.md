---
search:
  boost: 5.0
---

# Slot: role 

<div data-search-exclude markdown="1">



URI: [pc:role](https://pruzhany.org/ns/sourced-entities#role)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mention](Mention.md) | The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention. |  no  |
| [MediaDecision](MediaDecision.md) | A review or a clearance: whose role made it (the owner or the project) and on what day. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Mention](Mention.md), [MediaDecision](MediaDecision.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:role |
| native | pc:role |




## LinkML Source

<details>
```yaml
name: role
domain_of:
- Mention
- MediaDecision
range: string

```
</details></div>
