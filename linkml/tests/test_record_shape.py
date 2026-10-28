"""The record's modules (sourced_entities, media, shared_record, shared) against the sources they
copy: the version stamps against the generated vocabulary contracts, the fixed lists against
the files they come from, the patterns against the twins, and the terms they map to, by count.
"""

import collections
import importlib.util
import json
import re
import unittest

import yaml
from jsonschema import Draft201909Validator
from linkml_runtime.utils.schemaview import SchemaView

from support import LINKML, ROOT

GENERATED = json.loads((LINKML / 'generated' / 'json-schema' / 'shared_record.schema.json').read_text(encoding='utf-8'))
DEFS = GENERATED['$defs']
VIEW = SchemaView(str(LINKML / 'schema' / 'shared_record.yaml'))
MODULES = ['sourced_entities', 'media', 'shared_record', 'shared']
MAPPING_KEYS = {'meaning', 'class_uri', 'slot_uri', 'mappings', 'exact_mappings', 'close_mappings',
                'related_mappings', 'narrow_mappings', 'broad_mappings', 'via'}

spec = importlib.util.spec_from_file_location('check_alignment', ROOT / 'standards' / 'check_alignment.py')
check_alignment = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_alignment)


def text(path):
    return (ROOT / path).read_text(encoding='utf-8')


def attribute(class_name, slot):
    return VIEW.induced_slot(slot, class_name)


def refused(class_name, value):
    validator = Draft201909Validator({'$schema': GENERATED['$schema'], '$defs': DEFS,
                                      '$ref': f'#/$defs/{class_name}'})
    return not validator.is_valid(value)


def mapping_values(node, key=None):
    """(key, value) for every mapping a schema file writes, read by PyYAML."""
    if isinstance(node, dict):
        for name, value in node.items():
            yield from mapping_values(value, name)
    elif isinstance(node, list):
        for value in node:
            yield from mapping_values(value, key)
    elif isinstance(node, str) and key in MAPPING_KEYS:
        yield key, node


EMPTY_RECORD = {'version': '1', 'vocabulary_version': '1.3.0', 'persons': [], 'families': [], 'places': [],
                'organizations': [], 'events': [], 'sources': [], 'facts': [], 'relations': []}


class VersionStamps(unittest.TestCase):
    def test_the_vocabulary_version_is_the_generated_contracts(self):
        released = json.loads(text('vocabulary/sourced-entities.json'))['version']
        zod = re.search(r"export const vocabularyVersion = '([^']+)'", text('zod/sourced-entities.vocabulary.ts'))
        python = re.search(r"VOCABULARY_VERSION = '([^']+)'", text('pydantic/sourced_entities_vocabulary.py'))
        self.assertEqual({released, zod.group(1), python.group(1),
                          attribute('SharedRecord', 'vocabulary_version').equals_string,
                          DEFS['SharedRecord']['properties']['vocabulary_version']['const']}, {released})

    def test_the_record_version_is_the_twins(self):
        zod = re.search(r"version: z\.literal\('([^']+)'\)", text('zod/shared-record.schema.ts'))
        python = re.search(r"version: Literal\['([^']+)'\]", text('pydantic/shared_record.py'))
        self.assertEqual({zod.group(1), python.group(1), attribute('SharedRecord', 'version').equals_string,
                          DEFS['SharedRecord']['properties']['version']['const']}, {'1'})

    def test_another_stamp_is_refused(self):
        self.assertFalse(refused('SharedRecord', EMPTY_RECORD))
        self.assertTrue(refused('SharedRecord', dict(EMPTY_RECORD, vocabulary_version='1.2.0')))
        self.assertTrue(refused('SharedRecord', dict(EMPTY_RECORD, version='2')))


class FixedLists(unittest.TestCase):
    def test_the_media_rights_are_the_pinned_list(self):
        rights = json.loads(text('standards/media-rights.json'))['uris']
        self.assertEqual(attribute('PublicMedia', 'rights').equals_string_in, rights)
        self.assertEqual(DEFS['PublicMedia']['properties']['rights']['enum'], rights)

    def test_the_served_widths_are_the_twins(self):
        widths = json.loads(text('zod/media-widths.json'))
        pattern = attribute('MediaDerivative', 'url').pattern
        self.assertIn('-w(?:' + '|'.join(map(str, widths)) + r')\.webp', pattern)

    def test_the_released_event_kinds_are_the_vocabulary_s(self):
        kinds = list(VIEW.get_enum('EventTypes').permissible_values)
        none_of = VIEW.get_class('SharedEvent').none_of[0].slot_conditions['proposed_type']
        self.assertEqual(none_of.equals_string_in, kinds)

    def test_a_list_refuses_what_it_does_not_hold(self):
        medium = {'id': 'medium-a', 'source_id': 'source-a', 'kind': 'audio', 'caption': {'text': 'A song', 'lang': 'yi'},
                  'depicted': [], 'shows_unidentified': False, 'credit': 'The family'}
        self.assertFalse(refused('PublicMedia', dict(medium, rights='https://creativecommons.org/licenses/by/4.0/')))
        self.assertTrue(refused('PublicMedia', dict(medium, rights='https://creativecommons.org/licenses/by/3.0/')))
        self.assertTrue(refused('PublicMedia', dict(medium, rights=None)))


