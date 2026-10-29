---
search:
  boost: 5.0
---

# Slot: input_fingerprint 


_An input fingerprint where kept: English pieces keys are xxh3_64 text digests; structure and joining request values are truncated SHA-256 fingerprints of whole requests. Structure trials also keep request and sent fingerprints with different scopes; an index must choose and document its input scope. Latin request is a prompt code, not an input fingerprint. Omit when no input fingerprint was kept, including trial rows._



<div data-search-exclude markdown="1">



URI: [pc:input_fingerprint](https://pruzhany.org/ns/sourced-entities#input_fingerprint)
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
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [KeptAsking](KeptAsking.md) |










## See Also

* [https://www.w3.org/TR/prov-o/#used](https://www.w3.org/TR/prov-o/#used)



## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/exchanges




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:input_fingerprint |
| native | pc:input_fingerprint |




## LinkML Source

<details>
```yaml
name: input_fingerprint
description: 'An input fingerprint where kept: English pieces keys are xxh3_64 text
  digests; structure and joining request values are truncated SHA-256 fingerprints
  of whole requests. Structure trials also keep request and sent fingerprints with
  different scopes; an index must choose and document its input scope. Latin request
  is a prompt code, not an input fingerprint. Omit when no input fingerprint was kept,
  including trial rows.'
from_schema: https://pruzhany.org/ns/exchanges
see_also:
- https://www.w3.org/TR/prov-o/#used
rank: 1000
owner: KeptAsking
domain_of:
- KeptAsking
range: ExchangeCode

```
</details></div>
