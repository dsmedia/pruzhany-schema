"""known-looser.yaml against the shapes of today.

The five exports are made again from this checkout's Zod (linkml/export_zod.ts). For each kind
in known-looser.yaml a finder below walks them and lists every place of that kind; the list
must be exactly the file's `where`, so a place that is gone, or one Zod gained that the file
does not name, fails here.
"""

import re
import unittest

import yaml

from support import LINKML, ROOT, resolve, walk, zod_exports

KNOWN = yaml.safe_load((LINKML / 'known-looser.yaml').read_text(encoding='utf-8'))
FIELDS = {'kind', 'count', 'where', 'export_says', 'linkml_says', 'why', 'enforced_by'}


def nullable(schema):
    return any(branch.get('type') == 'null' for branch in schema.get('anyOf', []))


def properties(document):
    """(pointer, schema, required) for every property of every object in the export."""
    for pointer, node in walk(document):
        required = set(node.get('required', []))
        for name, schema in node.get('properties', {}).items():
            yield f"{pointer}/properties/{name.replace('~', '~0').replace('/', '~1')}", schema, name in required


def required_key_nullable(document):
    return [p for p, schema, required in properties(document) if required and nullable(schema)]


NAMING_RULE = re.compile(r'^[a-z][_a-z0-9]+$')


def written_as_equals_string_in(schema):
    """An enum whose values `linkml lint`'s naming rule refuses, or that are addresses.

    The house style (README.md) writes such a list as the slot's `equals_string_in`, whose
    generated `enum` refuses null as the export's does; a list of plain names is a LinkML enum,
    which keeps an optional key's null branch.
    """
    values = schema.get('enum')
    return bool(values) and any(not isinstance(v, str) or not NAMING_RULE.match(v) for v in values)


def optional_key_not_nullable(document):
    # A const refuses null by itself, as LinkML's equals_string does, so it is no difference;
    # nor is an enum the house style writes as equals_string_in.
    return [p for p, schema, required in properties(document)
            if not required and not nullable(schema) and 'const' not in schema
            and not written_as_equals_string_in(schema)]


def position_wise_bounds(document):
    # prefixItems whose positions all say the same thing is what a multivalued slot says.
    return [p for p, node in walk(document)
            if 'prefixItems' in node and any(item != node['prefixItems'][0] for item in node['prefixItems'])]


def exclusive_minimum_on_a_number(document):
    # On a whole number, minimum_value one above says the same; within prefixItems, the kind
    # above holds it.
    return [p for p, node in walk(document)
            if 'exclusiveMinimum' in node and node.get('type') == 'number' and '/prefixItems/' not in p]


FINDERS = {
    'required-key-nullable': required_key_nullable,
    'optional-key-not-nullable': optional_key_not_nullable,
    'position-wise-bounds': position_wise_bounds,
    'exclusive-minimum-on-a-number': exclusive_minimum_on_a_number,
}


class KnownLooser(unittest.TestCase):
    def test_the_exports_named_are_the_ones_made_from_zod(self):
        self.assertEqual(sorted(KNOWN['exports']), sorted(zod_exports()))

    def test_each_entry_has_its_fields_and_a_kind_this_test_can_find(self):
        kinds = [entry['kind'] for entry in KNOWN['entries']]
        self.assertEqual(len(kinds), len(set(kinds)), 'a kind is listed twice')
        self.assertEqual(set(kinds), set(FINDERS))
        for entry in KNOWN['entries']:
            with self.subTest(kind=entry['kind']):
                self.assertEqual(set(entry), FIELDS)
                self.assertEqual(entry['count'], len(entry['where']))
                for field in ('export_says', 'linkml_says', 'why'):
                    self.assertIsInstance(entry[field], str)
                    self.assertTrue(entry[field].strip())
                self.assertTrue(entry['enforced_by'])

    def test_every_place_named_still_exists(self):
        exports = zod_exports()
        for entry in KNOWN['entries']:
            for place in entry['where']:
                with self.subTest(kind=entry['kind'], pointer=place['pointer']):
                    self.assertIn(place['file'], exports)
                    self.assertIsNotNone(resolve(exports[place['file']], place['pointer']))

    def test_every_place_of_each_kind_is_named_and_no_other(self):
        exports = zod_exports()
        for entry in KNOWN['entries']:
            with self.subTest(kind=entry['kind']):
                found = {(name, pointer) for name, document in exports.items()
                         for pointer in FINDERS[entry['kind']](document)}
                listed = {(place['file'], place['pointer']) for place in entry['where']}
                self.assertEqual(sorted(listed - found), [], 'listed but no longer of this kind')
                self.assertEqual(sorted(found - listed), [], 'of this kind but not listed')

    def test_each_file_of_this_checkout_it_cites_exists(self):
        for entry in KNOWN['entries']:
            for line in entry['enforced_by']:
                for path in re.findall(r'\b(?:zod|pydantic)/[\w.-]+', line):
                    with self.subTest(kind=entry['kind'], path=path):
                        self.assertTrue((ROOT / path).is_file())


class Finders(unittest.TestCase):
    """Each finder on a planted shape, so a finder that finds nothing cannot pass unnoticed."""

    PLANTED = {
        'type': 'object',
        'properties': {
            'required_null': {'anyOf': [{'type': 'string'}, {'type': 'null'}]},
            'optional_null': {'anyOf': [{'type': 'string'}, {'type': 'null'}]},
            'optional_plain': {'type': 'number'},
            'optional_const': {'type': 'string', 'const': 'en'},
            'box': {'type': 'array', 'prefixItems': [{'type': 'number', 'minimum': 0},
                                                     {'type': 'number', 'exclusiveMinimum': 0}]},
            'pair': {'type': 'array', 'prefixItems': [{'type': 'number'}, {'type': 'number'}]},
            'duration': {'type': 'number', 'exclusiveMinimum': 0},
            'pixels': {'type': 'integer', 'exclusiveMinimum': 0},
            # An optional enum of addresses is written as equals_string_in and refuses null (house
            # style), so it is not of the kind; an optional enum of plain names is a LinkML enum
            # that keeps its null branch, so it is.
            'optional_address_list': {'type': 'string', 'enum': ['https://a.example/x', 'https://b.example/y']},
            'optional_names_list': {'type': 'string', 'enum': ['one', 'two']},
        },
        'required': ['required_null', 'box', 'pair', 'duration', 'pixels'],
    }

    def test_each_finds_its_planted_place_and_only_that(self):
        expected = {
            'required-key-nullable': ['/properties/required_null'],
            'optional-key-not-nullable': ['/properties/optional_plain', '/properties/optional_names_list'],
            'position-wise-bounds': ['/properties/box'],
            'exclusive-minimum-on-a-number': ['/properties/duration'],
        }
        for kind, finder in FINDERS.items():
            with self.subTest(kind=kind):
                self.assertEqual(finder(self.PLANTED), expected[kind])


if __name__ == '__main__':
    unittest.main()
