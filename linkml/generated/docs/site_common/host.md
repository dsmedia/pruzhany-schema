---
search:
  boost: 5.0
---

# Slot: host 


_The web host the source's records are served from, without www: every address cited from it is on that host or a subdomain of it._



<div data-search-exclude markdown="1">



URI: [pc:site_source_host](https://pruzhany.org/ns/sourced-entities#site_source_host)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [HostName](HostName.md) |
| Domain Of | [Source](Source.md) |
| Slot URI | [pc:site_source_host](https://pruzhany.org/ns/sourced-entities#site_source_host) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Source](Source.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:site_source_host |
| native | pc:host |




## LinkML Source

<details>
```yaml
name: host
description: 'The web host the source''s records are served from, without www: every
  address cited from it is on that host or a subdomain of it.'
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
slot_uri: pc:site_source_host
owner: Source
domain_of:
- Source
range: HostName

```
</details></div>
