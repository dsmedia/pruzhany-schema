"""Derive runtime policy and exact-English bindings from the LinkML definition."""

from linkml_runtime.utils.schemaview import SchemaView


def policy(linkml_dir):
    view = SchemaView(str(linkml_dir / 'schema' / 'shared_record.yaml'))
    rules = [r for r in view.get_class('Citation').rules
             if r.title == 'require_non_english_quote_english']
    if len(rules) != 1 or rules[0].deactivated is None:
        raise ValueError('Citation needs exactly one explicit quote-English activation switch')
    fields = {}
    # All owned modules, including standalone older Mention.
    import json
    for entry in json.loads((linkml_dir / 'modules.json').read_text())['modules']:
        if 'external_contract' in entry:
            continue
        schema = SchemaView(str(linkml_dir / entry['schema']))
        for name in schema.all_classes(imports=False):
            pairs = {}
            for slot in schema.class_induced_slots(name):
                annotation = (slot.annotations.get('english_of') if isinstance(slot.annotations, dict)
                              else getattr(slot.annotations, 'english_of', None))
                if annotation:
                    if 'Translation' not in schema.class_ancestors(slot.range) or str(annotation.value) not in schema.class_slots(name):
                        raise ValueError(f'{name}.{slot.name}: invalid exact-English binding')
                    pairs[str(slot.name)] = str(annotation.value)
            if pairs:
                fields[str(name)] = pairs
    return not rules[0].deactivated, dict(sorted(fields.items()))


def outputs(linkml_dir):
    import json
    active, fields = policy(linkml_dir)
    python = ('"""Generated from LinkML by linkml/generate.py. Do not edit."""\n'
              f'REQUIRE_NON_ENGLISH_QUOTE_ENGLISH = {active!r}\n'
              f'ENGLISH_FIELDS = {fields!r}\n')
    ts = ('// Generated from LinkML by linkml/generate.py. Do not edit.\n'
          f'export const REQUIRE_NON_ENGLISH_QUOTE_ENGLISH = {str(active).lower()};\n'
          'export const ENGLISH_FIELDS = ' + json.dumps(fields, indent='\t')
          .replace('"', "'") + ' as const;\n')
    import re
    ts = re.sub(r"'(\w+)':", r'\1:', ts)
    # Use the same trailing-comma style as the existing Zod backend.
    lines = ts.splitlines()
    for i in range(len(lines)-1):
        if lines[i].startswith('\t') and not lines[i].endswith(('{', ',')):
            lines[i] += ','
    return python, '\n'.join(lines) + '\n'
