# Setup and verification

Run commands from the schema checkout's root unless stated otherwise. Read
`bin/verify`'s header for its nine steps and [README.md](../../README.md#verify)
for the contracts they protect.

## Setup

Install the tools pinned in `mise.toml` (Bun, Python and gitleaks; just is an
optional command runner). With mise available, `mise install` installs those pins.
The checks also require bash, git and uv; CI installs uv 0.11.13. Then run:

```sh
bun install --frozen-lockfile
bin/verify
```

`bin/verify` uses uv to provision Python 3.11 package environments. Its vocabulary
step also calls `python3` from PATH. The LinkML step creates and removes a separate
environment, syncing `linkml/requirements.lock` with required hashes and
`linkml/build-constraints.txt`; do not replace that with an unlocked install.
For generation commands, read [linkml/README.md](../../linkml/README.md#commands).

If the default uv cache is outside the writable sandbox, set `UV_CACHE_DIR` to a
dedicated directory inside the worktree for the check, then remove that directory.
When piping a check's output, use `set -o pipefail` so a failed check stays a failure.

`bin/verify <step>...` runs selected steps for iteration; the full `bin/verify`
remains the check before merging. Do not skip or loosen checks.

The `zod` step also runs `tests/documentation/`: CHANGELOG heading/date checks,
the README quick-start extractor and planted failures. The fresh-clone workflow
runs the extracted commands on `ubuntu-24.04`, with no sibling checkouts or restored
tool/dependency caches. It uses ci.yml's Bun 1.3.11 and uv 0.11.13 setup actions,
plus mise 2026.10.25; the README's `mise install` installs the `mise.toml` tools
(Bun 1.3.11, Python 3.11, gitleaks 8.24.3 and just 1.56.0). Bash, Git, Node.js
and coreutils come from the runner; its inventory step prints their versions.
uv provisions Python 3.11 environments and the Python dependencies
named in `bin/verify`; LinkML uses its hashed requirements and build constraints.
Vitest 4.1.9, TypeScript 5.9.3, Prettier 3.8.0, Zod 4.3.5 and Node types 22.19.0
come from `package.json`/`bun.lock` through `bun install --frozen-lockfile`.
Vitest/tsc/Prettier run through their Node shebangs; newcomers need Node.js 22.
Read 1 November 2026: [Bun's bunx shebang behaviour](https://bun.sh/docs/pm/bunx).
Neither the website nor Playwright is needed for this workflow.

## Consumer checks

Before a change here merges, run these in pruzhany-svelte with its
`src/lib/schemas` symlink resolving to the schema files being checked:

```sh
bun run format:check
bun run lint
bun run check
bun run test:run
bun run validate:data
```

A temporary copy of the website can use this checkout's schema files while
preserving the original website checkout's recorded submodule pin. Install its
dependencies from its lockfile if they are not already available. Do not substitute
checks against the old submodule contents for checks against the changed schema.

In pruzhany-steps, `site_shapes refresh` requires a clean committed schema HEAD.
Until that commit exists, preview generated differences separately rather than
refreshing the recorded exports. The Zod↔Pydantic lockstep runs here in
`bin/verify contract`; its older location in pruzhany-press is retired.
