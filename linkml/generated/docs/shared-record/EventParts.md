---
search:
  boost: 2.0
---


# Enum: EventParts 




_Event parts: the values of event_parts in vocabulary/sourced-entities.json, version 1.3.0._



<div data-search-exclude markdown="1">

URI: [pc:EventParts](https://pruzhany.org/ns/sourced-entities#EventParts)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| baby | pc:part_baby | The baby at a birth. | Title: Baby<br>|
| parent | pc:part_parent | The parent at a birth. | Title: Parent<br>|
| bride | pc:part_bride | The bride at an engagement or a wedding. | Title: Bride<br>|
| groom | pc:part_groom | The groom at an engagement or a wedding. | Title: Groom<br>|
| boy | pc:part_boy | The boy at his bar mitzvah. | Title: Boy<br>|
| deceased | pc:part_deceased | The person who died, at a death. | Title: Deceased<br>|
| remembered | pc:part_remembered | The person remembered, at a memorial. | Title: Remembered<br>|




## Slots

| Name | Description |
| ---  | --- |
| [part](part.md) | The person's part in the event. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record






## LinkML Source

<details>
```yaml
name: EventParts
description: 'Event parts: the values of event_parts in vocabulary/sourced-entities.json,
  version 1.3.0.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
permissible_values:
  baby:
    text: baby
    description: The baby at a birth.
    meaning: pc:part_baby
    title: Baby
    comments:
    - The birth happens to this person; RiC-O has no baby part.
  parent:
    text: parent
    description: The parent at a birth.
    meaning: pc:part_parent
    title: Parent
    comments:
    - A parent participates in a birth but is not the person born; RiC-O has no birth-parent
      part.
  bride:
    text: bride
    description: The bride at an engagement or a wedding.
    meaning: pc:part_bride
    title: Bride
    comments:
    - The engagement or wedding happens to the bride; RiC-O has no bride part.
  groom:
    text: groom
    description: The groom at an engagement or a wedding.
    meaning: pc:part_groom
    title: Groom
    comments:
    - The engagement or wedding happens to the groom; RiC-O has no groom part.
  boy:
    text: boy
    description: The boy at his bar mitzvah.
    meaning: pc:part_boy
    title: Boy
    comments:
    - The bar mitzvah happens to this boy; RiC-O has no bar-mitzvah part.
  deceased:
    text: deceased
    description: The person who died, at a death.
    meaning: pc:part_deceased
    title: Deceased
    comments:
    - The death happens to this person; RiC-O has no deceased part.
  remembered:
    text: remembered
    description: The person remembered, at a memorial.
    meaning: pc:part_remembered
    title: Remembered
    comments:
    - The commemoration concerns this person without asserting another death; RiC-O
      has no remembered part.

```
</details>

</div>
