---
search:
  boost: 2.0
---


# Enum: SourceQuoteCondition 




_The owner's condition on a private source's cleared quotes._



<div data-search-exclude markdown="1">

URI: [pc:SourceQuoteCondition](https://pruzhany.org/ns/sourced-entities#SourceQuoteCondition)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| unique_information | None | A quote is shown only where no other record states the same (the owner's word of 24 October 2026). |




## Slots

| Name | Description |
| ---  | --- |
| [quote_condition](quote_condition.md) | The owner's condition on the cleared quotes: shown only where no other record says the same. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions






## LinkML Source

<details>
```yaml
name: SourceQuoteCondition
description: The owner's condition on a private source's cleared quotes.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
permissible_values:
  unique_information:
    text: unique_information
    description: A quote is shown only where no other record states the same (the
      owner's word of 24 October 2026).

```
</details>

</div>
