"""RiC-O mappings read their axioms from the owner's pin, never a copied rule table.

Behavior and local/RiC-CM restrictions run in both runtimes in `contract`.
This file stays outside zod/: the site's symlink has only bun and zod/.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RICO = 'https://www.ica.org/standards/RiC/ontology#'


class LifeEventMeaning(unittest.TestCase):
    def setUp(self):
        self.axioms = {a['iri']: a for a in json.loads(
            (ROOT / 'standards/rico-1.1-axioms.json').read_text())['axioms']}
        self.vocab = json.loads((ROOT / 'vocabulary/site-content.json').read_text())
        self.released = json.loads((ROOT / 'vocabulary/sourced-entities.json').read_text())
        self.bindings = {b['id']: b['mapping'] for b in self.vocab['bindings']}
        self.profile = (ROOT / 'vocabulary/profile.ttl').read_text()
        self.ehri = {t['iri']: t for t in json.loads(
            (ROOT / 'standards/ehri-0.2.0.json').read_text())['terms']}

    def ancestors(self, iri):
        return {iri} | {ancestor for parent in self.axioms.get(iri, {}).get('superclasses', [])
                        for ancestor in self.ancestors(parent)}

    def test_rico_5_family_and_person_are_disjoint_through_the_pinned_hierarchy(self):
        family = self.bindings['family']['ehri']
        person = self.bindings['person']['ehri']
        namespace = 'http://lod.ehri-project-test.eu/ontology#'
        families = {x for p in self.ehri[namespace + family]['superclasses'] for x in self.ancestors(p)}
        people = {x for p in self.ehri[namespace + person]['superclasses'] for x in self.ancestors(p)}
        self.assertTrue(any(people.intersection(self.axioms.get(f, {}).get('disjoint_with', []))
                            for f in families))

    def test_local_8_parts_narrow_the_actual_rico_participant_properties(self):
        parts = self.released['groups']['event_parts']
        self.assertEqual({p['id']: p['rico_parent'] for p in parts}, {
            'baby': 'rico:affectsOrAffected', 'parent': 'rico:hasOrHadParticipant',
            **{p: 'rico:affectsOrAffected' for p in ['bride', 'groom', 'boy', 'deceased', 'remembered']}})
        for part in parts:
            with self.subTest(part=part['id']):
                parent = RICO + part['rico_parent'].removeprefix('rico:')
                axiom = self.axioms[parent]
                self.assertTrue(parent == RICO + 'hasOrHadParticipant' or
                                RICO + 'hasOrHadParticipant' in axiom['superproperties'])
                declaration = re.search(re.escape(part['mapping']['local']) + r' a .*?\.(?:\n|$)', self.profile)[0]
                for domain in axiom['domain']:
                    self.assertIn('rdfs:domain rico:' + domain.removeprefix(RICO), declaration)
                self.assertIn('rdfs:subPropertyOf ' + part['rico_parent'], declaration)
                self.assertIn('rdfs:range ' + part['range_class'], declaration)
                self.assertTrue(set(axiom['range']) <= self.ancestors(
                    RICO + part['range_class'].removeprefix('rico:')))
                self.assertIn(json.dumps(part['mapping']['reason']), declaration)

    def test_rico_7_released_memorial_is_an_instance_of_the_actual_event_type_range(self):
        axiom = self.axioms[RICO + self.bindings['event_type']['rico']]
        kind = next(e for e in self.released['groups']['event_types'] if e['id'] == 'memorial')
        self.assertIn(RICO + kind['concept_class'].removeprefix('rico:'), axiom['range'])
        self.assertIn(RICO + self.bindings['life_event']['rico'], axiom['domain'])

    def test_rico_10_date_fields_have_the_pinned_date_domain(self):
        date_class = RICO + self.bindings['event_date']['rico']
        for field in ['event_date_printed', 'event_date_normalized', 'event_date_qualifier']:
            axiom = self.axioms[RICO + self.bindings[field]['rico']]
            self.assertIn(date_class, axiom['domain'])
            self.assertTrue(axiom['range'])

    def test_rico_evidence_is_the_inverse_of_evidences_with_record_resource_range(self):
        evidence = RICO + self.bindings['fact_source']['rico']
        self.assertIn(evidence, self.axioms[RICO + 'evidences']['inverse_of'])
        axiom = self.axioms[evidence]
        self.assertIn(RICO + self.bindings['relation']['rico'], axiom['domain'])
        namespace = 'http://lod.ehri-project-test.eu/ontology#'
        self.assertTrue(set(axiom['range']) <= set(self.ehri[
            namespace + self.bindings['source']['ehri']]['superclasses']))

    def test_rico_parent_relation_uses_the_actual_source_to_target_chain(self):
        vocab = json.loads((ROOT / 'vocabulary/sourced-entities.json').read_text())
        parent = next(v for v in vocab['groups']['relationship_types'] if v['id'] == 'parent_of')['mapping']
        prop = self.axioms[RICO + parent['rico']]
        relation = self.axioms[RICO + parent['via']]
        chain = next(c for c in prop['property_chains'] if set(c) & set(relation['rolified_by']))
        source = self.axioms[chain[0]]['inverse_of']
        source_end = next(c for c in relation['cardinalities'] if c['on_property'] in source)
        target_end = next(c for c in relation['cardinalities'] if c['on_property'] == chain[-1])
        self.assertEqual(source_end['on_class'], prop['domain'])
        self.assertEqual(target_end['on_class'], prop['range'])

    def test_rico_grandparent_descent_and_inverses_use_the_pinned_chains(self):
        relationships = {e['id']: e for e in self.released['groups']['relationship_types']}
        terms = {t['iri']: t['kind'] for t in json.loads(
            (ROOT / 'standards/rico-1.1.json').read_text())['terms']}
        for id in ['grandparent_of', 'great_grandparent_of']:
            with self.subTest(id=id):
                forward = relationships[id]
                inverse = relationships[forward['inverse']]
                self.assertEqual(forward['mapping'], {'rico': 'hasDescendant', 'via': 'DescendanceRelation'})
                self.assertEqual(inverse['mapping']['via'], forward['mapping']['via'])
                prop = self.axioms[RICO + forward['mapping']['rico']]
                inverse_prop = self.axioms[RICO + inverse['mapping']['rico']]
                self.assertIn(RICO + inverse['mapping']['rico'], prop['inverse_of'])
                self.assertIn(RICO + forward['mapping']['rico'], inverse_prop['inverse_of'])
                relation = self.axioms[RICO + forward['mapping']['via']]
                self.assertEqual(terms[relation['iri']], 'class')
                for direction, start, end in [(prop, 'thingIsSourceOfRelation', 'relationHasTarget'),
                                              (inverse_prop, 'thingIsTargetOfRelation', 'relationHasSource')]:
                    self.assertEqual(terms[direction['iri']], 'object property')
                    chain = next(c for c in direction['property_chains'] if set(c) & set(relation['rolified_by']))
                    self.assertEqual(chain[0], RICO + start)
                    self.assertEqual(chain[-1], RICO + end)
                    self.assertEqual(direction['domain'], [RICO + 'Person'])
                    self.assertEqual(direction['range'], [RICO + 'Person'])


if __name__ == '__main__':
    unittest.main()
