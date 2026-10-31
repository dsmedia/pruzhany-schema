"""Exact procedural wire bytes and planted changes, with no archive data."""

import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

import jsonschema
import yaml

from support import LINKML, load

backend = load('answer_generator')
generate = load('generate')

# Immutable SHA-256 of the current steps answer.schema.json files: four inspected 30 October 2026,
# quote_english (steps prompts/quote_english/3cb9e3e4cd4ad29d) on 31 October 2026. These are procedural schemas, never real answers or prompt text.
BASELINE = {
    'find_items': (1542, 'b44547bd3d88515a54d9c8544cdd8595d2308b4cf9112ce8af862463d43560b0'),
    'read_latin': (635, '529977c7df7b63f79a97d8e975ef5043e5cfc0257727736262342acf4fc3097e'),
    'write_english': (4565, '8bd979a3c233cc8dc0e20d27a38d8c176e4687eca9560e2a5176630791e91b59'),
    'join_people': (950, '2d73aab39f5b878e66d1bd465feff0064c469a3b2e0f227699756d01335d9297'),
    'quote_english': (649, 'b59b12bcecfb09dd34482d1fb63b8be2e8d3feb66d5c78bcd988b214600bc3d9'),
}


class Answers(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name) / 'linkml'
        (self.root / 'schema').mkdir(parents=True)
        self.source = self.root / 'schema/answers.yaml'
        shutil.copyfile(LINKML / 'schema/answers.yaml', self.source)
        self.data = yaml.safe_load(self.source.read_text())
        entry = next(e for e in generate.modules(LINKML) if e['name'] == 'answers')
        (self.root / 'modules.json').write_text(json.dumps({'modules': [entry]}))

    def save(self):
        self.source.write_text(yaml.safe_dump(self.data, sort_keys=False), encoding='utf-8')

    def test_every_wire_string_equals_the_released_bytes(self):
        answers, _ = backend.build(self.source)
        self.assertEqual(answers.keys(), BASELINE.keys())
        for asking, text in answers.items():
            raw = text.encode('utf-8')
            with self.subTest(asking=asking):
                self.assertEqual((len(raw), hashlib.sha256(raw).hexdigest()), BASELINE[asking])
                self.assertEqual(raw, (LINKML / 'generated/external/answers' / f'{asking}.schema.json').read_bytes())
                self.assertFalse(raw.endswith(b'\n'))
                jsonschema.Draft202012Validator.check_schema(json.loads(text))

    def test_description_enum_order_and_requiredness_each_change_wire_bytes(self):
        original, _ = backend.build(self.source)
        for fault in ('class description', 'field description', 'enum value', 'enum order', 'field order', 'requiredness', 'nullable', 'default'):
            with self.subTest(fault=fault):
                self.data = yaml.safe_load((LINKML / 'schema/answers.yaml').read_text())
                cls = self.data['classes']['JoinPeopleGroup']
                fields = cls['attributes']
                if fault == 'class description':
                    cls['description'] += ' Changed.'
                elif fault == 'field description':
                    fields['name']['description'] += ' Changed.'
                elif fault == 'enum value':
                    fields['certainty']['equals_string_in'][0] = 'invented'
                elif fault == 'enum order':
                    fields['certainty']['equals_string_in'].reverse()
                elif fault == 'field order':
                    cls['attributes'] = dict(reversed(list(fields.items())))
                elif fault == 'requiredness':
                    fields['name']['required'] = False
                elif fault == 'nullable':
                    fields['name'].setdefault('annotations', {})['nullable'] = True
                else:
                    fields['names'].setdefault('annotations', {})['default_empty_list'] = True
                self.save()
                changed, _ = backend.build(self.source)
                self.assertNotEqual(changed['join_people'], original['join_people'])
                self.assertEqual({k: v for k, v in changed.items() if k != 'join_people'},
                                 {k: v for k, v in original.items() if k != 'join_people'})

    def test_unsupported_constructs_are_refused_instead_of_dropped(self):
        for fault in ('pattern', 'is_a', 'unknown annotation', 'unknown range', 'bad flag', 'list default', 'recursive', 'imports', 'class title collision', 'enum range', 'unused class'):
            with self.subTest(fault=fault):
                self.data = yaml.safe_load((LINKML / 'schema/answers.yaml').read_text())
                cls = self.data['classes']['JoinPeopleGroup']
                slot = cls['attributes']['name']
                if fault == 'pattern':
                    slot['pattern'] = '^x$'
                elif fault == 'is_a':
                    cls['is_a'] = 'FindItemsAnswer'
                elif fault == 'unknown annotation':
                    slot['annotations'] = {'future_rule': True}
                elif fault == 'unknown range':
                    slot['range'] = 'date'
                elif fault == 'bad flag':
                    slot['required'] = 'false'
                elif fault == 'list default':
                    slot['annotations'] = {'default_empty_list': True}
                elif fault == 'recursive':
                    slot.update(range='JoinPeopleGroup', inlined=True)
                elif fault == 'imports':
                    self.data['imports'].append('unreviewed')
                elif fault == 'class title collision':
                    cls['title'] = 'Answer'
                elif fault == 'enum range':
                    cls['attributes']['certainty']['range'] = 'integer'
                else:
                    self.data['classes']['Unused'] = dict(cls)
                self.save()
                with self.assertRaises(ValueError):
                    backend.build(self.source)

    def test_required_nullable_and_defaults_keep_the_wire_contract(self):
        answers, _ = backend.build(self.source)
        english = json.loads(answers['write_english'])
        piece = english['$defs']['AnsweredPiece']
        self.assertIn('life_event', piece['required'])
        self.assertEqual(piece['properties']['life_event']['anyOf'][1], {'type': 'null'})
        schema = json.loads(answers['find_items'])
        self.assertIn('headings', schema['required'])
        self.assertEqual(schema['properties']['headings']['default'], [])
        validator = jsonschema.Draft202012Validator(schema)
        self.assertTrue(validator.is_valid({'items': [], 'headings': [], 'running_head': []}))
        self.assertFalse(validator.is_valid({'items': []}))
        self.assertFalse(validator.is_valid({'items': [], 'headings': None, 'running_head': []}))

    def test_generation_check_names_changed_missing_and_extra_answer_files(self):
        generate.regenerate(self.root)
        self.assertEqual(generate.differences(self.root), [])
        target = self.root / 'generated/external/answers/find_items.schema.json'
        original = target.read_bytes()
        target.write_bytes(original + b' ')
        self.assertIn('external/answers/find_items.schema.json: differs', '\n'.join(generate.differences(self.root)))
        target.unlink()
        extra = target.with_name('stale.schema.json')
        extra.write_bytes(original)
        faults = '\n'.join(generate.differences(self.root))
        self.assertIn('external/answers/find_items.schema.json: missing', faults)
        self.assertIn('external/answers/stale.schema.json: extra', faults)

    def test_external_inventory_covers_all_classes_without_entering_the_site_contract(self):
        inventory = json.loads((LINKML / 'generated/external/answers/contract.json').read_text())
        site = json.loads((LINKML / 'generated/contract.json').read_text())
        self.assertEqual(inventory['external_contract'], 'model-answers')
        self.assertEqual(inventory['classes'].keys(), self.data['classes'].keys())
        self.assertFalse(inventory['classes'].keys() & site['classes'].keys())
