---
search:
  boost: 5.0
---

# Slot: scope 


_What the permission covers._



<div data-search-exclude markdown="1">



URI: [pc:scope](https://pruzhany.org/ns/sourced-entities#scope)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaConsent](MediaConsent.md) | The private record of the permission to show a medium: its basis, who gave it by role, what it covers, the document that holds it and any withdrawal. Never public. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MediaConsentScope](MediaConsentScope.md) |
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


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:scope |
| native | pc:scope |




## LinkML Source

<details>
```yaml
name: scope
description: What the permission covers.
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: MediaConsent
domain_of:
- MediaConsent
range: MediaConsentScope
required: true
inlined: true

```
</details></div>
