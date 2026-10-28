---
search:
  boost: 2.0
---


# Enum: MentionRoles 




_Mention roles: the values of mention_roles in vocabulary/sourced-entities.json, version 1.3.0._



<div data-search-exclude markdown="1">

URI: [pc:MentionRoles](https://pruzhany.org/ns/sourced-entities#MentionRoles)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| subject | pc:mention_roles_subject | The person whom the source passage concerns. | Title: Subject<br>|
| deceased | pc:mention_roles_deceased | The person whose death the passage concerns; a mention role alone is not death evidence. | Title: Deceased<br>|
| honoree | pc:mention_roles_honoree | The person being honored or congratulated. | Title: Honoree<br>|
| signer | pc:mention_roles_signer | A person signing the item. | Title: Signer<br>|
| mourner | pc:mention_roles_mourner | A person identified as mourning. | Title: Mourner<br>|
| advertiser | pc:mention_roles_advertiser | A person placing or represented by an advertisement. | Title: Advertiser<br>|
| author | pc:mention_roles_author | The author identified by a byline or attribution. | Title: Author<br>|
| office_holder | pc:mention_roles_office_holder | A person named in an official capacity; an office fact requires its own evidence. | Title: Office holder<br>|
| donor | pc:mention_roles_donor | A person identified as a donor. | Title: Donor<br>|
| named | pc:mention_roles_named | A person named without a more specific established role. | Title: Named<br>|
| betrothed | pc:mention_roles_betrothed | A person identified as engaged to marry. | Title: Betrothed<br>|
| parent | pc:mention_roles_parent | A participant identified as a parent; a named parent-child link belongs in relationships. | Title: Parent<br>|




## Slots

| Name | Description |
| ---  | --- |
| [role](role.md) | The person's role in the piece. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common






## LinkML Source

<details>
```yaml
name: MentionRoles
description: 'Mention roles: the values of mention_roles in vocabulary/sourced-entities.json,
  version 1.3.0.'
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
permissible_values:
  subject:
    text: subject
    description: The person whom the source passage concerns.
    meaning: pc:mention_roles_subject
    title: Subject
    comments:
    - Application-specific mention roles category; no exact pinned ontology value
      is established.
  deceased:
    text: deceased
    description: The person whose death the passage concerns; a mention role alone
      is not death evidence.
    meaning: pc:mention_roles_deceased
    title: Deceased
    comments:
    - Application-specific mention roles category; no exact pinned ontology value
      is established.
  honoree:
    text: honoree
    description: The person being honored or congratulated.
    meaning: pc:mention_roles_honoree
    title: Honoree
    comments:
    - Application-specific mention roles category; no exact pinned ontology value
      is established.
  signer:
    text: signer
    description: A person signing the item.
    meaning: pc:mention_roles_signer
    title: Signer
    comments:
    - Application-specific mention roles category; no exact pinned ontology value
      is established.
  mourner:
    text: mourner
    description: A person identified as mourning.
    meaning: pc:mention_roles_mourner
    title: Mourner
    comments:
    - Application-specific mention roles category; no exact pinned ontology value
      is established.
  advertiser:
    text: advertiser
    description: A person placing or represented by an advertisement.
    meaning: pc:mention_roles_advertiser
    title: Advertiser
    comments:
    - Application-specific mention roles category; no exact pinned ontology value
      is established.
  author:
    text: author
    description: The author identified by a byline or attribution.
    meaning: pc:mention_roles_author
    title: Author
    comments:
    - Application-specific mention roles category; no exact pinned ontology value
      is established.
  office_holder:
    text: office_holder
    description: A person named in an official capacity; an office fact requires its
      own evidence.
    meaning: pc:mention_roles_office_holder
    title: Office holder
    comments:
    - Application-specific mention roles category; no exact pinned ontology value
      is established.
  donor:
    text: donor
    description: A person identified as a donor.
    meaning: pc:mention_roles_donor
    title: Donor
    comments:
    - Application-specific mention roles category; no exact pinned ontology value
      is established.
  named:
    text: named
    description: A person named without a more specific established role.
    meaning: pc:mention_roles_named
    title: Named
    comments:
    - Application-specific mention roles category; no exact pinned ontology value
      is established.
  betrothed:
    text: betrothed
    description: A person identified as engaged to marry.
    meaning: pc:mention_roles_betrothed
    title: Betrothed
    comments:
    - Application-specific mention roles category; no exact pinned ontology value
      is established.
  parent:
    text: parent
    description: A participant identified as a parent; a named parent-child link belongs
      in relationships.
    meaning: pc:mention_roles_parent
    title: Parent
    comments:
    - Application-specific mention roles category; no exact pinned ontology value
      is established.

```
</details>

</div>
