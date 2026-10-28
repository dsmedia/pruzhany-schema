---
search:
  boost: 2.0
---


# Enum: NameKinds 




_Name kinds: the values of name_kinds in vocabulary/sourced-entities.json, version 1.3.0._



<div data-search-exclude markdown="1">

URI: [pc:NameKinds](https://pruzhany.org/ns/sourced-entities#NameKinds)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| printed | pc:name_kinds_printed | A name exactly as printed in a source. | Title: Printed<br>|
| birth | pc:name_kinds_birth | A name used at birth, including a maiden name. | Title: Birth<br>|
| married | pc:name_kinds_married | A name used following marriage. | Title: Married<br>|
| later | pc:name_kinds_later | A name used later in life, without assuming the reason for its adoption. | Title: Later<br>|
| nickname | pc:name_kinds_nickname | A familiar or informal name. | Title: Nickname<br>|
| alias | pc:name_kinds_alias | An alternative assumed name. | Title: Alias<br>|
| religious | pc:name_kinds_religious | A name used in religious life. | Title: Religious<br>|
| spelling | pc:name_kinds_spelling | An alternative spelling of a name, without asserting a different identity. | Title: Spelling<br>|
| supplied | pc:site_name_supplied | An attributed description used to name a person whom the source does not name. | Title: Supplied description<br>|













## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items






## LinkML Source

<details>
```yaml
name: NameKinds
description: 'Name kinds: the values of name_kinds in vocabulary/sourced-entities.json,
  version 1.3.0.'
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
permissible_values:
  printed:
    text: printed
    description: A name exactly as printed in a source.
    meaning: pc:name_kinds_printed
    title: Printed
    comments:
    - Application-specific name kinds category; no exact pinned ontology value is
      established.
  birth:
    text: birth
    description: A name used at birth, including a maiden name.
    meaning: pc:name_kinds_birth
    title: Birth
    comments:
    - Application-specific name kinds category; no exact pinned ontology value is
      established.
  married:
    text: married
    description: A name used following marriage.
    meaning: pc:name_kinds_married
    title: Married
    comments:
    - Application-specific name kinds category; no exact pinned ontology value is
      established.
  later:
    text: later
    description: A name used later in life, without assuming the reason for its adoption.
    meaning: pc:name_kinds_later
    title: Later
    comments:
    - Application-specific name kinds category; no exact pinned ontology value is
      established.
  nickname:
    text: nickname
    description: A familiar or informal name.
    meaning: pc:name_kinds_nickname
    title: Nickname
    comments:
    - Application-specific name kinds category; no exact pinned ontology value is
      established.
  alias:
    text: alias
    description: An alternative assumed name.
    meaning: pc:name_kinds_alias
    title: Alias
    comments:
    - Application-specific name kinds category; no exact pinned ontology value is
      established.
  religious:
    text: religious
    description: A name used in religious life.
    meaning: pc:name_kinds_religious
    title: Religious
    comments:
    - Application-specific name kinds category; no exact pinned ontology value is
      established.
  spelling:
    text: spelling
    description: An alternative spelling of a name, without asserting a different
      identity.
    meaning: pc:name_kinds_spelling
    title: Spelling
    comments:
    - Application-specific name kinds category; no exact pinned ontology value is
      established.
  supplied:
    text: supplied
    description: An attributed description used to name a person whom the source does
      not name.
    meaning: pc:site_name_supplied
    title: Supplied description
    comments:
    - RiC-O has AgentName but no name kind separating our supplied description from
      printed words.

```
</details>

</div>
