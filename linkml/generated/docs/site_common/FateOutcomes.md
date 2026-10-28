---
search:
  boost: 2.0
---


# Enum: FateOutcomes 




_Fate outcomes: the values of fate_outcomes in vocabulary/sourced-entities.json, version 1.3.0._



<div data-search-exclude markdown="1">

URI: [pc:FateOutcomes](https://pruzhany.org/ns/sourced-entities#FateOutcomes)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| unknown | pc:fate_outcomes_unknown | Compatibility value unknown: preserved unchanged from production fate outcomes. | Title: Unknown<br>|
| perished | pc:fate_outcomes_perished | Compatibility value perished: preserved unchanged from production fate outcomes. How sure the conclusion is lives in the fate's separate confidence; the site's legacy likely_* values are derived from outcome plus confidence. | Title: Perished<br>|
| survived | pc:fate_outcomes_survived | Compatibility value survived: preserved unchanged from production fate outcomes. How sure the conclusion is lives in the fate's separate confidence; the site's legacy likely_* values are derived from outcome plus confidence. | Title: Survived<br>|
| died_before | pc:fate_outcomes_died_before | Compatibility value died_before: preserved unchanged from production fate outcomes. | Title: Died before<br>|
| not_applicable | pc:fate_outcomes_not_applicable | Compatibility value not_applicable: preserved unchanged from production fate outcomes. | Title: Not applicable<br>|




## Slots

| Name | Description |
| ---  | --- |
| [outcome](outcome.md) | What became of the person: unknown, perished, survived, died before, or not applicable. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common






## LinkML Source

<details>
```yaml
name: FateOutcomes
description: 'Fate outcomes: the values of fate_outcomes in vocabulary/sourced-entities.json,
  version 1.3.0.'
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
permissible_values:
  unknown:
    text: unknown
    description: 'Compatibility value unknown: preserved unchanged from production
      fate outcomes.'
    meaning: pc:fate_outcomes_unknown
    title: Unknown
    comments:
    - Application-specific fate outcomes category; no exact pinned ontology value
      is established.
  perished:
    text: perished
    description: 'Compatibility value perished: preserved unchanged from production
      fate outcomes. How sure the conclusion is lives in the fate''s separate confidence;
      the site''s legacy likely_* values are derived from outcome plus confidence.'
    meaning: pc:fate_outcomes_perished
    title: Perished
    comments:
    - Application-specific fate outcomes category; no exact pinned ontology value
      is established.
  survived:
    text: survived
    description: 'Compatibility value survived: preserved unchanged from production
      fate outcomes. How sure the conclusion is lives in the fate''s separate confidence;
      the site''s legacy likely_* values are derived from outcome plus confidence.'
    meaning: pc:fate_outcomes_survived
    title: Survived
    comments:
    - Application-specific fate outcomes category; no exact pinned ontology value
      is established.
  died_before:
    text: died_before
    description: 'Compatibility value died_before: preserved unchanged from production
      fate outcomes.'
    meaning: pc:fate_outcomes_died_before
    title: Died before
    comments:
    - Application-specific fate outcomes category; no exact pinned ontology value
      is established.
  not_applicable:
    text: not_applicable
    description: 'Compatibility value not_applicable: preserved unchanged from production
      fate outcomes.'
    meaning: pc:fate_outcomes_not_applicable
    title: Not applicable
    comments:
    - Application-specific fate outcomes category; no exact pinned ontology value
      is established.

```
</details>

</div>
