"""A content item's summary maps to rico:scopeAndContent, read from the owner's pins.

RiC-O 1.1 gives scopeAndContent a RecordResource domain and a literal range; the content item's
class, ehri:RecordResource, is a RiC-O RecordResource; and the pinned EHRI holdings profile
carries the property as a language-tagged string. The LinkML is read as text: this step runs
without a YAML library.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RICO = 'https://www.ica.org/standards/RiC/ontology#'
EHRI = 'http://lod.ehri-project-test.eu/ontology#'
HOLDINGS = ROOT / 'standards/ehri-holdings-1.1-1c2325f9'


def block(text, name, indent):
    """The lines of the YAML key `name` at `indent` spaces, up to the next key at that indent."""
    match = re.search(rf'(?m)^{" " * indent}{name}:\n((?:{" " * indent} .*\n|\n)*)', text)
    assert match, name
    return match.group(1)


class SummaryMeaning(unittest.TestCase):
    def setUp(self):
        self.axioms = {a['iri']: a for a in json.loads(
            (ROOT / 'standards/rico-1.1-axioms.json').read_text(encoding='utf-8'))['axioms']}
        self.ehri = {t['iri']: t for t in json.loads(
            (ROOT / 'standards/ehri-0.2.0.json').read_text(encoding='utf-8'))['terms']}
        self.schema = (ROOT / 'linkml/schema/content_items.yaml').read_text(encoding='utf-8')

    def test_the_summary_slot_is_scope_and_content_of_a_record_resource(self):
        item = block(self.schema, 'ContentItem', 2)
        self.assertIn('class_uri: ehri:RecordResource', item)
        self.assertIn('slot_uri: rico:scopeAndContent', block(item, 'summary', 6))
        axiom = self.axioms[RICO + 'scopeAndContent']
        self.assertEqual(axiom['domain'], [RICO + 'RecordResource'])
        self.assertEqual(axiom['range'], ['http://www.w3.org/2000/01/rdf-schema#Literal'])
        self.assertIn(RICO + 'RecordResource', self.ehri[EHRI + 'RecordResource']['superclasses'])

    def test_the_holdings_profile_carries_it_as_a_language_tagged_string(self):
        self.assertRegex((HOLDINGS / 'holdings.shex').read_text(encoding='utf-8'),
                         r'rico:scopeAndContent rdf:langString \*')
        self.assertRegex((HOLDINGS / 'holdings.shacl.ttl').read_text(encoding='utf-8'),
                         r'sh:datatype\s+rdf:langString\s*;\s*sh:path\s+rico:scopeAndContent')
        summary = block(self.schema, 'Summary', 2)
        self.assertRegex(block(summary, 'language', 6), r'equals_string: en\n')


if __name__ == '__main__':
    unittest.main()
