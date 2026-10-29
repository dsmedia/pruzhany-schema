---
search:
  boost: 5.0
---

# Slot: style 


_Style id in the separate issue file's s list; no style fields are added here._



<div data-search-exclude markdown="1">



URI: [pc:style](https://pruzhany.org/ns/sourced-entities#style)
Alias: s

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalWord](PhysicalWord.md) | One OCR token (a word or word part), with its own box and surface text. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [PhysicalWord](PhysicalWord.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalWord](PhysicalWord.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json r[].p[].l[].t[].s; issue.schema.json s. |
| alto | String/@STYLEREFS after mapping this numeric issue style id to an ALTO Styles ID. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:style |
| native | pc:style |




## LinkML Source

<details>
```yaml
name: style
annotations:
  impresso:
    tag: impresso
    value: page.schema.json r[].p[].l[].t[].s; issue.schema.json s.
  alto:
    tag: alto
    value: String/@STYLEREFS after mapping this numeric issue style id to an ALTO
      Styles ID.
description: Style id in the separate issue file's s list; no style fields are added
  here.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
alias: s
owner: PhysicalWord
domain_of:
- PhysicalWord
range: integer

```
</details></div>
