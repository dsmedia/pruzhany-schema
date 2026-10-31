# Current structured model answers

The four current paid answer shapes. Procedural descriptions and titles are the exact strings sent by steps; no prompt text or answer data is included.

URI: https://pruzhany.org/ns/answers

Name: pruzhany_answers



## Classes

| Class | Description |
| --- | --- |
| [FindItemsAnswer](FindItemsAnswer.md) | The page's items in reading order, the headings over several items, the running head. |
| [FindItemsAnswerHeading](FindItemsAnswerHeading.md) | A heading over several items as the model gives it: its lines, and the items' numbers. |
| [FindItemsAnswerItem](FindItemsAnswerItem.md) | One item as the model gives it: its parts in order, its kind, language and headline. |
| [JoinPeopleAnswer](JoinPeopleAnswer.md) | The groups of names that are one person; a name in no group is a person of its own. |
| [JoinPeopleGroup](JoinPeopleGroup.md) | Names that are one person, and the name the person is given. |
| [QuoteEnglishAnswer](QuoteEnglishAnswer.md) | The answer about a batch of quotations: every quotation it was sent, by its number. |
| [QuoteEnglishQuotedEnglish](QuoteEnglishQuotedEnglish.md) | One quotation's English, with the number it was sent under. |
| [ReadLatinAnswer](ReadLatinAnswer.md) | The model's answer to one message: a line for each picture, empty where it saw no text. |
| [ReadLatinLine](ReadLatinLine.md) | One picture as the model answers for it: the picture's number and the text printed in it. |
| [WriteEnglishAnswer](WriteEnglishAnswer.md) | The answer about one page: every piece it was sent, by its number. |
| [WriteEnglishAnsweredPiece](WriteEnglishAnsweredPiece.md) | A piece of the answer, with the number it was sent under. |
| [WriteEnglishDoubt](WriteEnglishDoubt.md) | A word or short phrase the model believes the machine misread. |
| [WriteEnglishLifeEvent](WriteEnglishLifeEvent.md) | The one family event a piece announces, greets or mourns. |
| [WriteEnglishOrganization](WriteEnglishOrganization.md) | An organisation, institution or named business a piece names. |
| [WriteEnglishPerson](WriteEnglishPerson.md) | A person a piece names. |
| [WriteEnglishPlace](WriteEnglishPlace.md) | A place a piece names. |



## Slots

| Slot | Description |
| --- | --- |
| [category](category.md) | The category field in the AnsweredPiece response. |
| [certainty](certainty.md) | The certainty field in the Group response. |
| [date_gregorian](date_gregorian.md) | YYYY-MM-DD, only as printed. |
| [date_hebrew](date_hebrew.md) | The date_hebrew field in the LifeEvent response. |
| [died](died.md) | True only if the piece says the person has died. |
| [doubts](doubts.md) | The doubts field in the AnsweredPiece response. |
| [english](english.md) | The english field in the AnsweredPiece response. |
| [gender](gender.md) | The gender field in the Person response. |
| [groups](groups.md) | The groups field in the Answer response. |
| [headings](headings.md) | The headings field in the Answer response. |
| [headline](headline.md) | The headline field in the AnswerItem response. |
| [items](items.md) | The items field in the Answer response. |
| [kind](kind.md) | The kind field in the AnswerItem response. |
| [language](language.md) | The language field in the AnswerItem response. |
| [life_event](life_event.md) | The life_event field in the AnsweredPiece response. |
| [likely](likely.md) | The likely field in the Doubt response. |
| [lines](lines.md) | The lines field in the AnswerHeading response. |
| [lives_in](lives_in.md) | The town the piece says the person lives in. |
| [minor](minor.md) | True only if the piece shows the person was a child. |
| [name](name.md) | A short English name for the event. |
| [names](names.md) | The numbers of the names that are one person. |
| [number](number.md) | The number field in the AnsweredPiece response. |
| [organizations](organizations.md) | The organizations field in the AnsweredPiece response. |
| [over](over.md) | The over field in the AnswerHeading response. |
| [parts](parts.md) | The parts field in the AnswerItem response. |
| [people](people.md) | The people field in the AnsweredPiece response. |
| [picture](picture.md) | The picture field in the Line response. |
| [pieces](pieces.md) | The pieces field in the Answer response. |
| [places](places.md) | The places field in the AnsweredPiece response. |
| [principals](principals.md) | Their English names as in people. |
| [printed](printed.md) | The printed field in the Doubt response. |
| [quotations](quotations.md) | The quotations field in the Answer response. |
| [role](role.md) | What the person is in this piece, in a few words. |
| [running_head](running_head.md) | The running_head field in the Answer response. |
| [text](text.md) | The text field in the Line response. |
| [title](title.md) | The title field in the AnsweredPiece response. |
| [why](why.md) | The why field in the Doubt response. |


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
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model. |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model. |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular day |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
