---
search:
  boost: 5.0
---

# Slot: wkd_id 


_The person's Wikidata id, where one is known._



<div data-search-exclude markdown="1">



URI: [pc:wkd_id](https://pruzhany.org/ns/sourced-entities#wkd_id)
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



### Annotations

| property | value |
| --- | --- |
| impresso | The Wikidata id of a linked entity mention (wkd_id) in Impresso's entity linking, which Impresso-2 names wkdata_qid (docs/design/2026-10-23-standards-foundation-vetting.md). |




### Schema Source


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:wkd_id |
| native | pc:wkd_id |




## LinkML Source

<details>
```yaml
name: wkd_id
annotations:
  impresso:
    tag: impresso
    value: The Wikidata id of a linked entity mention (wkd_id) in Impresso's entity
      linking, which Impresso-2 names wkdata_qid (docs/design/2026-10-23-standards-foundation-vetting.md).
description: The person's Wikidata id, where one is known.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
owner: IssueMention
domain_of:
- IssueMention
range: string

```
</details></div>
