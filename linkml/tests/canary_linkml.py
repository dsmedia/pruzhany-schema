"""Canaries: LinkML 1.12.1's faults that the house lint and known-looser.yaml rest on.

Each test asserts today's behaviour, measured in the plan (pruzhany-steps
.scratch/linkml/plan.md, section 3, items 1 to 3). When an upgrade of LinkML changes it, fixed
or otherwise, the canary fails: then the rule it guards in linkml/lint.py, and what README.md
and known-looser.yaml say about it, are read again and changed with the canary in one commit.
Each canary also runs a control case that the same tool does catch, so a canary cannot pass
because the tool did nothing.
"""

import json
import unittest

from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.generators.pydanticgen import PydanticGenerator
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin, PydanticValidationPlugin
from linkml_runtime.utils.compile_python import compile_python

from support import FIXTURES

CANARY = FIXTURES / 'canary'


class ExactCardinalityIsDropped(unittest.TestCase):
    """Guards the house lint's exact-cardinality rule (plan section 3, item 1).

    gen-json-schema writes minItems and maxItems for minimum_cardinality with
    maximum_cardinality, and nothing at all for exact_cardinality.
    """

    def test(self):
        schema = json.loads(JsonSchemaGenerator(str(CANARY / 'cardinality.yaml'), top_class='Pairs').serialize())
        bounded = schema['properties']['bounded_pair']
        self.assertEqual((bounded.get('minItems'), bounded.get('maxItems')), (2, 2))  # the control
        exact = schema['properties']['exact_pair']
        self.assertNotIn('minItems', exact)
        self.assertNotIn('maxItems', exact)
        self.assertEqual(exact['items'], {'type': 'integer'})


class PydanticBoundsTheWholeList(unittest.TestCase):
    """Guards the house lint's bound-on-a-list rule (plan section 3, item 2).

    gen-pydantic on the trial's page schema (pruzhany-steps docs/record/linkml-trial/, copied
    into fixtures/canary/) puts minimum_value 1 of the multivalued slot `dimensions` on the
    list itself, and the trial's own sample page is then refused: "Unable to apply constraint
    'ge' to supplied value [3200, 4794]". The raw text is validated, as strict Pydantic needs.
    """

    def test(self):
        code = PydanticGenerator(str(CANARY / 'page.linkml.yaml')).serialize()
        dimensions = next(line.strip() for line in code.splitlines() if line.strip().startswith('dimensions:'))
        self.assertTrue(dimensions.startswith('dimensions: list[int] = Field('), dimensions)
        self.assertIn('ge=1', dimensions)
        self.assertIn('min_length=2, max_length=2', dimensions)
        models = compile_python(code)
        sample = (CANARY / '1938-12-16-page1-with-words.json').read_text(encoding='utf-8')
        with self.assertRaisesRegex(Exception, r"Unable to apply constraint 'ge' to supplied value \[3200, 4794\]"):
            models.PagesData.model_validate_json(sample)
        # The control: the same models refuse a page without its number, by validation.
        page = json.loads(sample)
        del page['pages'][0]['page_number']
        page['pages'][0]['dimensions'] = 2  # not a list, so the fault above is not what refuses it
        with self.assertRaisesRegex(Exception, 'page_number'):
            models.PagesData.model_validate_json(json.dumps(page))


class UniqueKeysAreNotEnforced(unittest.TestCase):
    """Guards the house lint's unique-keys rule (plan section 3, item 3).

    linkml-validate, with its JSON Schema plugin and with its Pydantic plugin, finds no issue in
    a container whose two items share the key that unique_keys declares. LinkML's JSON Schema
    page says so ("Currently JSON-Schema does not yet support unique keys",
    https://linkml.io/linkml/generators/json-schema.html, read 28 October 2026).
    """

    def test(self):
        schema = str(CANARY / 'unique-keys.yaml')
        shared_key = {'items': [{'key': 'a'}, {'key': 'a'}]}
        missing_key = {'items': [{'key': 'a'}, {}]}
        for plugin in (JsonschemaValidationPlugin(closed=True), PydanticValidationPlugin()):
            with self.subTest(plugin=type(plugin).__name__):
                validator = Validator(schema, validation_plugins=[plugin])
                self.assertEqual(validator.validate(shared_key, 'Container').results, [])
                self.assertNotEqual(validator.validate(missing_key, 'Container').results, [])  # the control


if __name__ == '__main__':
    unittest.main()
