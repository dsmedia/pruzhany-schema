---
search:
  boost: 5.0
---

# Slot: organizations 


_Every organisation._



<div data-search-exclude markdown="1">



URI: [pc:organizations](https://pruzhany.org/ns/sourced-entities#organizations)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedRecord](SharedRecord.md) | The shared record whole: its version, the vocabulary version it uses, and every person, family, place, organisation, event, source, holder, fact, relation and medium. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SharedOrganization](SharedOrganization.md) |
| Domain Of | [SharedRecord](SharedRecord.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SharedRecord](SharedRecord.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:organizations |
| native | pc:organizations |




## LinkML Source

<details>
```yaml
name: organizations
description: Every organisation.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: SharedRecord
domain_of:
- SharedRecord
range: SharedOrganization
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
