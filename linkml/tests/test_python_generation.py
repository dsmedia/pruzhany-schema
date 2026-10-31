"""Generated Python preserves the released API and cannot lose constraints or hooks."""

import copy
import importlib.util
import json
import sys
import tempfile
from typing import Annotated
import unittest
from pathlib import Path
from unittest.mock import patch

from pydantic import TypeAdapter, ValidationError

from support import LINKML, ROOT, load

backend = load('python_generator')
inventory = load('python_inventory')


def package():
    name = 'generation_tests_schema'
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, ROOT / 'pydantic/__init__.py',
                                                     submodule_search_locations=[str(ROOT / 'pydantic')])
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


def models():
    package()
    return sys.modules['generation_tests_schema.generated.models']


def contract_cases():
    spec = importlib.util.spec_from_file_location('python_generation_corpus', ROOT / 'tests/contract/check_site_shapes.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return list(module.fixture_cases())


class PythonGeneration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((LINKML / 'generated/contract.json').read_text())
        cls.profile = json.loads((LINKML / 'python-compatibility.json').read_text())

    def test_all_previous_model_fields_requiredness_enums_and_config_are_preserved(self):
        previous = json.loads((LINKML / 'tests/fixtures/python-baseline.json').read_text())
        self.assertEqual(previous['commit'], self.profile['baseline_commit'])
        # Ticket 03's exact optional additions, applied to the immutable baseline and
        # its nested definitions. All previous constraints/defaults/config remain checked.
        additions = {
            'PlaceIdentifier': {'type': {'anyOf': [
                {'const': 'old_identifier', 'type': 'string'}, {'type': 'null'}], 'default': None}},
            **{name: {'identifiers': {'anyOf': [
                {'items': {'$ref': '#/$defs/PlaceIdentifier'}, 'minItems': 1, 'type': 'array'},
                {'type': 'null'}], 'default': None}}
               for name in ('SharedPerson', 'SharedOrganization')},
        }
        # Ticket 02: exact optional Translation additions, including inherited fields.
        # Expected field names are independent of generated declarations.
        english_fields = {
            'Citation': ['quote_english'], 'SiteCitation': ['quote_english'],
            'Source': ['title_english'], 'MediaFamilyWords': ['quote_english'],
        }
        for name, fields in english_fields.items():
            additions.setdefault(name, {}).update({field: {'anyOf': [
                {'$ref': '#/$defs/CitedTranslation'}, {'type': 'null'}], 'default': None} for field in fields})
        for name, old in previous['models'].items():
            with self.subTest(model=name):
                # Owner-approved site-content 1.1.0, 31 October 2026; preserve the
                # frozen fixture and prescribe only the newly accepted stamp.
                content = (old['schema'] if name == 'ContentItemsData' else
                           old['schema'].get('$defs', {}).get('ContentItemsData'))
                if content is not None:
                    version = content['properties']['vocabulary_version']
                    self.assertEqual(version['enum'], ['0.1.0', '1.0.0'])
                    version['enum'] = ['0.1.0', '1.0.0', '1.1.0']
                expected = copy.deepcopy(old['schema'])
                for class_name, fields in additions.items():
                    target = expected if class_name == name else expected.get('$defs', {}).get(class_name)
                    if target is not None:
                        target['properties'].update(copy.deepcopy(fields))
                if name in ('SharedPerson', 'SharedOrganization'):
                    expected.setdefault('$defs', {}).update(copy.deepcopy(
                        previous['models']['PlaceIdentifier']['schema'].get('$defs', {})))
                    expected['$defs']['PlaceIdentifier'] = copy.deepcopy(
                        previous['models']['PlaceIdentifier']['schema'])
                    expected['$defs']['PlaceIdentifier']['properties'].update(
                        copy.deepcopy(additions['PlaceIdentifier']))
                if any(class_name == name or class_name in expected.get('$defs', {})
                       for class_name in english_fields):
                    translation = copy.deepcopy(previous['models']['Translation']['schema'])
                    translation['properties']['based_on'] = {'$ref': '#/$defs/CitedTextBasis'}
                    definitions = translation.pop('$defs', {})
                    expected.setdefault('$defs', {}).update({key: value for key, value in definitions.items()
                                                            if key not in expected.get('$defs', {})})
                    basis = copy.deepcopy(definitions['TextBasis'])
                    basis['required'].remove('addresses')
                    addresses = basis['properties']['addresses']
                    basis['properties']['addresses'] = {'anyOf': [addresses, {'type': 'null'}], 'default': None}
                    expected['$defs']['CitedTextBasis'] = basis
                    expected['$defs']['CitedTranslation'] = translation
                model = getattr(models(), name)
                new = model.model_json_schema()
                self.assertEqual(backend.canonical(new, new.get('$defs', {})),
                                 backend.canonical(expected, expected.get('$defs', {})))
                expected_order = old['order'] + list(additions.get(name, {}))
                parent = {'SiteCitation': 'Citation'}.get(name)
                if parent:
                    fields = english_fields[name]
                    expected_order = [field for field in expected_order if field not in fields]
                    at = len(previous['models'][parent]['order'])
                    expected_order[at:at] = fields
                self.assertEqual(list(model.model_fields), expected_order)
                self.assertEqual(model.model_config, old['config'])
                for field in old['schema']['properties']:
                    before = old['schema']['properties'][field]
                    after = new['properties'][field]
                    self.assertEqual('default' in before, 'default' in after)
                    self.assertEqual(before.get('default'), after.get('default'))
                module = __import__(f'generation_tests_schema.{old["module"]}', fromlist=[name])
                self.assertIs(getattr(module, name), model)

    def test_the_package_has_exactly_the_definition_classes(self):
        self.assertEqual(set(models().__all__), set(self.index['classes']))
        self.assertEqual(set(self.profile['models']), set(self.index['classes']))
        # All references use the same classes, including the hand-written carriers.
        self.assertIs(package().SiteArchive.model_fields['shared_record'].annotation, models().SharedRecord)
        self.assertIs(package().SiteIssue.model_fields['pages'].annotation, models().PagesData)
        self.assertTrue(issubclass(models().SiteCitation, models().Citation))

    def test_generation_is_identical_and_needs_no_linkml_at_runtime(self):
        made = backend.build_python(LINKML, self.index)
        self.assertEqual(made, backend.build_python(LINKML, self.index))
        for filename, text in made.items():
            self.assertEqual(text, (ROOT / 'pydantic/generated' / filename).read_text())
            self.assertNotIn(str(ROOT), text)
            self.assertNotIn('from linkml', text)
            self.assertNotIn('import linkml', text)

    def test_missing_nullable_key_and_nested_bad_coordinates_fail(self):
        block = dict(id='b', bbox=[0, 0, 1, 1], transcription='words', unit_id=None)
        parsed = models().Block.model_validate_json(json.dumps(block))
        self.assertIsInstance(parsed.bbox, tuple)
        del block['unit_id']
        with self.assertRaises(ValidationError):
            models().Block.model_validate_json(json.dumps(block))
        for bbox in ([0, 0, 0, 1], [0, 0, 1], [-1, 0, 1, 1]):
            with self.subTest(bbox=bbox), self.assertRaises(ValidationError):
                models().PrintedTitle.model_validate_json(json.dumps(dict(text='words', addresses=[dict(image_uri='p', text='words', bbox=bbox)])))

    def test_calendar_host_bounds_and_coercion_hooks_still_run(self):
        for model, document in [
            ('Attribution', {'by':'person', 'on':'1938-02-30'}),
            ('Source', {'id':'s', 'kind':'book', 'title':'source', 'host':'www.example.org'}),
            ('MediaRegion', {'x':0, 'y':0, 'w':0, 'h':1}),
            ('MediaRegion', {'x':'0', 'y':0, 'w':1, 'h':1}),
        ]:
            with self.subTest(model=model, document=document), self.assertRaises(ValidationError):
                getattr(models(), model).model_validate_json(json.dumps(document))
        item = next(c['value'] for c in contract_cases() if c['model']=='ContentItem' and c['valid'])
        item = copy.deepcopy(item)
        item['block_breaks'] = [0.0]
        parsed = models().ContentItem.model_validate_json(json.dumps(item))
        self.assertEqual(parsed.block_breaks, [0])
        self.assertIs(type(parsed.block_breaks[0]), int)
        for value in ('0', True, -1):
            item['block_breaks'] = [value]
            with self.subTest(value=value), self.assertRaises(ValidationError):
                models().ContentItem.model_validate_json(json.dumps(item))

    def test_catalog_aliases_omissions_unknowns_and_bounds(self):
        catalog = {'editions':[{'date':'1938-12-16','hebrewDate':'date','hebrewMonth':9,'hebrewYear':5699}],
                   'holidays':[], 'historicalEvents':[], 'availableDates':['1938-12-16']}
        model = package().EditionsCatalog.model_validate_json(json.dumps(catalog))
        self.assertEqual(model.model_dump(mode='json'), catalog)
        integral = copy.deepcopy(catalog)
        integral['editions'][0]['hebrewYear'] = 5699.0
        self.assertEqual(package().EditionsCatalog.model_validate_json(json.dumps(integral)).editions[0].hebrewYear, 5699)
        for key, value in [('holiday', None), ('hebrewMonth', 14), ('hebrewYear', '5699'), ('surprise', 1)]:
            changed = copy.deepcopy(catalog)
            changed['editions'][0][key] = value
            with self.subTest(key=key), self.assertRaises(ValidationError):
                package().EditionsCatalog.model_validate_json(json.dumps(changed))
        for model, value, optional in [
            ('Holiday', {'date':'1938-12-16','name':'holiday'}, 'hebrewName'),
            ('HistoricalEvent', {'date':'1938-12-16','name':'event','description':'description'}, 'endDate'),
        ]:
            getattr(package(), model).model_validate_json(json.dumps(value))
            value[optional] = None
            with self.subTest(model=model), self.assertRaisesRegex(ValidationError, 'present value must not be null'):
                getattr(package(), model).model_validate_json(json.dumps(value))

    def test_unhandled_constraints_cannot_be_silently_dropped(self):
        for shape in [{'type':'string','format':'uri'}, {'type':'integer','multipleOf':2},
                      {'$ref':'#/$defs/Page','minimum':1}, {'anyOf':[{'type':'string'}],'pattern':'x'},
                      {'type':'array','items':False}]:
            with self.subTest(shape=shape), self.assertRaises(ValueError):
                backend.expression(shape)

    def test_nullable_type_does_not_override_a_nonnullable_enum(self):
        node = backend.canonical({'type':['string','null'], 'enum':['a','b']}, {})
        self.assertEqual(node, {'type':'string', 'enum':['a','b']})

    def test_new_conditional_rule_requires_explicit_python_review(self):
        index = copy.deepcopy(self.index)
        index['$defs']['Page']['not'] = {'required':['id']}
        with self.assertRaisesRegex(ValueError, 'conditional rules changed'):
            backend.build_python(LINKML, index)

    def test_missing_or_stale_adjustments_and_model_mappings_fail(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for mutate in [lambda p:p['models'].pop('Page'),
                           lambda p:p['models']['Page'].update(fields={'orphan': {'required':True}}),
                           lambda p:p['adjustments'].append(copy.deepcopy(p['adjustments'][0])),
                           lambda p:p['adjustments'][0].update(python=p['adjustments'][0]['definition']),
                           lambda p:p['adjustments'][0]['definition'].update(type='string')]:
                profile = copy.deepcopy(self.profile)
                mutate(profile)
                (root/'python-compatibility.json').write_text(json.dumps(profile))
                with self.assertRaises(ValueError):
                    backend.checked_profile(root, self.index)

    def test_deleting_a_callback_binding_is_detected(self):
        self.assertEqual(inventory.binding_problems(ROOT), [])
        profile = copy.deepcopy(self.profile)
        del profile['models']['IssueMention']['validators']
        self.assertTrue(any('mention_contract' in p for p in inventory.binding_problems(ROOT, profile)))
        profile = copy.deepcopy(self.profile)
        profile['models']['IssueMention']['validators'][0]['function'] = 'does_not_exist'
        self.assertTrue(any('missing' in p for p in inventory.binding_problems(ROOT, profile)))

    def test_every_python_adjustment_has_exercised_synthetic_witnesses(self):
        witnesses = json.loads((LINKML / 'tests/fixtures/python-adjustments.json').read_text())
        places = [(w['model'], w['field']) for w in witnesses]
        self.assertEqual(len(places), len(set(places)), 'duplicate witness')
        self.assertEqual(set(places), {(e['model'], e['field']) for e in self.profile['adjustments']},
                         'missing or orphaned adjustment witnesses')
        for witness in witnesses:
            model = getattr(models(), witness['model'])
            field = model.model_fields[witness['field']]
            annotation = Annotated[field.annotation, *field.metadata] if field.metadata else field.annotation
            adapter = TypeAdapter(annotation, config=model.model_config)
            self.assertTrue(any(c['valid'] for c in witness['cases']))
            self.assertTrue(any(not c['valid'] for c in witness['cases']))
            for case in witness['cases']:
                with self.subTest(model=witness['model'], field=witness['field'], value=case['value']):
                    if case['valid']:
                        parsed = adapter.validate_json(json.dumps(case['value']))
                        self.assertEqual(type(parsed).__name__, case['python_type'])
                    else:
                        with self.assertRaises(ValidationError):
                            adapter.validate_json(json.dumps(case['value']))

    def test_the_original_behavior_corpus_exercises_retained_callbacks(self):
        seen, refused = set(), set()
        original = models()._call

        def observed(module, function, *args):
            seen.add((module, function))
            try:
                return original(module, function, *args)
            except ValueError:
                refused.add((module, function))
                raise

        with patch.object(models(), '_call', observed):
            for case in contract_cases():
                with self.subTest(case=case['name']):
                    try:
                        getattr(package(), case['model']).model_validate_json(json.dumps(case['value']))
                        valid = True
                    except ValidationError:
                        valid = False
                    self.assertEqual(valid, case['valid'])
            for model, value in [
                ('Fate', dict(outcome='perished', confidence='possible', rests_on=[], review={'state':'pending'})),
                ('MediaConsentScope', dict(use='site', person_ids=['person-a', 'person-a'], unidentified=False)),
            ]:
                with self.subTest(model=model), self.assertRaises(ValidationError):
                    getattr(models(), model).model_validate_json(json.dumps(value))
        expected = {(v['module'], v['function']) for cfg in self.profile['models'].values()
                    for v in [*cfg.get('validators', []), *cfg.get('field_validators', [])]}
        self.assertEqual(expected - seen, set(), 'retained validators need synthetic coverage')
        self.assertEqual(expected - refused, set(), 'every retained validator must reject a planted fault')


if __name__ == '__main__':
    unittest.main()
