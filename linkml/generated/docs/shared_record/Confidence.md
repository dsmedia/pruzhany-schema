---
search:
  boost: 2.0
---


# Enum: Confidence 




_Confidence: the values of confidence in vocabulary/sourced-entities.json, version 1.3.0._



<div data-search-exclude markdown="1">

URI: [pc:Confidence](https://pruzhany.org/ns/sourced-entities#Confidence)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| confirmed | pc:confidence_confirmed | The cited evidence directly supports the assertion at the confirmed level; separate from identity confidence and editorial approval. | Title: Confirmed<br>|
| probable | pc:confidence_probable | The evidence supports the assertion with remaining uncertainty. | Title: Probable<br>|
| possible | pc:confidence_possible | The evidence permits the assertion but does not establish it as probable. | Title: Possible<br>|




## Slots

| Name | Description |
| ---  | --- |
| [evidence_confidence](evidence_confidence.md) | How sure the evidence makes the statement. |
| [identity_confidence](identity_confidence.md) | How sure it is that the statement is about this person. |
| [confidence](confidence.md) | How sure the outcome is. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record






## LinkML Source

<details>
```yaml
name: Confidence
description: 'Confidence: the values of confidence in vocabulary/sourced-entities.json,
  version 1.3.0.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
permissible_values:
  confirmed:
    text: confirmed
    description: The cited evidence directly supports the assertion at the confirmed
      level; separate from identity confidence and editorial approval.
    meaning: pc:confidence_confirmed
    title: Confirmed
    comments:
    - Application-specific confidence category; no exact pinned ontology value is
      established.
  probable:
    text: probable
    description: The evidence supports the assertion with remaining uncertainty.
    meaning: pc:confidence_probable
    title: Probable
    comments:
    - Application-specific confidence category; no exact pinned ontology value is
      established.
  possible:
    text: possible
    description: The evidence permits the assertion but does not establish it as probable.
    meaning: pc:confidence_possible
    title: Possible
    comments:
    - Application-specific confidence category; no exact pinned ontology value is
      established.

```
</details>

</div>
