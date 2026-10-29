---
search:
  boost: 5.0
---

# Slot: prompt_code 


_The associated PromptVersion.code, resolved by steps from the stored prompt code, companion setting or recovered history. English stores the code as prompt and Latin as request. Structure and joining request values include inputs; their association requires recovery, not an assumption that they hash only instructions. A recovered version may retain a whole-request code._



<div data-search-exclude markdown="1">



URI: [pc:prompt_code](https://pruzhany.org/ns/sourced-entities#prompt_code)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KeptAsking](KeptAsking.md) | A reference to a kept answer file or an identified input within an accumulated file. Model and prompt metadata can come from a companion trial setting or history; fields absent from storage are not invented. This is not a promise that one file is one paid call. Payloads retain their existing steps formats. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ExchangeCode](ExchangeCode.md) |
| Domain Of | [KeptAsking](KeptAsking.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [KeptAsking](KeptAsking.md) |










## Comments

* A PROV-O plan link would pass through the asking's qualified association; hadPlan is not a direct Activity property.

## See Also

* [https://www.w3.org/TR/prov-o/#hadPlan](https://www.w3.org/TR/prov-o/#hadPlan)



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| references | PromptVersion.code |




### Schema Source


* from schema: https://pruzhany.org/ns/exchanges




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:prompt_code |
| native | pc:prompt_code |




## LinkML Source

<details>
```yaml
name: prompt_code
annotations:
  references:
    tag: references
    value: PromptVersion.code
description: The associated PromptVersion.code, resolved by steps from the stored
  prompt code, companion setting or recovered history. English stores the code as
  prompt and Latin as request. Structure and joining request values include inputs;
  their association requires recovery, not an assumption that they hash only instructions.
  A recovered version may retain a whole-request code.
comments:
- A PROV-O plan link would pass through the asking's qualified association; hadPlan
  is not a direct Activity property.
from_schema: https://pruzhany.org/ns/exchanges
see_also:
- https://www.w3.org/TR/prov-o/#hadPlan
rank: 1000
owner: KeptAsking
domain_of:
- KeptAsking
range: ExchangeCode
required: true

```
</details></div>
