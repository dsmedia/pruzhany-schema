---
search:
  boost: 2.0
---


# Enum: AuthorshipKind 




_Whether a person or a program wrote a supplied title or a translation._



<div data-search-exclude markdown="1">

URI: [pc:AuthorshipKind](https://pruzhany.org/ns/sourced-entities#AuthorshipKind)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| person | None | A person wrote it. |
| model | None | A language model wrote it. |




## Slots

| Name | Description |
| ---  | --- |
| [kind](kind.md) | Whether a person or a model wrote it. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions






## LinkML Source

<details>
```yaml
name: AuthorshipKind
description: Whether a person or a program wrote a supplied title or a translation.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
permissible_values:
  person:
    text: person
    description: A person wrote it.
  model:
    text: model
    description: A language model wrote it.

```
</details>

</div>
