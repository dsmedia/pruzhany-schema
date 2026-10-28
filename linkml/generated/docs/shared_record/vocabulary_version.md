---
search:
  boost: 5.0
---

# Slot: vocabulary_version 


_The version of the sourced-entities vocabulary the record uses._



<div data-search-exclude markdown="1">



URI: [pc:vocabulary_version](https://pruzhany.org/ns/sourced-entities#vocabulary_version)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedRecord](SharedRecord.md) | The shared record whole: its version, the vocabulary version it uses, and every person, family, place, organisation, event, source, holder, fact, relation and medium. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SharedRecord](SharedRecord.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SharedRecord](SharedRecord.md) |


<details>
<summary>Additional Constraints</summary>
**Must Equal:** `1.3.0`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:vocabulary_version |
| native | pc:vocabulary_version |




## LinkML Source

<details>
```yaml
name: vocabulary_version
description: The version of the sourced-entities vocabulary the record uses.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: SharedRecord
domain_of:
- SharedRecord
range: string
required: true
equals_string: 1.3.0

```
</details></div>
