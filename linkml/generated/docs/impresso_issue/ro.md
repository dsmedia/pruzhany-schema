---
search:
  boost: 5.0
---

# Slot: ro 


_Reading order index of the content item, for the table of contents view on the interface. If not defined, the CI number (after 'i' in the ID) should be used._



<div data-search-exclude markdown="1">



URI: [pc:ro](https://pruzhany.org/ns/sourced-entities#ro)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoMetadata](ImpressoMetadata.md) | Metadata for an entry in the canonical issue, including its page or audio references. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [ImpressoMetadata](ImpressoMetadata.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoMetadata](ImpressoMetadata.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.metadata.ro |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:ro |
| native | pc:ro |




## LinkML Source

<details>
```yaml
name: ro
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.ro
description: Reading order index of the content item, for the table of contents view
  on the interface. If not defined, the CI number (after 'i' in the ID) should be
  used.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: integer

```
</details></div>
