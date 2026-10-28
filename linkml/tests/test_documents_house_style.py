"""What LinkML 1.12.1 generates for each row README.md ("House style") gained with the issue
documents (ticket 02): fixtures/documents/house-style.yaml writes one element each way, and the
JSON Schema gen-json-schema makes of it must be what the README shows. A LinkML upgrade that
changes any of it fails here, and the README is read again.
"""

import json
import unittest

import jsonschema
from linkml.generators.jsonschemagen import JsonSchemaGenerator

from support import FIXTURES

SCHEMA = json.loads(JsonSchemaGenerator(str(FIXTURES / 'documents' / 'house-style.yaml'),
                                        top_class='Document', not_closed=False).serialize())
VALID = {'id': 'x', 'hebrewDate': 'date', 'version': '1.0.0', 'check': {'judgement_id': 'j:title'},
         'checks': [], 'roles': ['words'], 'grain': 'words', 'printed_name': 'Name'}


def property_of(name):
    return {key: value for key, value in SCHEMA['properties'][name].items() if key != 'description'}


def accepts(**changes):
    document = {**VALID, **changes}
    for key, value in changes.items():
        if value is ...:
            del document[key]
    return jsonschema.Draft201909Validator(SCHEMA).is_valid(document)


class DocumentsHouseStyle(unittest.TestCase):
    def test_an_object_inside_another_and_a_list_of_them(self):
        self.assertEqual(property_of('check'), {'$ref': '#/$defs/TitleCheck'})
        self.assertEqual(property_of('optional_check'), {'anyOf': [{'$ref': '#/$defs/TitleCheck'}, {'type': 'null'}]})
        self.assertEqual(property_of('checks'), {'items': {'$ref': '#/$defs/TitleCheck'}, 'type': 'array'})

    def test_an_id_is_a_required_slot_and_no_identifier(self):
        self.assertIn('id', SCHEMA['required'])
        self.assertEqual(property_of('id'), {'pattern': '\\S', 'type': 'string'})

    def test_a_camel_case_key_is_the_alias(self):
        self.assertIn('hebrewDate', SCHEMA['properties'])
        self.assertNotIn('hebrew_date', SCHEMA['properties'])
        self.assertIn('hebrewDate', SCHEMA['required'])
        self.assertFalse(accepts(hebrewDate=..., hebrew_date='date'))

    def test_a_subclass_narrows_its_field_and_keeps_the_rest(self):
        self.assertEqual(SCHEMA['$defs']['Check']['properties']['judgement_id']['pattern'], '^[^\\s]+:(title|text)$')
        self.assertEqual(SCHEMA['$defs']['TitleCheck']['properties']['judgement_id']['pattern'], '^[^\\s]+:title$')
        self.assertEqual(SCHEMA['$defs']['TitleCheck']['required'], ['judgement_id'])
        self.assertFalse(accepts(check={'judgement_id': 'j:text'}))

    def test_a_version_stamp_is_its_pattern(self):
        self.assertEqual(property_of('version'), {'pattern': '^(0\\.1\\.0|1\\.0\\.0)$(?![\\s\\S])', 'type': 'string'})
        self.assertTrue(accepts(version='0.1.0'))
        for other in ('1.1.0', '1.0.0\n', '1x0x0'):
            self.assertFalse(accepts(version=other), other)

    def test_a_rule_is_if_then_and_its_postconditions_are_required(self):
        words, regions = SCHEMA['allOf']
        self.assertEqual(words, {'if': {'properties': {'grain': {'const': 'words'}}, 'required': ['grain']},
                                 'then': {'properties': {'printed_name': {}}, 'required': ['printed_name']}})
        self.assertEqual(regions, {'if': {'properties': {'grain': {'enum': ['regions']}}, 'required': ['grain']},
                                   'then': {'properties': {'printed_name': {'pattern': '^$'}}}})

    def test_no_value_lets_null_and_absence_pass_and_refuses_text(self):
        self.assertTrue(accepts(grain='regions', printed_name=None))
        self.assertTrue(accepts(grain='regions', printed_name=...))
        self.assertFalse(accepts(grain='regions', printed_name='Name'))
        self.assertFalse(accepts(grain='words', printed_name=...))
        # What it cannot say: a words mention whose name is null.
        self.assertTrue(accepts(grain='words', printed_name=None))

    def test_items_that_must_differ_get_no_unique_items(self):
        self.assertEqual(property_of('roles'), {'items': {'$ref': '#/$defs/Grain'}, 'type': 'array'})
        self.assertTrue(accepts(roles=['words', 'words']))

    def test_a_mapping_leaves_no_trace_in_the_json_schema(self):
        text = json.dumps(SCHEMA)
        for word in ('rico:', 'site_mention', 'impresso', 'hasEventType'):
            self.assertNotIn(word, text)


if __name__ == '__main__':
    unittest.main()
