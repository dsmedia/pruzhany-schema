"""The physical contract agrees with Impresso, including its permissive edges.

The upstream oracle is pinned locally so CI needs neither network nor private data.
Every real page is also checked when a steps checkout has editions/: PRUZHANY_STEPS,
otherwise pruzhany-steps beside this checkout or any of its parents. Diagnostics
contain only ordinal numbers and schema paths, never private text or record values.
"""

import copy
import hashlib
import itertools
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from jsonschema.validators import validator_for
from linkml_runtime.utils.schemaview import SchemaView

from support import FIXTURES, LINKML, ROOT, load

FOLDER = FIXTURES / 'physical'
ORACLE_PATH = ROOT / 'standards/impresso-329323c/page.schema.json'
ORACLE = json.loads(ORACLE_PATH.read_text(encoding='utf-8'))
GENERATED = json.loads((LINKML / 'generated/json-schema/physical.schema.json').read_text(encoding='utf-8'))
PAGE = json.loads((FOLDER / 'page.json').read_text(encoding='utf-8'))
VIEW = SchemaView(str(LINKML / 'schema/physical.yaml'))
EXTERNAL = load('external_schema')
MISSING = object()


def validator(schema):
    cls = validator_for(schema)
    cls.check_schema(schema)
    return cls(schema, format_checker=cls.FORMAT_CHECKER)


def steps_checkout():
    explicit = os.environ.get('PRUZHANY_STEPS')
    if explicit:
        return Path(explicit)
    return next((parent / 'pruzhany-steps' for parent in (ROOT, *ROOT.parents)
                 if (parent / 'pruzhany-steps/editions').is_dir()), None)


def at(document, path):
    for key in path:
        document = document[key]
    return document


class PhysicalContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.upstream = validator(ORACLE)
        cls.generated = validator(GENERATED)

    def agree(self, document, expected=None):
        original = self.upstream.is_valid(document)
        self.assertEqual(self.generated.is_valid(document), original)
        if expected is not None:
            self.assertEqual(original, expected)

    def test_oracle_pin_and_fictional_fixture(self):
        self.assertEqual(hashlib.sha256(ORACLE_PATH.read_bytes()).hexdigest(),
                         'b6a6ca37167b30d318eb175a844dc50c80d245f9753ddc279a5e198b47f53b2c')
        self.agree(PAGE, True)

    def test_every_class_field_required_key_and_mapping_is_accounted_for(self):
        paths = {
            'PhysicalPage': (),
            'PhysicalRegion': ('properties', 'r', 'items'),
            'PhysicalParagraph': ('properties', 'r', 'items', 'properties', 'p', 'items'),
            'PhysicalLine': ('properties', 'r', 'items', 'properties', 'p', 'items', 'properties', 'l', 'items'),
            'PhysicalWord': ('properties', 'r', 'items', 'properties', 'p', 'items', 'properties', 'l',
                             'items', 'properties', 't', 'items'),
        }
        self.assertEqual(set(VIEW.all_classes(imports=False)), set(paths))
        inventory = json.loads((LINKML / 'generated/external/physical/contract.json').read_text())
        learning = json.loads((LINKML / 'generated/external/physical/docs/model-index.json').read_text())
        self.assertEqual(set(inventory['classes']), set(paths))
        self.assertEqual(set(learning['models']), set(paths))
        for name, path in paths.items():
            with self.subTest(cls=name):
                source, made = at(ORACLE, path), GENERATED['$defs'][name]
                self.assertEqual(set(source['properties']), set(made['properties']))
                self.assertEqual(set(source['required']), set(made['required']))
                self.assertIs(made['additionalProperties'], True)
                cls = VIEW.get_class(name)
                for element in (cls, *VIEW.class_induced_slots(name)):
                    self.assertTrue(element.description)
                    self.assertIn('impresso', element.annotations)
                    self.assertIn('alto', element.annotations)
                fields = {slot.alias or slot.name for slot in VIEW.class_induced_slots(name)}
                self.assertEqual(fields, set(source['properties']))
        # A box stays an array. Computed ids are metadata, never new stored properties.
        box = GENERATED['$defs']['PhysicalWord']['properties']['c']
        self.assertEqual({k: v for k, v in box.items() if k != 'description'},
                         {'type': 'array', 'items': {'type': 'integer'}, 'minItems': 4, 'maxItems': 4})
        for name in ('PhysicalRegion', 'PhysicalLine', 'PhysicalWord'):
            self.assertIn('computed_id', VIEW.get_class(name).annotations)
            self.assertNotIn('id', GENERATED['$defs'][name]['properties'])
        description = VIEW.schema.description
        for phrase in ('999', 'across all', 'never stored', 'tombstones', 'redirects'):
            self.assertIn(phrase, description)

    def test_image_and_timestamp_alternatives(self):
        for image, legacy, timestamp, old_time in itertools.product((False, True), repeat=4):
            page = dict(id=PAGE['id'], r=[])
            for present, key in ((image, 'iiif_img_base_uri'), (legacy, 'iiif'),
                                 (timestamp, 'ts'), (old_time, 'cdt')):
                if present:
                    page[key] = ''  # No URI, date or nonblank constraint upstream.
            with self.subTest(image=image, legacy=legacy, timestamp=timestamp, old_time=old_time):
                self.agree(page, image != legacy and (timestamp or old_time))

    def test_paired_dimensions_and_source_types(self):
        for width, height in itertools.product((MISSING, None, -1, 0, 1, 1.5, '1'), repeat=2):
            page = copy.deepcopy(PAGE)
            for key, value in (('fw', width), ('fh', height)):
                page.pop(key, None)
                if value is not MISSING:
                    page[key] = value
            with self.subTest(width=repr(width), height=repr(height)):
                self.agree(page)
        sources = (MISSING, None, *ORACLE['properties']['st']['enum'], 'other')
        for source, medium in itertools.product(sources, (MISSING, None, 'print', 'typescript', 'audio')):
            page = copy.deepcopy(PAGE)
            for key, value in (('st', source), ('sm', medium)):
                page.pop(key, None)
                if value is not MISSING:
                    page[key] = value
            with self.subTest(source=repr(source), medium=repr(medium)):
                self.agree(page)

    def test_every_stored_field_absence_null_and_wrong_types(self):
        paths = [(), ('r', 0), ('r', 0, 'p', 0), ('r', 0, 'p', 0, 'l', 0),
                 ('r', 0, 'p', 0, 'l', 0, 't', 0)]
        for path in paths:
            for key in at(PAGE, path):
                for value in (MISSING, None, True, 3.5, {}, [], '', 'invented'):
                    page = copy.deepcopy(PAGE)
                    target = at(page, path)
                    target.pop(key)
                    if value is not MISSING:
                        target[key] = value
                    with self.subTest(path=path, field=key, value=repr(value)):
                        self.agree(page)
            page = copy.deepcopy(PAGE)
            at(page, path)['unrecognized'] = {'any': [None, 7, 'invented']}
            self.agree(page, True)
        # The less common legacy and optional fields are exercised separately too.
        for path, field in (((), 'iiif'), ((), 'cdt'), (('r', 0), 'section_pOf'),
                            (('r', 0, 'p', 0, 'l', 0, 't', 0), 'nf')):
            for value in (None, True, 1, {}, [], '', 'invented'):
                page = copy.deepcopy(PAGE)
                at(page, path)[field] = value
                self.agree(page)

    def test_boxes_and_nullable_section_members(self):
        for path in (('r', 0), ('r', 0, 'p', 0), ('r', 0, 'p', 0, 'l', 0),
                     ('r', 0, 'p', 0, 'l', 0, 't', 0)):
            for box in ([], [0, 1, 2], [0, 1, 2, 3, 4], [-1, 0, -2, 0],
                        [0, 0, 1.5, 2], [False, 0, 1, 2], [0, 0, None, 1], [0, 0, 1, 2]):
                page = copy.deepcopy(PAGE)
                at(page, path)['c'] = box
                with self.subTest(path=path, box=box):
                    self.agree(page)
        for value in (None, [], [None], ['item', None], [None, None], [''], [7], [False], [{}]):
            page = copy.deepcopy(PAGE)
            page['r'][0]['section_pOf'] = value
            with self.subTest(section=value):
                self.agree(page)

    def test_empty_lists_and_the_identifier_limit_are_not_extra_impresso_constraints(self):
        for path, field in (((), 'r'), (('r', 0), 'p'), (('r', 0, 'p', 0), 'l'),
                            (('r', 0, 'p', 0, 'l', 0), 't')):
            page = copy.deepcopy(PAGE)
            at(page, path)[field] = []
            self.agree(page, True)
        page = copy.deepcopy(PAGE)
        line = page['r'][0]['p'][0]['l'][0]
        line['t'] = [line['t'][0]] * 1000
        self.agree(page, True)  # The steps id producer, not this wire schema, must refuse ids.

    def test_external_inventory_is_separate_from_the_site_twins(self):
        production = json.loads((LINKML / 'generated/contract.json').read_text())
        self.assertTrue(set(VIEW.all_classes(imports=False)).isdisjoint(production['classes']))
        self.assertEqual(load('generate').modules(LINKML)[0]['external_contract'], 'impresso-page')

    def test_data_discovery_checks_ancestors_and_honors_an_explicit_root(self):
        with tempfile.TemporaryDirectory() as folder, patch.dict(os.environ, {}, clear=True):
            base = Path(folder)
            checkout = base / 'pruzhany-steps'
            (checkout / 'editions').mkdir(parents=True)
            with patch.dict(steps_checkout.__globals__, ROOT=base / 'wt/s1'):
                self.assertEqual(steps_checkout(), checkout)
                with patch.dict(os.environ, PRUZHANY_STEPS=str(base / 'explicit')):
                    self.assertEqual(steps_checkout(), base / 'explicit')

    def test_required_nullable_scalar_retains_requiredness(self):
        shape = json.loads((LINKML / 'generated/json-schema/impresso_contentitem.schema.json').read_text())
        self.assertIn('tp', shape['required'])
        self.assertEqual(shape['properties']['tp']['type'], ['string', 'null'])

    def test_explicit_null_annotations_fail_closed_on_unsupported_settings(self):
        from linkml.generators.jsonschemagen import SlotResult
        from linkml_runtime.linkml_model import ClassDefinition, SlotDefinition
        slot = SlotDefinition('value', annotations={'nullable': 'maybe'})
        with self.assertRaises(ValueError):
            EXTERNAL.flag(slot, 'nullable')
        for settings, shape in (({'nullable': True}, {'$ref': '#/$defs/Test'}),
                                ({'nullable_items': True}, {'type': 'string'})):
            slot = SlotDefinition('value', required=True, annotations=settings)
            if '$ref' in shape:
                slot.required = False
            fake_view = type('View', (), {'induced_slot': lambda *args: slot})()
            with self.subTest(settings=settings), self.assertRaises(ValueError):
                EXTERNAL.ExplicitNullGenerator.after_generate_class_slot(
                    None, SlotResult.model_construct(source=slot, schema_=shape),
                    ClassDefinition('Test'), fake_view)


