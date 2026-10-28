---
search:
  boost: 1.0
---# Type: Sha256Hex 




_A SHA-256 digest: exactly 64 lowercase hexadecimal digits and nothing after them. Some shapes write the pattern without its last part and add a length of 64, which says the same; LinkML has no length of a string, hence the last part._



<div data-search-exclude markdown="1">

URI: [xsd:string](http://www.w3.org/2001/XMLSchema#string)

## Type Properties

| Property | Value |
| --- | --- |
| Type Of | [String](String.md) |
| Base | `str` |
| Type URI | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
## Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[0-9a-f]{64}$(?![\s\S])` |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:Sha256Hex |
| native | pc:Sha256Hex |




</div>
