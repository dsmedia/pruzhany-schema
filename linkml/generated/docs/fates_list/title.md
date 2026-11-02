---
search:
  boost: 5.0
---

# Slot: title 

<div data-search-exclude markdown="1">



URI: [pc:title](https://pruzhany.org/ns/sourced-entities#title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |
| [Mention](Mention.md) | The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Source](Source.md), [Mention](Mention.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:title |
| native | pc:title |




## LinkML Source

<details>
```yaml
name: title
domain_of:
- Source
- Mention
range: string

```
</details></div>
