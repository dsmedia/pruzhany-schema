"""Ticket 03: the definition owns shared identifier shapes and their meanings."""
import copy
import json
import unittest

from jsonschema import Draft201909Validator
from linkml_runtime.utils.schemaview import SchemaView
from support import LINKML, ROOT


class SharedIdentifiers(unittest.TestCase):
    def test_all_four_carriers_reuse_one_evidenced_shape(self):
        view = SchemaView(str(LINKML / 'schema/shared_record.yaml'))
        for name in ('SharedPerson', 'SharedOrganization', 'SharedPlace', 'Holder'):
            with self.subTest(model=name):
                field = view.induced_slot('identifiers', name)
                self.assertEqual(field.range, 'PlaceIdentifier')
                self.assertEqual(field.slot_uri, 'rico:hasOrHadIdentifier')
                self.assertTrue(field.multivalued)
                self.assertEqual(field.minimum_cardinality, 1)
                self.assertFalse(field.required)
        field = view.induced_slot('type', 'PlaceIdentifier')
        self.assertEqual(field.slot_uri, 'rico:hasIdentifierType')
        self.assertEqual(field.range, 'IdentifierTypes')
        value = view.all_enums()['IdentifierTypes'].permissible_values['old_identifier']
        self.assertEqual(value.meaning, 'pc:old_identifier')

    def test_generated_document_keeps_evidence_constraints_on_each_new_carrier(self):
        schema = json.loads((LINKML / 'generated/json-schema/shared_record.schema.json').read_text())
        fixture = json.loads((ROOT / 'tests/contract/identifiers.fixtures.json').read_text())['example']
        validator = Draft201909Validator(schema)
        validator.validate(fixture)
        for carrier in ('persons', 'organizations'):
            for field in ('source_id', 'value', 'accessed', 'attribution'):
                changed = copy.deepcopy(fixture)
                del changed[carrier][0]['identifiers'][0][field]
                with self.subTest(carrier=carrier, field=field):
                    self.assertFalse(validator.is_valid(changed))
            for value in ([], [{'type': 'same_as'}]):
                changed = copy.deepcopy(fixture)
                changed[carrier][0]['identifiers'] = value
                with self.subTest(carrier=carrier, value=value):
                    self.assertFalse(validator.is_valid(changed))


if __name__ == '__main__':
    unittest.main()
