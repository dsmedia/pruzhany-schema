---
search:
  boost: 2.0
---


# Enum: MediaGrantedBy 




_Who gave the permission to show a medium, by role; never a person's name._



<div data-search-exclude markdown="1">

URI: [pc:MediaGrantedBy](https://pruzhany.org/ns/sourced-entities#MediaGrantedBy)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| owner | None | The owner. |
| family | None | The family. |
| holder | None | The holder. |
| institution | None | An institution. |




## Slots

| Name | Description |
| ---  | --- |
| [granted_by](granted_by.md) | Who gave the permission, by role; never a person's name. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media






## LinkML Source

<details>
```yaml
name: MediaGrantedBy
description: Who gave the permission to show a medium, by role; never a person's name.
from_schema: https://pruzhany.org/ns/media
rank: 1000
permissible_values:
  owner:
    text: owner
    description: The owner.
  family:
    text: family
    description: The family.
  holder:
    text: holder
    description: The holder.
  institution:
    text: institution
    description: An institution.

```
</details>

</div>
