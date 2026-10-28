"""linkml/checks/documents.yaml: every check the twins of the documents make, accounted for.

The Zod refinements and Pydantic validators of the modules it names are counted afresh and must
be exactly its entries, each at the place it names; each LinkML rule it cites is on its class and
refuses a planted failure; each rule id it cites from pruzhany-steps' record/rules.yaml is there
(when that checkout is at hand). Also here: the two rules whose values come from elsewhere, the
content items' version stamp and the subtypes' parents, against their sources.
"""

import ast
import copy
import json
import os
import re
import unittest
from pathlib import Path

import yaml
from linkml_runtime.utils.schemaview import SchemaView

from support import LINKML, ROOT, load
from test_documents import fixture, generated, refusals

CHECKS_FILE = LINKML / 'checks' / 'documents.yaml'
CHECKS = yaml.safe_load(CHECKS_FILE.read_text(encoding='utf-8'))
HOW = {'linkml_rule', 'rule_catalog', 'twin_only'}
ZOD_REFINEMENT = re.compile(r'\.(?:refine|superRefine|check)\(')
PYDANTIC_VALIDATOR = re.compile(r'@(?:model_validator|field_validator)\b|\b(?:Before|After|Plain|Wrap)Validator\(')
KEBAB = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


def steps_checkout():
    """pruzhany-steps, where its rule catalog is: $PRUZHANY_STEPS, or beside this checkout's owner."""
    for candidate in (os.environ.get('PRUZHANY_STEPS'), '/home/user/pruzhany-steps', ROOT.parent / 'pruzhany-steps'):
        if candidate and (Path(candidate) / 'record' / 'rules.yaml').is_file():
            return Path(candidate)
    return None


def zod_span(file, schema):
    """The text of `export const <schema> = ...` up to the next top-level export."""
    text = (ROOT / file).read_text(encoding='utf-8')
    start = text.index(f'export const {schema} =')
    following = re.search(r'^export ', text[start + 1:], re.M)
    return text[start:start + 1 + following.start()] if following else text[start:]


def pydantic_validators(file, place):
    """How many validators stand at `Class.method` (its decorators) or on a module-level function
    (the XValidator(function) calls that use it)."""
    tree = ast.parse((ROOT / file).read_text(encoding='utf-8'))
    if '.' in place:
        cls_name, method = place.split('.')
        cls = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == cls_name)
        function = next(node for node in cls.body if isinstance(node, ast.FunctionDef) and node.name == method)
        return sum(bool(re.match(r'(?:model|field)_validator\b', ast.unparse(d))) for d in function.decorator_list)
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == place)
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Call) and re.fullmatch(r'(?:Before|After|Plain|Wrap)Validator', getattr(node.func, 'id', ''))
               and any(getattr(arg, 'id', None) == function.name for arg in node.args))


def literal_values(file, name):
    """The strings of `<name> = Literal[...]` in a Python module, read without importing it."""
    tree = ast.parse((ROOT / file).read_text(encoding='utf-8'))
    node = next(n for n in tree.body if isinstance(n, ast.Assign) and n.targets[0].id == name)
    elements = node.value.slice.elts if isinstance(node.value.slice, ast.Tuple) else [node.value.slice]
    return [element.value for element in elements]


