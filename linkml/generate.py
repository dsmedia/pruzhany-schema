"""Make what linkml/modules.json lists from the LinkML definition, or check what is committed.

    python -I linkml/generate.py           make linkml/generated/ afresh
    python -I linkml/generate.py --check   make it in a temporary folder and compare; exit 1,
                                           naming each file that differs, is missing or is extra

Run it in the linkml step's locked environment (bin/verify linkml). Each module of the
manifest gives its documentation under generated/docs/<name>/ (gen-doc) and, when it names a
top class, generated/json-schema/<name>.schema.json (gen-json-schema with that one top class,
closed by default; explicit extra_slots controls external formats). One top class a file,
because one JSON Schema with several roots merges their top-level rules (the review package's traps).

Every file is written as UTF-8 with "\\n" line ends, whatever the machine, and LinkML 1.12.1
stamps no date unless asked (its --generation-date is off by default) and no path of this
machine; so a second run, or a run on Windows, gives the same bytes.
"""

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
from pathlib import Path

from linkml.generators.docgen import DocGenerator
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml_runtime.utils.schemaview import SchemaView
import yaml

# Loaded by path because this command deliberately runs with python -I.
import importlib.util
_python_spec = importlib.util.spec_from_file_location('python_generator', Path(__file__).with_name('python_generator.py'))
_python_backend = importlib.util.module_from_spec(_python_spec)
_python_spec.loader.exec_module(_python_backend)
_learning_spec = importlib.util.spec_from_file_location('learning_index', Path(__file__).with_name('learning_index.py'))
_learning_backend = importlib.util.module_from_spec(_learning_spec)
_learning_spec.loader.exec_module(_learning_backend)
_rdf_spec = importlib.util.spec_from_file_location('rdf_generator', Path(__file__).with_name('rdf_generator.py'))
_rdf_backend = importlib.util.module_from_spec(_rdf_spec)
_rdf_spec.loader.exec_module(_rdf_backend)
_external_spec = importlib.util.spec_from_file_location('external_schema', Path(__file__).with_name('external_schema.py'))
_external_backend = importlib.util.module_from_spec(_external_spec)
_external_spec.loader.exec_module(_external_backend)

LINKML = Path(__file__).resolve().parent


def modules(linkml_dir):
    """The manifest: each entry names a schema file, its top class (or null) and an output name."""
    manifest = json.loads((linkml_dir / 'modules.json').read_text(encoding='utf-8'))
    entries = manifest['modules']
    names = [entry['name'] for entry in entries]
    if len(set(names)) != len(names):
        raise SystemExit('linkml/modules.json: an output name is used twice')
    for entry in entries:
        if 'external_contract' in entry and (entry['external_contract'] != 'impresso-page'
                                              or not entry['top_class']):
            raise ValueError('unsupported external contract or missing top class')
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
            # read 28 October 2026, re-read 29 October: closed by default; optional slots
            # accept null. The external adapter honors explicitly declared null policy.
            text = _external_backend.generator(schema, entry['top_class']).serialize()
            write_text(destination / 'json-schema' / f"{entry['name']}.schema.json", text)
        # gen-doc writes its own files with the machine's line ends; they are made in a
        # scratch folder and written again here with "\n".
        with tempfile.TemporaryDirectory() as scratch:
            DocGenerator(schema, directory=scratch, truncate_descriptions=False).serialize()
            for made in sorted(Path(scratch).rglob('*')):
                if made.is_file():
                    target = destination / 'docs' / entry['name'] / made.relative_to(scratch)
                    write_text(target, made.read_text(encoding='utf-8'))
    build_index_and_dictionary(linkml_dir, destination)


def schema_index(linkml_dir, destination):
    """Every owned site class, including maps and non-roots; external inventories are separate."""
    # The site twins' contract remains complete for the site. An external wire contract
    # has its own complete inventory and upstream comparison, rather than acquiring
    # site Zod/Pydantic models the consumers do not use.
    entries = [entry for entry in modules(linkml_dir) if 'external_contract' not in entry]
    views = [(entry, SchemaView(str(linkml_dir / entry['schema']))) for entry in entries]
    definitions = {}
    for path in sorted(destination / 'json-schema' / f"{entry['name']}.schema.json"
                       for entry in entries if entry['top_class']):
        for name, definition in json.loads(path.read_text(encoding='utf-8')).get('$defs', {}).items():
            if name in definitions and definitions[name] != definition:
                raise ValueError(f'{name}: generated definitions differ between document roots')
            definitions[name] = definition
    owned = {name: entry['schema'] for entry, view in views for name in view.all_classes(imports=False)}
    for name, source in sorted(owned.items()):
        if name not in definitions:
            made = json.loads(JsonSchemaGenerator(str(linkml_dir / source), top_class=name,
                                                   not_closed=False).serialize())
            for extra, definition in made['$defs'].items():
                if extra in definitions and definitions[extra] != definition:
                    raise ValueError(f'{extra}: generated definitions differ for standalone {name}')
                definitions[extra] = definition
    known_path = linkml_dir / 'known-looser.yaml'
    known = yaml.safe_load(known_path.read_text(encoding='utf-8')) if known_path.exists() else {'entries': []}
    index = {'$schema': 'https://json-schema.org/draft/2019-09/schema', '$defs': definitions,
             'classes': owned, 'known_looser': known['entries']}
    write_text(destination / 'contract.json', json.dumps(index, ensure_ascii=False, indent=2, sort_keys=True))
    return views, index


