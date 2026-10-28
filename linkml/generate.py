"""Make what linkml/modules.json lists from the LinkML definition, or check what is committed.

    python -I linkml/generate.py           make linkml/generated/ afresh
    python -I linkml/generate.py --check   make it in a temporary folder and compare; exit 1,
                                           naming each file that differs, is missing or is extra

Run it in the linkml step's locked environment (bin/verify linkml). Each module of the
manifest gives its documentation under generated/docs/<name>/ (gen-doc) and, when it names a
top class, generated/json-schema/<name>.schema.json (gen-json-schema with that one top class,
closed to keys the schema does not declare). One top class a file, because one JSON Schema with
several roots merges their top-level rules (the review package's traps).

Every file is written as UTF-8 with "\\n" line ends, whatever the machine, and LinkML 1.12.1
stamps no date unless asked (its --generation-date is off by default) and no path of this
machine; so a second run, or a run on Windows, gives the same bytes.
"""

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

from linkml.generators.docgen import DocGenerator
from linkml.generators.jsonschemagen import JsonSchemaGenerator

LINKML = Path(__file__).resolve().parent


def modules(linkml_dir):
    """The manifest: each entry names a schema file, its top class (or null) and an output name."""
    manifest = json.loads((linkml_dir / 'modules.json').read_text(encoding='utf-8'))
    entries = manifest['modules']
    names = [entry['name'] for entry in entries]
    if len(set(names)) != len(names):
        raise SystemExit('linkml/modules.json: an output name is used twice')
    return entries


def write_text(path, text):
    """Write UTF-8 with "\\n" line ends and exactly one at the end, as git and editors keep it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip('\n') + '\n', encoding='utf-8', newline='\n')


def build(linkml_dir, destination):
    """Write every output of the manifest under `destination`, which must be empty."""
    for entry in modules(linkml_dir):
        schema = str(linkml_dir / entry['schema'])
        if entry['top_class']:
            # LinkML "JSON Schema" generator, https://linkml.io/linkml/generators/json-schema.html,
            # read 28 October 2026: closed by default; optional slots also accept null.
            text = JsonSchemaGenerator(schema, top_class=entry['top_class'], not_closed=False).serialize()
            write_text(destination / 'json-schema' / f"{entry['name']}.schema.json", text)
        # gen-doc writes its own files with the machine's line ends; they are made in a
        # scratch folder and written again here with "\n".
        with tempfile.TemporaryDirectory() as scratch:
            DocGenerator(schema, directory=scratch, truncate_descriptions=False).serialize()
            for made in sorted(Path(scratch).rglob('*')):
                if made.is_file():
                    target = destination / 'docs' / entry['name'] / made.relative_to(scratch)
                    write_text(target, made.read_text(encoding='utf-8'))


def files(folder):
    if not folder.exists():
        return {}
    return {path.relative_to(folder).as_posix(): path.read_bytes()
            for path in sorted(folder.rglob('*')) if path.is_file()}


def differences(linkml_dir):
    """Make every output afresh and list how linkml/generated/ differs from it."""
    with tempfile.TemporaryDirectory() as scratch:
        build(linkml_dir, Path(scratch))
        fresh = files(Path(scratch))
    committed = files(linkml_dir / 'generated')
    shown = 'linkml/generated/'
    problems = []
    for name in sorted(fresh.keys() | committed.keys()):
        if name not in committed:
            problems.append(f'{shown}{name}: missing; run linkml/generate.py')
        elif name not in fresh:
            problems.append(f'{shown}{name}: extra; generate.py makes no such file')
        elif fresh[name] != committed[name]:
            problems.append(f'{shown}{name}: differs from what generate.py makes now')
    return problems


def regenerate(linkml_dir):
    """Replace linkml/generated/ with what the definition makes now, removing stale files."""
    with tempfile.TemporaryDirectory() as scratch:
        build(linkml_dir, Path(scratch))
        target = linkml_dir / 'generated'
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(scratch, target)


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--check', action='store_true', help='compare with linkml/generated/ and change nothing')
    args = parser.parse_args(argv)
    if not args.check:
        regenerate(LINKML)
        print(f"generate: {len(files(LINKML / 'generated'))} file(s) in linkml/generated/")
        return 0
    problems = differences(LINKML)
    for problem in problems:
        print(problem)
    if problems:
        print(f'generate --check: {len(problems)} file(s) not as generate.py makes them', file=sys.stderr)
        return 1
    print(f"generate --check: {len(files(LINKML / 'generated'))} file(s) as generate.py makes them")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
