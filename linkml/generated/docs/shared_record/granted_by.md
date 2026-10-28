---
search:
  boost: 5.0
---

# Slot: granted_by 


_Who gave the permission, by role; never a person's name._



<div data-search-exclude markdown="1">



URI: [pc:granted_by](https://pruzhany.org/ns/sourced-entities#granted_by)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaConsent](MediaConsent.md) | The private record of the permission to show a medium: its basis, who gave it by role, what it covers, the document that holds it and any withdrawal. Never public. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MediaGrantedBy](MediaGrantedBy.md) |
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
| self | pc:granted_by |
| native | pc:granted_by |




## LinkML Source

<details>
```yaml
name: granted_by
description: Who gave the permission, by role; never a person's name.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: MediaConsent
domain_of:
- MediaConsent
range: MediaGrantedBy
required: true

```
</details></div>
