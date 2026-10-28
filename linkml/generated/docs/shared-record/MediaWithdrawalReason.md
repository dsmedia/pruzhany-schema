---
search:
  boost: 2.0
---


# Enum: MediaWithdrawalReason 




_Why a medium was withdrawn._



<div data-search-exclude markdown="1">

URI: [pc:MediaWithdrawalReason](https://pruzhany.org/ns/sourced-entities#MediaWithdrawalReason)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| family | None | At the family's request. |
| holder | None | At the holder's request. |
| error | None | For an error. |




## Slots

| Name | Description |
| ---  | --- |
| [reason](reason.md) | Why: at the family's or the holder's request, or for an error. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record






## LinkML Source

<details>
```yaml
name: MediaWithdrawalReason
description: Why a medium was withdrawn.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
permissible_values:
  family:
    text: family
    description: At the family's request.
  holder:
    text: holder
    description: At the holder's request.
  error:
    text: error
    description: For an error.

```
</details>

</div>
