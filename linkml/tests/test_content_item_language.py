"""Issue #56: fictional printed-language cases and the existing standards binding."""

import copy
import importlib.util
import json
import unittest

from jsonschema import Draft201909Validator
from linkml_runtime.utils.schemaview import SchemaView

from support import LINKML, ROOT


class ContentItemLanguage(unittest.TestCase):
    def test_optional_scalar_reuses_the_source_language_binding(self):
        slot = SchemaView(str(LINKML / 'schema/content_items.yaml')).get_class(
            'ContentItem').attributes['language']
        self.assertEqual(slot.range, 'LanguageTag')
        self.assertFalse(slot.required)
        self.assertFalse(slot.multivalued)
        impresso = json.loads((ROOT / 'standards/impresso-329323c/'
                             'paper_contentitem.schema.json').read_text())
        # Impresso's own lg pattern, with the house end guard: a bare $ admits a final newline in Python.
        self.assertEqual(slot.pattern, impresso['properties']['lg']['pattern'] + r'(?![\s\S])')
        vocabulary = json.loads((ROOT / 'vocabulary/site-content.json').read_text())
        binding, = [b for b in vocabulary['bindings'] if b['id'] == 'source_language']
        self.assertEqual(slot.slot_uri, 'rico:' + binding['mapping']['rico'])
        self.assertEqual(slot.description,
                         'The language most of the item is printed in, as the reading step judged it, '
                         "as a two- or three-letter ISO 639 code (Impresso's lg).")
        for source in ('lg', 'paper_contentitem.schema.json', 'issue.schema.json'):
            self.assertIn(source, slot.annotations['impresso'].value)

    def test_contract_cases_validate_in_the_linkml_class_and_document(self):
        # jsonschema 4.26.0, Schema Validation, read 1 November 2026:
        # https://python-jsonschema.readthedocs.io/en/v4.26.0/validate/
        schema = json.loads((LINKML / 'generated/json-schema/content_items.schema.json').read_text())
        item_validator = Draft201909Validator({
            '$schema': schema['$schema'], '$defs': schema['$defs'], '$ref': '#/$defs/ContentItem'})
        document_validator = Draft201909Validator(schema)
        spec = importlib.util.spec_from_file_location(
            'language_contract_cases', ROOT / 'tests/contract/check_site_shapes.py')
        corpus = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(corpus)
        cases = [c for c in corpus.cases_from_file('site-shapes.fixtures.json')
                 if c['name'].startswith('ContentItem language:')]
        self.assertGreaterEqual(len(cases), 4)
        missing, = [c for c in cases if c['name'] == 'ContentItem language: omitted']
        self.assertNotIn('language', missing['value'])
        for case in cases:
            with self.subTest(case=case['name']):
                value = copy.deepcopy(case['value'])
                document = {'issue_date': '2000-01-01', 'vocabulary_version': '1.1.0',
                            'content_items': [value], 'sections': []}
                self.assertEqual(item_validator.is_valid(value), case['valid'])
                self.assertEqual(document_validator.is_valid(document), case['valid'])


if __name__ == '__main__':
    unittest.main()
