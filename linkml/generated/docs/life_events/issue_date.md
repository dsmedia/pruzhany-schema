---
search:
  boost: 5.0
---

# Slot: issue_date 


_The issue's date, written YYYY-MM-DD._



<div data-search-exclude markdown="1">



URI: [pc:issue_date](https://pruzhany.org/ns/sourced-entities#issue_date)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IssueLifeEventsData](IssueLifeEventsData.md) | One issue's life events document: the issue's date and the life events it prints. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IsoDay](IsoDay.md) |
| Domain Of | [IssueLifeEventsData](IssueLifeEventsData.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [IssueLifeEventsData](IssueLifeEventsData.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/life_events




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:issue_date |
| native | pc:issue_date |




## LinkML Source

<details>
```yaml
name: issue_date
description: The issue's date, written YYYY-MM-DD.
from_schema: https://pruzhany.org/ns/life_events
rank: 1000
owner: IssueLifeEventsData
domain_of:
- IssueLifeEventsData
range: IsoDay
required: true

```
</details></div>
