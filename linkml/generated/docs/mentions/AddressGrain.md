---
search:
  boost: 2.0
---


# Enum: AddressGrain 




_How a mention is pinned to the page: to the words of the printed name, or only to whole regions where the words are not located._



<div data-search-exclude markdown="1">

URI: [pc:AddressGrain](https://pruzhany.org/ns/sourced-entities#AddressGrain)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| words | None | The mention is pinned to the printed name's words. |
| regions | None | The mention is pinned to whole regions of print; its printed name is not located. |




## Slots

| Name | Description |
| ---  | --- |
| [address_grain](address_grain.md) | Whether the mention is pinned to the name's words or only to whole regions. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions






## LinkML Source

<details>
```yaml
name: AddressGrain
description: 'How a mention is pinned to the page: to the words of the printed name,
  or only to whole regions where the words are not located.'
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
permissible_values:
  words:
    text: words
    description: The mention is pinned to the printed name's words.
  regions:
    text: regions
    description: The mention is pinned to whole regions of print; its printed name
      is not located.

```
</details>

</div>
