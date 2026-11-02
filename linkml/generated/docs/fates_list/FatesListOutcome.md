---
search:
  boost: 2.0
---


# Enum: FatesListOutcome 




_The fates the list holds: the shared record's fate outcomes perished and survived._



<div data-search-exclude markdown="1">

URI: [pc:FatesListOutcome](https://pruzhany.org/ns/sourced-entities#FatesListOutcome)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| perished | pc:fate_outcomes_perished | The person perished, as the shared record's fate says. |
| survived | pc:fate_outcomes_survived | The person survived, as the shared record's fate says. |




## Slots

| Name | Description |
| ---  | --- |
| [outcome](outcome.md) | The record's fate: perished or survived. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/fates_list






## LinkML Source

<details>
```yaml
name: FatesListOutcome
description: 'The fates the list holds: the shared record''s fate outcomes perished
  and survived.'
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
permissible_values:
  perished:
    text: perished
    description: The person perished, as the shared record's fate says.
    meaning: pc:fate_outcomes_perished
  survived:
    text: survived
    description: The person survived, as the shared record's fate says.
    meaning: pc:fate_outcomes_survived

```
</details>

</div>
