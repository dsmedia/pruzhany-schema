"""The vocabulary's LinkML form (linkml/schema/vocabulary.yaml), read as LinkML reads it.

vocabulary/generate.py writes the file on the standard library alone, every value as JSON; its
own tests (vocabulary/test_vocabulary.py) check what it holds and that a hand edit fails
`generate.py --check`. Here PyYAML, which LinkML reads with, must read the committed file back
as exactly what the generator meant, and read back the words YAML 1.1 misreads when bare; and
LinkML's SchemaView must find each value's meaning and `via` annotation.
"""

import importlib.util
import json
import unittest

import yaml
from linkml_runtime.utils.schemaview import SchemaView

from support import LINKML, ROOT, load

spec = importlib.util.spec_from_file_location('vocabulary_generate', ROOT / 'vocabulary' / 'generate.py')
generate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate)

VOCABULARY = ROOT / generate.LINKML_VOCABULARY

# Text that YAML 1.1 reads as something else when it is written bare, or that breaks a line.
TRAPS = ['on', 'Off', 'yes', 'NO', 'y', 'n', 'true', 'null', '~', '', '1.0', '1.3.0', '0x10', '1e3', '0o7',
         '2026-10-28', '12:30', ': x', '- x', '# x', 'a: b, c', '[a, b]', '{a: b}', '&anchor', '*alias',
         '!tag', '%x', '@x', '`x', '|', '>', "it's", '"quoted"', 'back\\slash', 'tab\there',
         'line\nbreak', 'a b', 'a\x85b', 'a\x7fb', ' leading', 'trailing ', 'ייִדיש', 'Pružany',
         '\U0001F600', '﻿bom']


class TheCommittedFile(unittest.TestCase):
    def test_pyyaml_reads_it_as_the_generator_made_it(self):
        loaded = yaml.safe_load(VOCABULARY.read_text(encoding='utf-8'))
        self.assertEqual(loaded, generate.linkml_vocabulary(ROOT))

    def test_it_is_a_module_of_the_manifest_with_no_top_class(self):
        manifest = json.loads((LINKML / 'modules.json').read_text(encoding='utf-8'))
        self.assertIn({'schema': 'schema/vocabulary.yaml', 'name': 'vocabulary', 'top_class': None},
                      manifest['modules'])

    def test_linkml_finds_each_meaning_and_via(self):
        view = SchemaView(str(VOCABULARY))
        namespaces = {prefix: str(view.schema.prefixes[prefix].prefix_reference) for prefix in ('rico', 'ehri', 'pc')}
        self.assertEqual(namespaces, generate.NAMESPACES)
        self.assertEqual(view.schema.default_prefix, 'pc')
        self.assertTrue(view.schema.id.startswith('https://pruzhany.org/ns/'))
        counts = {'rico': 0, 'ehri': 0, 'pc': 0, None: 0}
        vias = 0
        for name, enum in view.all_enums(imports=False).items():
            self.assertTrue(enum.description, name)
            for text, value in enum.permissible_values.items():
                with self.subTest(enum=name, value=text):
                    self.assertTrue(value.description)
                    prefix = value.meaning.split(':')[0] if value.meaning else None
                    counts[prefix] += 1
                    if value.meaning:
                        self.assertEqual(view.expand_curie(value.meaning),
                                         generate.NAMESPACES[prefix] + value.meaning.split(':', 1)[1])
                    if 'via' in value.annotations:
                        vias += 1
                        self.assertEqual(prefix, 'rico')
                        self.assertRegex(value.annotations['via'].value, r'^rico:[A-Za-z]+Relation$')
        # A tally, so a value that loses its meaning or its via shows here as well.
        self.assertEqual(counts, {'rico': 28, 'ehri': 3, 'pc': 160, None: 13})
        self.assertEqual(vias, 23)
        self.assertEqual(set(view.all_enums(imports=False)['ImpressoTypes'].permissible_values),
                         set(json.loads((ROOT / 'vocabulary/site-content.json').read_text(encoding='utf-8'))
                             ['impresso_types']))


class TheWriter(unittest.TestCase):
    def test_each_trap_is_real(self):
        """Control: written bare, most of the traps are read as something other than the text."""
        misread = [word for word in TRAPS if word.isascii() and '\n' not in word and '\x7f' not in word
                   and self.bare(word) != word]
        self.assertGreaterEqual(len(misread), 20, misread)

    @staticmethod
    def bare(word):
        try:
            return yaml.safe_load(f'key: {word}\n')['key']
        except yaml.YAMLError:
            return None

    def test_every_trap_is_read_back_as_written_as_key_and_as_value(self):
        data = {'values': {word: word for word in TRAPS},
                'lists': [TRAPS, [{'nested': TRAPS}], {}, []],
                'others': {'none': None, 'yes': True, 'no': False, 'count': 42}}
        text = generate.to_yaml(data)
        self.assertEqual(yaml.safe_load(text), data)

    def test_what_it_writes_passes_the_house_lint(self):
        self.assertEqual(load('lint').lint(VOCABULARY), [])


if __name__ == '__main__':
    unittest.main()
