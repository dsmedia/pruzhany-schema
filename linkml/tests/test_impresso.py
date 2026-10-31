"""Issue and rebuilt-content contracts preserve each field and Impresso's edges.

Read 31 October 2026: Impresso README and the three schemas at master 329323c;
LinkML JSON Schema, Slots, Advanced features and Arrays documentation.
https://linkml.io/linkml/generators/json-schema.html
The oracle is the unchanged, licensed standards pin; fixtures are fictional.
"""

import copy
import itertools
import json
import unittest

from linkml_runtime.utils.schemaview import SchemaView

from support import FIXTURES, LINKML, ROOT, load
from test_physical import at, validator, MISSING

PIN = ROOT / 'standards/impresso-329323c'
CASES = {
    'issue': ('impresso_issue', 'issue.schema.json', {
        'ImpressoIssue': (),
        'ImpressoIssueItem': ('i', 0),
        'ImpressoMetadata': ('i', 0, 'm'),
        'ImpressoLegacy': ('i', 0, 'l'),
        'ImpressoLegacyPart': ('i', 0, 'l', 'parts', 0),
        'ImpressoIssueSection': ('i', 0, 'section_title'),
        'ImpressoStyle': ('s', 0),
    }),
    'contentitem': ('impresso_contentitem', 'paper_contentitem.schema.json', {
        'ImpressoContentItem': (),
        'ImpressoContentSection': ('section_title',),
        'ImpressoRebuiltPage': ('ppreb', 0),
        'ImpressoRebuiltToken': ('ppreb', 0, 't', 0),
    }),
}


def resolve(node, root):
    if '$ref' in node:
        return resolve(at(root, node['$ref'][2:].split('/')), root)
    return node


def shape(node, root):
    """Normalize local field constraints, independently of generated class conditions."""
    node = resolve(node, root)
    if 'anyOf' in node and 'properties' not in node:  # Nullable bounded quality score.
        node = {**node['anyOf'][0], 'type': [node['anyOf'][0]['type'], 'null']}
    if 'oneOf' in node and 'properties' not in node:  # Nullable language code.
        node = {**resolve(node['oneOf'][1], root), 'type': ['string', 'null']}
    result = {key: value for key, value in node.items()
              if key not in {'$schema', '$id', '$defs', 'metamodel_version', 'version', 'description', 'title', 'allOf', 'oneOf',
                             'dependentRequired', 'anyOf', 'additionalProperties', 'required', 'properties', 'items'}}
    if result.get('minItems') == 0:  # Explicit zero and absence have identical meaning.
        result.pop('minItems')
    if 'type' in result:
        types = result['type'] if isinstance(result['type'], list) else [result['type']]
        if 'enum' in result and None not in result['enum']:
            types = [t for t in types if t != 'null']
        result['type'] = sorted(types)
    if 'properties' in node:
        result['properties'] = {key: shape(value, root) for key, value in node['properties'].items()}
        result['required'] = sorted(node.get('required', []))
        result['additionalProperties'] = node.get('additionalProperties', True)
    if 'items' in node:
        result['items'] = shape(node['items'], root)
    return result


class ImpressoContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = {}
        cls.checkers = {}
        for kind, (module, oracle, paths) in CASES.items():
            upstream = json.loads((PIN / oracle).read_text())
            made = json.loads((LINKML / f'generated/json-schema/{module}.schema.json').read_text())
            fixture = json.loads((FIXTURES / f'physical/{kind}.json').read_text())
            cls.cases[kind] = (upstream, made, fixture, paths)
            cls.checkers[kind] = (validator(upstream), validator(made))

    def agree(self, kind, document, expected=None):
        upstream, made = self.checkers[kind]
        original = upstream.is_valid(document)
        self.assertEqual(made.is_valid(document), original)
        if expected is not None:
            self.assertEqual(original, expected)

    def test_fictional_fixtures_and_field_by_field_equality(self):
        for kind, (upstream, made, fixture, paths) in self.cases.items():
            self.agree(kind, fixture, True)
            module = CASES[kind][0]
            view = SchemaView(str(LINKML / f'schema/{module}.yaml'))
            inventory = json.loads((LINKML / f'generated/external/{module}/contract.json').read_text())
            self.assertEqual(set(inventory['classes']), set(paths))
            self.assertEqual(set(view.all_classes(imports=False)), set(paths))
            self.assertEqual(shape(upstream, upstream), shape(made, made))
            for name, path in paths.items():
                with self.subTest(kind=kind, cls=name):
                    self.assertEqual({slot.alias or slot.name for slot in view.class_induced_slots(name)},
                                     set(made['$defs'][name]['properties']))
                    for element in (view.get_class(name), *view.class_induced_slots(name)):
                        self.assertTrue(element.description)
                        self.assertIn('impresso', element.annotations)

    def test_each_stored_field_absence_null_types_bounds_and_unknown_properties(self):
        values = (MISSING, None, True, False, -1, 0, 0.5, 1, 2, {}, [], '', '\n', 'invented',
                  'en', 'eng', 'EN', '1900-01-01T00:00:00Z', [None], [1], [''],
                  [0, 0, 1, 2], [0, 0, 1, 2, 3], [[0, 0, 1, 2]], [1, {}, None])
        for kind, (_, _, fixture, paths) in self.cases.items():
            for path in paths.values():
                for key in at(fixture, path):
                    for value in values:
                        document = copy.deepcopy(fixture)
                        target = at(document, path)
                        target.pop(key)
                        if value is not MISSING:
                            target[key] = value
                        with self.subTest(kind=kind, path=path, key=key, value=repr(value)):
                            self.agree(kind, document)
                document = copy.deepcopy(fixture)
                at(document, path)['unknown'] = {'anything': [None, {}, 7]}
                self.agree(kind, document, True)

    def test_issue_timestamp_source_dependencies_and_metadata_alternatives(self):
        for timestamp, legacy in itertools.product((MISSING, None, '', '1900-01-01T00:00:00Z'), repeat=2):
            doc = {'id': 'FABLE-1900-01-01-a', 'i': []}
            for key, value in (('ts', timestamp), ('cdt', legacy)):
                if value is not MISSING:
                    doc[key] = value
            self.agree('issue', doc)
        for source, medium, pages, records, olr in itertools.product(
                (MISSING, 'newspaper', 'radio_broadcast'), (MISSING, 'print', 'typescript', 'audio'),
                (False, True), (False, True), (False, True)):
            doc = {'id': 'FABLE-1900-01-01-a', 'i': [{}], 'cdt': ''}
            for key, value in (('st', source), ('sm', medium),
                               ('pp', [] if pages else MISSING), ('rr', [] if records else MISSING),
                               ('olr', False if olr else MISSING)):
                if value is not MISSING:
                    doc[key] = value
            self.agree('issue', doc)
        fixture = self.cases['issue'][2]
        for pages, records in itertools.product((False, True), repeat=2):
            doc = copy.deepcopy(fixture)
            metadata = doc['i'][0]['m']
            metadata.pop('pp')
            if pages:
                metadata['pp'] = []
            if records:
                metadata['rr'] = []
            self.agree('issue', doc, pages != records)
        # lg is required yet null is accepted; tp's enum excludes null despite its type.
        self.agree('issue', fixture, True)
        doc = copy.deepcopy(fixture)
        doc['i'][0]['m']['tp'] = None
        self.agree('issue', doc, False)

    def test_content_radio_condition_also_applies_when_source_is_absent(self):
        for source, order in itertools.product((MISSING, 'newspaper', 'radio_broadcast'),
                                              (MISSING, None, 0, 1, 2)):
            doc = {'id': 'FABLE-1900-01-01-a-i0001', 'tp': None, 'olr': False,
                   'ts': '1900-01-01T00:00:00Z'}
            if source is not MISSING:
                doc.update(st=source, sm='print')
            if order is not MISSING:
                doc['ro'] = order
            self.agree('contentitem', doc, order is MISSING or
                       (type(order) is int and (order == 1 or source == 'newspaper')))

    def test_every_metadata_dependency_is_enforced_on_minimal_controls(self):
        for trigger, needs in (('consolidated_reocr_run_id',
                               ('consolidated_reocr_applied', 'consolidated_ocrqa', 'consolidated_char_len')),
                               ('consolidated_lg', ('consolidated_langident_run_id',))):
            for present in itertools.product((False, True), repeat=len(needs)):
                metadata = {'id': 'FABLE-1900-01-01-a-i0001', 'tp': 'article', 'lg': None,
                            'pp': [], trigger: 'en' if trigger == 'consolidated_lg' else ''}
                values = {'consolidated_reocr_applied': False, 'consolidated_ocrqa': None,
                          'consolidated_char_len': None, 'consolidated_langident_run_id': ''}
                for name, keep in zip(needs, present):
                    if keep:
                        metadata[name] = values[name]
                self.agree('issue', {'id': 'FABLE-1900-01-01-a', 'cdt': '',
                                     'i': [{'m': metadata}]}, all(present))


class WireAnnotations(unittest.TestCase):
    def test_unsupported_annotations_refuse_instead_of_erasing_constraints(self):
        from linkml.generators.jsonschemagen import SlotResult
        from linkml_runtime.linkml_model import ClassDefinition, SlotDefinition
        external = load('external_schema')
        cases = (
            ({'json_types': 'string'}, {'type': 'string'}),
            ({'json_types': 'string,string'}, {'type': 'string'}),
            ({'json_types': 'string,alien'}, {'type': 'string'}),
            ({'json_types': 'string,array'}, {'type': 'string', 'pattern': '^x'}),
            ({'json_item_types': 'object,string'}, {'type': 'string'}),
            ({'json_min_length': '-1'}, {'type': 'string'}),
            ({'json_min_length': '1.5'}, {'type': 'string'}),
            ({'json_min_length': '1'}, {'type': 'integer'}),
        )
        for settings, shape in cases:
            slot = SlotDefinition('value', annotations=settings)
            view = type('View', (), {'induced_slot': lambda *args: slot})()
            with self.subTest(settings=settings, shape=shape), self.assertRaises(ValueError):
                external.ExplicitNullGenerator.after_generate_class_slot(
                    None, SlotResult.model_construct(source=slot, schema_=shape),
                    ClassDefinition('Test'), view)
