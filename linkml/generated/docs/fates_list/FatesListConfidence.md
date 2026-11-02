---
search:
  boost: 2.0
---


# Enum: FatesListConfidence 




_How sure the fate is: the shared record's confidences confirmed and probable._



<div data-search-exclude markdown="1">

URI: [pc:FatesListConfidence](https://pruzhany.org/ns/sourced-entities#FatesListConfidence)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| confirmed | pc:confidence_confirmed | The evidence establishes the fate. |
| probable | pc:confidence_probable | The evidence supports the fate with remaining uncertainty. |




## Slots

| Name | Description |
| ---  | --- |
| [confidence](confidence.md) | How sure the fate is: confirmed or probable. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/fates_list






## LinkML Source

<details>
```yaml
name: FatesListConfidence
description: 'How sure the fate is: the shared record''s confidences confirmed and
  probable.'
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
permissible_values:
  confirmed:
    text: confirmed
    description: The evidence establishes the fate.
    meaning: pc:confidence_confirmed
  probable:
    text: probable
    description: The evidence supports the fate with remaining uncertainty.
    meaning: pc:confidence_probable

```
</details>

</div>
