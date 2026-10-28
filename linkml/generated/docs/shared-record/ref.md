---
search:
  boost: 5.0
---

# Slot: ref 


_The private reference of the document that holds the permission._



<div data-search-exclude markdown="1">



URI: [pc:ref](https://pruzhany.org/ns/sourced-entities#ref)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaConsent](MediaConsent.md) | The private record of the permission to show a medium: its basis, who gave it by role, what it covers, the document that holds it and any withdrawal. Never public. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [MediaConsent](MediaConsent.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaConsent](MediaConsent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:ref |
| native | pc:ref |




## LinkML Source

<details>
```yaml
name: ref
description: The private reference of the document that holds the permission.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: MediaConsent
domain_of:
- MediaConsent
range: NonBlankText
required: true

```
</details></div>
