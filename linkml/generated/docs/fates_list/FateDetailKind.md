---
search:
  boost: 2.0
---


# Enum: FateDetailKind 




_The kind of statement a fate detail comes from: a death, a survival or a deportation._



<div data-search-exclude markdown="1">

URI: [pc:FateDetailKind](https://pruzhany.org/ns/sourced-entities#FateDetailKind)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| death | pc:fates_list_death | The person's death, or the death event it names. |
| survival | pc:fact_types_survival | Evidence that the person was alive at a time and place. |
| deportation | pc:fact_types_deportation | The person's forced removal. |




## Slots

| Name | Description |
| ---  | --- |
| [kind](kind.md) | The kind of statement: death, survival or deportation. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/fates_list






## LinkML Source

<details>
```yaml
name: FateDetailKind
description: 'The kind of statement a fate detail comes from: a death, a survival
  or a deportation.'
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
permissible_values:
  death:
    text: death
    description: The person's death, or the death event it names.
    meaning: pc:fates_list_death
  survival:
    text: survival
    description: Evidence that the person was alive at a time and place.
    meaning: pc:fact_types_survival
  deportation:
    text: deportation
    description: The person's forced removal.
    meaning: pc:fact_types_deportation

```
</details>

</div>
