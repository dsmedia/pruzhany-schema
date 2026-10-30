"""Static Zod generation: real inherited fields, bounded constructs and drift canaries.

All fixtures are synthetic. Runtime compatibility/type checks stay under zod/ and
need only bun; these backend tests run in bin/verify linkml's hashed environment.
"""

import copy
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from support import FIXTURES, LINKML, ROOT, load

backend = load('zod_generator')
generate = load('generate')


def object_shape(properties, required=()):
    return {'type': 'object', 'additionalProperties': False,
            'properties': properties, 'required': list(required)}


def fixture(field=None):
    return {'classes': {'Fixture': 'schema/fixture.yaml'},
            '$defs': {'Fixture': object_shape({'value': field or {'type': 'string'}}, ['value'])}}


class ZodGeneration(unittest.TestCase):
    def test_production_index_covers_every_class_including_resolved_ancestors(self):
        index = json.loads((LINKML / 'generated/contract.json').read_text())
        made = backend.build_zod(index)
        self.assertEqual(made, backend.build_zod(copy.deepcopy(index)))
        for name, source in index['classes'].items():
            with self.subTest(model=name):
                text = made[Path(source).stem + '.ts']
                self.assertEqual(text.count(f'export const {name}Shape = '), 1)
                for field in index['$defs'][name].get('properties', {}):
                    self.assertIn(f'\t{field}: ', text)
        # TitleCheck includes every EnglishCheck and Attribution field after LinkML resolves it.
        text = made['site_common.ts'].split('export const TitleCheckShape = ')[1].split('});')[0]
        for field in index['$defs']['EnglishCheck']['properties']:
            self.assertIn(f'\t{field}: ', text)
        self.assertIn('judgement_id:', text)
        self.assertIn('export const FactQualifiersShape = z.record(z.string(), z.string());',
                      made['sourced_entities.ts'])
        self.assertNotIn('z.any()', '\n'.join(made.values()))
        for text in made.values():
            self.assertTrue(text.startswith(backend.HEADER))
            self.assertTrue(text.endswith('\n'))
            self.assertNotIn('\r', text)
            self.assertNotIn(str(LINKML), text)

    def test_field_order_enums_once_cross_module_imports_and_nullable_forms(self):
        index = fixture({'$ref': '#/$defs/Choice'})
        index['classes']['Child'] = 'schema/child.yaml'
        index['$defs']['Choice'] = {'type': 'string', 'enum': ['first', 'second']}
        index['$defs']['Fixture'] = object_shape({
            'zebra': {'$ref': '#/$defs/Child'},
            'choice': {'$ref': '#/$defs/Choice'},
            'nullable': {'type': ['string', 'null'], 'pattern': r'\S'},
            'child': {'anyOf': [{'$ref': '#/$defs/Child'}, {'type': 'null'}]},
            'optional': {'type': ['string', 'null'], 'enum': ['first', 'second']},
            'required_null': {'type': ['number', 'null']},
            'fixed': {'type': ['string', 'null'], 'const': 'en'},
        }, ['zebra', 'choice', 'required_null'])
        index['$defs']['Child'] = object_shape({'value': {'$ref': '#/$defs/Choice'}}, ['value'])
        made = backend.build_zod(index)
        self.assertEqual(made['enums.ts'].count('z.enum('), 1)
        text = made['fixture.ts']
        self.assertIn("import { ChildShape } from './child';", text)
        self.assertLess(text.index('\tzebra:'), text.index('\tchoice:'))
        for expected in ('nullable: z.string().regex(pattern1).nullish()',
                         'child: ChildShape.nullish()', 'optional: ChoiceEnum.optional()',
                         'required_null: z.number().nullable()', "fixed: z.literal('en').optional()"):
            self.assertIn(expected, text)

    def test_supported_bounds_patterns_constants_maps_and_enum_intersection(self):
        index = fixture()
        fields = {
            'words': {'type': 'string', 'minLength': 2, 'maxLength': 8, 'pattern': r'^a/b$(?![\s\S])'},
            'number': {'type': 'number', 'minimum': -2, 'maximum': 4, 'exclusiveMinimum': -3,
                       'exclusiveMaximum': 5},
            'items': {'type': 'array', 'minItems': 1, 'maxItems': 4,
                      'items': {'type': 'integer', 'minimum': 0}},
            'map': {'type': 'object', 'additionalProperties': {'type': 'string'}},
            'uri': {'type': 'string', 'format': 'uri', 'pattern': r'^https://'},
            'flag': {'type': 'boolean'},
            'choice': {'$ref': '#/$defs/Choice', 'enum': ['second']},
        }
        index['$defs']['Fixture'] = object_shape(fields, fields)
        index['$defs']['Choice'] = {'type': 'string', 'enum': ['first', 'second']}
        made = backend.build_zod(index)
        text = made['fixture.ts']
        for expected in ('z.string().min(2).max(8).regex(pattern1)',
                         'z.number().min(-2).max(4).gt(-3).lt(5)',
                         'z.array(z.number().int().min(0)).min(1).max(4)',
                         'z.record(z.string(), z.string())', 'z.url().regex(pattern2)',
                         'z.boolean()', r'/^a\/b$(?![\s\S])/'):
            self.assertIn(expected, text)
        self.assertIn("z.enum(['second'])", made['enums.ts'])

    def test_regex_delimiters_preserve_the_runtime_source_even_after_backslashes(self):
        for pattern in (r'^a/b$', r'^a\/b$', r'^a\\/b$', r'^a\\\/b$', r'^[^/]+$'):
            with self.subTest(pattern=pattern):
                made = backend.build_zod(fixture({'type': 'string', 'pattern': pattern}))
                script = made['fixture.ts'] + (
                    '\nif (z.toJSONSchema(FixtureShape).properties.value.pattern !== '
                    f'new RegExp({json.dumps(pattern)}).source) throw new Error("regex source changed");')
                subprocess.run(['bun', '-e', script], cwd=ROOT, check=True, capture_output=True)

    def test_conditions_are_recognized_but_left_to_the_retained_rules(self):
        index = fixture()
        index['$defs']['Fixture']['allOf'] = [
            {'if': {'properties': {'value': {'const': 'first'}}, 'required': ['value']},
             'then': {'not': {'anyOf': [{'required': ['value']}]}}}]
        made = backend.build_zod(index)
        self.assertNotIn('.refine', made['fixture.ts'])
        self.assertNotIn('.superRefine', made['fixture.ts'])
        index['$defs']['Fixture']['allOf'][0]['then']['unknown_rule'] = True
        with self.assertRaisesRegex(ValueError, r'Fixture.*unknown_rule'):
            backend.build_zod(index)

    def test_unknown_field_constructs_are_refused_by_field_name(self):
        bad = [
            {'type': 'string', 'minLength': 1, 'unknown': True},
            {'type': 'string', 'format': 'date'},
            {'type': 'string', 'default': 'implicit'},
            {'type': 'string', 'minLength': -1},
            {'type': 'number', 'minimum': True},
            {'type': 'array', 'items': {}, 'uniqueItems': True},
            {'type': 'array', 'items': {'type': 'string'}, 'maxItems': 1.5},
            {'type': 'array', 'prefixItems': [{'type': 'string'}]},
            {'type': ['string', 'boolean', 'null']},
            {'anyOf': [{'type': 'string'}, {'type': 'number'}]},
            {'$ref': 'https://example.test/external'},
            {'$ref': '#/$defs/Missing'},
            {'type': 'object', 'additionalProperties': True},
            {'type': 'string', 'pattern': '\n'},
            {'type': 'string', 'enum': []},
            {'type': 'string', 'enum': ['duplicated', 'duplicated']},
            {'type': 'integer', 'enum': [1, 2]},
        ]
        for field in bad:
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'Fixture(?:Value|.value)'):
                backend.build_zod(fixture(field))

    def test_unknown_class_constraints_open_objects_invalid_requiredness_and_cycles_fail(self):
        for key, value in [('unknown', True), ('additionalProperties', True), ('required', ['missing'])]:
            index = fixture()
            index['$defs']['Fixture'][key] = value
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, 'Fixture'):
                backend.build_zod(index)
        index = fixture({'$ref': '#/$defs/Fixture'})
        with self.assertRaisesRegex(ValueError, 'cycle.*Fixture'):
            backend.build_zod(index)
        # The class graph is acyclic, but grouping classes can create a JS import cycle.
        index = fixture({'$ref': '#/$defs/Other'})
        index['classes'].update(Other='schema/other.yaml', Leaf='schema/fixture.yaml')
        index['$defs'].update(Other=object_shape({'leaf': {'$ref': '#/$defs/Leaf'}}, ['leaf']),
                             Leaf=object_shape({'value': {'type': 'string'}}, ['value']))
        with self.assertRaisesRegex(ValueError, 'module import cycle'):
            backend.build_zod(index)

    def test_generate_writes_checks_and_removes_stale_zod_files(self):
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch) / 'linkml'
            shutil.copytree(FIXTURES / 'generate', root)
            generate.regenerate(root)
            target = root.parent / 'zod/generated'
            self.assertTrue((target / 'boxes.ts').is_file())
            self.assertEqual(generate.differences(root), [])
            original = (target / 'boxes.ts').read_bytes()
            for changed in (original.replace(b'BoxShape', b'boxShape', 1), None):
                if changed is None:
                    (target / 'boxes.ts').unlink()
                else:
                    (target / 'boxes.ts').write_bytes(changed)
                self.assertEqual(generate.differences(root),
                                 ['zod/generated/boxes.ts: missing, extra or differs from generation'])
                (target / 'boxes.ts').write_bytes(original)
            (target / 'stale.ts').write_text('// stale\n')
            self.assertEqual(generate.differences(root),
                             ['zod/generated/stale.ts: missing, extra or differs from generation'])
            generate.regenerate(root)
            self.assertFalse((target / 'stale.ts').exists())
            self.assertEqual(generate.differences(root), [])


if __name__ == '__main__':
    unittest.main()