class TheAccount(unittest.TestCase):
    def test_every_refinement_and_validator_of_the_twins_is_an_entry(self):
        zod = sum(len(ZOD_REFINEMENT.findall((ROOT / f).read_text(encoding='utf-8'))) for f in CHECKS['twins']['zod'])
        pydantic = sum(len(PYDANTIC_VALIDATOR.findall((ROOT / f).read_text(encoding='utf-8')))
                       for f in CHECKS['twins']['pydantic'])
        entries = CHECKS['checks']
        self.assertEqual(zod, sum('zod' in entry for entry in entries), 'Zod refinements and entries differ')
        self.assertEqual(pydantic, sum('pydantic' in entry for entry in entries),
                         'Pydantic validators and entries differ')
        # Measured on 28 October 2026; a change in the twins shows here first.
        self.assertEqual((zod, pydantic, len(entries)), (10, 12, 12))

    def test_each_entry_names_one_refinement_or_validator_where_it_is(self):
        for entry in CHECKS['checks']:
            with self.subTest(check=entry['id']):
                self.assertTrue('zod' in entry or 'pydantic' in entry)
                if 'zod' in entry:
                    self.assertIn(entry['zod']['file'], CHECKS['twins']['zod'])
                    span = zod_span(entry['zod']['file'], entry['zod']['schema'])
                    self.assertEqual(len(ZOD_REFINEMENT.findall(span)), 1, span[:80])
                if 'pydantic' in entry:
                    self.assertIn(entry['pydantic']['file'], CHECKS['twins']['pydantic'])
                    self.assertEqual(pydantic_validators(entry['pydantic']['file'], entry['pydantic']['validator']), 1)

    def test_a_planted_refinement_is_counted(self):
        """Control: one more refinement in a span is seen, and one less."""
        span = zod_span('zod/content-item.schema.ts', 'ContentItemSchema')
        self.assertEqual(len(ZOD_REFINEMENT.findall(span + '.refine((v) => true)')), 2)
        self.assertEqual(len(ZOD_REFINEMENT.findall(span.replace('.superRefine(', '.transform('))), 0)
        self.assertEqual(len(PYDANTIC_VALIDATOR.findall("@model_validator(mode='after')\n@field_validator('x')")), 2)

    def test_every_entry_and_part_is_complete(self):
        ids = [entry['id'] for entry in CHECKS['checks']]
        self.assertEqual(len(ids), len(set(ids)))
        proposed = []
        for entry in CHECKS['checks']:
            self.assertTrue(entry['holds'].strip())
            self.assertTrue(entry['parts'])
            for part in entry['parts']:
                with self.subTest(check=entry['id'], part=part['holds'][:40]):
                    self.assertIn(part['how'], HOW)
                    self.assertTrue(part['holds'].strip())
                    if part['how'] == 'rule_catalog':
                        self.assertEqual(('rule' in part) + ('proposed' in part), 1)
                        rule = part.get('rule') or part['proposed']
                        self.assertRegex(rule, KEBAB)
                        if 'statement' in part:
                            proposed.append(part.get('rule') or part['proposed'])
                            self.assertTrue(part['statement'].strip())
                    elif part['how'] == 'twin_only':
                        self.assertTrue(part['why'].strip())
                    else:
                        self.assertTrue(hasattr(LinkMLRules, part['planted'].rsplit('.', 1)[-1]), part['planted'])
        self.assertEqual(len(proposed), len(set(proposed)), 'an id is proposed twice')

    def test_the_tally(self):
        """How the definition holds the twins' checks, part by part."""
        tally = {'linkml_rule': 0, 'existing': 0, 'proposed': 0, 'twin_only': 0}
        for entry in CHECKS['checks']:
            for part in entry['parts']:
                if part['how'] == 'rule_catalog':
                    tally['existing' if 'rule' in part else 'proposed'] += 1
                else:
                    tally[part['how']] += 1
        self.assertEqual(tally, {'linkml_rule': 2, 'existing': 40, 'proposed': 0, 'twin_only': 2})

    def test_it_passes_the_house_lint(self):
        self.assertEqual(load('lint').lint(CHECKS_FILE), [])

    @unittest.skipIf(steps_checkout() is None, 'pruzhany-steps (its record/rules.yaml) is not at hand; set PRUZHANY_STEPS')
    def test_cited_rules_are_in_the_rule_catalog(self):
        catalog = yaml.safe_load((steps_checkout() / 'record' / 'rules.yaml').read_text(encoding='utf-8'))
        existing = {rule['id'] for rule in catalog['rules']}
        for entry in CHECKS['checks']:
            for part in entry['parts']:
                with self.subTest(check=entry['id'], part=part['holds'][:40]):
                    if 'rule' in part:
                        self.assertIn(part['rule'], existing)
                    if 'proposed' in part:
                        self.assertNotIn(part['proposed'], existing)


