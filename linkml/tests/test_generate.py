"""The generation command (linkml/generate.py) on a small module of its own (fixtures/generate/).

The real definition is checked by `generate.py --check` in bin/verify; here a copy of the fixture
module is made, checked, and then changed by one byte, by a missing file and by an extra file,
each of which --check must name.
"""

import contextlib
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from support import FIXTURES, ROOT, load

generate = load('generate')


class Generate(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name) / 'linkml'
        shutil.copytree(FIXTURES / 'generate', self.root)
        generate.regenerate(self.root)
        self.made = self.root / 'generated'

    def test_it_makes_the_json_schema_of_the_top_class_and_the_docs(self):
        schema = json.loads((self.made / 'json-schema' / 'boxes.schema.json').read_text(encoding='utf-8'))
        self.assertEqual(schema['required'], ['boxes'])
        self.assertIs(schema['additionalProperties'], False)
        self.assertIs(schema['$defs']['Box']['additionalProperties'], False)
        self.assertTrue((self.made / 'docs' / 'boxes' / 'index.md').is_file())
        self.assertTrue((self.made / 'docs' / 'boxes' / 'Box.md').is_file())

    def test_what_it_makes_is_the_same_again_and_holds_no_machine_detail(self):
        self.assertEqual(generate.differences(self.root), [])
        for path in self.made.rglob('*'):
            if path.is_file():
                data = path.read_bytes()
                with self.subTest(file=path.name):
                    self.assertNotIn(b'\r', data)
                    self.assertNotIn(str(self.root.parent).encode(), data)
                    self.assertNotIn(str(ROOT).encode(), data)
                    self.assertTrue(data.endswith(b'\n'))

    def test_check_names_a_file_changed_by_one_byte(self):
        target = self.made / 'json-schema' / 'boxes.schema.json'
        data = bytearray(target.read_bytes())
        data[data.index(b'"boxes"')] = ord(' ')  # one byte
        target.write_bytes(bytes(data))
        self.assertEqual(generate.differences(self.root),
                         ['linkml/generated/json-schema/boxes.schema.json: differs from what generate.py makes now'])

    def test_check_names_a_missing_file_and_an_extra_one(self):
        (self.made / 'docs' / 'boxes' / 'Box.md').unlink()
        (self.made / 'docs' / 'boxes' / 'Stale.md').write_text('# Stale\n', encoding='utf-8')
        self.assertEqual(generate.differences(self.root), [
            'linkml/generated/docs/boxes/Box.md: missing; run linkml/generate.py',
            'linkml/generated/docs/boxes/Stale.md: extra; generate.py makes no such file',
        ])

    def test_python_check_refuses_changed_missing_and_extra_outputs(self):
        profile = {'models': {
            'Box': {'config': {'extra': 'forbid'}, 'order': ['label']},
            'Boxes': {'config': {'extra': 'forbid'}, 'order': ['boxes']},
        }, 'adjustments': []}
        (self.root / 'python-compatibility.json').write_text(json.dumps(profile))
        generate.regenerate(self.root)
        target = self.root.parent / 'pydantic/generated'
        self.assertEqual(generate.differences(self.root), [])
        original = (target / 'models.py').read_text()
        for changed in ('# changed\n' + original, None):
            with self.subTest(changed=changed is not None):
                if changed is None:
                    (target / 'models.py').unlink()
                else:
                    (target / 'models.py').write_text(changed)
                self.assertEqual(generate.differences(self.root),
                                 ['pydantic/generated/models.py: missing, extra or differs from generation'])
                (target / 'models.py').write_text(original)
        (target / 'stale.py').write_text('# stale\n')
        self.assertEqual(generate.differences(self.root),
                         ['pydantic/generated/stale.py: missing, extra or differs from generation'])

    def test_regenerating_removes_a_stale_file_and_restores_a_changed_one(self):
        (self.made / 'docs' / 'boxes' / 'Stale.md').write_text('# Stale\n', encoding='utf-8')
        (self.made / 'docs' / 'boxes' / 'index.md').write_text('changed\n', encoding='utf-8')
        generate.regenerate(self.root)
        self.assertEqual(generate.differences(self.root), [])
        self.assertFalse((self.made / 'docs' / 'boxes' / 'Stale.md').exists())

    def test_main_check_fails_on_drift_and_passes_on_the_committed_definition(self):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(generate.main(['--check']), 0)
            original, generate.LINKML = generate.LINKML, self.root
            try:
                (self.made / 'docs' / 'boxes' / 'Box.md').unlink()
                self.assertEqual(generate.main(['--check']), 1)
            finally:
                generate.LINKML = original

    def test_a_name_used_twice_in_the_manifest_is_refused(self):
        manifest = json.loads((self.root / 'modules.json').read_text(encoding='utf-8'))
        manifest['modules'].append(dict(manifest['modules'][0]))
        (self.root / 'modules.json').write_text(json.dumps(manifest), encoding='utf-8')
        with self.assertRaises(SystemExit):
            generate.modules(self.root)

    def test_planned_requirements_change_docs_but_never_the_document_schema(self):
        target = self.made / 'json-schema' / 'boxes.schema.json'
        before = target.read_bytes()
        planned = {'items': [{'id': 'future', 'title': 'Future field',
                              'summary': 'A phantom field planned for later.',
                              'source': {'root': 'steps', 'file': 'plan.md', 'line': 1,
                                         'quote': 'A future requirement'}}]}
        (self.root / 'planned.yaml').write_text(json.dumps(planned), encoding='utf-8')
        generate.regenerate(self.root)
        self.assertEqual(target.read_bytes(), before)
        dictionary = (self.made / 'docs/data-dictionary.md').read_text(encoding='utf-8')
        self.assertIn('A phantom field planned for later.', dictionary)
        self.assertNotIn('phantom', target.read_text(encoding='utf-8'))

    def test_every_owned_class_is_indexed_even_when_it_is_not_a_document_root(self):
        index = json.loads((self.made / 'contract.json').read_text(encoding='utf-8'))
        self.assertEqual(set(index['classes']), {'Box', 'Boxes'})
        self.assertTrue(set(index['classes']) <= index['$defs'].keys())


if __name__ == '__main__':
    unittest.main()
