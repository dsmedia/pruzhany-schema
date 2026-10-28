---
search:
  boost: 2.0
---


# Enum: ReviewStates 




_Review states: the values of review_states in vocabulary/sourced-entities.json, version 1.3.0._



<div data-search-exclude markdown="1">

URI: [pc:ReviewStates](https://pruzhany.org/ns/sourced-entities#ReviewStates)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| pending | pc:review_states_pending | Awaiting human editorial approval. | Title: Pending<br>|
| approved | pc:review_states_approved | Human editorial review has approved the item; publication remains subject to downstream privacy rules. | Title: Approved<br>|













## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/life_events






## LinkML Source

<details>
```yaml
name: ReviewStates
description: 'Review states: the values of review_states in vocabulary/sourced-entities.json,
  version 1.3.0.'
from_schema: https://pruzhany.org/ns/life_events
rank: 1000
permissible_values:
  pending:
    text: pending
    description: Awaiting human editorial approval.
    meaning: pc:review_states_pending
    title: Pending
    comments:
    - Application-specific review states category; no exact pinned ontology value
      is established.
  approved:
    text: approved
    description: Human editorial review has approved the item; publication remains
      subject to downstream privacy rules.
    meaning: pc:review_states_approved
    title: Approved
    comments:
    - Application-specific review states category; no exact pinned ontology value
      is established.

```
</details>

</div>