class LinkMLRules(unittest.TestCase):
    """Each LinkML rule the account cites, on its class, refusing a planted failure."""

    def test_every_rule_of_the_documents_is_cited_and_every_cited_rule_is_there(self):
        cited = {}
        for entry in CHECKS['checks']:
            for part in entry['parts']:
                if part['how'] == 'linkml_rule':
                    cited[part['class']] = cited.get(part['class'], 0) + part['rules']
        found = {}
        for module in ('site_common', 'pages', 'content_items', 'mentions', 'life_events', 'editions'):
            for name, cls in SchemaView(str(LINKML / 'schema' / f'{module}.yaml')).all_classes(imports=False).items():
                if cls.rules:
                    found[name] = len(cls.rules)
                    for rule in cls.rules:
                        self.assertTrue(rule.description and rule.description.strip(), name)
        self.assertEqual(cited, found)

    @staticmethod
    def without_rules(schema, cls):
        """The same JSON Schema with the class's rules taken out: the control for a planted case."""
        schema = copy.deepcopy(schema)
        schema['$defs'][cls].pop('allOf')
        return schema

    def test_a_subtype_under_another_type_is_refused(self):
        schema = generated('content_items')
        control = self.without_rules(schema, 'ContentItem')
        parents = subtype_parents()
        for subtype, parent in parents.items():
            for kind in ('article', 'ad', 'death_notice', 'entertainment', 'table'):
                document = copy.deepcopy(fixture('content_items'))
                document['content_items'][0].update(subtype=subtype, type=kind)
                with self.subTest(subtype=subtype, type=kind):
                    self.assertEqual(refusals(control, document), [])
                    self.assertEqual(refusals(schema, document) == [], kind == parent)
        document = copy.deepcopy(fixture('content_items'))
        for subtype in (None, ...):
            item = document['content_items'][0]
            item.pop('subtype') if subtype is ... else item.update(subtype=None)
            item['type'] = 'table'
            with self.subTest(subtype='left out' if subtype is ... else 'null'):
                self.assertEqual(refusals(schema, document), [])

    def test_a_printed_name_that_does_not_fit_the_grain_is_refused(self):
        schema = generated('mentions')
        control = self.without_rules(schema, 'IssueMention')
        words, regions = (copy.deepcopy(fixture('mentions')) for _ in range(2))
        del words['mentions'][0]['printed_name']           # words, and no printed name
        regions['mentions'][1]['printed_name'] = 'second'  # regions, and a printed name
        for name, document in (('words without a name', words), ('regions with a name', regions)):
            with self.subTest(name):
                self.assertEqual(refusals(control, document), [])
                self.assertNotEqual(refusals(schema, document), [])
        # What the rules cannot say (documents.yaml says so): a words mention whose name is null.
        null_name = copy.deepcopy(fixture('mentions'))
        null_name['mentions'][0]['printed_name'] = None
        self.assertEqual(refusals(schema, null_name), [])
        # A regions mention may leave the key out or give null (known-looser: required-key-nullable).
        absent = copy.deepcopy(fixture('mentions'))
        del absent['mentions'][1]['printed_name']
        self.assertEqual(refusals(schema, absent), [])


def subtype_parents():
    """Each subtype and its Impresso parent, as the rules of content_items.yaml say it."""
    cls = SchemaView(str(LINKML / 'schema' / 'content_items.yaml')).get_class('ContentItem')
    parents = {}
    for rule in cls.rules:
        parent = rule.postconditions.slot_conditions['type'].equals_string
        for subtype in rule.preconditions.slot_conditions['subtype'].equals_string_in:
            parents[subtype] = parent
    return parents


class ValuesFromElsewhere(unittest.TestCase):
    def test_the_subtype_rules_are_the_vocabulary_parents(self):
        vocabulary = json.loads((ROOT / 'vocabulary' / 'site-content.json').read_text(encoding='utf-8'))
        expected = {value['id']: value['parent_type'] for value in vocabulary['groups']['content_item_subtypes']}
        self.assertEqual(subtype_parents(), expected)

    def test_the_version_stamp_is_the_generated_compatible_versions(self):
        versions = literal_values('pydantic/site_content_vocabulary.py', 'SiteVocabularyVersion')
        slot = SchemaView(str(LINKML / 'schema' / 'content_items.yaml')).induced_slot('vocabulary_version',
                                                                                         'ContentItemsData')
        match = re.fullmatch(r'\^\((.+)\)\$\(\?!\[\\s\\S\]\)', slot.pattern)
        self.assertIsNotNone(match, slot.pattern)
        self.assertEqual([alternative.replace('\\.', '.') for alternative in match.group(1).split('|')], versions)
        self.assertEqual(versions, ['0.1.0', '1.0.0'])
        pattern = generated('content_items')['properties']['vocabulary_version']['pattern']
        for version in versions:
            self.assertRegex(version, pattern)
        for other in ('1.1.0', '1.0.0\n', '1x0x0', '01.0.0', ' 1.0.0', '1.0'):
            self.assertNotRegex(other, pattern)


if __name__ == '__main__':
    unittest.main()