class HouseStyleRows(unittest.TestCase):
    """The rows linkml/README.md ("House style") adds for these modules, as generated."""

    def prop(self, class_name, slot):
        return {k: v for k, v in DEFS[class_name]['properties'][slot].items() if k != 'description'}

    def test_an_enum_on_an_optional_key_keeps_its_null_branch(self):
        self.assertEqual(self.prop('SourcedDate', 'precision'),
                         {'anyOf': [{'$ref': '#/$defs/SourcedDatePrecision'}, {'type': 'null'}]})

    def test_a_list_on_the_slot_is_an_enum_on_the_property(self):
        self.assertEqual(self.prop('MediaConsentScope', 'use'), {'enum': ['site', 'site+download'], 'type': 'string'})

    def test_a_narrowed_vocabulary_enum_keeps_both(self):
        self.assertEqual(self.prop('SourcedRelation', 'type'), {'$ref': '#/$defs/FactTypes', 'enum': ['kinship', 'other']})

    def test_an_https_address_has_its_format_and_its_pattern(self):
        self.assertEqual(self.prop('Citation', 'url'), {'format': 'uri', 'pattern': VIEW.get_type('HttpsUri').pattern,
                                                        'type': ['string', 'null']})

    def test_coordinates_are_two_bounded_numbers(self):
        self.assertEqual(self.prop('SharedPlace', 'coordinates'),
                         {'items': {'maximum': 180, 'minimum': -180, 'type': 'number'}, 'maxItems': 2, 'minItems': 2,
                          'type': ['array', 'null']})


class Patterns(unittest.TestCase):
    def test_an_https_address_is_the_pydantic_twin_s_pattern(self):
        pattern = VIEW.get_type('HttpsUri').pattern
        for path, model in (('pydantic/sourced_entities.py', 'Citation'), ('pydantic/shared_record.py', 'PlaceIdentifier')):
            with self.subTest(model=model):
                body = text(path).split(f'class {model}(', 1)[1]
                found = re.search(r'url: Annotated\[str, Field\(pattern=r"([^"]+)"\)\]', body)
                self.assertEqual(found.group(1), pattern)
        self.assertEqual(attribute('Citation', 'url').range, 'HttpsUri')
        self.assertEqual(attribute('PlaceIdentifier', 'url').range, 'HttpsUri')
        self.assertTrue(refused('Citation', {'source_id': 'source-a', 'url': 'http://example.org/a'}))

    def test_a_coordinate_is_bounded_as_the_longitude_is(self):
        coordinate = VIEW.get_type('Coordinate')
        self.assertEqual((coordinate.minimum_value, coordinate.maximum_value), (-180, 180))
        self.assertIn('z.number().min(-180).max(180)', text('zod/shared-record.schema.ts'))

    def test_a_printed_address_has_the_twins_keys(self):
        address = DEFS['PrintedAddress']
        self.assertEqual(set(address['properties']), {'image_uri', 'bbox', 'text'})
        self.assertEqual(set(address['required']), {'image_uri', 'bbox', 'text'})


class Meaning(unittest.TestCase):
    def test_the_alignment_check_reads_every_mapping_as_yaml_does(self):
        for path in sorted((LINKML / 'schema').glob('*.yaml')):
            with self.subTest(file=path.name):
                content = path.read_text(encoding='utf-8')
                read = sorted((key, value) for _, key, value in check_alignment.linkml_scalars(content)
                              if key in MAPPING_KEYS)
                self.assertEqual(read, sorted(mapping_values(yaml.safe_load(content))))

    @staticmethod
    def wrong_kinds(schemas):
        """A class mapped to what the pins hold as a property, or a slot to a class."""
        kinds = {}
        for name, namespace, prefix in (('rico-1.1.json', check_alignment.RICO, 'rico'),
                                        ('ehri-0.2.0.json', check_alignment.EHRI, 'ehri')):
            for term in json.loads(text(f'standards/{name}'))['terms']:
                kinds[prefix + ':' + term['iri'].removeprefix(namespace)] = term['kind']
        wrong = []
        for schema in schemas:
            for key, value in mapping_values(schema):
                if value.split(':')[0] in ('rico', 'ehri'):
                    if key == 'class_uri' and kinds[value] != 'class':
                        wrong.append((key, value))
                    if key in ('slot_uri', 'related_mappings') and not kinds[value].endswith(' property'):
                        wrong.append((key, value))
        return wrong

    def test_a_class_maps_to_a_class_and_a_slot_to_a_property(self):
        schemas = [yaml.safe_load((LINKML / 'schema' / f'{module}.yaml').read_text(encoding='utf-8'))
                   for module in MODULES]
        self.assertEqual(self.wrong_kinds(schemas), [])
        planted = {'classes': {'Thing': {'class_uri': 'rico:hasChild',
                                         'attributes': {'part': {'slot_uri': 'rico:Person'}}}}}
        self.assertEqual(self.wrong_kinds([planted]), [('class_uri', 'rico:hasChild'), ('slot_uri', 'rico:Person')])

    def test_the_mappings_by_standard(self):
        """A tally, so a mapping lost or added shows here."""
        counts = collections.Counter()
        for module in MODULES:
            schema = yaml.safe_load((LINKML / 'schema' / f'{module}.yaml').read_text(encoding='utf-8'))
            for key, value in mapping_values(schema):
                counts[(key, value.split(':')[0])] += 1
        self.assertEqual(dict(counts), {
            ('class_uri', 'rico'): 9, ('class_uri', 'ehri'): 4, ('class_uri', 'pc'): 1,
            ('slot_uri', 'rico'): 34, ('slot_uri', 'pc'): 29,
            ('meaning', 'rico'): 2, ('meaning', 'ehri'): 3, ('meaning', 'pc'): 4,
            ('related_mappings', 'pc'): 6, ('related_mappings', 'rico'): 1, ('via', 'rico'): 1})


if __name__ == '__main__':
    unittest.main()
