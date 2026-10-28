---
search:
  boost: 2.0
---


# Enum: SourceDerivationRelation 




_How a source we hold was made from another: a copy of it, or a transcription of it._



<div data-search-exclude markdown="1">

URI: [pc:SourceDerivationRelation](https://pruzhany.org/ns/sourced-entities#SourceDerivationRelation)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| copy | ehri:isCopyOf | A copy of the original record. |
| transcription | rico:describesOrDescribed | A transcription of the original record, which describes it and is not a copy of it. |




## Slots

| Name | Description |
| ---  | --- |
| [relation](relation.md) | Whether this source is a copy or a transcription of the original. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common






## LinkML Source

<details>
```yaml
name: SourceDerivationRelation
description: 'How a source we hold was made from another: a copy of it, or a transcription
  of it.'
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
permissible_values:
  copy:
    text: copy
    description: A copy of the original record.
    meaning: ehri:isCopyOf
  transcription:
    text: transcription
    description: A transcription of the original record, which describes it and is
      not a copy of it.
    meaning: rico:describesOrDescribed

```
</details>

</div>
