---
search:
  boost: 5.0
---

# Slot: id 


_The life event, by its id in the shared record._



<div data-search-exclude markdown="1">



URI: [pc:id](https://pruzhany.org/ns/sourced-entities#id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IssueLifeEvent](IssueLifeEvent.md) | A life event of the shared record as this issue prints it: the content items that print it, each with its part. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [IssueLifeEvent](IssueLifeEvent.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [IssueLifeEvent](IssueLifeEvent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/life_events




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:id |
| native | pc:id |




## LinkML Source

<details>
```yaml
name: id
description: The life event, by its id in the shared record.
from_schema: https://pruzhany.org/ns/life_events
rank: 1000
owner: IssueLifeEvent
domain_of:
- IssueLifeEvent
range: NonBlankText
required: true

```
</details></div>
