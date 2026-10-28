---
search:
  boost: 5.0
---

# Slot: on 

<div data-search-exclude markdown="1">



URI: [pc:on](https://pruzhany.org/ns/sourced-entities#on)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Review](Review.md) | Whether a person has reviewed a statement, who and on what day. |  no  |
| [Attribution](Attribution.md) | Who made or allowed something, on what day, with an optional note. |  no  |
| [MediaDecision](MediaDecision.md) | A review or a clearance: whose role made it (the owner or the project) and on what day. |  no  |
| [MediaWithdrawal](MediaWithdrawal.md) | That a medium was withdrawn from the site, on what day and why; its record stays. |  no  |
| [MediaFixity](MediaFixity.md) | A dated check that a master file still has its digest. |  no  |
| [Authorship](Authorship.md) | Who wrote a supplied title, a translation or a check of one, a person or a model, and on which day. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Review](Review.md), [Attribution](Attribution.md), [MediaDecision](MediaDecision.md), [MediaWithdrawal](MediaWithdrawal.md), [MediaFixity](MediaFixity.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:on |
| native | pc:on |




## LinkML Source

<details>
```yaml
name: 'on'
domain_of:
- Review
- Attribution
- MediaDecision
- MediaWithdrawal
- MediaFixity
range: string

```
</details></div>
