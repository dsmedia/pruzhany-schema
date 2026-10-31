"""Identifier meanings use the pinned RiC-O 1.1 shapes, without inferring identity."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
RICO = 'https://www.ica.org/standards/RiC/ontology#'


class IdentifierMeaning(unittest.TestCase):
    def test_identifier_attachment_and_type_have_the_pinned_domains_and_ranges(self):
        axioms = {a['iri']: a for a in json.loads(
            (ROOT / 'standards/rico-1.1-axioms.json').read_text())['axioms']}
        attachment = axioms[RICO + 'hasOrHadIdentifier']
        self.assertEqual(attachment['domain'], [RICO + 'Thing'])
        self.assertEqual(attachment['range'], [RICO + 'Identifier'])
        typing = axioms[RICO + 'hasIdentifierType']
        self.assertEqual(typing['domain'], [RICO + 'Identifier'])
        self.assertEqual(typing['range'], [RICO + 'IdentifierType'])
        self.assertEqual(axioms[RICO + 'IdentifierType']['superclasses'], [RICO + 'Type'])

    def test_old_identifier_is_a_type_value_not_a_person_or_equivalence(self):
        vocabulary = json.loads((ROOT / 'vocabulary/identifiers.json').read_text())
        self.assertEqual([v['id'] for v in vocabulary['identifier_types']], ['old_identifier'])
        term = vocabulary['identifier_types'][0]['mapping']['local']
        profile = (ROOT / 'vocabulary/identifiers.profile.ttl').read_text()
        self.assertIn(term + ' a rico:IdentifierType, skos:Concept', profile)
        self.assertNotIn('sameAs', profile)


if __name__ == '__main__':
    unittest.main()
