"""Media mappings use the pinned domains and ranges, not remembered ontology terms."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RICO = 'https://www.ica.org/standards/RiC/ontology#'


class MediaMeaning(unittest.TestCase):
    def setUp(self):
        self.axioms = {a['iri']: a for a in json.loads(
            (ROOT / 'standards/rico-1.1-axioms.json').read_text())['axioms']}
        self.bindings = {b['id']: b for b in json.loads(
            (ROOT / 'vocabulary/media.json').read_text())['bindings']}

    def axiom(self, binding):
        return self.axioms[RICO + self.bindings[binding]['mapping']['rico']]

    def test_instantiation_points_to_record_and_record_to_subject(self):
        medium = RICO + self.bindings['medium']['mapping']['rico']
        source = self.axiom('media_source')
        self.assertEqual(source['domain'], [medium])
        self.assertEqual(source['range'], [RICO + 'RecordResource'])
        self.assertIn(RICO + 'hasOrHadInstantiation', source['inverse_of'])
        subjects = self.axiom('source_subjects')
        self.assertEqual(subjects['domain'], source['range'])
        self.assertEqual(subjects['range'], [RICO + 'Thing'])

    def test_terms_and_dimensions_belong_to_instantiations(self):
        medium = RICO + self.bindings['medium']['mapping']['rico']
        self.assertIn(medium, self.axiom('media_conditions_of_use')['domain'])
        for field in ['media_width', 'media_height']:
            self.assertEqual(self.axiom(field)['domain'], [RICO + 'Thing'])
            self.assertIn(RICO + 'Thing', self.axioms[medium]['superclasses'])

    def test_presentation_kind_does_not_claim_a_record_content_type(self):
        mapping = self.bindings['media_kind']['mapping']
        self.assertEqual(mapping['local'], 'pc:media_kind')
        self.assertIn('has not been read', mapping['reason'])
        self.assertNotIn(RICO + 'Instantiation', self.axioms[RICO + 'hasContentOfType']['domain'])
