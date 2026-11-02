---
search:
  boost: 2.0
---


# Enum: AgeKnownBy 




_How a person's age is known._



<div data-search-exclude markdown="1">

URI: [pc:AgeKnownBy](https://pruzhany.org/ns/sourced-entities#AgeKnownBy)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| birth_year | pc:fates_list_age_birth_year | The person's own records give one year of birth. |
| birth_announced | pc:fates_list_age_birth_announced | The paper announced the person's birth: the person is the baby of a birth the paper printed. |
| birth_years_disagree | pc:fates_list_age_birth_years_disagree | The person's own records give years of birth that disagree, so the age is not known. |




## Slots

| Name | Description |
| ---  | --- |
| [known_by](known_by.md) | How the age is known: one year of birth, a birth the paper announced, or years that disagree. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/fates_list






## LinkML Source

<details>
```yaml
name: AgeKnownBy
description: How a person's age is known.
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
permissible_values:
  birth_year:
    text: birth_year
    description: The person's own records give one year of birth.
    meaning: pc:fates_list_age_birth_year
  birth_announced:
    text: birth_announced
    description: 'The paper announced the person''s birth: the person is the baby
      of a birth the paper printed.'
    meaning: pc:fates_list_age_birth_announced
  birth_years_disagree:
    text: birth_years_disagree
    description: The person's own records give years of birth that disagree, so the
      age is not known.
    meaning: pc:fates_list_age_birth_years_disagree

```
</details>

</div>
