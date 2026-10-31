# IIIF Presentation 3 JSON Schema

Read 31 October 2026: [Presentation API 3.0.0](https://iiif.io/api/presentation/3.0/)
and [IIIF/presentation-validator](https://github.com/IIIF/presentation-validator),
main at `3891f47ce7dbaa896027a5fab5f63a109de4bd70` (an untagged source pin,
not a new Presentation release). `pin.json` records source URLs and hashes.
The schema and upstream README are unchanged. Never edit a pinned file in place.

The upstream v3 validator uses Draft 7 and this self-contained schema; references
are local fragments. Steps compiles it offline with its existing jsonschema-rs,
selecting Manifest explicitly, and tests both valid fictional manifests and
planted faults. `bin/verify standards` checks pin integrity and provenance.
No website contract, LinkML definition or consumer dependency changes.

No explicit licence was found in the schema or upstream README; the checked
root `LICENSE` and `LICENSE.md` addresses returned 404. Attribution is retained;
no additional licence grant is asserted. This says nothing about picture rights.
