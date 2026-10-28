---
search:
  boost: 2.0
---


# Enum: ClaimStatus 




_Claim status: the values of claim_status in vocabulary/sourced-entities.json, version 1.3.0._



<div data-search-exclude markdown="1">

URI: [pc:ClaimStatus](https://pruzhany.org/ns/sourced-entities#ClaimStatus)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| proposed | pc:claim_status_proposed | An assertion put forward and not yet accepted, disputed or rejected; never published. | Title: Proposed<br>|
| accepted | pc:claim_status_accepted | An assertion retained as accepted; this alone does not authorize publication. | Title: Accepted<br>|
| disputed | pc:claim_status_disputed | An assertion retained with an unresolved challenge. | Title: Disputed<br>|
| rejected | pc:claim_status_rejected | An assertion retained as rejected so it is not silently reintroduced. | Title: Rejected<br>|




## Slots

| Name | Description |
| ---  | --- |
| [status](status.md) | The statement's standing: proposed, accepted, disputed or rejected. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions






## LinkML Source

<details>
```yaml
name: ClaimStatus
description: 'Claim status: the values of claim_status in vocabulary/sourced-entities.json,
  version 1.3.0.'
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
permissible_values:
  proposed:
    text: proposed
    description: An assertion put forward and not yet accepted, disputed or rejected;
      never published.
    meaning: pc:claim_status_proposed
    title: Proposed
    comments:
    - Application-specific claim status category; no exact pinned ontology value is
      established.
  accepted:
    text: accepted
    description: An assertion retained as accepted; this alone does not authorize
      publication.
    meaning: pc:claim_status_accepted
    title: Accepted
    comments:
    - Application-specific claim status category; no exact pinned ontology value is
      established.
  disputed:
    text: disputed
    description: An assertion retained with an unresolved challenge.
    meaning: pc:claim_status_disputed
    title: Disputed
    comments:
    - Application-specific claim status category; no exact pinned ontology value is
      established.
  rejected:
    text: rejected
    description: An assertion retained as rejected so it is not silently reintroduced.
    meaning: pc:claim_status_rejected
    title: Rejected
    comments:
    - Application-specific claim status category; no exact pinned ontology value is
      established.

```
</details>

</div>
