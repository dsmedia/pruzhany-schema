---
search:
  boost: 5.0
---

# Slot: function 


_The person's occupation or part in the content item, in a few words, such as bride, mourner or well-wisher._



<div data-search-exclude markdown="1">



URI: [pc:function](https://pruzhany.org/ns/sourced-entities#function)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IssueMention](IssueMention.md) | A person of the shared record named in a content item, pinned to the printed words of the name or to whole regions, with the person's roles there. A mention alone does not say the content item is about the person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [IssueMention](IssueMention.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [IssueMention](IssueMention.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:function |
| native | pc:function |




## LinkML Source

<details>
```yaml
name: function
description: The person's occupation or part in the content item, in a few words,
  such as bride, mourner or well-wisher.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
owner: IssueMention
domain_of:
- IssueMention
range: string

```
</details></div>
