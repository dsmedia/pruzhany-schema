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
        holder_url = credit.attributes['holder_url']
        self.assertEqual(holder_url.range, 'uri')
        self.assertFalse(holder_url.required)
        self.assertEqual(holder_url.slot_uri, 'pc:picture_holder_url')
        self.assertEqual(holder_url.close_mappings, ['rdfs:seeAlso'])
        self.assertEqual(credit.attributes['shelf_mark'].slot_uri, 'rico:identifier')
        self.assertEqual(credit.attributes['url'].slot_uri, 'pc:holding_object_url')
        self.assertEqual(credit.attributes['url'].close_mappings, ['rdfs:seeAlso'])
        self.assertEqual(paper.attributes['title'].slot_uri, 'rico:title')
        rights = credit.attributes['rights']
        self.assertEqual(rights.slot_uri, 'rico:conditionsOfUse')
        self.assertEqual(rights.range, 'NonBlankText')
        self.assertFalse(rights.required)
        self.assertEqual(rights.description, 'The rights statement for the pictures, as text.')
        rights_url = credit.attributes['rights_url']
        self.assertEqual(rights_url.slot_uri, 'pc:picture_rights_url')
        self.assertEqual(rights_url.range, 'uri')
        self.assertFalse(rights_url.required)
        self.assertEqual(rights_url.description, 'The address where the rights statement was read.')
        for field in ['rights', 'rights_url']:
            self.assertNotIn(field, paper.attributes)
            inherited = view('editions').induced_slot(field, 'Newspaper')
            original = credit.attributes[field]
            for attribute in ['range', 'required', 'slot_uri', 'description',
                              'exact_mappings', 'close_mappings', 'related_mappings']:
                self.assertEqual(getattr(inherited, attribute), getattr(original, attribute))
        service = view('pages').get_class('Page').attributes['image_service']
        self.assertEqual(service.range, 'uri')
        self.assertFalse(service.required)
        self.assertEqual(service.slot_uri, 'pc:image_service')

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

    def test_page_rights_and_service_at_class_and_document_boundaries(self):
        spec = importlib.util.spec_from_file_location(
            'picture_service_cases', ROOT / 'tests/contract/check_site_shapes.py')
        corpus = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(corpus)
        schema = generated('pages')
        for case in corpus.cases_from_file('picture-service.fixtures.json'):
            name, value = case['model'], copy.deepcopy(case['value'])
            cls = {'$schema': schema['$schema'], '$defs': schema['$defs'],
                   '$ref': f'#/$defs/{name}'}
            document = fixture('pages')
            if name == 'PagesData':
                document = value
            elif name == 'Page':
                document['pages'] = [value]
            else:
                document['pages'][0]['picture_source'] = value
            with self.subTest(case=case['name']):
                for shape, data in [(cls, value), (schema, document)]:
                    check = validator(shape)
                    check.format_checker = FormatChecker()
                    self.assertEqual(check.is_valid(data), case['valid'])

    def test_generated_python_uri_fields_keep_formats_and_exact_strings(self):
        for name, fields in [('PictureSource', ['holder_url', 'url', 'rights_url']),
                             ('Newspaper', ['holder_url', 'url', 'rights_url']),
                             ('Page', ['image_service']),
                             ('Edition', ['object_url'])]:
            for field in fields:
                with self.subTest(model=name, field=field):
                    shape = getattr(models(), name).model_json_schema()['properties'][field]
                    self.assertEqual(shape['anyOf'], [
                        {'type': 'string', 'format': 'uri'}, {'type': 'null'}])
        paper = models().Newspaper.model_validate_json(
            '{"id":"fictional-paper","code":"abc","title":"Fictional Gazette",'
            '"holder":"Fictional Library","url":"https://library.example.org",'
            '"holder_url":"https://LIBRARY.example.org/holdings/42%2F1"}')
        self.assertEqual(paper.url, 'https://library.example.org')
        self.assertEqual(paper.holder_url, 'https://LIBRARY.example.org/holdings/42%2F1')
        self.assertEqual(paper.model_dump(mode='json')['holder_url'], paper.holder_url)
        self.assertTrue(issubclass(models().Newspaper, models().PictureSource))

    def test_omitted_holder_url_stays_absent_when_serialized(self):
        credit = models().PictureSource(holder='Fictional Library')
        paper = models().Newspaper(
            holder='Fictional Library', id='fictional-paper', code='abc',
            title='Fictional Gazette')
        for value in [credit, paper]:
            with self.subTest(model=type(value).__name__):
                self.assertNotIn('holder_url', value.model_dump(mode='json'))

    def test_omitted_rights_and_service_stay_absent_when_serialized(self):
        credit = models().PictureSource(holder='Fictional Library')
        self.assertEqual(credit.model_dump(mode='json'), {'holder': 'Fictional Library'})
        page = models().Page.model_validate(fixture('pages')['pages'][0])
        self.assertNotIn('image_service', page.model_dump(mode='json'))


if __name__ == '__main__':
    unittest.main()
