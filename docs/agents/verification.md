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
