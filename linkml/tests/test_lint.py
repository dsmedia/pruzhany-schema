"""The house lint (linkml/lint.py) and the configuration of `linkml lint` (linkml/linkml-lint.yaml).

Each rule of the house lint has a planted file in fixtures/lint/ named after it, with the line
it must be refused on marked `# refused here`; fixtures/lint/clean.yaml writes each construct
the way the house lint accepts.
"""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from support import FIXTURES, LINKML, linkml_lint, load

lint = load('lint')


def marked_line(path):
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), start=1):
        if '# refused here' in line:
            return number
    raise AssertionError(f'{path.name} has no line marked "# refused here"')


class HouseLint(unittest.TestCase):
    def test_each_planted_file_is_refused_on_its_marked_line_by_its_rule(self):
        planted = sorted(path for path in (FIXTURES / 'lint').glob('*.yaml') if path.stem != 'clean')
        rules_planted = set()
        for path in planted:
            rule = next(rule for rule in lint.MESSAGES if path.stem.startswith(rule))
            rules_planted.add(rule)
            with self.subTest(fixture=path.name):
                findings = lint.lint(path)
                self.assertEqual([(f.line, f.rule) for f in findings], [(marked_line(path), rule)],
                                 '\n'.join(map(str, findings)))
        # Every rule but `unreadable` has at least one planted file.
        self.assertEqual(rules_planted, set(lint.MESSAGES) - {'unreadable'})

    def test_the_clean_file_is_accepted(self):
        self.assertEqual(lint.lint(FIXTURES / 'lint' / 'clean.yaml'), [])

    def test_a_file_yaml_cannot_read_is_refused(self):
        clean = (FIXTURES / 'lint' / 'clean.yaml').read_text(encoding='utf-8')
        with tempfile.TemporaryDirectory() as scratch:
            path = Path(scratch) / 'unreadable.yaml'
            path.write_text(clean.replace('classes:', 'classes: [', 1), encoding='utf-8')
            self.assertEqual([f.rule for f in lint.lint(path)], ['unreadable'])

    def test_main_reports_and_fails_on_a_planted_file_and_passes_on_the_definition(self):
        with contextlib.redirect_stdout(io.StringIO()) as out, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(lint.main([str(FIXTURES / 'lint' / 'unique-keys.yaml')]), 1)
            self.assertEqual(lint.main([]), 0)
        self.assertIn('unique-keys.yaml:14: unique-keys:', out.getvalue())

    def test_the_definition_and_known_looser_are_what_it_reads_by_default(self):
        names = {path.relative_to(LINKML).as_posix() for path in lint.default_files()}
        self.assertIn('schema/types.yaml', names)
        self.assertIn('known-looser.yaml', names)


class LinkmlLintConfiguration(unittest.TestCase):
    """`linkml lint` runs every recommended rule; canonical_prefixes reads a list without pc."""

    def test_pc_as_the_project_prefix_passes_with_the_configuration_and_not_without(self):
        path = FIXTURES / 'linkml-lint' / 'pc-prefix.yaml'
        self.assertEqual(linkml_lint(path)[0], 0)
        status, output = linkml_lint(path, config=None)
        self.assertNotEqual(status, 0)
        self.assertIn('canonical_prefixes', output)

    def test_a_wrong_namespace_for_a_known_prefix_still_fails(self):
        status, output = linkml_lint(FIXTURES / 'linkml-lint' / 'wrong-skos.yaml')
        self.assertNotEqual(status, 0)
        self.assertIn('canonical_prefixes', output)

    def test_a_class_without_a_description_fails(self):
        status, output = linkml_lint(FIXTURES / 'linkml-lint' / 'no-description.yaml')
        self.assertNotEqual(status, 0)
        self.assertIn('recommended', output)

    def test_the_planted_and_clean_house_lint_files_pass_linkml_lint_where_the_lint_trap_is_silent(self):
        # The traps the house lint refuses are ones `linkml lint` does not see.
        for name in ('clean', 'exact-cardinality', 'bound-on-a-list', 'unique-keys'):
            with self.subTest(fixture=name):
                status, output = linkml_lint(FIXTURES / 'lint' / f'{name}.yaml')
                self.assertEqual(status, 0, output)


if __name__ == '__main__':
    unittest.main()
