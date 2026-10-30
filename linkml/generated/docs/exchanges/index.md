# Kept exchanges with models

Metadata for a version of a model's instructions, and references to kept answers outside this repository. PromptVersion describes the metadata in prompts/<asking>/<code>/ in steps; its sibling files hold the system text, prompt text and, when recovered, the answer's JSON Schema. KeptAsking is an index entry describing a stored answer, not a replacement wire shape for the different readings files. A kept file can accumulate several calls and retries. Answer payloads and prompt text stay in steps; the current answer shapes are defined in answers.yaml. The steps exchange check must resolve prompt references, verify codes from exact prompt bytes, check history and date ordering, and validate answers against their own recovered shapes.

URI: https://pruzhany.org/ns/exchanges

Name: pruzhany_exchanges



## Classes

| Class | Description |
| --- | --- |
| [KeptAsking](KeptAsking.md) | A reference to a kept answer file or an identified input within an accumulated file. Model and prompt metadata can come from a companion trial setting or history; fields absent from storage are not invented. This is not a promise that one file is one paid call. Payloads retain their existing steps formats. |
| [PromptVersion](PromptVersion.md) | One prompt version's metadata, kept beside its exact text and recovered answer shape. First and last refer to its presence in code history, not paid-call dates. A shape may be unrecoverable even when the prompt text and its history are known. |



## Slots

| Slot | Description |
| --- | --- |
| [answer_file](answer_file.md) | The kept answer's file path relative to the steps repository. The path locates an existing payload; it is not that payload or a public download URI. |
| [asking](asking.md) | The asking served by these instructions, such as find_items, read_latin, write_english or join_people. Trial variants are registered by steps; this field is not a new controlled vocabulary. |
| [budget_usd](budget_usd.md) | The configured maximum budget in US dollars, separate from an answer's recorded cost. Zero is allowed; no undocumented upper bound is imposed. |
| [code](code.md) | The sixteen-character code naming this stored version and its directory. Some historical codes cover an expanded whole request rather than only instructions; the steps registry must establish the recipe and scope. |
| [cost_usd](cost_usd.md) | The cost in US dollars where kept, including zero. It retains the stored file's accounting scope: English and Latin accumulate calls, and structure may include retries. Do not sum the same file's cost again for every input or interpret it as a measured per-call cost. Omit when unavailable. |
| [day](day.md) | An asking day where actually kept: English answered_on for the indexed input or the trial directory's day. Omit when unknown; a first committed day is not an observed asking day and must not be silently substituted. |
| [effort](effort.md) | The explicit effort setting when known; omit when no setting was supplied or recovered. Model-dependent effort values are not enumerated here. |
| [first_commit](first_commit.md) | The first steps commit known to contain this prompt version in code. |
| [first_day](first_day.md) | The day of first_commit, as established by steps' history recovery. |
| [input_fingerprint](input_fingerprint.md) | An input fingerprint where kept: English pieces keys are xxh3_64 text digests; structure and joining request values are truncated SHA-256 fingerprints of whole requests. Structure trials also keep request and sent fingerprints with different scopes; an index must choose and document its input scope. Latin request is a prompt code, not an input fingerprint. Omit when no input fingerprint was kept, including trial rows. |
| [last_commit](last_commit.md) | The last steps commit known to contain this prompt version in code, not necessarily the latest kept answer or the commit removing the version. |
| [last_day](last_day.md) | The day of last_commit. Agreement with history and first_day ordering are checked in steps, not by this single-document shape. |
| [model](model.md) | The model selector used with this version. It is recorded configuration, not an assertion that two selectors denote the same model release. |
| [prompt_code](prompt_code.md) | The associated PromptVersion.code, resolved by steps from the stored prompt code, companion setting or recovered history. English stores the code as prompt and Latin as request. Structure and joining request values include inputs; their association requires recovery, not an assumption that they hash only instructions. A recovered version may retain a whole-request code. |
| [shape_name](shape_name.md) | The answer shape's name, qualified by its module when needed. Knowing this name does not imply that the exact schema bytes were recovered. |
| [shape_recovered](shape_recovered.md) | Whether the exact answer JSON Schema was recovered reproducibly and kept beside the prompt. False explicitly records the limit on answer validation; a shape name by itself is not recovery. |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal specification |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [ExchangeCode](ExchangeCode.md) | Exactly sixteen lowercase hexadecimal characters. Prompt codes and the stored short input fingerprints share this lexical form; it does not identify the hash algorithm or what is covered. The steps registry owns the byte-level rule. |
| [ExchangeCommit](ExchangeCommit.md) | A full forty-character Git SHA-1 commit id in the steps repository, not an abbreviated id, branch or a claim that this commit exists in the schema repository. |
| [ExchangeDay](ExchangeDay.md) | A calendar day as YYYY-MM-DD, with JSON Schema date format validation enabled by the consumer. No time of day or timezone is inferred. |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [HostName](HostName.md) | A lowercase internet host name with at least one dot, such as collections.yadvashem.org. |
| [Integer](Integer.md) | An integer |
| [IsoDay](IsoDay.md) | A calendar day written YYYY-MM-DD, such as 1938-12-16. |
| [IsoYearMonthOrDay](IsoYearMonthOrDay.md) | A year, a month or a day, as far as it is known: YYYY, YYYY-MM or YYYY-MM-DD. |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. |
| [LanguageTag](LanguageTag.md) | A BCP 47 language tag, by the pattern in vocabulary/citation-requirements.json. |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model. |
| [NonBlankText](NonBlankText.md) | Text with at least one character that is not white space. |
| [NonNegativeInteger](NonNegativeInteger.md) | A whole number from 0 to 9007199254740991, the largest integer JavaScript holds exactly. As the range of a multivalued slot it bounds each item, not the list. |
| [NonNegativeNumber](NonNegativeNumber.md) | A number at least 0, such as each of the four numbers of a box on a page picture; the shapes bound the box's width and height above 0, which known-looser.yaml records. |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model. |
| [PositiveInteger](PositiveInteger.md) | A whole number from 1 to 9007199254740991; the shapes say above 0, which for a whole number is the same. |
| [ScriptCode](ScriptCode.md) | A four-letter ISO 15924 script code, such as Hebr or Latn. |
| [Sha256Hex](Sha256Hex.md) | A SHA-256 digest: exactly 64 lowercase hexadecimal digits and nothing after them. Some shapes write the pattern without its last part and add a length of 64, which says the same; LinkML has no length of a string, hence the last part. |
| [SimpleLanguageTag](SimpleLanguageTag.md) | A language tag in its simple form, letters then hyphenated parts, such as yi or yi-Latn. |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular day |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
