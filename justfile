# pruzhany-schema command runner. The one verify entry point is bin/verify
# (CI runs it verbatim); the recipes below delegate to it.

default:
    @just --list

# Everything CI runs: gitleaks, zod tests/typecheck, pydantic and isolated pilot.
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

# The Zod<->Pydantic lockstep (bin/verify step `contract`).
test-contract:
    bin/verify contract
