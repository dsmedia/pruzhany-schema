# pruzhany-schema command runner. The one verify entry point is bin/verify
# (CI runs it verbatim); the recipes below delegate to it. `test-contract` is
# the one check bin/verify cannot run: it needs the private pruzhany-press
# sibling checkout (see the header of bin/verify).

press_dir := env_var_or_default("PRUZHANY_PRESS_DIR", justfile_directory() / ".." / "pruzhany-press")

default:
    @just --list

# Everything CI runs: gitleaks scan, zod tests + typecheck, pydantic load check.
verify *steps:
    bin/verify {{steps}}

# One-time setup per clone: install and register the gitleaks pre-commit hook.
pre-commit-install:
    uv tool install pre-commit && uvx pre-commit install

# gitleaks over the full history (bin/verify step `scan`).
scan:
    bin/verify scan

# The zod/*.test.ts suite and a strict typecheck, standalone (bin/verify step `zod`).
test-zod:
    bin/verify zod

# Zod<->Pydantic drift gate, run from the pruzhany-press checkout (the sibling
# by default; set PRUZHANY_PRESS_DIR from a worktree) against THIS checkout
# rather than press's submodule pin. Not in CI: pruzhany-press is private.
test-contract:
    cd "{{press_dir}}" && PRUZHANY_SCHEMA_ROOT="{{justfile_directory()}}" uv run --group dev python -m pytest tests/contract/
