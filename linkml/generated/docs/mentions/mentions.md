---
search:
  boost: 5.0
---

# Slot: mentions 


_The issue's mentions._



<div data-search-exclude markdown="1">



URI: [pc:mentions](https://pruzhany.org/ns/sourced-entities#mentions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IssueMentionsData](IssueMentionsData.md) | One issue's mentions document: the issue's date and its mentions. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IssueMention](IssueMention.md) |
| Domain Of | [IssueMentionsData](IssueMentionsData.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [IssueMentionsData](IssueMentionsData.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:mentions |
| native | pc:mentions |




## LinkML Source

<details>
```yaml
name: mentions
description: The issue's mentions.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
owner: IssueMentionsData
domain_of:
- IssueMentionsData
range: IssueMention
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
