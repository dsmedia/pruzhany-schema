"""The shared types (linkml/schema/types.yaml) against the shapes they were copied from."""

import json
import unittest

from linkml_runtime.utils.schemaview import SchemaView

from support import LINKML, ROOT, walk, zod_exports

TYPES = SchemaView(str(LINKML / 'schema' / 'types.yaml'))
OWN = TYPES.all_types(imports=False)


class SharedTypes(unittest.TestCase):
    def test_every_pattern_appears_in_the_exports_as_written(self):
        patterns = {node['pattern'] for document in zod_exports().values()
                    for _, node in walk(document) if 'pattern' in node}
        for name, kind in OWN.items():
            if kind.pattern is not None:
                with self.subTest(type=name):
                    self.assertIn(kind.pattern, patterns)

    def test_the_language_tag_is_the_pattern_the_twins_read(self):
        table = json.loads((ROOT / 'vocabulary' / 'citation-requirements.json').read_text(encoding='utf-8'))
        self.assertEqual(OWN['LanguageTag'].pattern, table['language_tag_pattern'])

    def test_the_whole_number_bounds_are_the_exports(self):
        maxima = {node['maximum'] for document in zod_exports().values()
                  for _, node in walk(document) if node.get('type') == 'integer' and 'maximum' in node}
        # The sixth export adds the calendar's Hebrew month, bounded to 13.
        self.assertEqual(maxima, {13, 9007199254740991})
        month = zod_exports()['schemas/site/editions.schema.json']['properties']['editions']['items']['properties']['hebrewMonth']
        self.assertEqual((month['minimum'], month['maximum']), (1, 13))
        for name in ('NonNegativeInteger', 'PositiveInteger'):
            with self.subTest(type=name):
                self.assertEqual(OWN[name].maximum_value, 9007199254740991)
        self.assertEqual((OWN['NonNegativeInteger'].minimum_value, OWN['PositiveInteger'].minimum_value), (0, 1))

    def test_every_type_says_what_it_is(self):
        for name, kind in OWN.items():
            with self.subTest(type=name):
                self.assertTrue(kind.description and kind.description.strip())


if __name__ == '__main__':
    unittest.main()
