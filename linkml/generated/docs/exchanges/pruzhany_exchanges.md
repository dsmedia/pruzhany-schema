# pruzhany_exchanges 

Metadata for a version of a model's instructions, and references to kept answers outside this repository. PromptVersion describes the metadata in prompts/<asking>/<code>/ in steps; its sibling files hold the system text, prompt text and, when recovered, the answer's JSON Schema. KeptAsking is an index entry describing a stored answer, not a replacement wire shape for the different readings files. A kept file can accumulate several calls and retries. Answer payloads and prompt text stay in steps; generating the answer shapes from LinkML belongs to a later slice. The steps exchange check must resolve prompt references, verify codes from exact prompt bytes, check history and date ordering, and validate answers against their own recovered shapes.

URI: https://pruzhany.org/ns/exchanges
