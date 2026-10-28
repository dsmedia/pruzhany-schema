---
search:
  boost: 5.0
---

# Slot: unidentified 


_True when the permission also covers people shown and not identified._



<div data-search-exclude markdown="1">



URI: [pc:unidentified](https://pruzhany.org/ns/sourced-entities#unidentified)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaConsentScope](MediaConsentScope.md) | What a permission covers: the use, the people shown, and whether people not identified are covered. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [MediaConsentScope](MediaConsentScope.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaConsentScope](MediaConsentScope.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:unidentified |
| native | pc:unidentified |




## LinkML Source

<details>
```yaml
name: unidentified
description: True when the permission also covers people shown and not identified.
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: MediaConsentScope
domain_of:
- MediaConsentScope
range: boolean
required: true

```
</details></div>
