---
search:
  boost: 5.0
---

# Slot: address_grain 


_Whether the mention is pinned to the name's words or only to whole regions._



<div data-search-exclude markdown="1">



URI: [pc:site_mention_address_grain](https://pruzhany.org/ns/sourced-entities#site_mention_address_grain)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IssueMention](IssueMention.md) | A person of the shared record named in a content item, pinned to the printed words of the name or to whole regions, with the person's roles there. A mention alone does not say the content item is about the person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AddressGrain](AddressGrain.md) |
| Domain Of | [IssueMention](IssueMention.md) |
| Slot URI | [pc:site_mention_address_grain](https://pruzhany.org/ns/sourced-entities#site_mention_address_grain) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


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
| self | pc:site_mention_address_grain |
| native | pc:address_grain |




## LinkML Source

<details>
```yaml
name: address_grain
description: Whether the mention is pinned to the name's words or only to whole regions.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
slot_uri: pc:site_mention_address_grain
owner: IssueMention
domain_of:
- IssueMention
range: AddressGrain
required: true

```
</details></div>
