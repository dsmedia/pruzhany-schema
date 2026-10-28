---
search:
  boost: 5.0
---

# Slot: date 

<div data-search-exclude markdown="1">



URI: [pc:date](https://pruzhany.org/ns/sourced-entities#date)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Edition](Edition.md) | One edition of the paper: its date in the common calendar and in the Hebrew one, and the holiday it falls on, if any. |  no  |
| [Holiday](Holiday.md) | A Jewish holiday on a given day. |  no  |
| [HistoricalEvent](HistoricalEvent.md) | An event in the world outside the town, such as Kristallnacht, on a day or over a span of days. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Edition](Edition.md), [Holiday](Holiday.md), [HistoricalEvent](HistoricalEvent.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:date |
| native | pc:date |




## LinkML Source

<details>
```yaml
name: date
domain_of:
- Edition
- Holiday
- HistoricalEvent
range: string

```
</details></div>
