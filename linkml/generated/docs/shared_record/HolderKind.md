---
search:
  boost: 2.0
---


# Enum: HolderKind 




_What kind of holder keeps a source._



<div data-search-exclude markdown="1">

URI: [pc:HolderKind](https://pruzhany.org/ns/sourced-entities#HolderKind)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| institution | ehri:Institution | An institution, such as an archive or a library. |
| family | ehri:Family | A family holding papers. |
| private | rico:Person | A private person holding papers; the name is never published. |




## Slots

| Name | Description |
| ---  | --- |
| [kind](kind.md) | An institution, a family or a private person. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record






## LinkML Source

<details>
```yaml
name: HolderKind
description: What kind of holder keeps a source.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
permissible_values:
  institution:
    text: institution
    description: An institution, such as an archive or a library.
    meaning: ehri:Institution
  family:
    text: family
    description: A family holding papers.
    meaning: ehri:Family
  private:
    text: private
    description: A private person holding papers; the name is never published.
    meaning: rico:Person

```
</details>

</div>
