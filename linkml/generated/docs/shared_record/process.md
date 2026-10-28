---
search:
  boost: 5.0
---

# Slot: process 


_How the copy was made: resizing alone._



<div data-search-exclude markdown="1">



URI: [pc:process](https://pruzhany.org/ns/sourced-entities#process)
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


<details>
<summary>Additional Constraints</summary>
**Must Equal:** `resize`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:process |
| native | pc:process |




## LinkML Source

<details>
```yaml
name: process
description: 'How the copy was made: resizing alone.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: MediaDerivative
domain_of:
- MediaDerivative
range: string
required: true
equals_string: resize

```
</details></div>
