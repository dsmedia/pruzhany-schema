"""The four issue documents and the editions catalog in LinkML (linkml/schema/site_common.yaml,
pages.yaml, content_items.yaml, mentions.yaml, life_events.yaml and editions.yaml).

Checked here: each document is a module of the manifest with its top class; the classes are the
twins' classes by name; every mapping names a term of the pinned standards or a declared local
term; every pattern is the exports' own; the generated JSON Schema of each document has the
export's keys, required keys, enums and patterns, apart from the differences named below and in
known-looser.yaml; a small valid file of each document (fixtures/documents/), which Zod accepts,
is accepted, and each planted fault in it is refused.
"""

import copy
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from functools import cache
from pathlib import Path

import jsonschema
import yaml
from linkml_runtime.utils.schemaview import SchemaView

from support import FIXTURES, LINKML, ROOT, zod_exports

GENERATED = LINKML / 'generated' / 'json-schema'
DOCUMENT_FIXTURES = FIXTURES / 'documents'

# module -> (top class, where pruzhany-steps keeps its Zod export, Zod module, Zod schema)
DOCUMENTS = {
    'pages': ('PagesData', 'schemas/site/pages.schema.json', 'zod/page.schema.ts', 'PagesDataSchema'),
    'content_items': ('ContentItemsData', 'schemas/site-next/content-items.schema.json',
                      'zod/content-item.schema.ts', 'ContentItemsDataSchema'),
    'mentions': ('IssueMentionsData', 'schemas/site-next/mentions.schema.json',
                 'zod/site-issue.schema.ts', 'IssueMentionsDataSchema'),
    'life_events': ('IssueLifeEventsData', 'schemas/site-next/life-events.schema.json',
                    'zod/site-issue.schema.ts', 'IssueLifeEventsDataSchema'),
    # pruzhany-steps keeps no export of the catalog; it is made here as export_zod.ts makes the others.
    'editions': ('EditionsCatalog', None, 'zod/editions.schema.ts', 'EditionsCatalogSchema'),
}
MODULES = ['site_common', *DOCUMENTS]
# Stage two includes the catalog's generated Python models.
NO_PYDANTIC_TWIN = set()
KNOWN = yaml.safe_load((LINKML / 'known-looser.yaml').read_text(encoding='utf-8'))
NAMESPACES = {
    'rico': 'https://www.ica.org/standards/RiC/ontology#',
    'ehri': 'http://lod.ehri-project-test.eu/ontology#',
}


def view(module):
    return SchemaView(str(LINKML / 'schema' / f'{module}.yaml'))


def generated(module):
    return json.loads((GENERATED / f'{module}.schema.json').read_text(encoding='utf-8'))


def fixture(module):
    return json.loads((DOCUMENT_FIXTURES / f'{module}.json').read_text(encoding='utf-8'))


def validator(schema):
    return jsonschema.validators.validator_for(schema)(schema)


def refusals(schema, document):
    return [f'{error.json_path}: {error.message}' for error in validator(schema).iter_errors(document)]


@cache
def zod_export(module):
    """The Zod export of one document's shape: pruzhany-steps' copy made again, or the catalog's."""
    _, export, source, name = DOCUMENTS[module]
    if export is not None:
        return zod_exports()[export]
    return json.loads(_bun(
        "import { z } from 'zod/v4';"
        f"import {{ {name} }} from '{(ROOT / source).as_posix()}';"
        f"console.log(JSON.stringify(z.toJSONSchema({name}, {{ target: 'draft-2020-12', io: 'output' }})));"))


def _bun(code):
    return subprocess.run(['bun', '-e', code], cwd=ROOT, check=True, capture_output=True, text=True).stdout


