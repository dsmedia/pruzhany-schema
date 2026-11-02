---
search:
  boost: 5.0
---

# Slot: precision 

<div data-search-exclude markdown="1">



URI: [pc:precision](https://pruzhany.org/ns/sourced-entities#precision)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListDate](FatesListDate.md) | A normalized date: its start, how precise it is and, for a range, its end. |  no  |
| [SourcedDate](SourcedDate.md) | A date a source gives: a normalized start (and end, for a range) with how precise it is, or the words as printed with their calendar, or both. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FatesListDate](FatesListDate.md), [SourcedDate](SourcedDate.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:precision |
| native | pc:precision |




## LinkML Source

<details>
```yaml
name: precision
domain_of:
- FatesListDate
- SourcedDate
range: string

```
</details></div>
