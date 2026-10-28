---
search:
  boost: 5.0
---

# Slot: life_events 


_The life events the issue prints._



<div data-search-exclude markdown="1">



URI: [pc:life_events](https://pruzhany.org/ns/sourced-entities#life_events)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IssueLifeEventsData](IssueLifeEventsData.md) | One issue's life events document: the issue's date and the life events it prints. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IssueLifeEvent](IssueLifeEvent.md) |
| Domain Of | [IssueLifeEventsData](IssueLifeEventsData.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


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
| self | pc:life_events |
| native | pc:life_events |




## LinkML Source

<details>
```yaml
name: life_events
description: The life events the issue prints.
from_schema: https://pruzhany.org/ns/life_events
rank: 1000
owner: IssueLifeEventsData
domain_of:
- IssueLifeEventsData
range: IssueLifeEvent
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