@cache
def zod_accepts(module):
    """The Zod schema's own verdict on the module's fixture: the list of its issues."""
    _, _, source, name = DOCUMENTS[module]
    path = (DOCUMENT_FIXTURES / f'{module}.json').as_posix()
    return json.loads(_bun(
        f"import {{ {name} }} from '{(ROOT / source).as_posix()}';"
        f"const r = {name}.safeParse(await Bun.file('{path}').json());"
        "console.log(JSON.stringify(r.success ? [] : r.error.issues));"))


# --- What the term lists hold -------------------------------------------------------------

@cache
def pinned_terms():
    """{curie: kind} for every term of the pinned RiC-O and EHRI lists."""
    terms = {}
    for prefix, file in (('rico', 'rico-1.1.json'), ('ehri', 'ehri-0.2.0.json')):
        for term in json.loads((ROOT / 'standards' / file).read_text(encoding='utf-8'))['terms']:
            if term['iri'].startswith(NAMESPACES[prefix]):
                terms[f"{prefix}:{term['iri'][len(NAMESPACES[prefix]):]}"] = term['kind']
    return terms


@cache
def declared_local_terms():
    """{curie: what it is declared as} for every pc: term a vocabulary profile declares."""
    declared = {}
    for path in sorted((ROOT / 'vocabulary').glob('*.ttl')):
        for match in re.finditer(r'^(pc:[A-Za-z0-9_]+) a ([^;]+);', path.read_text(encoding='utf-8'), re.M):
            declared[match.group(1)] = match.group(2).strip()
    return declared


def mapping_faults(module_view):
    """Each mapping of the module's own classes and slots that names no term it may name."""
    pinned, local = pinned_terms(), declared_local_terms()
    faults = []

    def check(where, curie, wanted):
        prefix = curie.split(':', 1)[0]
        if prefix in NAMESPACES:
            kind = pinned.get(curie)
            if kind is None:
                faults.append(f'{where}: {curie} is not in the pinned list')
            elif wanted and not kind.endswith(wanted):
                faults.append(f'{where}: {curie} is a {kind}, not a {wanted}')
        elif prefix == 'pc':
            if curie not in local:
                faults.append(f'{where}: {curie} is declared in no vocabulary profile')
        elif prefix != 'schema':
            faults.append(f'{where}: {curie} has a prefix no mapping here may use')

    elements = []
    for name, cls in module_view.all_classes(imports=False).items():
        elements.append((name, cls, 'class'))
        for slot_name, slot in (cls.attributes or {}).items():
            elements.append((f'{name}.{slot_name}', slot, 'property'))
    for where, element, wanted in elements:
        uri = element.class_uri if wanted == 'class' else element.slot_uri
        if uri:
            check(where, uri, wanted)
        for field in ('exact_mappings', 'close_mappings', 'related_mappings', 'narrow_mappings', 'broad_mappings'):
            for curie in getattr(element, field) or []:
                check(where, curie, None)
    return faults


# --- Generated JSON Schema against the export ---------------------------------------------

def _deref(node, root):
    while isinstance(node, dict) and '$ref' in node:
        node = root['$defs'][node['$ref'].rsplit('/', 1)[-1]]
    return node


def _unwrap(node, root):
    """(the schema without its null branch, whether it allows null, pointer to the branch)."""
    node = _deref(node, root)
    branches = node.get('anyOf') if isinstance(node, dict) else None
    if branches and any(b.get('type') == 'null' for b in branches):
        index, rest = next((i, b) for i, b in enumerate(branches) if b.get('type') != 'null')
        if len(branches) == 2:
            return _deref(rest, root), True, f'/anyOf/{index}'
    if isinstance(node.get('type'), list) and 'null' in node['type']:
        kinds = [kind for kind in node['type'] if kind != 'null']
        return {**node, 'type': kinds[0] if len(kinds) == 1 else kinds}, True, ''
    return node, False, ''


LEAF = ('type', 'pattern', 'enum', 'const', 'minimum', 'maximum', 'exclusiveMinimum', 'minLength', 'maxLength',
        'format', 'minItems', 'maxItems')
GUARD = '(?![\\s\\S])'


