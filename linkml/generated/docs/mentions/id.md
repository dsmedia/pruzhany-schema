---
search:
  boost: 5.0
---

# Slot: id 

<div data-search-exclude markdown="1">



URI: [pc:id](https://pruzhany.org/ns/sourced-entities#id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IssueMention](IssueMention.md) | A person of the shared record named in a content item, pinned to the printed words of the name or to whole regions, with the person's roles there. A mention alone does not say the content item is about the person. |  no  |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |
| [Mention](Mention.md) | The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [IssueMention](IssueMention.md), [Source](Source.md), [Fact](Fact.md), [Mention](Mention.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:id |
| native | pc:id |




## LinkML Source

<details>
```yaml
name: id
domain_of:
- IssueMention
- Source
- Fact
- Mention
range: string

```
</details></div>
