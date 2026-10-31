# IIIF Presentation 3 schema source pin

Not redistributed: the upstream repository grants no licence. This directory
contains only provenance in `pin.json` and this README, never the upstream schema
or a copy of its README. The source pin is IIIF/presentation-validator commit
`3891f47ce7dbaa896027a5fab5f63a109de4bd70`; it is not a new Presentation release.

From the schema checkout, run `python3 -P standards/fetch_iiif.py` (also run by
`bin/verify standards`). The stdlib-only tool downloads the exact raw URL in
`pin.json` to ignored `standards/.cache/iiif-presentation-3-3891f47/iiif_3_0.json`.
It checks SHA-256 before saving and on every reuse. A mismatched cache, mismatched
download or failed download fails loudly; there is no alternate or unpinned copy.
An empty cache requires network. Steps invokes this same tool when its cache is
absent, verifies the bytes again, then compiles the self-contained Draft 7 schema
offline, selecting Manifest explicitly. The pin test validates a fictional Manifest
and rejects a planted fault; no newspaper data belongs here.

Read **31 October 2026**: upstream [README](https://github.com/IIIF/presentation-validator/blob/3891f47ce7dbaa896027a5fab5f63a109de4bd70/README.md)
and [pyproject.toml](https://github.com/IIIF/presentation-validator/blob/3891f47ce7dbaa896027a5fab5f63a109de4bd70/pyproject.toml)
grant no licence. The same day's review found no upstream LICENSE. IIIF's
Apache-2.0 [iiif-prezi3 licence](https://github.com/iiif-prezi/iiif-prezi3/blob/main/LICENSE)
and [regeneration tool](https://github.com/iiif-prezi/iiif-prezi3/blob/main/utils/regenerate_skeleton.py)
were also read that day: that tool fetches this schema from raw.githubusercontent.com
at use. Our fetch uses the immutable commit and verifies its checksum.
