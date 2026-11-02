"""Fictional picture credits at generated class and document boundaries."""
import copy
import importlib.util
import unittest

from jsonschema import FormatChecker

from support import ROOT
from test_documents import fixture, generated, validator, view
from test_python_generation import models


class PictureSources(unittest.TestCase):
    def test_shared_credit_inheritance_and_standard_mappings(self):
        credit = view('picture_source').get_class('PictureSource')
        paper = view('editions').get_class('Newspaper')
        self.assertEqual(paper.is_a, 'PictureSource')
        self.assertEqual(paper.class_uri, 'ehri:RecordSet')
        self.assertEqual(credit.class_uri, 'pc:PictureSource')
        self.assertEqual(credit.attributes['holder'].slot_uri, 'pc:picture_holder_name')
        self.assertEqual(credit.attributes['holder'].close_mappings, ['rico:hasOrHadHolder'])
        self.assertEqual(credit.attributes['shelf_mark'].slot_uri, 'rico:identifier')
        self.assertEqual(credit.attributes['url'].slot_uri, 'pc:holding_object_url')
        self.assertEqual(credit.attributes['url'].close_mappings, ['rdfs:seeAlso'])
        self.assertEqual(paper.attributes['title'].slot_uri, 'rico:title')
        self.assertEqual(paper.attributes['rights'].slot_uri, 'rico:conditionsOfUse')

    def test_new_fields_and_formats_at_class_and_document_boundaries(self):
        spec = importlib.util.spec_from_file_location(
            'picture_source_cases', ROOT / 'tests/contract/check_site_shapes.py')
        corpus = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(corpus)
        cases = [c for c in corpus.cases_from_file('site-shapes.fixtures.json')
                 if c['name'].startswith('picture source:')]
        self.assertGreater(len(cases), 50)
        for case in cases:
            name, value = case['model'], copy.deepcopy(case['value'])
            module = 'pages' if name in ('Page', 'PictureSource') else 'editions'
            schema = generated(module)
            cls = {'$schema': schema['$schema'], '$defs': schema['$defs'],
                   '$ref': f'#/$defs/{name}'}
            document = fixture(module)
            if name == 'EditionsCatalog':
                document = value
            elif name == 'Edition':
                document['editions'] = [value]
            elif name == 'Newspaper':
                document['editions'] = []
                document['newspapers'] = [value]
            elif name == 'Page':
                document['pages'] = [value]
            else:
                document['pages'][0]['picture_source'] = value
            # LinkML cannot compare ids within or between lists; both twins do.
            expected = case['valid'] or case.get('error') in {
                'duplicate newspaper id', 'edition newspaper is not listed'}
            with self.subTest(case=case['name']):
                for shape, data in [(cls, value), (schema, document)]:
                    check = validator(shape)
                    check.format_checker = FormatChecker()
                    self.assertEqual(check.is_valid(data), expected)

    def test_generated_python_uri_fields_keep_formats_and_exact_strings(self):
        for name, fields in [('PictureSource', ['url']),
                             ('Newspaper', ['url', 'rights_url']),
                             ('Edition', ['object_url'])]:
            for field in fields:
                with self.subTest(model=name, field=field):
                    shape = getattr(models(), name).model_json_schema()['properties'][field]
                    self.assertEqual(shape['anyOf'], [
                        {'type': 'string', 'format': 'uri'}, {'type': 'null'}])
        paper = models().Newspaper.model_validate_json(
            '{"id":"fictional-paper","code":"abc","title":"Fictional Gazette",'
            '"holder":"Fictional Library","url":"https://library.example.org"}')
        self.assertEqual(paper.url, 'https://library.example.org')
        self.assertTrue(issubclass(models().Newspaper, models().PictureSource))


if __name__ == '__main__':
    unittest.main()
