---
search:
  boost: 5.0
---

# Slot: qualifier 


_reported_in: the day is the first issue's that reported the event, not the day it happened._



<div data-search-exclude markdown="1">



URI: [rico:dateQualifier](https://www.ica.org/standards/RiC/ontology#dateQualifier)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LifeEventDate](LifeEventDate.md) | One date of a life event: the words printed with their calendar, or, where no date is printed, the day of the first issue that reported it, or the preferred record statement's date for a death known from records alone. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [LifeEventDate](LifeEventDate.md) |
| Slot URI | [rico:dateQualifier](https://www.ica.org/standards/RiC/ontology#dateQualifier) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [LifeEventDate](LifeEventDate.md) |


<details>
<summary>Additional Constraints</summary>
**Must Equal:** `reported_in`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:dateQualifier |
| native | pc:qualifier |




## LinkML Source

<details>
```yaml
name: qualifier
description: 'reported_in: the day is the first issue''s that reported the event,
  not the day it happened.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
slot_uri: rico:dateQualifier
owner: LifeEventDate
domain_of:
- LifeEventDate
range: string
equals_string: reported_in

```
</details></div>
