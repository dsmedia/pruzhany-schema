---
search:
  boost: 5.0
---

# Slot: withdrawn_on 


_The day the permission was withdrawn._



<div data-search-exclude markdown="1">



URI: [pc:withdrawn_on](https://pruzhany.org/ns/sourced-entities#withdrawn_on)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaConsent](MediaConsent.md) | The private record of the permission to show a medium: its basis, who gave it by role, what it covers, the document that holds it and any withdrawal. Never public. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IsoDay](IsoDay.md) |
| Domain Of | [MediaConsent](MediaConsent.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaConsent](MediaConsent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:withdrawn_on |
| native | pc:withdrawn_on |




## LinkML Source

<details>
```yaml
name: withdrawn_on
description: The day the permission was withdrawn.
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: MediaConsent
domain_of:
- MediaConsent
range: IsoDay

```
</details></div>
