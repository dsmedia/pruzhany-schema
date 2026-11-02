"""Ticket 01: fictional paper identity at the generated class and document boundaries."""

import copy
import importlib.util
import json
import unittest

from linkml_runtime.utils.schemaview import SchemaView

from support import LINKML, ROOT
from test_documents import fixture, generated, validator


class Newspaper(unittest.TestCase):
    def test_required_paper_field_has_the_declared_local_mapping(self):
        for module, name in [('editions', 'Edition'), ('pages', 'Page'),
                             ('content_items', 'ContentItem')]:
            slot = SchemaView(str(LINKML / f'schema/{module}.yaml')).get_class(
                name).attributes['newspaper']
            with self.subTest(model=name):
                self.assertTrue(slot.required)
                self.assertEqual(slot.range, 'NonBlankText')
                self.assertEqual(slot.slot_uri, 'pc:site_newspaper')
                self.assertFalse(slot.close_mappings)
                self.assertIn('media alias', slot.annotations['impresso'].value)

    def test_fictional_two_paper_cases_at_class_and_document_boundaries(self):
        # jsonschema Schema Validation, read 2 November 2026:
        # https://python-jsonschema.readthedocs.io/en/v4.26.0/validate/
        spec = importlib.util.spec_from_file_location(
            'newspaper_cases', ROOT / 'tests/contract/check_site_shapes.py')
        corpus = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(corpus)
        cases = list(corpus.cases_from_file('newspaper.fixtures.json'))
        self.assertEqual(len(cases), 38)
        for case in cases:
            name, value = case['model'], copy.deepcopy(case['value'])
            module = {'Edition': 'editions', 'Page': 'pages',
                      'Block': 'pages', 'ContentItem': 'content_items'}[name]
            schema = generated(module)
            cls = {'$schema': schema['$schema'], '$defs': schema['$defs'],
                   '$ref': f'#/$defs/{name}'}
            document = fixture(module)
            if name == 'Edition':
                document['editions'] = [value]
            elif name == 'Page':
                document['pages'] = [value]
            elif name == 'Block':
                document['pages'][0]['blocks'] = [value]
            else:
                document['content_items'] = [value]
            # Sibling-value equality belongs to both retained runtime validators.
            expected = case['valid'] or 'key date disagrees' in case['name']
            with self.subTest(case=case['name']):
                self.assertEqual(validator(cls).is_valid(value), expected)
                self.assertEqual(validator(schema).is_valid(document), expected)


if __name__ == '__main__':
    unittest.main()
