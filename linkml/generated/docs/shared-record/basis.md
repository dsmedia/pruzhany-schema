---
search:
  boost: 5.0
---

# Slot: basis 


_What the permission rests on: an institution's terms, the holder's licence, the family's permission, the public domain, or the owner's family papers._



<div data-search-exclude markdown="1">



URI: [pc:basis](https://pruzhany.org/ns/sourced-entities#basis)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaConsent](MediaConsent.md) | The private record of the permission to show a medium: its basis, who gave it by role, what it covers, the document that holds it and any withdrawal. Never public. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MediaConsent](MediaConsent.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaConsent](MediaConsent.md) |


<details>
<summary>Additional Constraints</summary>
**Must Be One Of:** institution-terms, holder-licence, family-permission, public-domain, owner-family-papers

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:basis |
| native | pc:basis |




## LinkML Source

<details>
```yaml
name: basis
description: 'What the permission rests on: an institution''s terms, the holder''s
  licence, the family''s permission, the public domain, or the owner''s family papers.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: MediaConsent
domain_of:
- MediaConsent
range: string
required: true
equals_string_in:
- institution-terms
- holder-licence
- family-permission
- public-domain
- owner-family-papers

```
</details></div>