def prose(value):
    return ' '.join(str(value or '').split()).replace('|', r'\|')


def mappings(element):
    found = []
    for key in ('class_uri', 'slot_uri', 'meaning', 'exact_mappings', 'close_mappings',
                'related_mappings', 'narrow_mappings', 'broad_mappings'):
        value = getattr(element, key, None)
        if value:
            values = value if isinstance(value, list) else [value]
            found.extend(f'{prose(v)} ({key.replace("_", " ")})' for v in values)
    annotations = getattr(element, 'annotations', {}) or {}
    if 'via' in annotations:
        found.append('via ' + prose(annotations['via'].value))
    return '; '.join(found) or 'No direct mapping recorded'


def value_shape(slot):
    parts = [str(getattr(slot, 'range', None) or getattr(slot, 'typeof', None) or 'string')]
    if getattr(slot, 'multivalued', False):
        parts[0] = 'list of ' + parts[0]
    for key, label in (
        ('minimum_cardinality', 'minimum items'), ('maximum_cardinality', 'maximum items'),
        ('minimum_value', 'minimum'), ('maximum_value', 'maximum'),
        ('pattern', 'pattern'), ('equals_string', 'fixed value'), ('equals_string_in', 'one of'),
    ):
        value = getattr(slot, key, None)
        if value is not None and value != []:
            parts.append(f'{label}: {value}')
    return prose('; '.join(parts))


def read_planned(linkml_dir):
    path = linkml_dir / 'planned.yaml'
    if not path.exists():
        return []
    entries = yaml.safe_load(path.read_text(encoding='utf-8'))['items']
    seen = set()
    for entry in entries:
        if entry['id'] in seen or not entry.get('summary'):
            raise ValueError('planned requirements need distinct IDs and a summary')
        seen.add(entry['id'])
        source = entry['source']
        if not source.get('file') or not source.get('quote') or not isinstance(source.get('line'), int):
            raise ValueError(f"{entry['id']}: planned requirement needs a source line and quote")
    return entries


