"""External prompt metadata and kept-answer references, using invented data only.

The steps exchange check owns byte hashes, history and validation of private answer
payloads. These tests enforce the metadata contract and its separation from site models.
"""

import copy
import json
import unittest

from jsonschema.validators import validator_for
from linkml_runtime.utils.schemaview import SchemaView

from support import FIXTURES, LINKML, load

FOLDER = FIXTURES / 'exchanges'
SCHEMA = json.loads((LINKML / 'generated/json-schema/exchanges.schema.json').read_text(encoding='utf-8'))
PROMPT = json.loads((FOLDER / 'prompt-version.json').read_text(encoding='utf-8'))
ASKING = json.loads((FOLDER / 'kept-asking.json').read_text(encoding='utf-8'))
VIEW = SchemaView(str(LINKML / 'schema/exchanges.yaml'))


def validator(document):
    cls = validator_for(document)
    cls.check_schema(document)
    return cls(document, format_checker=cls.FORMAT_CHECKER)


class Exchanges(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prompt = validator(SCHEMA)
        cls.asking = validator({'$schema': SCHEMA['$schema'], '$defs': SCHEMA['$defs'],
                               '$ref': '#/$defs/KeptAsking'})

    def test_direct_metadata_root_and_separate_kept_asking_definition(self):
        self.prompt.validate(PROMPT)
        self.asking.validate(ASKING)
        self.assertFalse(self.prompt.is_valid(ASKING))
        self.assertFalse(self.asking.is_valid(PROMPT))
        self.assertEqual(SCHEMA['$schema'], 'https://json-schema.org/draft/2019-09/schema')

    def test_every_metadata_field_and_required_key(self):
        expected = {
            'PromptVersion': (PROMPT, self.prompt, {'effort'}),
            'KeptAsking': (ASKING, self.asking, {'day', 'input_fingerprint', 'cost_usd'}),
        }
        self.assertEqual(set(VIEW.all_classes(imports=False)), set(expected))
        for name, (fixture, check, optional) in expected.items():
            shape = SCHEMA['$defs'][name]
            self.assertEqual(set(shape['properties']), set(fixture))
            self.assertEqual(set(shape['required']), set(fixture) - optional)
            self.assertIs(shape['additionalProperties'], False)
            for field in fixture:
                document = copy.deepcopy(fixture)
                del document[field]
                with self.subTest(cls=name, missing=field):
                    self.assertEqual(check.is_valid(document), field in optional)
                document[field] = None
                with self.subTest(cls=name, null=field):
                    self.assertFalse(check.is_valid(document))

    def test_optional_fields_can_all_be_absent_without_fabricating_values(self):
        prompt = {k: v for k, v in PROMPT.items() if k != 'effort'}
        asking = {k: ASKING[k] for k in ('prompt_code', 'model', 'answer_file')}
        self.prompt.validate(prompt)
        self.asking.validate(asking)

    def test_prompt_codes_and_input_fingerprints_are_short_hex_not_full_sha256(self):
        for fixture, check, field in ((PROMPT, self.prompt, 'code'),
                                      (ASKING, self.asking, 'prompt_code'),
                                      (ASKING, self.asking, 'input_fingerprint')):
            for value in ('', 'a' * 15, 'a' * 17, 'a' * 64, 'A' * 16, 'g' * 16,
                          'a' * 16 + '\n', 123, True):
                with self.subTest(field=field, value=value):
                    self.assertFalse(check.is_valid({**fixture, field: value}))
            self.assertTrue(check.is_valid({**fixture, field: 'a' * 16}))

    def test_history_uses_full_commit_ids(self):
        for field in ('first_commit', 'last_commit'):
            for value in ('abc1234', 'a' * 39, 'a' * 41, 'G' * 40, 'a' * 40 + '\n', 123):
                with self.subTest(field=field, value=value):
                    self.assertFalse(self.prompt.is_valid({**PROMPT, field: value}))

    def test_calendar_days_need_format_checking_and_no_invented_time(self):
        for fixture, check, field in ((PROMPT, self.prompt, 'first_day'),
                                      (PROMPT, self.prompt, 'last_day'),
                                      (ASKING, self.asking, 'day')):
            for value in ('2026-02-29', '2026-04-31', '2026-13-01', '2026-1-01',
                          '2026-10-15T00:00:00Z', '2026-10-15\n', 20261015):
                with self.subTest(field=field, value=value):
                    self.assertFalse(check.is_valid({**fixture, field: value}))
            self.assertTrue(check.is_valid({**fixture, field: '2024-02-29'}))

    def test_budget_and_cost_are_nonnegative_numbers_and_distinct(self):
        for fixture, check, field in ((PROMPT, self.prompt, 'budget_usd'),
                                      (ASKING, self.asking, 'cost_usd')):
            for value in (0, 0.125, 100):
                self.assertTrue(check.is_valid({**fixture, field: value}))
            for value in (-0.01, '1.25', True, [], {}):
                with self.subTest(field=field, value=value):
                    self.assertFalse(check.is_valid({**fixture, field: value}))
        self.assertFalse(self.prompt.is_valid({**PROMPT, 'cost_usd': 1}))
        self.assertFalse(self.asking.is_valid({**ASKING, 'budget_usd': 1}))

    def test_shape_recovery_is_explicit_boolean_including_false(self):
        self.prompt.validate({**PROMPT, 'shape_recovered': False})
        for value in ('false', 0, 1, [], {}):
            with self.subTest(value=value):
                self.assertFalse(self.prompt.is_valid({**PROMPT, 'shape_recovered': value}))

    def test_names_model_settings_and_paths_are_nonblank_text(self):
        for fixture, check, fields in ((PROMPT, self.prompt, ('asking', 'model', 'effort', 'shape_name')),
                                       (ASKING, self.asking, ('model', 'answer_file'))):
            for field in fields:
                for value in ('', ' \n\t', 7, [], {}):
                    with self.subTest(field=field, value=value):
                        self.assertFalse(check.is_valid({**fixture, field: value}))
        # No moving list of model or effort selectors is frozen into this contract.
        self.prompt.validate({**PROMPT, 'model': 'another-invented-model', 'effort': 'invented-effort'})

    def test_closed_metadata_refuses_payloads_and_misspelled_fields(self):
        for fixture, check in ((PROMPT, self.prompt), (ASKING, self.asking)):
            for field in ('typo', 'answer', 'pieces', 'system', 'prompt', 'request'):
                with self.subTest(field=field):
                    self.assertFalse(check.is_valid({**fixture, field: 'invented'}))

    def test_external_inventory_learning_reference_and_dictionary_cover_both_classes(self):
        classes = {'PromptVersion', 'KeptAsking'}
        inventory = json.loads((LINKML / 'generated/external/exchanges/contract.json').read_text())
        learning = json.loads((LINKML / 'generated/external/exchanges/docs/model-index.json').read_text())
        production = json.loads((LINKML / 'generated/contract.json').read_text())
        self.assertEqual(inventory['external_contract'], 'model-exchanges')
        self.assertEqual(set(inventory['classes']), classes)
        self.assertEqual(set(learning['models']), classes)
        self.assertTrue(classes.isdisjoint(production['classes']))
        fields = {field['name']: field for field in learning['models']['KeptAsking']['fields']}
        self.assertEqual(fields['prompt_code']['references'], ['PromptVersion.code'])
        self.assertEqual(fields['prompt_code']['relationship'], 'reference')
        dictionary = (LINKML / 'generated/docs/data-dictionary.md').read_text()
        for name in classes:
            self.assertIn('### ' + name + '\n', dictionary)

    def test_prov_is_documented_without_ontology_bindings_or_new_prefix(self):
        self.assertEqual(set(VIEW.schema.prefixes), {'linkml', 'pc'})
        self.assertEqual(str(VIEW.schema.annotations['json_schema_nulls'].value), 'explicit')
        for name in VIEW.all_classes(imports=False):
            cls = VIEW.get_class(name)
            self.assertTrue(any(url.startswith('https://www.w3.org/TR/prov-o/#') for url in cls.see_also))
            for element in (cls, *VIEW.class_induced_slots(name)):
                self.assertIsNone(getattr(element, 'class_uri', None))
                self.assertIsNone(getattr(element, 'slot_uri', None))
                for key in ('exact_mappings', 'close_mappings', 'related_mappings',
                            'broad_mappings', 'narrow_mappings'):
                    self.assertFalse(getattr(element, key))

    def test_external_manifest_registers_the_direct_metadata_root(self):
        # The general generator tests plant unknown contracts and missing roots.
        entries = load('generate').modules(LINKML)
        entry = next(entry for entry in entries if entry['name'] == 'exchanges')
        self.assertEqual(entry['top_class'], 'PromptVersion')
        self.assertEqual(entry['external_contract'], 'model-exchanges')


if __name__ == '__main__':
    unittest.main()
