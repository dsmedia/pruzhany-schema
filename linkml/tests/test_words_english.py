"""Fictional exact-English witnesses, including both positions of the one switch."""
import copy
from functools import cache
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from jsonschema import Draft201909Validator
from support import LINKML, ROOT, load
from test_python_generation import package, models

backend = load('external_schema')
words = load('words_policy')


@cache
def activated_schema():
    generator = backend.ReleaseGenerator(str(LINKML / 'schema/shared_record.yaml'),
                                         top_class='SharedRecord', not_closed=False)
    rule, = [r for r in generator.schemaview.get_class('Citation').rules
             if r.title == 'require_non_english_quote_english']
    assert rule.deactivated
    rule.deactivated = False
    return json.loads(backend.release_rules(generator).serialize())


def validator(schema, name):
    return Draft201909Validator({'$schema': schema['$schema'], '$defs': schema['$defs'],
                                '$ref': '#/$defs/' + name})


class WordsEnglish(unittest.TestCase):
    def test_the_one_source_switch_generates_both_runtime_values(self):
        active, pairs = words.policy(LINKML)
        self.assertFalse(active)
        self.assertEqual(pairs['Citation'], {'quote_english': 'quote'})
        self.assertEqual(sum(len(fields) for cls, fields in pairs.items()
                             if cls != 'SiteCitation'), 3)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(LINKML / 'schema', root / 'schema')
            shutil.copyfile(LINKML / 'modules.json', root / 'modules.json')
            source = root / 'schema/sourced_entities.yaml'
            text = source.read_text()
            self.assertEqual(text.count('deactivated: true'), 1)
            source.write_text(text.replace('deactivated: true', 'deactivated: false'))
            python, ts = words.outputs(root)
            self.assertIn('REQUIRE_NON_ENGLISH_QUOTE_ENGLISH = True', python)
            self.assertIn('REQUIRE_NON_ENGLISH_QUOTE_ENGLISH = true', ts)
            self.assertEqual(words.policy(root)[1], pairs)

    def test_active_rule_agrees_with_both_twins_including_inherited_citations(self):
        package()
        runtime = importlib.import_module('generation_tests_schema.words_english')
        original = 'Di erd iz rund.'
        english = {'text': 'The earth is round.', 'language': 'en',
                   'based_on': {'source_text': original, 'addresses': [
                       {'image_uri': 'fictional.png', 'bbox': [0, 0, 10, 10], 'text': original}]},
                   'attribution': {'kind': 'person', 'by': 'Fictional translator', 'on': '2000-01-01'}}
        released = json.loads((LINKML / 'generated/json-schema/shared_record.schema.json').read_text())
        cases = []
        missing = object()
        for model in ('Citation', 'SiteCitation'):
            active_validator = validator(activated_schema(), model)
            for language in (missing, None, 'yi', 'de', 'und', 'en', 'en-US', 'EN-gb'):
                for translation in (missing, None, english):
                    value = {'source_id': 'fictional-source', 'page': '1', 'quote': original}
                    if language is not missing:
                        value['quote_language'] = language
                    if translation is not missing:
                        value['quote_english'] = translation
                    expected = translation is english or language in ('en', 'en-US', 'EN-gb')
                    with self.subTest(model=model, language=repr(language), english=translation is english):
                        self.assertTrue(validator(released, model).is_valid(value))
                        self.assertEqual(active_validator.is_valid(value), expected)
                        with patch.object(runtime, 'REQUIRE_NON_ENGLISH_QUOTE_ENGLISH', True):
                            try:
                                getattr(models(), model).model_validate_json(json.dumps(value))
                                accepted = True
                            except ValueError:
                                accepted = False
                        self.assertEqual(accepted, expected)
                    cases.append({'model': model, 'value': value, 'valid': expected})
            for quote in (missing, None, '', '  '):
                value = {'source_id': 'fictional-source', 'page': '1'}
                if quote is not missing:
                    value['quote'] = quote
                self.assertTrue(active_validator.is_valid(value))
                cases.append({'model': model, 'value': value, 'valid': True})
        result = subprocess.run(['bun', str(ROOT / 'tests/contract/check_quote_english.ts')],
                                input=json.dumps(cases), capture_output=True, text=True,
                                cwd=ROOT, check=True)
        self.assertEqual(json.loads(result.stdout), [c['valid'] for c in cases])

    def test_released_json_schema_validates_translation_shapes_but_twins_compare_text(self):
        # The runtime corpus rejects exact-text mismatches. JSON Schema deliberately
        # cannot compare sibling values; assert that boundary rather than claiming it can.
        from test_python_generation import contract_cases
        index = json.loads((LINKML / 'generated/contract.json').read_text())
        source = json.loads((ROOT / 'tests/contract/words-english.fixtures.json').read_text())
        names = {c['name'] for c in source['cases']}
        for case in contract_cases():
            if case['name'] not in names:
                continue
            binding_mismatch = ('changed bytes refused' in case['name']
                                or case['name'].endswith('document binding False'))
            # Tuple/calendar behavior belongs to the already retained twins too.
            shape_only = binding_mismatch or 'bad box' in case['name'] or 'bad attribution day' in case['name'] or 'null check' in case['name']
            with self.subTest(case=case['name']):
                accepted = validator(index, case['model']).is_valid(case['value'])
                self.assertEqual(accepted, case['valid'] or shape_only)

    def test_typed_rule_conditions_are_opt_in_and_fail_closed(self):
        # A null Translation must not satisfy the enabled requirement, and an
        # unannotated existing condition still has its pinned native semantics.
        active = validator(activated_schema(), 'Citation')
        self.assertFalse(active.is_valid({'source_id': 's', 'page': '1', 'quote': 'words',
                                         'quote_language': 'yi', 'quote_english': None}))
        import yaml
        with tempfile.TemporaryDirectory() as folder:
            schema = yaml.safe_load((LINKML / 'schema/sourced_entities.yaml').read_text())
            condition = schema['classes']['Citation']['rules'][0]['postconditions']['slot_conditions']['quote_english']
            del condition['range']
            # Keep relative imports resolvable without modifying the checkout.
            shutil.copytree(LINKML / 'schema', Path(folder) / 'schema')
            target = Path(folder) / 'schema/sourced_entities.yaml'
            target.write_text(yaml.safe_dump(schema, sort_keys=False))
            generator = backend.ReleaseGenerator(str(target), top_class='Citation')
            with self.assertRaisesRegex(ValueError, 'typed condition needs an explicit range'):
                generator.serialize()


if __name__ == '__main__':
    unittest.main()
