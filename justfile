# pruzhany-schema command runner. This repo is a pure contract layer with no
# build or test of its own (CLAUDE.md "Testing") — the two delegating recipes
# below run this repo's tests from its sibling consumer checkouts, exactly as
# CLAUDE.md documents. `pre-commit-install`/`scan` wrap the one thing that is
# genuinely local: the gitleaks secret scan (.pre-commit-config.yaml).

default:
    @just --list

# One-time setup per clone: install and register the gitleaks pre-commit hook.
pre-commit-install:
    uv tool install pre-commit && pre-commit install

# Run the pre-commit hooks (gitleaks) against the whole repo.
scan:
    pre-commit run --all-files

# Run the zod/*.test.ts suite via the pruzhany-svelte sibling checkout's vitest.
test-zod:
    cd ../pruzhany-svelte && npx vitest run src/lib/schemas

# Run the Zod<->Pydantic drift gate via the pruzhany-press sibling checkout.
test-contract:
    cd ../pruzhany-press && uv run --group dev python -m pytest tests/contract/
