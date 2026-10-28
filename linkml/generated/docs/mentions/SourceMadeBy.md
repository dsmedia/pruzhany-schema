---
search:
  boost: 2.0
---


# Enum: SourceMadeBy 




_Who made a source, as a category: never an agent, so never its creator._



<div data-search-exclude markdown="1">

URI: [pc:SourceMadeBy](https://pruzhany.org/ns/sourced-entities#SourceMadeBy)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| family | None | The family. |
| studio | None | A photographer's studio. |
| institution | None | An institution. |
| perpetrator | None | The perpetrators. |
| unknown | None | Not known. |




## Slots

| Name | Description |
| ---  | --- |
| [made_by](made_by.md) | Who made the source, as a category (family, studio, institution, perpetrator, unknown); never its creator. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions






## LinkML Source

<details>
```yaml
name: SourceMadeBy
description: 'Who made a source, as a category: never an agent, so never its creator.'
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
permissible_values:
  family:
    text: family
    description: The family.
  studio:
    text: studio
    description: A photographer's studio.
  institution:
    text: institution
    description: An institution.
  perpetrator:
    text: perpetrator
    description: The perpetrators.
  unknown:
    text: unknown
    description: Not known.

```
</details>

</div>
