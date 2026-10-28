"""Every check of the record's twins is accounted for in linkml/checks/record.yaml.

The twins' checks are found afresh in their files (a Zod .refine(, .superRefine( or .check(; a
Pydantic @model_validator, @field_validator or AfterValidator and its kin), each by the name it
belongs to, and must be exactly the checks the file lists. A part held by a LinkML rule names
the rule, which must exist, and gives an instance that passes and one that fails, both tried
against the generated JSON Schema; every rule of the record's modules must be named by some
part. A part held by the rule catalog names a rule id or proposes one with its statement.
"""

import ast
import collections
import copy
import json
import os
import re
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft201909Validator

from support import LINKML, ROOT

CHECKS = LINKML / 'checks' / 'record.yaml'
SCHEMA = json.loads((LINKML / 'generated' / 'json-schema' / 'shared-record.schema.json').read_text(encoding='utf-8'))
MODULES = ['sourced_entities', 'media', 'shared_record', 'shared']
ZOD = ['zod/sourced-entities.schema.ts', 'zod/shared-record.schema.ts', 'zod/media.schema.ts',
       'zod/shared.schema.ts', 'zod/citation-requirements.ts']
PYDANTIC = ['pydantic/sourced_entities.py', 'pydantic/shared_record.py', 'pydantic/media.py',
            'pydantic/shared.py', 'pydantic/citation_requirements.py']
PYDANTIC_DECORATORS = {'model_validator', 'field_validator'}
PYDANTIC_CALLS = {'AfterValidator', 'BeforeValidator', 'PlainValidator', 'WrapValidator'}


def sibling(name, variable):
    """Another checkout: where the variable names, else a folder of that name beside this one."""
    if os.environ.get(variable):
        return Path(os.environ[variable])
    return next((folder / name for folder in ROOT.parents if (folder / name).is_dir()), Path(name))


STEPS_RULES = sibling('pruzhany-steps', 'PRUZHANY_STEPS') / 'record' / 'rules.yaml'


def zod_checks(text):
    """(name, call) for each refinement, named by the const or function it is written in."""
    owner = None
    for line in text.splitlines():
        found = re.match(r'^(?:export )?(?:const|function) (\w+)', line)
        if found:
            owner = found.group(1)
        for call in re.findall(r'\.(refine|superRefine|check)\(', line):
            yield owner, call


def pydantic_checks(text):
    """(name, kind) for each validator: Class.method for a decorator, the alias for a call."""
    for node in ast.parse(text).body:
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    for decorator in item.decorator_list:
                        target = decorator.func if isinstance(decorator, ast.Call) else decorator
                        name = getattr(target, 'id', getattr(target, 'attr', None))
                        if name in PYDANTIC_DECORATORS:
                            yield f'{node.name}.{item.name}', name
        for sub in ast.walk(node):
            if isinstance(sub, ast.Call) and getattr(sub.func, 'id', None) in PYDANTIC_CALLS:
                if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
                    owner = node.targets[0].id
                else:
                    owner = getattr(node, 'name', type(node).__name__)
                yield owner, sub.func.id


def found_in_twins(root=ROOT):
    found = collections.Counter()
    for path in ZOD:
        for name, call in zod_checks((root / path).read_text(encoding='utf-8')):
            found[('zod', path, name, call)] += 1
    for path in PYDANTIC:
        for name, call in pydantic_checks((root / path).read_text(encoding='utf-8')):
            found[('pydantic', path, name, call)] += 1
    return found


def listed(checks):
    listed_ = collections.Counter()
    for entry in checks:
        for twin in ('zod', 'pydantic'):
            for place in entry.get(twin, []):
                listed_[(twin, place['file'], place['at'], place['call'])] += 1
    return listed_


def unaccounted(found, listed_):
    """What the twins hold and the file does not list, and what it lists and the twins do not."""
    return sorted(found - listed_), sorted(listed_ - found)


def words(text):
    return ' '.join(text.split())


def schema_classes():
    return {name: cls for module in MODULES
            for name, cls in (yaml.safe_load((LINKML / 'schema' / f'{module}.yaml').read_text(encoding='utf-8'))
                              .get('classes') or {}).items()}


def schema_rules(classes):
    """(class, kind, description) for every rule, any_of and none_of the classes carry."""
    for name, cls in classes.items():
        for rule in cls.get('rules') or []:
            yield name, 'rules', words(rule['description'])
        for kind in ('any_of', 'none_of'):
            if cls.get(kind):
                yield name, kind, words(cls[kind][0]['description'])


