---
search:
  boost: 2.0
---


# Enum: SharedFactRepresentation 




_The form a fact is kept in: a structured statement, retained prose, or an image path._



<div data-search-exclude markdown="1">

URI: [pc:SharedFactRepresentation](https://pruzhany.org/ns/sourced-entities#SharedFactRepresentation)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| structured | None | A structured statement of a released type. |
| prose | None | Retained prose, kept as other with a proposed type until it is reviewed. |
| image | None | An image path, kept as other with a proposed type. |




## Slots

| Name | Description |
| ---  | --- |
| [representation](representation.md) | The form the statement is kept in: structured, prose or an image path. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record






## LinkML Source

<details>
```yaml
name: SharedFactRepresentation
description: 'The form a fact is kept in: a structured statement, retained prose,
  or an image path.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
permissible_values:
  structured:
    text: structured
    description: A structured statement of a released type.
  prose:
    text: prose
    description: Retained prose, kept as other with a proposed type until it is reviewed.
  image:
    text: image
    description: An image path, kept as other with a proposed type.

```
</details>

</div>
