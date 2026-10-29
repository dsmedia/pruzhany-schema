---
search:
  boost: 5.0
---

# Slot: day 


_An asking day where actually kept: English answered_on for the indexed input or the trial directory's day. Omit when unknown; a first committed day is not an observed asking day and must not be silently substituted._



<div data-search-exclude markdown="1">



URI: [pc:day](https://pruzhany.org/ns/sourced-entities#day)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KeptAsking](KeptAsking.md) | A reference to a kept answer file or an identified input within an accumulated file. Model and prompt metadata can come from a companion trial setting or history; fields absent from storage are not invented. This is not a promise that one file is one paid call. Payloads retain their existing steps formats. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ExchangeDay](ExchangeDay.md) |
| Domain Of | [KeptAsking](KeptAsking.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [KeptAsking](KeptAsking.md) |










## Comments

* This day has less precision than the PROV-O timestamp property.

## See Also

* [https://www.w3.org/TR/prov-o/#endedAtTime](https://www.w3.org/TR/prov-o/#endedAtTime)



## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/exchanges




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:day |
| native | pc:day |




## LinkML Source

<details>
```yaml
name: day
description: 'An asking day where actually kept: English answered_on for the indexed
  input or the trial directory''s day. Omit when unknown; a first committed day is
  not an observed asking day and must not be silently substituted.'
comments:
- This day has less precision than the PROV-O timestamp property.
from_schema: https://pruzhany.org/ns/exchanges
see_also:
- https://www.w3.org/TR/prov-o/#endedAtTime
rank: 1000
owner: KeptAsking
domain_of:
- KeptAsking
range: ExchangeDay

```
</details></div>