def shape_differences(old, new, old_root, new_root, pointer='', out=None):
    """Every difference of the generated schema `new` from the export `old`, as (pointer, kind, detail).

    The pointer is into the export, as known-looser.yaml writes it. A `rules` entry of the
    definition (if/then under allOf) is not compared: the export carries no refinement.
    """
    out = [] if out is None else out
    old, old_null, branch = _unwrap(old, old_root)
    new, new_null, _ = _unwrap(new, new_root)
    if old_null != new_null:
        out.append((pointer, 'null', f'export {old_null}, definition {new_null}'))
    pointer += branch
    if 'properties' in old:
        old_keys, new_keys = set(old['properties']), set(new.get('properties', {}))
        if old_keys != new_keys:
            out.append((pointer, 'keys', f'export only {sorted(old_keys - new_keys)}, '
                                         f'definition only {sorted(new_keys - old_keys)}'))
        old_required, new_required = set(old.get('required', [])), set(new.get('required', []))
        for key in sorted(old_required - new_required):
            out.append((f'{pointer}/properties/{key}', 'not-required', ''))
        for key in sorted(new_required - old_required):
            out.append((f'{pointer}/properties/{key}', 'required', ''))
        if old.get('additionalProperties') is not new.get('additionalProperties'):
            out.append((pointer, 'closed', f"{old.get('additionalProperties')} {new.get('additionalProperties')}"))
        for key in sorted(old_keys & new_keys):
            shape_differences(old['properties'][key], new['properties'][key], old_root, new_root,
                              f'{pointer}/properties/{key}', out)
        return out
    if old.get('type') == 'array' and 'prefixItems' in old:
        out.append((pointer, 'positions', json.dumps([old['prefixItems'], _deref(new.get('items'), new_root),
                                                      new.get('minItems'), new.get('maxItems')])))
        return out
    if old.get('type') == 'array':
        for key in ('minItems', 'maxItems'):
            if old.get(key) != new.get(key):
                out.append((pointer, key, f'{old.get(key)} {new.get(key)}'))
        shape_differences(old.get('items', {}), new.get('items', {}), old_root, new_root, f'{pointer}/items', out)
        return out
    old_leaf = {key: old[key] for key in LEAF if key in old}
    new_leaf = {key: new[key] for key in LEAF if key in new}
    # Exactly 64 digits: the export's length 64 and pattern, the definition's pattern with the guard.
    if (old_leaf.get('minLength') == old_leaf.get('maxLength') == 64 and 'pattern' in old_leaf
            and new_leaf.get('pattern') == old_leaf['pattern'] + GUARD):
        del old_leaf['minLength'], old_leaf['maxLength'], old_leaf['pattern'], new_leaf['pattern']
    if old_leaf != new_leaf:
        out.append((pointer, 'leaf', json.dumps([old_leaf, new_leaf])))
    return out


# Where the definition says more than the export, on purpose (README.md, "Some of it is
# stricter"): each place, the difference the comparison finds there, and why.
STRICTER = {
    ('pages', '/properties/pages/items/properties/page_number', 'leaf'):
        'a whole number, as Pydantic (int) and every real file have it',
    ('pages', '/properties/pages/items/properties/dimensions', 'positions'):
        'two whole numbers, as Pydantic (tuple[int, int]) has them',
    ('pages', '/properties/pages/items/properties/blocks/items/properties/bbox', 'positions'):
        'four whole numbers at least 0: Pydantic says int, the house style bounds a box at 0',
    ('content_items', '/properties/vocabulary_version', 'leaf'):
        'a pattern of the compatible versions in place of an enum: the same values, LinkML lint refuses 1.0.0 as an enum value',
}
# The catalog is not among the exports known-looser.yaml reads; its optional keys that refuse null.
CATALOG_OPTIONAL_NOT_NULLABLE = {
    '/properties/editions/items/properties/holiday',
    '/properties/holidays/items/properties/hebrewName',
    '/properties/historicalEvents/items/properties/endDate',
}