def holds_rule(classes, rules, name, description):
    """The class carries the rule, or inherits it: the generated JSON Schema gives a class its
    ancestors' rules, and not their any_of or none_of (linkml/README.md, measured)."""
    if any((name, kind, description) in rules for kind in ('rules', 'any_of', 'none_of')):
        return name
    parent = classes.get(name, {}).get('is_a')
    while parent:
        if (parent, 'rules', description) in rules:
            return parent
        parent = classes.get(parent, {}).get('is_a')
    return None


def instance(base, changes):
    made = copy.deepcopy(base)
    for key, value in changes.items():
        if value is None:
            made.pop(key, None)
        else:
            made[key] = value
    return made


def errors(class_name, value):
    validator = Draft201909Validator({'$schema': SCHEMA['$schema'], '$defs': SCHEMA['$defs'],
                                      '$ref': f'#/$defs/{class_name}'})
    return [error.message for error in validator.iter_errors(value)]


class TheAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file = yaml.safe_load(CHECKS.read_text(encoding='utf-8'))
        cls.checks = cls.file['checks']
        cls.parts = [(entry['id'], part) for entry in cls.checks for part in entry['parts']]

    def test_every_check_of_the_twins_is_listed_and_every_listed_one_exists(self):
        missing, stale = unaccounted(found_in_twins(), listed(self.checks))
        self.assertEqual(missing, [], 'checks in the twins that linkml/checks/record.yaml does not list')
        self.assertEqual(stale, [], 'checks linkml/checks/record.yaml lists that the twins no longer hold')

    def test_the_count(self):
        """A tally, so a check added to or taken from the twins shows here too."""
        found = found_in_twins()
        self.assertEqual(sum(n for key, n in found.items() if key[0] == 'zod'), 20)
        self.assertEqual(sum(n for key, n in found.items() if key[0] == 'pydantic'), 19)
        self.assertEqual(len(self.checks), 19)
        hows = collections.Counter(part['how'] for _, part in self.parts)
        self.assertEqual(hows, {'linkml_rule': 44, 'rule_catalog': 48})

    def test_a_planted_refinement_and_a_planted_validator_are_found_and_named(self):
        found = found_in_twins()
        planted = 'export const PlantedSchema = z.string()\n\t.refine((v) => v !== "x");\n'
        for name, call in zod_checks(planted):
            found[('zod', ZOD[0], name, call)] += 1
        planted = ('class Planted(Strict):\n    @model_validator(mode="after")\n    def check(self):\n'
                   '        return self\n\nNumber = Annotated[int, AfterValidator(abs)]\n')
        for name, call in pydantic_checks(planted):
            found[('pydantic', PYDANTIC[0], name, call)] += 1
        missing, stale = unaccounted(found, listed(self.checks))
        self.assertEqual(missing, [('pydantic', PYDANTIC[0], 'Number', 'AfterValidator'),
                                   ('pydantic', PYDANTIC[0], 'Planted.check', 'model_validator'),
                                   ('zod', ZOD[0], 'PlantedSchema', 'refine')])
        self.assertEqual(stale, [])

    def test_a_listed_check_the_twins_no_longer_hold_is_named(self):
        checks = copy.deepcopy(self.checks)
        checks[0]['zod'].append({'file': ZOD[0], 'at': 'GoneSchema', 'call': 'superRefine'})
        self.assertEqual(unaccounted(found_in_twins(), listed(checks)),
                         ([], [('zod', ZOD[0], 'GoneSchema', 'superRefine')]))

    def test_every_entry_says_what_it_holds_and_every_part_how(self):
        ids = [entry['id'] for entry in self.checks]
        self.assertEqual(len(ids), len(set(ids)))
        for entry in self.checks:
            with self.subTest(check=entry['id']):
                self.assertTrue(entry['holds'].strip())
                self.assertTrue(entry['parts'])
        for check, part in self.parts:
            with self.subTest(check=check, part=part['holds']):
                self.assertTrue(part['holds'].strip())
                self.assertIn(part['how'], ('linkml_rule', 'rule_catalog', 'twin_only'))
                if part['how'] == 'twin_only':
                    self.assertTrue(part['why'].strip())


