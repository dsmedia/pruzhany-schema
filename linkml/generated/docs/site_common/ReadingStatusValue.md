---
search:
  boost: 2.0
---


# Enum: ReadingStatusValue 




_Reading states: the values of a content item's reading_status, from vocabulary/reading-status.json, whose entry reading_status describes the field: Optional per-field reading provenance. Null is unrecorded. A session check may cover particular words only._



<div data-search-exclude markdown="1">

URI: [pc:ReadingStatusValue](https://pruzhany.org/ns/sourced-entities#ReadingStatusValue)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| machine | pc:site_reading_machine | A machine reading without a recorded qualifying check. |
| session_checked | pc:site_reading_session_checked | An AI session checked or corrected the field, possibly particular words only. |
| person_corrected | pc:site_reading_person_corrected | A recorded human author corrected the field; AI drafts and approvals alone do not qualify. |













## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common






## LinkML Source

<details>
```yaml
name: ReadingStatusValue
description: 'Reading states: the values of a content item''s reading_status, from
  vocabulary/reading-status.json, whose entry reading_status describes the field:
  Optional per-field reading provenance. Null is unrecorded. A session check may cover
  particular words only.'
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
permissible_values:
  machine:
    text: machine
    description: A machine reading without a recorded qualifying check.
    meaning: pc:site_reading_machine
    comments:
    - Application-specific reading provenance state, not a state defined in either
      pinned ontology.
  session_checked:
    text: session_checked
    description: An AI session checked or corrected the field, possibly particular
      words only.
    meaning: pc:site_reading_session_checked
    comments:
    - Application-specific reading provenance state, not a state defined in either
      pinned ontology.
  person_corrected:
    text: person_corrected
    description: A recorded human author corrected the field; AI drafts and approvals
      alone do not qualify.
    meaning: pc:site_reading_person_corrected
    comments:
    - Application-specific reading provenance state, not a state defined in either
      pinned ontology.

```
</details>

</div>