def known(kind):
    entry = next(entry for entry in KNOWN['entries'] if entry['kind'] == kind)
    return {(place['file'], place['pointer']) for place in entry['where']}


def explained(module, difference):
    """Why a difference is allowed, or None when nothing allows it."""
    pointer, kind, detail = difference
    export = DOCUMENTS[module][1]
    if (module, pointer, kind) in STRICTER:
        return STRICTER[(module, pointer, kind)]
    if kind == 'not-required' and (export, pointer) in known('required-key-nullable'):
        return 'known-looser: required-key-nullable'
    if kind == 'null' and (export, pointer) in known('optional-key-not-nullable'):
        return 'known-looser: optional-key-not-nullable'
    if kind == 'null' and module == 'editions' and pointer in CATALOG_OPTIONAL_NOT_NULLABLE:
        return 'optional and not nullable in the catalog, which known-looser.yaml does not read'
    if kind == 'positions':
        positions, items, least, most = json.loads(detail)
        bounded = (export, pointer) in known('position-wise-bounds')
        same = all({key: p[key] for key in p if key != 'exclusiveMinimum'} == {**items, 'minimum': 0}
                   or (bounded and p.get('exclusiveMinimum') == 0 and items == {'type': 'number', 'minimum': 0})
                   for p in positions)
        if least == most == len(positions) and same:
            return 'a box of exactly four numbers each at least 0; known-looser: position-wise-bounds'
    return None


class Manifest(unittest.TestCase):
    def test_each_document_is_a_module_with_its_top_class(self):
        manifest = json.loads((LINKML / 'modules.json').read_text(encoding='utf-8'))['modules']
        entries = {entry['name']: entry for entry in manifest}
        self.assertEqual(entries['site_common'], {'schema': 'schema/site_common.yaml', 'name': 'site_common',
                                                  'top_class': None})
        for module, (top, *_) in DOCUMENTS.items():
            with self.subTest(module=module):
                self.assertEqual(entries[module], {'schema': f'schema/{module}.yaml', 'name': module, 'top_class': top})
                self.assertTrue(view(module).get_class(top).tree_root)
                self.assertTrue((GENERATED / f'{module}.schema.json').is_file())

    def test_each_module_is_under_the_project_namespace_with_its_one_prefix(self):
        for module in MODULES:
            with self.subTest(module=module):
                schema = view(module).schema
                self.assertEqual(schema.id, f'https://pruzhany.org/ns/{module}')
                self.assertEqual(schema.default_prefix, 'pc')
                self.assertEqual(str(schema.prefixes['pc'].prefix_reference), 'https://pruzhany.org/ns/sourced-entities#')


class TheTwinsNames(unittest.TestCase):
    def test_every_class_is_a_class_of_the_twins_by_its_name(self):
        zod = '\n'.join(path.read_text(encoding='utf-8') for path in (ROOT / 'zod').glob('*.ts'))
        pydantic = '\n'.join(path.read_text(encoding='utf-8') for path in (ROOT / 'pydantic').rglob('*.py'))
        for module in MODULES:
            for name in view(module).all_classes(imports=False):
                with self.subTest(module=module, cls=name):
                    self.assertRegex(zod, rf'export const {name}Schema\b')
                    if name not in NO_PYDANTIC_TWIN:
                        self.assertRegex(pydantic, rf'\nclass {name}\(')

    def test_every_class_slot_and_enum_says_what_it_is(self):
        for module in MODULES:
            module_view = view(module)
            for name, cls in module_view.all_classes(imports=False).items():
                self.assertTrue(cls.description and cls.description.strip(), name)
                for slot_name, slot in (cls.attributes or {}).items():
                    self.assertTrue(slot.description and slot.description.strip(), f'{name}.{slot_name}')
            for name, enum in module_view.all_enums(imports=False).items():
                self.assertTrue(enum.description, name)


