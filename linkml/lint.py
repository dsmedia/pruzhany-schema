"""The house lint of the LinkML definition: refuse what LinkML 1.12.1 reads without complaint
but then mishandles, or what YAML reads differently from what was written.

    python -I linkml/lint.py [FILE ...]

Run it in the linkml step's locked environment (bin/verify linkml). With no file named it
reads every linkml/schema/**/*.yaml and linkml/known-looser.yaml. Each finding names the
file, the line, the rule and what to write instead; the exit status is 1 when there is one.

The rules, each with a planted failing file in linkml/tests/fixtures/lint/:

  exact-cardinality   gen-json-schema drops exact_cardinality (plan section 3, item 1).
  bound-on-a-list     gen-pydantic puts minimum_value or maximum_value of a multivalued
                      slot on the whole list, so a real box is refused (item 2).
  unique-keys         neither gen-json-schema nor linkml-validate enforces unique_keys
                      (item 3); a rule that compares records lives in pruzhany-steps
                      record/rules.yaml.
  yaml-boolean        YAML 1.1, which PyYAML and so LinkML read, turns a bare on, off,
                      yes or no into a boolean, and a key true or false into one.
  flow-prose          a comma inside a flow-style {...} or [...] splits prose silently.

Only the first three need the file to be a LinkML schema; known-looser.yaml is held to
the last two. A file that YAML or LinkML cannot read at all is reported as unreadable.
"""

import sys
from dataclasses import dataclass
from pathlib import Path

import yaml
from linkml_runtime.utils.schemaview import SchemaView

LINKML = Path(__file__).resolve().parent
ROOT = LINKML.parent

# YAML 1.1 booleans as PyYAML resolves them, compared without regard to case.
BOOLEAN_WORDS = {'on', 'off', 'yes', 'no'}
BOOLEAN_KEYS = BOOLEAN_WORDS | {'true', 'false'}
PROSE = {'description', 'comments', 'notes', 'title'}
PROSE_LISTS = {'comments', 'notes'}

MESSAGES = {
    'exact-cardinality': (
        'exact_cardinality is dropped by gen-json-schema; write minimum_cardinality and '
        'maximum_cardinality with the same number'),
    'bound-on-a-list': (
        'gen-pydantic puts this bound on the whole list; bound the items through a type '
        '(types.yaml) and give the slot that type as its range'),
    'unique-keys': (
        'unique_keys is enforced by neither gen-json-schema nor linkml-validate; write the '
        'rule in pruzhany-steps record/rules.yaml'),
    'yaml-boolean': 'YAML 1.1 reads this bare word as a boolean; quote it',
    'flow-prose': 'a comma in flow style splits prose silently; write it in block style',
    'unreadable': 'the file cannot be read',
}


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    rule: str
    detail: str = ''

    def __str__(self):
        try:
            shown = self.path.resolve().relative_to(ROOT).as_posix()
        except ValueError:
            shown = str(self.path)
        detail = f' ({self.detail})' if self.detail else ''
        return f'{shown}:{self.line}: {self.rule}: {MESSAGES[self.rule]}{detail}'


def default_files():
    return [*sorted((LINKML / 'schema').rglob('*.yaml')), LINKML / 'known-looser.yaml']


def is_boolean_word(node, words):
    """A plain (unquoted) scalar that YAML 1.1 reads as a boolean."""
    return (isinstance(node, yaml.ScalarNode) and node.style is None
            and node.value.lower() in words)


def yaml_findings(path, node):
    """Findings that need only the YAML: booleans, flow-style prose and the refused keys."""
    found = []

    def walk(node):
        if isinstance(node, yaml.MappingNode):
            for key, value in node.value:
                line = key.start_mark.line + 1
                if is_boolean_word(key, BOOLEAN_KEYS):
                    found.append(Finding(path, line, 'yaml-boolean', f'key {key.value!r}'))
                name = key.value if isinstance(key, yaml.ScalarNode) else None
                if name == 'exact_cardinality':
                    found.append(Finding(path, line, 'exact-cardinality'))
                if name == 'unique_keys':
                    found.append(Finding(path, line, 'unique-keys'))
                if name in PROSE and node.flow_style:
                    found.append(Finding(path, line, 'flow-prose', f'{name} inside {{...}}'))
                elif (name in PROSE_LISTS and isinstance(value, yaml.SequenceNode)
                      and value.flow_style):
                    found.append(Finding(path, line, 'flow-prose', f'{name} as [...]'))
                walk(value)
        elif isinstance(node, yaml.SequenceNode):
            for item in node.value:
                walk(item)
        elif is_boolean_word(node, BOOLEAN_WORDS):
            found.append(Finding(path, node.start_mark.line + 1, 'yaml-boolean',
                                 f'value {node.value!r}'))

    walk(node)
    return found


