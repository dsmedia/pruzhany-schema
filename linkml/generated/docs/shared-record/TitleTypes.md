---
search:
  boost: 2.0
---


# Enum: TitleTypes 




_Title types: the values of title_types in vocabulary/site-content.json, version 1.0.0._



<div data-search-exclude markdown="1">

URI: [pc:TitleTypes](https://pruzhany.org/ns/sourced-entities#TitleTypes)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| printed | pc:title_type_printed | The printed words naming a content item or a section. | Title: Printed title<br>|
| supplied | pc:title_type_supplied | An attributed English name pinned to the text it was made from. | Title: Supplied title<br>|













## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record






## LinkML Source

<details>
```yaml
name: TitleTypes
description: 'Title types: the values of title_types in vocabulary/site-content.json,
  version 1.0.0.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
permissible_values:
  printed:
    text: printed
    description: The printed words naming a content item or a section.
    meaning: pc:title_type_printed
    title: Printed title
    comments:
    - Distinguishes words printed in the source from a supplied name; RiC-O defines
      TitleType but not this controlled value.
    status: proposed
  supplied:
    text: supplied
    description: An attributed English name pinned to the text it was made from.
    meaning: pc:title_type_supplied
    title: Supplied title
    comments:
    - Distinguishes an attributed English name from printed words; RiC-O defines TitleType
      but not this controlled value.
    status: proposed

```
</details>

</div>
