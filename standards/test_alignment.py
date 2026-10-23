"""Tiny isolated alignment fixtures; no RDF library required."""
import json
import tempfile
import unittest
from pathlib import Path
from check_alignment import check, check_axioms, RICO, EHRI

STANDARDS = Path(__file__).resolve().parent


class AlignmentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'standards').mkdir()
        self.pilot = self.root / 'pilots/test'
        self.pilot.mkdir(parents=True)
        for name, terms in [('rico-1.0.2.json', [RICO+'Person', RICO+'OldTerm']), ('rico-1.1.json', [RICO+'Person', RICO+'NewTerm']), ('ehri-0.1.1.json', [EHRI+'Person', EHRI+'OldTerm']), ('ehri-0.2.0.json', [EHRI+'Person'])]:
            (self.root / 'standards' / name).write_text(json.dumps({'terms': [{'iri': t} for t in terms]}))
        self.axioms({'axioms': [{'iri': RICO + 'Person', 'superclasses': [RICO + 'NewTerm']}]})

    def axioms(self, value):
        (self.root / 'standards' / 'rico-1.1-axioms.json').write_text(json.dumps(value))

    def source(self, text):
        (self.pilot / 'profile.ttl').write_text(text)
        return check(self.root)

    def test_known_passes(self):
        self.assertEqual(self.source('x a rico:Person, ehri:Person .'), [])

    def test_unknown_rico_fails(self):
        self.assertTrue(self.source('x a rico:Typo .'))

    def test_term_new_in_11_passes(self):
        # EHRI 0.2.0 imports RiC-O 1.1, so 1.1 is the base (the owner's word of 2026-10-22).
        self.assertEqual(self.source('x a rico:NewTerm .'), [])

    def test_term_gone_from_11_fails(self):
        self.assertTrue(self.source('x a rico:OldTerm .'))

    def test_term_gone_from_ehri_020_fails(self):
        self.assertTrue(self.source('x a ehri:OldTerm .'))

    def test_unknown_ehri_fails(self):
        self.assertTrue(self.source('x a ehri:Typo .'))

    def test_local_requires_reason(self):
        (self.pilot / 'vocabulary.json').write_text(json.dumps({'types': {'custom': {'rico': None, 'local': 'pc:custom'}}}))
        self.assertTrue(any('reason' in e for e in self.source('pc:custom a rdf:Property .')))

    def test_explained_local_passes(self):
        (self.pilot / 'vocabulary.json').write_text(json.dumps({'types': {'custom': {'local': 'pc:custom', 'reason': 'Keeps review state.'}}}))
        self.assertEqual(self.source('pc:custom a rdf:Property .'), [])

    def test_emitted_dictionary_iri_checked(self):
        (self.pilot / 'build.py').write_text('predicate = RICO + {"birth": "Typo"}.get(kind, "")')
        self.assertTrue(check(self.root))

    def test_separate_vocabulary_profile(self):
        folder = self.root / 'vocabulary'
        folder.mkdir()
        (folder / 'profile.ttl').write_text('pc:released a rdf:Property .')
        (folder / 'proposed.json').write_text(json.dumps({'groups': [
            {'id': 'custom', 'mapping': {'local': 'pc:custom', 'reason': 'Keeps review state.'}}
        ]}))
        profile = folder / 'proposed.profile.ttl'
        profile.write_text('pc:custom a rdf:Property .')
        self.assertEqual(check(self.root), [])
        profile.write_text('pc:custom a rico:Typo .')
        self.assertTrue(any('proposed.profile.ttl' in e and 'Typo' in e for e in check(self.root)))
        profile.write_text('pc:different a rdf:Property .')
        self.assertTrue(any('local mapping' in e for e in check(self.root)))

    def test_axioms_from_another_file_fail(self):
        self.axioms({'sha256': 'another file', 'axioms': []})
        self.assertTrue(any('sha256 differs' in e for e in check(self.root)))

    def test_axiom_naming_an_unpinned_term_fails(self):
        self.axioms({'axioms': [{'iri': RICO + 'Person', 'superclasses': [RICO + 'Typo']}]})
        self.assertTrue(any('Typo is not a pinned term' in e for e in check(self.root)))


class PinnedAxiomsTests(unittest.TestCase):
    """The rules the vetting of 2026-10-23 cites, read from the pinned list itself."""

    def setUp(self):
        data = json.loads((STANDARDS / 'rico-1.1-axioms.json').read_text(encoding='utf-8'))
        self.of = {a['iri'].removeprefix(RICO): a for a in data['axioms']}

    def rico(self, *names):
        return [RICO + n for n in names]

    def test_pinned_from_the_terms_file(self):
        self.assertEqual(check_axioms(STANDARDS), [])

    def test_child_relation_runs_from_parent_to_child(self):
        self.assertEqual(self.of['hasChild']['inverse_of'], self.rico('isChildOf'))
        self.assertIn(self.rico('thingIsSourceOfRelation', 'childRelation_role', 'relationHasTarget'),
                      self.of['hasChild']['property_chains'])

    def test_spouse_sibling_and_family_ties_are_symmetric(self):
        for name in ('hasOrHadSpouse', 'hasSibling', 'hasFamilyAssociationWith'):
            self.assertIn('symmetric', self.of[name]['characteristics'], name)

    def test_affected_is_a_kind_of_participant(self):
        self.assertEqual(self.of['affectsOrAffected']['superproperties'], self.rico('hasOrHadParticipant'))
        self.assertEqual(self.of['hasOrHadParticipant']['domain'], self.rico('Event'))

    def test_a_group_is_never_a_person(self):
        self.assertIn(RICO + 'Person', self.of['Group']['disjoint_with'])
        self.assertIn(RICO + 'Group', self.of['Family']['superclasses'])

    def test_evidence_is_a_record_not_the_relation_s_source_end(self):
        self.assertEqual(self.of['isEvidencedBy']['range'], self.rico('RecordResource'))
        self.assertEqual(self.of['relationHasSource']['inverse_of'], self.rico('thingIsSourceOfRelation'))


if __name__ == '__main__':
    unittest.main()
