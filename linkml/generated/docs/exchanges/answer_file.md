---
search:
  boost: 5.0
---

# Slot: answer_file 


_The kept answer's file path relative to the steps repository. The path locates an existing payload; it is not that payload or a public download URI._



<div data-search-exclude markdown="1">



URI: [pc:answer_file](https://pruzhany.org/ns/sourced-entities#answer_file)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KeptAsking](KeptAsking.md) | A reference to a kept answer file or an identified input within an accumulated file. Model and prompt metadata can come from a companion trial setting or history; fields absent from storage are not invented. This is not a promise that one file is one paid call. Payloads retain their existing steps formats. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [KeptAsking](KeptAsking.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [KeptAsking](KeptAsking.md) |










## See Also

* [https://www.w3.org/TR/prov-o/#generated](https://www.w3.org/TR/prov-o/#generated)



## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/exchanges




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:answer_file |
| native | pc:answer_file |




## LinkML Source

<details>
```yaml
name: answer_file
description: The kept answer's file path relative to the steps repository. The path
  locates an existing payload; it is not that payload or a public download URI.
from_schema: https://pruzhany.org/ns/exchanges
see_also:
- https://www.w3.org/TR/prov-o/#generated
rank: 1000
owner: KeptAsking
domain_of:
- KeptAsking
range: NonBlankText
required: true

```
</details></div>