def key_lines(node, prefix=()):
    """Map every chain of mapping keys in the file to the line its last key is on."""
    lines = {}
    if isinstance(node, yaml.MappingNode):
        for key, value in node.value:
            if isinstance(key, yaml.ScalarNode):
                chain = (*prefix, key.value)
                lines[chain] = key.start_mark.line + 1
                lines.update(key_lines(value, chain))
    return lines


def bound_findings(path, node):
    """minimum_value or maximum_value on a multivalued slot, after inheritance and slot_usage.

    SchemaView works out each class's slots as LinkML does, so a bound added in slot_usage to
    a slot made multivalued elsewhere is found too. A bound on a type stays on the type (the
    JSON Schema puts it on each item), so a multivalued slot whose range is such a type passes.
    """
    lines = key_lines(node)
    view = SchemaView(str(path))
    found, seen = [], set()

    def report(name, places, detail):
        line = next((lines[p] for p in places if p in lines), 1)
        if (line, name) not in seen:
            seen.add((line, name))
            found.append(Finding(path, line, 'bound-on-a-list', detail))

    # SchemaView counts a class's attributes among the schema's slots; only a slot declared
    # under the top-level slots: is reported here, an attribute with its class below.
    for name, slot in view.all_slots(imports=False).items():
        if ('slots', name) in lines and slot.multivalued and (
                slot.minimum_value is not None or slot.maximum_value is not None):
            report(name, [('slots', name)], f'slot {name}')
    for cls in view.all_classes(imports=False):
        for slot in view.class_induced_slots(cls):
            if slot.multivalued and (slot.minimum_value is not None
                                     or slot.maximum_value is not None):
                report(slot.name, [('classes', cls, 'slot_usage', slot.name),
                                   ('classes', cls, 'attributes', slot.name),
                                   ('slots', slot.name), ('classes', cls)],
                       f'{cls}.{slot.name}')
    return found


def lint(path):
    """Return the findings for one file, sorted by line.

    A file is held to the LinkML rules when it has the two top-level keys every LinkML schema
    has, id and name (known-looser.yaml has neither), and YAML has read it as written.
    """
    path = Path(path)
    try:
        node = yaml.compose(path.read_text(encoding='utf-8'), Loader=yaml.SafeLoader)
    except yaml.YAMLError as error:
        mark = getattr(error, 'problem_mark', None)
        return [Finding(path, mark.line + 1 if mark else 1, 'unreadable', str(error).splitlines()[0])]
    if node is None:
        return []
    found = yaml_findings(path, node)
    top = key_lines(node)
    # Where YAML reads something other than what was written (a boolean, prose split at a
    # comma), LinkML would only report the consequence; the LinkML rules wait for the fix.
    misread = any(f.rule in ('yaml-boolean', 'flow-prose') for f in found)
    if ('id',) in top and ('name',) in top and not misread:
        try:
            found += bound_findings(path, node)
        except Exception as error:  # LinkML refuses the file; say so rather than stop the lint.
            found.append(Finding(path, 1, 'unreadable', f'LinkML: {str(error).splitlines()[0]}'))
    return sorted(found, key=lambda f: (f.line, f.rule))


def main(argv):
    files = [Path(a) for a in argv] or default_files()
    findings = [finding for path in files for finding in lint(path)]
    for finding in findings:
        print(finding)
    if findings:
        print(f'house lint: {len(findings)} finding(s) in {len(files)} file(s)', file=sys.stderr)
        return 1
    print(f'house lint: {len(files)} file(s), no finding')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
