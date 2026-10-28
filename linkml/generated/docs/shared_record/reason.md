---
search:
  boost: 5.0
---

# Slot: reason 


_Why: at the family's or the holder's request, or for an error._



<div data-search-exclude markdown="1">



URI: [pc:reason](https://pruzhany.org/ns/sourced-entities#reason)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaWithdrawal](MediaWithdrawal.md) | That a medium was withdrawn from the site, on what day and why; its record stays. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MediaWithdrawalReason](MediaWithdrawalReason.md) |
| Domain Of | [MediaWithdrawal](MediaWithdrawal.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaWithdrawal](MediaWithdrawal.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:reason |
| native | pc:reason |




## LinkML Source

<details>
```yaml
name: reason
description: 'Why: at the family''s or the holder''s request, or for an error.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: MediaWithdrawal
domain_of:
- MediaWithdrawal
range: MediaWithdrawalReason
required: true

```
</details></div>
