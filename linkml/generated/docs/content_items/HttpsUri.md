---
search:
  boost: 1.0
---# Type: HttpsUri 




_A web address that begins https:// and holds no white space, as the Pydantic twin's pattern says; the Zod twin asks for a URL whose protocol is https._



<div data-search-exclude markdown="1">

URI: [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI)

## Type Properties

| Property | Value |
| --- | --- |
| Type Of | [Uri](Uri.md) |
| Base | `URI` |
| Type URI | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Representation | `str` |
## Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^https://[^\s/?#]+[^\s]*$` |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:HttpsUri |
| native | pc:HttpsUri |




</div>
