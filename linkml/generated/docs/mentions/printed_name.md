---
search:
  boost: 5.0
---

# Slot: printed_name 


_The name as printed, found at the mention's addresses; null when the mention is pinned only to whole regions._



<div data-search-exclude markdown="1">



URI: [pc:printed_name](https://pruzhany.org/ns/sourced-entities#printed_name)
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
| self | pc:printed_name |
| native | pc:printed_name |




## LinkML Source

<details>
```yaml
name: printed_name
description: The name as printed, found at the mention's addresses; null when the
  mention is pinned only to whole regions.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
owner: IssueMention
domain_of:
- IssueMention
range: NonBlankText

```
</details></div>
