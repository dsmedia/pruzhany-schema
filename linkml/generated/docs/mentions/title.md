---
search:
  boost: 5.0
---

# Slot: title 


_An honorific printed with the name, such as Rabbi or Dr., where one is kept._



<div data-search-exclude markdown="1">



URI: [pc:title](https://pruzhany.org/ns/sourced-entities#title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IssueMention](IssueMention.md) | A person of the shared record named in a content item, pinned to the printed words of the name or to whole regions, with the person's roles there. A mention alone does not say the content item is about the person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [IssueMention](IssueMention.md) |
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
| self | pc:title |
| native | pc:title |




## LinkML Source

<details>
```yaml
name: title
description: An honorific printed with the name, such as Rabbi or Dr., where one is
  kept.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
owner: IssueMention
domain_of:
- IssueMention
range: string

```
</details></div>
