---
search:
  boost: 5.0
---

# Slot: source_id 

<div data-search-exclude markdown="1">



URI: [pc:source_id](https://pruzhany.org/ns/sourced-entities#source_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListOutsideRecord](FatesListOutsideRecord.md) | A record an archive holds about the person: the archive, the database it is in, the record's type and id as the archive gives them, and its own address where the record has one. |  no  |
| [FatesListArchiveCount](FatesListArchiveCount.md) | How many people an archive's database names, and how many of them with an address. |  no  |
| [SourceDerivation](SourceDerivation.md) | The record a source we hold was made from, and how: a copy or a transcription of it. |  no  |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FatesListOutsideRecord](FatesListOutsideRecord.md), [FatesListArchiveCount](FatesListArchiveCount.md), [SourceDerivation](SourceDerivation.md), [Citation](Citation.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:source_id |
| native | pc:source_id |




## LinkML Source

<details>
```yaml
name: source_id
domain_of:
- FatesListOutsideRecord
- FatesListArchiveCount
- SourceDerivation
- Citation
range: string

```
</details></div>