class Mappings(unittest.TestCase):
    def test_every_mapping_names_a_pinned_term_or_a_declared_local_one(self):
        for module in MODULES:
            with self.subTest(module=module):
                self.assertEqual(mapping_faults(view(module)), [])

    def test_a_planted_unpinned_or_undeclared_term_is_found(self):
        """Control: the check above can fail."""
        text = (LINKML / 'schema' / 'life_events.yaml').read_text(encoding='utf-8')
        for planted, found in (('rico:Event', 'rico:NoSuchEvent is not in the pinned list'),
                               ('rico:Event', 'rico:hasEventType is a object property, not a class'),
                               ('rico:Event', 'pc:site_no_such_term is declared in no vocabulary profile')):
            replacement = found.split(' ', 1)[0]
            with self.subTest(planted=replacement), _scratch_schema(text.replace(f'class_uri: {planted}',
                                                                                 f'class_uri: {replacement}')) as path:
                self.assertIn(f'IssueLifeEvent: {found}', mapping_faults(SchemaView(str(path))))

    def test_the_mappings_written_today(self):
        """A tally, so a mapping that is lost or added shows here as well."""
        counts = {'class_uri': 0, 'slot_uri': 0, 'exact_mappings': 0, 'close_mappings': 0, 'related_mappings': 0,
                  'impresso': 0}
        for module in MODULES:
            for cls in view(module).all_classes(imports=False).values():
                for element in (cls, *(cls.attributes or {}).values()):
                    for field in ('exact_mappings', 'close_mappings', 'related_mappings'):
                        counts[field] += len(getattr(element, field) or [])
                    counts['impresso'] += 'impresso' in element.annotations
                counts['class_uri'] += bool(cls.class_uri)
                counts['slot_uri'] += sum(bool(slot.slot_uri) for slot in (cls.attributes or {}).values())
        self.assertEqual(counts, {'class_uri': 6, 'slot_uri': 13, 'exact_mappings': 9, 'close_mappings': 3,
                                  'related_mappings': 3, 'impresso': 21})


class _scratch_schema:
    """A planted schema file in a copy of linkml/schema/ (so its imports resolve), removed afterwards."""

    def __init__(self, text):
        self.text = text
        self.folder = None

    def __enter__(self):
        self.folder = tempfile.TemporaryDirectory()
        schema = Path(self.folder.name) / 'schema'
        shutil.copytree(LINKML / 'schema', schema)
        path = schema / 'planted.yaml'
        path.write_text(self.text, encoding='utf-8')
        return path

    def __exit__(self, *_):
        self.folder.cleanup()


class Patterns(unittest.TestCase):
    def test_every_pattern_is_one_the_exports_use(self):
        """Character for character: one the exports use, or a regular expression the Zod module writes
        (EnglishCheck's, which no document uses but through its two narrower checks)."""
        patterns = {node['pattern'] for module in DOCUMENTS for node in _nodes(zod_export(module)) if 'pattern' in node}
        patterns |= set(re.findall(r'\.regex\(/(.+?)/\)', (ROOT / 'zod' / 'site-common.schema.ts').read_text(encoding='utf-8')))
        for module in MODULES:
            for name, cls in view(module).all_classes(imports=False).items():
                slots = {**(cls.attributes or {}), **(cls.slot_usage or {})}
                for slot_name, slot in slots.items():
                    if slot.pattern and slot_name != 'vocabulary_version':
                        with self.subTest(slot=f'{name}.{slot_name}'):
                            self.assertIn(slot.pattern, patterns)


def _nodes(node):
    if isinstance(node, dict):
        yield node
        for value in node.values():
            yield from _nodes(value)
    elif isinstance(node, list):
        for value in node:
            yield from _nodes(value)