class AvailablePhysicalPages(unittest.TestCase):
    def test_every_available_page_is_accepted(self):
        steps = steps_checkout()
        if steps is None:
            self.skipTest('no sibling editions; set PRUZHANY_STEPS to check private physical pages')
        editions = steps / 'editions'
        self.assertTrue(editions.is_dir(), 'PRUZHANY_STEPS must contain editions/')
        pages = sorted(editions.glob('*/*-p[0-9][0-9][0-9][0-9].json'))
        self.assertTrue(pages, 'available editions/ has no physical page files')
        generated, upstream = validator(GENERATED), validator(ORACLE)
        counts = dict(editions=set(), pages=0, regions=0, lines=0, words=0)
        for ordinal, path in enumerate(pages, 1):
            page = json.loads(path.read_text(encoding='utf-8'))
            for label, check in (('generated', generated), ('Impresso', upstream)):
                error = next(check.iter_errors(page), None)
                if error is not None:
                    self.fail(f'page {ordinal}: {label} refusal at schema path '
                              + '/'.join(map(str, error.absolute_schema_path)))
            counts['editions'].add(path.parent)
            counts['pages'] += 1
            counts['regions'] += len(page['r'])
            for region in page['r']:
                for paragraph in region['p']:
                    counts['lines'] += len(paragraph['l'])
                    counts['words'] += sum(len(line['t']) for line in paragraph['l'])
        counts['editions'] = len(counts['editions'])
        print('\nphysical: all available pages accepted by generated and Impresso schemas; '
              + ', '.join(f'{key}={value}' for key, value in counts.items()), flush=True)


if __name__ == '__main__':
    unittest.main()
