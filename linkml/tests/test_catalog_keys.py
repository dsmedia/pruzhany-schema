"""Fictional catalog keys and other papers' fates-list pieces at the generated JSON Schemas."""
import copy
import importlib.util
import unittest

from support import ROOT
from test_documents import generated, validator
from test_python_generation import models

# LinkML's generated JSON Schema cannot compare values within or across lists; both twins do.
TWIN_ONLY = {'duplicate available key', 'available key names no edition',
             'date-only available keys must equal availableDates'}


def cases(filename, prefix):
    spec = importlib.util.spec_from_file_location(
        'catalog_keys_cases', ROOT / 'tests/contract/check_site_shapes.py')
    corpus = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(corpus)
    return [c for c in corpus.cases_from_file(filename) if c['name'].startswith(prefix)]


class CatalogKeys(unittest.TestCase):
    def test_available_keys_is_optional_and_patterned(self):
        slot = generated('editions')['$defs']['EditionsCatalog']['properties']['availableKeys']
        self.assertEqual(slot['items']['pattern'], '^(?:[a-z]+-)?\\d{4}-\\d{2}-\\d{2}$(?![\\s\\S])')
        self.assertNotIn('availableKeys', generated('editions')['$defs']['EditionsCatalog']['required'])

    def test_the_catalog_cases_at_the_document_boundary(self):
        found = cases('catalog-keys.fixtures.json', 'catalog keys:')
        self.assertGreater(len(found), 10)
        check = validator(generated('editions'))
        for case in found:
            with self.subTest(case=case['name']):
                expected = case['valid'] or case.get('error') in TWIN_ONLY
                self.assertEqual(check.is_valid(copy.deepcopy(case['value'])), expected)

    def test_the_python_twin_refuses_each_case_for_its_reason(self):
        for case in cases('catalog-keys.fixtures.json', 'catalog keys:'):
            with self.subTest(case=case['name']):
                if case['valid']:
                    parsed = models().EditionsCatalog.model_validate(case['value'])
                    self.assertEqual(parsed.model_dump(mode='json'), case['value'])
                    continue
                with self.assertRaises(ValueError) as refused:
                    models().EditionsCatalog.model_validate(case['value'])
                if case.get('error'):
                    self.assertIn(case['error'], str(refused.exception))

    def test_fates_list_pieces_of_another_paper(self):
        found = cases('fates-list.fixtures.json', 'FatesListPiece:')
        self.assertGreater(len(found), 3)
        schema = generated('fates_list')
        check = validator({'$schema': schema['$schema'], '$defs': schema['$defs'],
                           '$ref': '#/$defs/FatesListPiece'})
        for case in found:
            with self.subTest(case=case['name']):
                self.assertEqual(check.is_valid(case['value']), case['valid'])


if __name__ == '__main__':
    unittest.main()