class AgainstTheExports(unittest.TestCase):
    def test_the_generated_shape_is_the_export_but_for_what_is_named(self):
        unexplained, found = [], set()
        for module in DOCUMENTS:
            export, made = zod_export(module), generated(module)
            for difference in shape_differences(export, made, export, made):
                reason = explained(module, difference)
                if reason is None:
                    unexplained.append((module, *difference))
                found.add((module, difference[0], difference[1]))
        self.assertEqual(unexplained, [])
        self.assertEqual({key for key in STRICTER if key not in found}, set(), 'a stricter place is gone')

    def test_a_planted_difference_is_found_and_not_explained(self):
        """Control: a key dropped, a required key made optional and an enum value lost are each reported."""
        export = zod_export('mentions')
        made = copy.deepcopy(generated('mentions'))
        mention = made['$defs']['IssueMention']
        del mention['properties']['function']
        mention['required'].remove('person_id')
        made['$defs']['AddressGrain']['enum'].remove('regions')
        differences = [d for d in shape_differences(export, made, export, made) if explained('mentions', d) is None]
        kinds = sorted(kind for _, kind, _ in differences)
        self.assertEqual(kinds, ['keys', 'leaf', 'not-required'])


class Fixtures(unittest.TestCase):
    def test_each_fixture_is_accepted_by_zod_and_by_the_definition(self):
        for module in DOCUMENTS:
            with self.subTest(module=module):
                self.assertEqual(zod_accepts(module), [])
                self.assertEqual(refusals(generated(module), fixture(module)), [])


def _set(path, value):
    def plant(document):
        *parents, last = path
        node = document
        for part in parents:
            node = node[part]
        if value is _DELETE:
            del node[last]
        else:
            node[last] = value
    return plant


def _rename(path, old, new):
    def plant(document):
        node = document
        for part in path:
            node = node[part]
        node[new] = node.pop(old)
    return plant


_DELETE = object()
ITEM = ('content_items', 0)
TITLE_CHECK = (*ITEM, 'supplied_title', 'checked_against')
ADDRESS = (*ITEM, 'printed_title', 'addresses', 0)
BLOCK = ('pages', 0, 'blocks', 0)

