"""Teaching metadata resolves inheritance and refuses invented reference links."""

import copy
import json
import unittest
from support import LINKML, load

learning = load('learning_index')


class LearningIndex(unittest.TestCase):
    def setUp(self):
        self.index = json.loads((LINKML / 'generated/docs/model-index.json').read_text())

    def test_every_owned_model_and_field_is_documented(self):
        contract = json.loads((LINKML / 'generated/contract.json').read_text())
        self.assertEqual(set(self.index['models']), set(contract['classes']))
        for name, model in self.index['models'].items():
            with self.subTest(name=name):
                self.assertEqual({f['name'] for f in model['fields']},
                                 set(contract['$defs'][name].get('properties', {})))
                self.assertIn(name + ':', model['yaml'])
                self.assertTrue(model['description'])

    def test_references_containment_and_inherited_fields_are_distinct(self):
        fields = {f['name']: f for f in self.index['models']['IssueMention']['fields']}
        self.assertEqual(fields['person_id']['references'], ['SharedPerson.id'])
        self.assertEqual(fields['addresses']['relationship'], 'contains')
        self.assertEqual(fields['printed_name']['relationship'], 'value')
        inherited = {f['name']: f for f in self.index['models']['SiteCitation']['fields']}
        self.assertEqual(inherited['source_id']['references'], ['Source.id'])
        self.assertTrue(self.index['types']['Confidence']['values'])

    def test_broken_and_duplicate_targets_fail(self):
        for refs in (['Missing.id'], ['SharedPerson.missing'], ['SharedPerson.id'] * 2):
            models = copy.deepcopy(self.index['models'])
            models['IssueMention']['fields'][0]['references'] = refs
            with self.subTest(refs=refs), self.assertRaises(ValueError):
                learning.validate_references(models)


if __name__ == '__main__':
    unittest.main()
