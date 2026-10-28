"""What LinkML 1.12.1 generates for each construct README.md's "House style" recommends.

fixtures/house-style.yaml writes one slot each way, with the real shared types; the JSON
Schema gen-json-schema makes of it must be what the README shows. A LinkML upgrade that changes
any of it fails here, and the README is read again.
"""

import json
import unittest

from linkml.generators.jsonschemagen import JsonSchemaGenerator

from support import FIXTURES

SCHEMA = json.loads(JsonSchemaGenerator(str(FIXTURES / 'house-style.yaml'), top_class='Document').serialize())
MAX_SAFE = 9007199254740991


def property_of(name):
    return {key: value for key, value in SCHEMA['properties'][name].items() if key != 'description'}


class HouseStyle(unittest.TestCase):
    def test_the_document_is_closed_and_draft_2019_09(self):
        self.assertEqual(SCHEMA['$schema'], 'https://json-schema.org/draft/2019-09/schema')
        self.assertIs(SCHEMA['additionalProperties'], False)
        self.assertIs(SCHEMA['$defs']['Check']['additionalProperties'], False)

    def test_required_is_never_null_and_optional_is_null_or_absent(self):
        self.assertIn('required_text', SCHEMA['required'])
        self.assertEqual(property_of('required_text'), {'pattern': '\\S', 'type': 'string'})
        self.assertNotIn('optional_text', SCHEMA['required'])
        self.assertEqual(property_of('optional_text'), {'pattern': '\\S', 'type': ['string', 'null']})
        self.assertEqual(property_of('required_check'), {'$ref': '#/$defs/Check'})
        self.assertEqual(property_of('optional_check'), {'anyOf': [{'$ref': '#/$defs/Check'}, {'type': 'null'}]})
        self.assertEqual(property_of('confidence'), {'type': ['number', 'null']})

    def test_patterns_of_the_shared_types(self):
        self.assertEqual(property_of('issue_date'), {'pattern': '^\\d{4}-\\d{2}-\\d{2}$', 'type': 'string'})
        self.assertEqual(property_of('digest'), {'pattern': '^[0-9a-f]{64}$(?![\\s\\S])', 'type': ['string', 'null']})

    def test_constant_uri_and_enumeration(self):
        self.assertEqual(property_of('language'), {'const': 'en', 'type': 'string'})
        self.assertEqual(property_of('url'), {'format': 'uri', 'type': ['string', 'null']})
        self.assertEqual(property_of('grain'), {'$ref': '#/$defs/AddressGrain'})
        grain = SCHEMA['$defs']['AddressGrain']
        self.assertEqual((grain['type'], grain['enum']), ('string', ['words', 'regions']))

    def test_lists_their_length_and_their_items_bounds(self):
        self.assertEqual(property_of('roles'),
                         {'items': {'$ref': '#/$defs/AddressGrain'}, 'minItems': 1, 'type': 'array'})
        self.assertEqual(property_of('bbox'), {'items': {'minimum': 0, 'type': 'number'},
                                               'maxItems': 4, 'minItems': 4, 'type': 'array'})
        self.assertEqual(property_of('block_breaks'), {'items': {'maximum': MAX_SAFE, 'minimum': 0, 'type': 'integer'},
                                                       'type': ['array', 'null']})
        self.assertEqual(property_of('width'), {'maximum': MAX_SAFE, 'minimum': 1, 'type': ['integer', 'null']})

    def test_a_map_of_text_to_text(self):
        self.assertEqual(property_of('qualifiers'), {'anyOf': [{'$ref': '#/$defs/Qualifiers'}, {'type': 'null'}]})
        qualifiers = SCHEMA['$defs']['Qualifiers']
        self.assertEqual((qualifiers['type'], qualifiers['additionalProperties']), ('object', {'type': 'string'}))
        self.assertNotIn('properties', qualifiers)


if __name__ == '__main__':
    unittest.main()