def build_index_and_dictionary(linkml_dir, destination):
    views, index = schema_index(linkml_dir, destination)
    _learning_backend.write_index(linkml_dir, destination, views, index, write_text)
    if json.loads((linkml_dir / 'modules.json').read_text(encoding='utf-8')).get('rdf_profile'):
        _rdf_backend.write_rdf(linkml_dir, destination,
                               _learning_backend.build_index(linkml_dir, views, index), index, write_text)
    for entry in modules(linkml_dir):
        if 'external_contract' not in entry:
            continue
        view = SchemaView(str(linkml_dir / entry['schema']))
        document = json.loads((destination / 'json-schema' / f"{entry['name']}.schema.json").read_text())
        external = {'$schema': document['$schema'], '$defs': document['$defs'],
                    'classes': {name: entry['schema'] for name in view.all_classes(imports=False)},
                    'known_looser': [], 'external_contract': entry['external_contract']}
        external_dir = destination / 'external' / entry['name']
        write_text(external_dir / 'contract.json', json.dumps(external, ensure_ascii=False, indent=2, sort_keys=True))
        _learning_backend.write_index(linkml_dir, external_dir, [(entry, view)], external, write_text)
        views.append((entry, view))  # All layers appear in the human data dictionary.
    planned = read_planned(linkml_dir)  # Never passed to SchemaView or a schema generator.
    sources = sorted((linkml_dir / 'schema').glob('*.yaml'))
    sources += [p for p in (linkml_dir / 'planned.yaml', linkml_dir / 'known-looser.yaml') if p.exists()]
    digest = hashlib.sha256(b''.join(p.name.encode() + b'\0' + p.read_bytes() for p in sources)).hexdigest()
    lines = [
        '# The Pruzhany data dictionary', '',
        'This is the guide to the data behind the Pruzhany newspaper: its pages and pieces, '
        'the people and events it names, and the evidence for what we say about them.', '',
        'LinkML defines the kinds and fields below and generates the Python models. '
        'The website’s Zod validators and the retained Python checks still enforce the '
        'rules about evidence, dates, relationships and publication. Passing a schema checks '
        'the form of a record, not whether a reading or '
        'historical claim is correct. Identity, trust, rights and release readiness have their '
        'own requirements in the record catalog.', '',
        'The four issue documents, the editions catalog and the shared record each have a '
        'generated JSON Schema. The shared record is checked after its 256 storage shards '
        'have been joined. Stored identifiers and file shapes are unchanged.', '',
        '“Required” in the tables means required by LinkML. Some runtime validators require '
        'a key while accepting null; those differences are listed under “Validator responsibilities”. '
        'An optional LinkML field generally also accepts null. Value ranges named in the '
        'tables are defined in “Types and vocabularies”. Mappings describe alignment with '
        'the pinned EHRI and RiC-O terms; they do not claim EHRI acceptance.', '',
        f'Definition fingerprint: `{digest}`.', '',
    ]
    for entry, view in views:
        classes = view.all_classes(imports=False)
        if not classes:
            continue
        lines += [f"## {prose(view.schema.title or entry['name'].replace('_', ' '))}", '']
        for name, cls in sorted(classes.items()):
            lines += [f'### {name}', '', prose(cls.description), '',
                      f'Meaning: {mappings(cls)}.', '',
                      '| Field | What it holds | Value | Required | Standard mapping |',
                      '| --- | --- | --- | --- | --- |']
            for slot in sorted(view.class_induced_slots(name), key=lambda s: s.alias or s.name):
                lines.append(f'| `{slot.alias or slot.name}` | {prose(slot.description)} | '
                             f'{value_shape(slot)} | {"Yes" if slot.required else "No"} | {mappings(slot)} |')
            if not view.class_induced_slots(name):
                lines.append('| Arbitrary keys | A dictionary of named text values | string values | No fixed keys | No direct mapping recorded |')
            lines += ['', f"Source: `linkml/{entry['schema']}`.", '']
    lines += ['## Types and vocabularies', '']
    for entry, view in views:
        for name, typ in sorted(view.all_types(imports=False).items()):
            lines += [f'### {name}', '', prose(typ.description), '', value_shape(typ), '']
        for name, enum in sorted(view.all_enums(imports=False).items()):
            lines += [f'### {name}', '', prose(enum.description), '',
                      '| Value | Meaning | Standard mapping |', '| --- | --- | --- |']
            for value, term in enum.permissible_values.items():
                lines.append(f'| `{prose(value)}` | {prose(term.description)} | {mappings(term)} |')
            lines.append('')
    lines += ['## Validator responsibilities', '',
              'The following measured differences are checked by `record compare linkml`. '
              'Its report must exercise every listed place, accept every real document and '
              'pass the bundled Zod archive and catalog checks. The generated Python models '
              'also validate every document and the complete archive. Python-specific API '
              'adjustments are recorded in `linkml/python-compatibility.json`, each with '
              'synthetic witnesses; retained rules still check dates, uniqueness and agreement '
              'between records.', '']
    for entry in index['known_looser']:
        lines += [f"### {entry['kind'].replace('-', ' ').capitalize()}", '', prose(entry['why']), '',
                  prose(entry['linkml_says']), '', 'Enforced by:', '']
        lines += ['- ' + prose(source) for source in entry['enforced_by']]
        lines += ['', 'Exact places:', '']
        lines += [f"- `{p['file']}#{p['pointer']}`" for p in entry['where']]
        lines.append('')
    lines += ['The complete refinement inventory is in `linkml/checks/documents.yaml` and '
              '`linkml/checks/record.yaml`. Rules about uniqueness, agreement between files, '
              'citation content and identity remain with the validators and record rule catalog.', '',
              '## Requirements still planned', '',
              'These are requirements recorded by the project, not extra fields accepted by '
              'the schemas. Existing family records, word boxes and corrections are not being '
              'declared absent; the gaps below describe what remains to complete their contracts.', '']
    for entry in planned:
        source = entry['source']
        lines += [f"### {entry['title']}", '', prose(entry['summary']), '',
                  f"Source: `{source['root']}:{source['file']}:{source['line']}` — “{prose(source['quote'])}”.", '']
    write_text(destination / 'docs' / 'data-dictionary.md', '\n'.join(lines))


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
        python = _python_backend.build_python(linkml_dir, json.loads(fresh['contract.json'])) if (linkml_dir / 'python-compatibility.json').exists() else None
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
    if python is not None:
        actual = {name: data for name, data in files(linkml_dir.parent / 'pydantic' / 'generated').items()
                  if '__pycache__' not in name.split('/')}
        expected = {name: text.encode('utf-8') for name, text in python.items()}
        for name in sorted(expected.keys() | actual.keys()):
            if expected.get(name) != actual.get(name):
                problems.append(f'pydantic/generated/{name}: missing, extra or differs from generation')
    return problems


def regenerate(linkml_dir):
    """Replace linkml/generated/ with what the definition makes now, removing stale files."""
    with tempfile.TemporaryDirectory() as scratch:
        build(linkml_dir, Path(scratch))
        python = _python_backend.build_python(linkml_dir, json.loads((Path(scratch) / 'contract.json').read_text())) if (linkml_dir / 'python-compatibility.json').exists() else None
        target = linkml_dir / 'generated'
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(scratch, target)
        if python is not None:
            target = linkml_dir.parent / 'pydantic' / 'generated'
            if target.exists():
                shutil.rmtree(target)
            for name, content in python.items():
                write_text(target / name, content)


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