# Each fault planted in a fixture, which the definition's JSON Schema must refuse.
PLANTED = {
    'pages': {
        'a page without its picture': _set(('pages', 0, 'image_uri'), _DELETE),
        'a page number with a fraction': _set(('pages', 0, 'page_number'), 1.5),
        'three dimensions': _set(('pages', 0, 'dimensions'), [3200, 4794, 1]),
        'a box of three numbers': _set((*BLOCK, 'bbox'), [1, 2, 3]),
        'a box of five numbers': _set((*BLOCK, 'bbox'), [1, 2, 3, 4, 5]),
        'a box with a fraction': _set((*BLOCK, 'bbox'), [1.5, 2, 3, 4]),
        'a box left of the picture': _set((*BLOCK, 'bbox'), [-1, 2, 3, 4]),
        'a region without its words': _set((*BLOCK, 'transcription'), _DELETE),
        'a key no shape has': _set((*BLOCK, 'words'), []),
    },
    'content_items': {
        'an unknown vocabulary version': _set(('vocabulary_version',), '1.2.0'),
        'a version with a line end after it': _set(('vocabulary_version',), '1.0.0\n'),
        'an issue date written otherwise': _set(('issue_date',), '16.12.1938'),
        'a blank content item id': _set((*ITEM, 'id'), ' '),
        'a type Impresso does not have': _set((*ITEM, 'type'), 'novel'),
        'a subject outside the vocabulary': _set((*ITEM, 'subject_ids'), ['weather']),
        'no regions': _set((*ITEM, 'page_blocks'), []),
        'a page reference with no region': _set((*ITEM, 'page_blocks', 0, 'block_ids'), []),
        'a negative block break': _set((*ITEM, 'block_breaks'), [-1]),
        'a block break with a fraction': _set((*ITEM, 'block_breaks'), [0.5]),
        'no supplied title': _set((*ITEM, 'supplied_title'), _DELETE),
        'a supplied title in Yiddish': _set((*ITEM, 'supplied_title', 'language'), 'yi'),
        'a title check judging the text': _set((*TITLE_CHECK, 'judgement_id'), 'judgement-1:text'),
        'a translation check judging the title':
            _set((*ITEM, 'translation', 'checked_against', 'judgement_id'), 'judgement-1:title'),
        'a judgement id with a space': _set((*TITLE_CHECK, 'judgement_id'), 'judgement 1:title'),
        'a judgement id with a line end after it': _set((*TITLE_CHECK, 'judgement_id'), 'judgement-1:title\n'),
        'a digest of 63 digits': _set((*TITLE_CHECK, 'reading_sha256'), 'a' * 63),
        'a digest in capitals': _set((*TITLE_CHECK, 'english_sha256'), 'A' * 64),
        'a check by neither a person nor a model': _set((*TITLE_CHECK, 'attribution', 'kind'), 'committee'),
        'an attribution without its day': _set((*ITEM, 'translation', 'attribution', 'on'), _DELETE),
        'a blank author': _set((*ITEM, 'translation', 'attribution', 'by'), ' '),
        'a printed title with no address': _set((*ITEM, 'printed_title', 'addresses'), []),
        'a box left of the picture': _set((*ADDRESS, 'bbox'), [-1, 200, 400, 30]),
        'an address of three numbers': _set((*ADDRESS, 'bbox'), [100, 200, 400]),
        'an address without its words': _set((*ADDRESS, 'text'), _DELETE),
        'a basis with no address': _set((*ITEM, 'supplied_title', 'based_on', 'addresses'), []),
        'a reading status outside the vocabulary': _set((*ITEM, 'reading_status', 'text'), 'checked'),
        'a cross-reference without its evidence': _set((*ITEM, 'cross_references', 0, 'evidence'), _DELETE),
        'a section with no content item': _set(('sections', 0, 'content_item_ids'), []),
        'a section without its printed title': _set(('sections', 0, 'printed_title'), None),
        'a key no shape has': _set((*ITEM, 'words'), []),
    },
    'mentions': {
        'a mention with no role': _set(('mentions', 0, 'roles'), []),
        'a role outside the vocabulary': _set(('mentions', 0, 'roles'), ['bystander']),
        'a grain other than words or regions': _set(('mentions', 0, 'address_grain'), 'letters'),
        'a blank printed name': _set(('mentions', 0, 'printed_name'), '  '),
        'no address': _set(('mentions', 0, 'addresses'), []),
        'no person': _set(('mentions', 0, 'person_id'), _DELETE),
        'a key no shape has': _set(('mentions', 0, 'unit_id'), 'cu-1'),
    },
    'life_events': {
        'a life event printed by no content item': _set(('life_events', 0, 'content_items'), []),
        'a part outside the vocabulary': _set(('life_events', 0, 'content_items', 0, 'role'), 'witness'),
        'a blank event id': _set(('life_events', 0, 'id'), ''),
    },
    'editions': {
        'a fourteenth month': _set(('editions', 0, 'hebrewMonth'), 14),
        'month nought': _set(('editions', 0, 'hebrewMonth'), 0),
        'a year with a fraction': _set(('editions', 0, 'hebrewYear'), 5699.5),
        'a key written in snake case': _rename(('editions', 0), 'hebrewDate', 'hebrew_date'),
        'an available date written otherwise': _set(('availableDates',), ['16.12.1938']),
        'a historical event without its description': _set(('historicalEvents', 0, 'description'), _DELETE),
        'no list of historical events': _set(('historicalEvents',), _DELETE),
    },
}


class PlantedFaults(unittest.TestCase):
    def test_each_planted_fault_is_refused(self):
        for module, plants in PLANTED.items():
            schema = generated(module)
            for name, plant in plants.items():
                document = copy.deepcopy(fixture(module))
                plant(document)
                with self.subTest(module=module, fault=name):
                    self.assertNotEqual(refusals(schema, document), [])


if __name__ == '__main__':
    unittest.main()
