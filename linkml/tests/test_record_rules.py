"""What a LinkML rule can say in the generated JSON Schema, and a guard that the record's rules
say only that.

Measured on 28 October 2026 with LinkML 1.12.1: in a rule's condition, and in a class's any_of
or none_of, the generator keeps a key's presence or absence (`required`, `value_presence`), a
fixed text (`equals_string`), one of a list (`equals_string_in`) and a `pattern`. It drops a
`range`, a list's length (`minimum_cardinality`, `maximum_cardinality`) and a condition on
some or all of a list's items (`has_member`, `all_members`), without a word; it writes two
absences in one condition as "not both" where "neither" was meant; a rule with no
precondition gives a `then` with no `if`, which JSON Schema ignores; and a class does not take
its parent's any_of or none_of, only its rules. The first class below shows each, so a LinkML
upgrade that changes any of them fails here; the guard then keeps the record's modules
(sourced_entities, media, shared_record) to what holds.
"""

import json
import tempfile
import unittest
from pathlib import Path

import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

from support import LINKML

MODULES = ['sourced_entities', 'media', 'shared_record']
DROPPED = ('range', 'minimum_cardinality', 'maximum_cardinality', 'exact_cardinality', 'has_member',
           'all_members')

MEASURED = """id: https://pruzhany.org/ns/fixture-record-rules
name: fixture_record_rules
description: Each construct of a rule, once.
prefixes:
  linkml: https://w3id.org/linkml/
  pc: https://pruzhany.org/ns/sourced-entities#
default_prefix: pc
default_range: string
imports:
  - linkml:types
classes:
  Item:
    description: An item of a list.
    attributes:
      flag:
        description: A key.
  Parent:
    description: A parent with an any_of.
    attributes:
      a:
        description: A key.
      b:
        description: A key.
      kind:
        description: A key.
      items:
        range: Item
        multivalued: true
        inlined_as_list: true
        description: A list.
    any_of:
      - slot_conditions:
          a:
            required: true
    rules:
      - description: two absences
        preconditions:
          slot_conditions:
            kind:
              equals_string: one
        postconditions:
          slot_conditions:
            a:
              value_presence: ABSENT
            b:
              value_presence: ABSENT
      - description: a range and a length
        preconditions:
          slot_conditions:
            kind:
              equals_string: two
        postconditions:
          slot_conditions:
            a:
              range: integer
            items:
              minimum_cardinality: 2
              all_members:
                range_expression:
                  slot_conditions:
                    flag:
                      required: true
      - description: some item
        preconditions:
          slot_conditions:
            items:
              has_member:
                range_expression:
                  slot_conditions:
                    flag:
                      required: true
        postconditions:
          slot_conditions:
            b:
              required: true
      - description: no precondition
        postconditions:
          slot_conditions:
            b:
              required: true
  Child:
    is_a: Parent
    description: A child.
"""


def generated(text, top='Parent'):
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / 'schema.yaml'
        path.write_text(text, encoding='utf-8')
        return json.loads(JsonSchemaGenerator(str(path), top_class=top).serialize())


def rule_findings(schema):
    """What a module's rules, any_of and none_of say that the generator would not keep."""
    found = []

    def expression(where, node):
        conditions = node.get('slot_conditions') or {}
        absent = [name for name, condition in conditions.items()
                  if (condition or {}).get('value_presence') == 'ABSENT']
        if len(absent) > 1:
            found.append(f'{where}: two absences in one condition ({", ".join(absent)}); use none_of')
        for name, condition in conditions.items():
            for key in DROPPED:
                if key in (condition or {}):
                    found.append(f'{where}: {name} uses {key}, which the generator drops')
        for kind in ('any_of', 'none_of', 'all_of', 'exactly_one_of'):
            for index, branch in enumerate(node.get(kind) or []):
                expression(f'{where} {kind}[{index}]', branch)

    for name, cls in (schema.get('classes') or {}).items():
        for rule in cls.get('rules') or []:
            where = f'{name} rule "{rule.get("description", "").strip()}"'
            if not rule.get('preconditions'):
                found.append(f'{where}: no precondition, so the generated then has no if')
            for part in ('preconditions', 'postconditions', 'elseconditions'):
                if rule.get(part):
                    expression(f'{where} {part}', rule[part])
        for kind in ('any_of', 'none_of'):
            for index, branch in enumerate(cls.get(kind) or []):
                expression(f'{name} {kind}[{index}]', branch)
    return found


class WhatTheGeneratorKeeps(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.defs = generated(MEASURED)['$defs']

    def rule(self, number):
        return self.defs['Parent']['allOf'][number]

    def test_two_absences_become_not_both(self):
        self.assertEqual(self.rule(0)['then']['not'], {'required': ['a', 'b']})

    def test_a_range_a_length_and_every_item_are_dropped(self):
        then = self.rule(1)['then']['properties']
        self.assertEqual(then['a'], {})
        self.assertEqual(then['items'], {'items': {}, 'type': 'array'})

    def test_some_item_is_dropped_and_the_condition_becomes_mere_presence(self):
        self.assertEqual(self.rule(2)['if'], {'properties': {'items': {'items': {}, 'type': 'array'}},
                                              'required': ['items']})

    def test_a_rule_without_a_precondition_has_no_if(self):
        self.assertNotIn('if', self.rule(3))
        self.assertIn('then', self.rule(3))

    def test_a_child_takes_its_parent_s_rules_and_not_its_any_of(self):
        self.assertIn('anyOf', self.defs['Parent'])
        self.assertNotIn('anyOf', self.defs['Child'])
        self.assertEqual(self.defs['Child']['allOf'], self.defs['Parent']['allOf'])


class TheGuard(unittest.TestCase):
    def test_the_record_s_modules_use_only_what_the_generator_keeps(self):
        for module in MODULES:
            with self.subTest(module=module):
                schema = yaml.safe_load((LINKML / 'schema' / f'{module}.yaml').read_text(encoding='utf-8'))
                self.assertEqual(rule_findings(schema), [])

    def test_the_guard_finds_each_planted_construct(self):
        findings = rule_findings(yaml.safe_load(MEASURED))
        self.assertEqual(len(findings), 6, findings)
        for words in ('two absences', 'a uses range', 'items uses minimum_cardinality',
                      'items uses all_members', 'items uses has_member', 'no precondition'):
            with self.subTest(construct=words):
                self.assertTrue(any(words in finding for finding in findings), findings)


if __name__ == '__main__':
    unittest.main()
