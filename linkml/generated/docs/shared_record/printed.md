---
search:
  boost: 5.0
---

# Slot: printed 

<div data-search-exclude markdown="1">



URI: [pc:printed](https://pruzhany.org/ns/sourced-entities#printed)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LifeEventDate](LifeEventDate.md) | One date of a life event: the words printed with their calendar, or, where no date is printed, the day of the first issue that reported it, or the preferred record statement's date for a death known from records alone. |  no  |
| [SourcedDate](SourcedDate.md) | A date a source gives: a normalized start (and end, for a range) with how precise it is, or the words as printed with their calendar, or both. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [LifeEventDate](LifeEventDate.md), [SourcedDate](SourcedDate.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:printed |
| native | pc:printed |




## LinkML Source

<details>
```yaml
name: printed
domain_of:
- LifeEventDate
- SourcedDate
range: string

```
</details></div>
