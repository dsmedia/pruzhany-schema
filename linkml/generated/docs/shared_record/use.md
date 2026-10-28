---
search:
  boost: 5.0
---

# Slot: use 


_The use allowed: shown on the site, or shown and downloaded._



<div data-search-exclude markdown="1">



URI: [pc:use](https://pruzhany.org/ns/sourced-entities#use)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaConsentScope](MediaConsentScope.md) | What a permission covers: the use, the people shown, and whether people not identified are covered. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MediaConsentScope](MediaConsentScope.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaConsentScope](MediaConsentScope.md) |


<details>
<summary>Additional Constraints</summary>
**Must Be One Of:** site, site+download

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:use |
| native | pc:use |




## LinkML Source

<details>
```yaml
name: use
description: 'The use allowed: shown on the site, or shown and downloaded.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: MediaConsentScope
domain_of:
- MediaConsentScope
range: string
required: true
equals_string_in:
- site
- site+download

```
</details></div>
