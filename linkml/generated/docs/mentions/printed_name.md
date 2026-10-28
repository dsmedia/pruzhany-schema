---
search:
  boost: 5.0
---

# Slot: printed_name 

<div data-search-exclude markdown="1">



URI: [pc:printed_name](https://pruzhany.org/ns/sourced-entities#printed_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IssueMention](IssueMention.md) | A person of the shared record named in a content item, pinned to the printed words of the name or to whole regions, with the person's roles there. A mention alone does not say the content item is about the person. |  no  |
| [Mention](Mention.md) | The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [IssueMention](IssueMention.md), [Mention](Mention.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:printed_name |
| native | pc:printed_name |




## LinkML Source

<details>
```yaml
name: printed_name
domain_of:
- IssueMention
- Mention
range: string

```
</details></div>
