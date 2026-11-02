---
search:
  boost: 5.0
---

# Slot: collection 


_The database's title, as the shared record's source gives it._



<div data-search-exclude markdown="1">



URI: [pc:collection](https://pruzhany.org/ns/sourced-entities#collection)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListOutsideRecord](FatesListOutsideRecord.md) | A record an archive holds about the person: the archive, the database it is in, the record's type and id as the archive gives them, and its own address where the record has one. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [FatesListOutsideRecord](FatesListOutsideRecord.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FatesListOutsideRecord](FatesListOutsideRecord.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/fates_list




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:collection |
| native | pc:collection |




## LinkML Source

<details>
```yaml
name: collection
description: The database's title, as the shared record's source gives it.
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
owner: FatesListOutsideRecord
domain_of:
- FatesListOutsideRecord
range: NonBlankText
required: true

```
</details></div>
