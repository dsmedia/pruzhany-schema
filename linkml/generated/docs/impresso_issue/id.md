---
search:
  boost: 5.0
---

# Slot: id 

<div data-search-exclude markdown="1">



URI: [pc:id](https://pruzhany.org/ns/sourced-entities#id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoIssue](ImpressoIssue.md) | Logical representation of the contents of a canonical issue (newspaper or broadcast). |  no  |
| [ImpressoMetadata](ImpressoMetadata.md) | Metadata for an entry in the canonical issue, including its page or audio references. |  no  |
| [ImpressoLegacy](ImpressoLegacy.md) | Legacy sections or components of the content item in the original OCR/OLR. They are meant to enable the reassignation of Impresso CIs (and enrichments) to the original OCR/OLR files. |  no  |
| [ImpressoStyle](ImpressoStyle.md) | One text style from the original OCR, identified locally within the issue. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoIssue](ImpressoIssue.md), [ImpressoMetadata](ImpressoMetadata.md), [ImpressoLegacy](ImpressoLegacy.md), [ImpressoStyle](ImpressoStyle.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:id |
| native | pc:id |




## LinkML Source

<details>
```yaml
name: id
domain_of:
- ImpressoIssue
- ImpressoMetadata
- ImpressoLegacy
- ImpressoStyle
range: string

```
</details></div>