class TheRules(unittest.TestCase):
    """Each part a LinkML rule holds: the rule is there, and the generated JSON Schema enforces it."""

    @classmethod
    def setUpClass(cls):
        data = yaml.safe_load(CHECKS.read_text(encoding='utf-8'))
        cls.bases = data['bases']
        cls.parts = [part for entry in data['checks'] for part in entry['parts'] if part['how'] == 'linkml_rule']
        cls.classes = schema_classes()
        cls.rules = set(schema_rules(cls.classes))

    def test_each_named_rule_exists_on_its_class_or_an_ancestor(self):
        for part in self.parts:
            with self.subTest(part=part['holds']):
                self.assertTrue(holds_rule(self.classes, self.rules, part['class'], words(part['rule'])))

    def unnamed(self, classes):
        rules = set(schema_rules(classes))
        named = {(holds_rule(classes, rules, part['class'], words(part['rule'])), words(part['rule']))
                 for part in self.parts}
        return {(name, rule) for name, _, rule in rules} - named

    def test_every_rule_of_the_record_s_modules_holds_some_check(self):
        self.assertEqual(self.unnamed(self.classes), set())

    def test_a_planted_rule_no_check_names_is_found(self):
        classes = copy.deepcopy(self.classes)
        classes['Review']['rules'].append({'description': 'A planted rule.'})
        self.assertEqual(self.unnamed(classes), {('Review', 'A planted rule.')})

    def test_a_rule_is_found_on_an_ancestor_and_an_any_of_is_not(self):
        rules = self.rules
        self.assertEqual(holds_rule(self.classes, rules, 'SharedName', words(
            'A supplied name has its attribution and its citations.')), 'Name')
        classes = copy.deepcopy(self.classes)
        del classes['SiteCitation']['any_of']
        self.assertIsNone(holds_rule(classes, set(schema_rules(classes)), 'SiteCitation',
                                     'A citation names where in its source the evidence is.'))
        self.assertIsNone(holds_rule(self.classes, rules, 'Review', 'A rule no class carries.'))

    def test_the_base_instances_pass(self):
        for name, base in self.bases.items():
            with self.subTest(base=name):
                self.assertEqual(errors(name, base), [])

    def test_each_rule_passes_its_control_and_refuses_its_planted_fault(self):
        for part in self.parts:
            with self.subTest(part=part['holds']):
                base = self.bases[part['class']]
                self.assertEqual(errors(part['class'], instance(base, part['passes'])), [])
                self.assertNotEqual(errors(part['class'], instance(base, part['fails'])), [])


class TheCatalogRules(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = yaml.safe_load(CHECKS.read_text(encoding='utf-8'))
        cls.parts = [part for entry in data['checks'] for part in entry['parts'] if part['how'] == 'rule_catalog']

    def test_each_names_a_rule_or_proposes_one_in_kebab_case_with_its_statement_and_tier(self):
        for part in self.parts:
            with self.subTest(part=part['holds']):
                self.assertEqual(('rule' in part) + ('proposed' in part), 1)
                if 'proposed' in part:
                    self.assertRegex(part['proposed'], r'^[a-z0-9]+(-[a-z0-9]+)*$')
                    self.assertTrue(part['statement'].strip())
                    self.assertIn(part['tier'], ('schema', 'rule'))
                    if part['tier'] == 'schema':
                        self.assertTrue(part['why'].strip(), 'a check within one object says why LinkML cannot')

    def test_a_proposed_id_has_one_statement(self):
        statements = collections.defaultdict(set)
        for part in self.parts:
            if 'proposed' in part:
                statements[part['proposed']].add((words(part['statement']), part['tier']))
        self.assertEqual({rule: found for rule, found in statements.items() if len(found) > 1}, {})

    @unittest.skipUnless(STEPS_RULES.is_file(), f'pruzhany-steps is not at {STEPS_RULES.parent.parent}')
    def test_against_the_catalog_a_named_rule_exists_and_a_proposed_one_does_not(self):
        catalog = {rule['id'] for rule in yaml.safe_load(STEPS_RULES.read_text(encoding='utf-8'))['rules']}
        for part in self.parts:
            with self.subTest(part=part['holds']):
                if 'rule' in part:
                    self.assertIn(part['rule'], catalog)
                else:
                    self.assertNotIn(part['proposed'], catalog)


if __name__ == '__main__':
    unittest.main()
