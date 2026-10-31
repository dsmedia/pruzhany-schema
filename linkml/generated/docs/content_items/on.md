---
search:
  boost: 5.0
---

# Slot: on 


_The day it was made or allowed._



<div data-search-exclude markdown="1">



URI: [pc:on](https://pruzhany.org/ns/sourced-entities#on)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Attribution](Attribution.md) | Who made or allowed something, on what day, with an optional note. |  no  |
| [Authorship](Authorship.md) | Who wrote a supplied title, a translation or a check of one, a person or a model, and on which day. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IsoDay](IsoDay.md) |
| Domain Of | [Attribution](Attribution.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Attribution](Attribution.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:on |
| native | pc:on |




## LinkML Source

<details>
```yaml
name: 'on'
description: The day it was made or allowed.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: Attribution
domain_of:
- Attribution
range: IsoDay
required: true

```
</details></div>
