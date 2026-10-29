---
search:
  boost: 5.0
---

# Slot: cost_usd 


_The cost in US dollars where kept, including zero. It retains the stored file's accounting scope: English and Latin accumulate calls, and structure may include retries. Do not sum the same file's cost again for every input or interpret it as a measured per-call cost. Omit when unavailable._



<div data-search-exclude markdown="1">



URI: [pc:cost_usd](https://pruzhany.org/ns/sourced-entities#cost_usd)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KeptAsking](KeptAsking.md) | A reference to a kept answer file or an identified input within an accumulated file. Model and prompt metadata can come from a companion trial setting or history; fields absent from storage are not invented. This is not a promise that one file is one paid call. Payloads retain their existing steps formats. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonNegativeNumber](NonNegativeNumber.md) |
| Domain Of | [KeptAsking](KeptAsking.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [KeptAsking](KeptAsking.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/exchanges




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:cost_usd |
| native | pc:cost_usd |




## LinkML Source

<details>
```yaml
name: cost_usd
description: 'The cost in US dollars where kept, including zero. It retains the stored
  file''s accounting scope: English and Latin accumulate calls, and structure may
  include retries. Do not sum the same file''s cost again for every input or interpret
  it as a measured per-call cost. Omit when unavailable.'
from_schema: https://pruzhany.org/ns/exchanges
rank: 1000
owner: KeptAsking
domain_of:
- KeptAsking
range: NonNegativeNumber

```
</details></div>
