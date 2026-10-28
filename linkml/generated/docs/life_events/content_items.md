---
search:
  boost: 5.0
---

# Slot: content_items 


_The content items of the issue that print the event._



<div data-search-exclude markdown="1">



URI: [pc:content_items](https://pruzhany.org/ns/sourced-entities#content_items)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IssueLifeEvent](IssueLifeEvent.md) | A life event of the shared record as this issue prints it: the content items that print it, each with its part. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ContentItemRef](ContentItemRef.md) |
| Domain Of | [IssueLifeEvent](IssueLifeEvent.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
| Minimum Cardinality | 1 |


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
| self | pc:content_items |
| native | pc:content_items |




## LinkML Source

<details>
```yaml
name: content_items
description: The content items of the issue that print the event.
from_schema: https://pruzhany.org/ns/life_events
rank: 1000
owner: IssueLifeEvent
domain_of:
- IssueLifeEvent
range: ContentItemRef
required: true
multivalued: true
inlined: true
inlined_as_list: true
minimum_cardinality: 1

```
</details></div>
