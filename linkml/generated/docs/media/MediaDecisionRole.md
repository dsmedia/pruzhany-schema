---
search:
  boost: 2.0
---


# Enum: MediaDecisionRole 




_Whose role made a decision about a medium._



<div data-search-exclude markdown="1">

URI: [pc:MediaDecisionRole](https://pruzhany.org/ns/sourced-entities#MediaDecisionRole)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| owner | None | The owner. |
| project | None | The project. |




## Slots

| Name | Description |
| ---  | --- |
| [role](role.md) | Who decided, by role: the owner or the project; never a person's name. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media






## LinkML Source

<details>
```yaml
name: MediaDecisionRole
description: Whose role made a decision about a medium.
from_schema: https://pruzhany.org/ns/media
rank: 1000
permissible_values:
  owner:
    text: owner
    description: The owner.
  project:
    text: project
    description: The project.

```
</details>

</div>
