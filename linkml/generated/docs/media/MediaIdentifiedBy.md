---
search:
  boost: 2.0
---


# Enum: MediaIdentifiedBy 




_What identifies a person shown in a picture._



<div data-search-exclude markdown="1">

URI: [pc:MediaIdentifiedBy](https://pruzhany.org/ns/sourced-entities#MediaIdentifiedBy)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| family | None | The family. |
| record | None | A record. |
| inscription | None | The picture's own inscription. |




## Slots

| Name | Description |
| ---  | --- |
| [identified_by](identified_by.md) | What identifies the person: the family, a record, or the picture's inscription. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media






## LinkML Source

<details>
```yaml
name: MediaIdentifiedBy
description: What identifies a person shown in a picture.
from_schema: https://pruzhany.org/ns/media
rank: 1000
permissible_values:
  family:
    text: family
    description: The family.
  record:
    text: record
    description: A record.
  inscription:
    text: inscription
    description: The picture's own inscription.

```
</details>

</div>
