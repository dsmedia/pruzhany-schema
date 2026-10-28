---
search:
  boost: 5.0
---

# Slot: subject_ids 


_What the content item is about, as subjects of the site-content vocabulary._



<div data-search-exclude markdown="1">



URI: [rico:hasOrHadSubject](https://www.ica.org/standards/RiC/ontology#hasOrHadSubject)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItem](ContentItem.md) | One article, notice, greeting or advertisement of the issue: its kind, its titles, its text and English, the regions it is printed in and what it names. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Subjects](Subjects.md) |
| Domain Of | [ContentItem](ContentItem.md) |
| Slot URI | [rico:hasOrHadSubject](https://www.ica.org/standards/RiC/ontology#hasOrHadSubject) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ContentItem](ContentItem.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:hasOrHadSubject |
| native | pc:subject_ids |




## LinkML Source

<details>
```yaml
name: subject_ids
description: What the content item is about, as subjects of the site-content vocabulary.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
slot_uri: rico:hasOrHadSubject
owner: ContentItem
domain_of:
- ContentItem
range: Subjects
required: true
multivalued: true

```
</details></div>
