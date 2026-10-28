---
search:
  boost: 5.0
---

# Slot: main_people 


_The people the event is about, each with their part; empty while unresolved._



<div data-search-exclude markdown="1">



URI: [rico:hasOrHadParticipant](https://www.ica.org/standards/RiC/ontology#hasOrHadParticipant)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedEvent](SharedEvent.md) | One life event, once for each happening across every issue (a birth, a wedding, a death, a memorial and so on): its kind, its main people and their parts, its dates and its place. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LifeEventMainPerson](LifeEventMainPerson.md) |
| Domain Of | [SharedEvent](SharedEvent.md) |
| Slot URI | [rico:hasOrHadParticipant](https://www.ica.org/standards/RiC/ontology#hasOrHadParticipant) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SharedEvent](SharedEvent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:hasOrHadParticipant |
| native | pc:main_people |




## LinkML Source

<details>
```yaml
name: main_people
description: The people the event is about, each with their part; empty while unresolved.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
slot_uri: rico:hasOrHadParticipant
owner: SharedEvent
domain_of:
- SharedEvent
range: LifeEventMainPerson
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
