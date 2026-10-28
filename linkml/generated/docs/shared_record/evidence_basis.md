---
search:
  boost: 5.0
---

# Slot: evidence_basis 


_records_only: a death known from records alone, which no issue prints._



<div data-search-exclude markdown="1">



URI: [pc:site_event_evidence_basis](https://pruzhany.org/ns/sourced-entities#site_event_evidence_basis)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedEvent](SharedEvent.md) | One life event, once for each happening across every issue (a birth, a wedding, a death, a memorial and so on): its kind, its main people and their parts, its dates and its place. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SharedEvent](SharedEvent.md) |
| Slot URI | [pc:site_event_evidence_basis](https://pruzhany.org/ns/sourced-entities#site_event_evidence_basis) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SharedEvent](SharedEvent.md) |


<details>
<summary>Additional Constraints</summary>
**Must Equal:** `records_only`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:site_event_evidence_basis |
| native | pc:evidence_basis |




## LinkML Source

<details>
```yaml
name: evidence_basis
description: 'records_only: a death known from records alone, which no issue prints.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
slot_uri: pc:site_event_evidence_basis
owner: SharedEvent
domain_of:
- SharedEvent
range: string
equals_string: records_only

```
</details></div>
