---
search:
  boost: 5.0
---

# Slot: part 


_The person's part in the event._



<div data-search-exclude markdown="1">



URI: [pc:part](https://pruzhany.org/ns/sourced-entities#part)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LifeEventMainPerson](LifeEventMainPerson.md) | One main person of a life event and their part in it (the baby, a parent, the bride, the groom, the boy, the one who died, the one remembered); each part means a declared local subproperty of rico:affectsOrAffected or rico:hasOrHadParticipant (EventParts). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EventParts](EventParts.md) |
| Domain Of | [LifeEventMainPerson](LifeEventMainPerson.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [LifeEventMainPerson](LifeEventMainPerson.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:part |
| native | pc:part |




## LinkML Source

<details>
```yaml
name: part
description: The person's part in the event.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: LifeEventMainPerson
domain_of:
- LifeEventMainPerson
range: EventParts
required: true

```
</details></div>
