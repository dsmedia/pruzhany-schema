---
search:
  boost: 2.0
---


# Enum: IdentifierTypes 




_Identifier types approved in ADR 0001 and linked-data ticket 03._



<div data-search-exclude markdown="1">

URI: [pc:IdentifierTypes](https://pruzhany.org/ns/sourced-entities#IdentifierTypes)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| old_identifier | pc:old_identifier | A merged identifier retained permanently on the surviving record, with the registered merge source, reading day and attribution. It redirects to the surviving id and is never reused. | Title: Old identifier<br>|













## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common






## LinkML Source

<details>
```yaml
name: IdentifierTypes
description: Identifier types approved in ADR 0001 and linked-data ticket 03.
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
permissible_values:
  old_identifier:
    text: old_identifier
    description: A merged identifier retained permanently on the surviving record,
      with the registered merge source, reading day and attribution. It redirects
      to the surviving id and is never reused.
    meaning: pc:old_identifier
    title: Old identifier
    comments:
    - RiC-O IdentifierType gives old identifier as an example but does not mint that
      value; this concept types our retained merged identifiers.

```
</details>

</div>
