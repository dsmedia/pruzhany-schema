# Domain docs

How the engineering skills of the plugin `mattpocock-skills` read this repository's
domain documentation. The layout is single-context.

## Before exploring, read these

- **`GLOSSARY.md`** at the repo root.
- **`docs/adr/`**: decision records that touch the area about to be worked in.
- The dated design docs in **`docs/design/`**: the existing record of the contract's
  decisions.
- **`standards/`**: the pinned EHRI and RiC-O vocabularies. Read the term there before
  naming or mapping anything; never from memory.

If `GLOSSARY.md` or `docs/adr/` does not exist, **proceed silently**. Don't flag the
absence or suggest creating them upfront: `/domain-modeling` creates them when a term or
decision is actually settled.

## File structure

```
/
├── GLOSSARY.md
├── docs/adr/
│   └── 0001-<decision>.md
├── docs/design/
├── standards/
├── zod/
└── pydantic/
```

## The glossary follows EHRI and RiC-O

The owner's rule (`CLAUDE.md`): prefer an EHRI class, else a RiC-O term in EHRI's RiC-O
version, else a local term with a reason. A glossary entry for a concept those standards
name uses their term and cites the `standards/` file it was read in. `/domain-modeling`
does not add vocabulary types; those are approved by the owner in batches (#16).

## Use the glossary's vocabulary

When output names a domain concept (an issue title, a refactor proposal, a hypothesis, a
test name), use the term as `GLOSSARY.md` defines it. Don't drift to synonyms it avoids.

If the concept isn't in the glossary yet, that is a signal: either language is being
invented that the project doesn't use (reconsider), or there's a real gap (note it for
`/domain-modeling`).

## Flag ADR conflicts

If output contradicts an ADR, a design doc listed above, or a rule in `CLAUDE.md`
/`AGENTS.md`, say so explicitly rather than silently overriding it:

> _Contradicts ADR-0007 (...), but worth reopening because…_
