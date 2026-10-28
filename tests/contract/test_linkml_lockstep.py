"""Planted field, required and enum drift must fail the stage-one contract gate."""

import copy
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('definition_lockstep', Path(__file__).with_name('check_linkml.py'))
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


class Lockstep(unittest.TestCase):
    def setUp(self):
        self.shape = {'type': 'object', 'properties': {'id': {'type': 'string'},
                      'kind': {'enum': ['a', 'b']}}, 'required': ['id']}
        self.zod = {'Thing': copy.deepcopy(self.shape)}
        self.index = {'classes': {'Thing': 'schema/fixture.yaml'},
                      '$defs': {'Thing': copy.deepcopy(self.shape)}, 'known_looser': []}
        self.mapping = {'models': {'Thing': {'zod': 'Thing', 'pointer': ''}},
                        'required_exceptions': {}, 'runtime_carriers': {}}

    def problems(self):
        return check.problems(self.zod, self.index, self.mapping)

    def test_control_and_a_field_added_to_either_side(self):
        self.assertEqual(self.problems(), [])
        self.index['$defs']['Thing']['properties']['new'] = {'type': 'string'}
        self.assertIn('fields differ', ' '.join(self.problems()))
        del self.index['$defs']['Thing']['properties']['new']
        self.zod['Thing']['properties']['other'] = {'type': 'string'}
        self.assertIn('fields differ', ' '.join(self.problems()))

    def test_a_required_flag_and_an_enum_value_changed(self):
        self.index['$defs']['Thing']['required'] = []
        self.assertIn('required differs', ' '.join(self.problems()))
        self.index['$defs']['Thing']['required'] = ['id']
        self.index['$defs']['Thing']['properties']['kind']['enum'].append('c')
        self.assertIn('enum differs', ' '.join(self.problems()))

    def test_missing_models_and_undeclared_runtime_exclusions_fail(self):
        self.index['classes']['New'] = 'schema/fixture.yaml'
        self.assertIn('model map', ' '.join(self.problems()))
        self.zod['Carrier'] = self.shape
        self.assertIn('Zod model coverage', ' '.join(self.problems()))

    def test_exact_required_exception_must_exist_and_still_differ(self):
        self.mapping['required_exceptions']['Thing.id'] = 'fixture#/properties/id'
        self.index['known_looser'] = [{'kind': 'required-key-nullable',
                                      'where': [{'file': 'fixture', 'pointer': '/properties/id'}]}]
        self.assertIn('stale', ' '.join(self.problems()))
        self.index['$defs']['Thing']['required'] = []
        self.assertEqual(self.problems(), [])
        self.mapping['required_exceptions']['Thing.id'] = 'fixture#/properties/wrong'
        self.assertIn('required differs', ' '.join(self.problems()))

    def test_reference_siblings_intersect_and_nullable_alternatives_union(self):
        root = {'$defs': {'Wide': {'enum': ['a', 'b', 'c']}}}
        node = {'$ref': '#/$defs/Wide', 'enum': ['a', 'b']}
        self.assertEqual(check.enum_values(node, root), frozenset(['a', 'b']))
        self.assertEqual(check.enum_values({'anyOf': [node, {'type': 'null'}]}, root), frozenset(['a', 'b']))
        self.assertIsNone(check.enum_values({'anyOf': [node, {'type': 'string'}]}, root))

    def test_only_literal_version_patterns_are_read_as_enum_values(self):
        self.assertEqual(check.literal_pattern(r'^(0\.1\.0|1\.0\.0)$(?![\s\S])'), {'0.1.0', '1.0.0'})
        self.assertIsNone(check.literal_pattern(r'^\d{4}-\d{2}-\d{2}$'))
        self.assertIsNone(check.literal_pattern(r'1.0.0'))


if __name__ == '__main__':
    unittest.main()
