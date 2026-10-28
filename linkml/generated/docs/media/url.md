---
search:
  boost: 5.0
---

# Slot: url 


_The copy's address, ending in its nominal width (zod/media-widths.json)._



<div data-search-exclude markdown="1">



URI: [pc:url](https://pruzhany.org/ns/sourced-entities#url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaDerivative](MediaDerivative.md) | One served copy of a picture: a WebP file at one of the exported widths, named by the master's digest, made by resizing alone. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MediaDerivative](MediaDerivative.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaDerivative](MediaDerivative.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^https://pictures\.pruzhanychronicles\.org/media/[0-9a-f]{64}-w(?:100|400|800|1200)\.webp$(?![\s\S])` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:url |
| native | pc:url |




## LinkML Source

<details>
```yaml
name: url
description: The copy's address, ending in its nominal width (zod/media-widths.json).
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: MediaDerivative
domain_of:
- MediaDerivative
range: string
required: true
pattern: ^https://pictures\.pruzhanychronicles\.org/media/[0-9a-f]{64}-w(?:100|400|800|1200)\.webp$(?![\s\S])

```
</details></div>
