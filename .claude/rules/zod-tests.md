---
paths:
  - "zod/**"
---

# Tests under zod/

No test under `zod/` may need anything but bun. pruzhany-svelte runs every
`*.test.ts` there through its `src/lib/schemas` symlink, with bun only (#15).

Pilot tests live beside their pilot; cross-language tests live in `tests/contract/`.
Both run through `bin/verify`, outside `zod/`.
