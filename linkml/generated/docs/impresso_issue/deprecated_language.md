---
search:
  boost: 5.0
---

# Slot: deprecated_language 


_Language of the content item (deprecated)._



<div data-search-exclude markdown="1">



URI: [pc:deprecated_language](https://pruzhany.org/ns/sourced-entities#deprecated_language)
Alias: l

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoMetadata](ImpressoMetadata.md) | Metadata for an entry in the canonical issue, including its page or audio references. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoMetadata](ImpressoMetadata.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoMetadata](ImpressoMetadata.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.metadata.l |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:deprecated_language |
| native | pc:deprecated_language |




## LinkML Source

<details>
```yaml
name: deprecated_language
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.l
description: Language of the content item (deprecated).
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
alias: l
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: string

```
</details></div>
