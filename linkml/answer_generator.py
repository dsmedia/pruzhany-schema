"""Emit the bounded answer contracts in the released Pydantic JSON layout.

Read 30 October 2026: LinkML "Slots" and "Annotations"
(https://linkml.io/linkml/schemas/slots.html and /annotations.html), Pydantic
"JSON Schema" (https://docs.pydantic.dev/latest/concepts/json_schema/), and
Python 3.13 "json" (https://docs.python.org/3.13/library/json.html).
The ordering/layout is witnessed against steps' Pydantic 2.13.5 serialization
schemas, not inferred from today's Pydantic defaults. No Pydantic dependency.

Nullable keys and empty-list defaults are explicit wire annotations: LinkML
does not distinguish required nullable keys from absent keys. This emitter
supports only the reviewed constructs below; every other construct is refused.
"""

import json
import re

import yaml


def only(value, allowed, where):
    unknown = value.keys() - allowed
    if unknown:
        raise ValueError(f'{where}: unsupported construct(s): {sorted(unknown)}')


def flag(annotations, name, where):
    value = annotations.get(name, False)
    if type(value) is not bool:
        raise ValueError(f'{where}: {name} must be a boolean')
    return value


def ordered(value, properties=False):
    """Pydantic sorts schema keys, preserving property, required and enum order."""
    if isinstance(value, dict):
        return {key: ordered(value[key], key == 'properties')
                for key in (value if properties else sorted(value))}
    if isinstance(value, list):
        return [ordered(item) for item in value]
    return value


def load_definition(path):
    """Refuse unsupported semantics before emitting any answer, including unused fields."""
    data = yaml.safe_load(path.read_text(encoding='utf-8'))
    only(data, {'id', 'name', 'title', 'description', 'prefixes', 'default_prefix',
                'default_range', 'imports', 'annotations', 'classes'}, 'answers')
    if data.get('imports') != ['linkml:types'] or data.get('default_range') != 'string':
        raise ValueError('answers: only linkml:types imports and string default range are supported')
    only(data.get('annotations', {}), {'mapping_policy', 'wire_policy'}, 'answers annotations')
    if data.get('annotations', {}).get('wire_policy') != 'pydantic-2.13.5-serialization':
        raise ValueError('answers: unsupported wire_policy')
    classes = data['classes']
    if classes.keys() & {'string', 'integer', 'boolean'}:
        raise ValueError('answers: overlapping class and primitive names')
    for name, cls in classes.items():
        only(cls, {'title', 'description', 'attributes', 'annotations'}, name)
        only(cls.get('annotations', {}), {'asking'}, name + ' annotations')
        if not cls.get('title') or not cls.get('attributes'):
            raise ValueError(f'{name}: title and attributes are required')
        for field, slot in cls['attributes'].items():
            where = f'{name}.{field}'
            only(slot, {'range', 'required', 'multivalued', 'inlined', 'inlined_as_list',
                        'title', 'description', 'annotations', 'equals_string_in'}, where)
            annotations = slot.get('annotations', {})
            only(annotations, {'nullable', 'default_empty_list', 'description_in_wire'}, where + ' annotations')
            for key in ('nullable', 'default_empty_list', 'description_in_wire'):
                flag(annotations, key, where)
            for key in ('required', 'multivalued', 'inlined', 'inlined_as_list'):
                flag(slot, key, where)
            target = slot.get('range', 'string')
            if target not in classes.keys() | {'string', 'integer', 'boolean'}:
                raise ValueError(f'{where}: unsupported range {target}')
            if 'equals_string_in' in slot:
                values = slot['equals_string_in']
                if target != 'string' or not isinstance(values, list) or not values or any(not isinstance(v, str) for v in values) or len(set(values)) != len(values):
                    raise ValueError(f'{where}: equals_string_in needs distinct literal strings with range string')
            is_object = target in classes
            is_list = slot.get('multivalued', False)
            if bool(slot.get('inlined')) != is_object or bool(slot.get('inlined_as_list')) != (is_object and is_list):
                raise ValueError(f'{where}: objects must be inlined, with lists explicitly inlined_as_list')
            if flag(annotations, 'default_empty_list', where) and not is_list:
                raise ValueError(f'{where}: empty-list default requires a list')
    return data


def class_shape(data, name, names):
    cls = data['classes'][name]
    properties, required = {}, []
    for field, slot in cls['attributes'].items():
        target = slot.get('range', 'string')
        if target in data['classes']:
            shape = {'$ref': '#/$defs/' + names[target]}
        else:
            shape = {'type': target}
        if 'equals_string_in' in slot:
            shape['enum'] = slot['equals_string_in']
        if slot.get('multivalued'):
            shape = {'items': shape, 'type': 'array'}
        annotations = slot.get('annotations', {})
        if annotations.get('nullable'):
            shape = {'anyOf': [shape, {'type': 'null'}]}
        for key in ('title', 'description'):
            if key in slot and (key != 'description' or annotations.get('description_in_wire', True)):
                shape[key] = slot[key]
        if annotations.get('default_empty_list'):
            shape['default'] = []
        properties[field] = shape
        if slot.get('required'):
            required.append(field)
    shape = {'additionalProperties': False, 'properties': properties,
             'title': cls['title'], 'type': 'object'}
    if 'description' in cls:
        shape['description'] = cls['description']
    if required:
        shape['required'] = required
    return ordered(shape)


def reachable(data, root):
    found, active = set(), set()

    def visit(name):
        if name in active:
            raise ValueError(f'{name}: recursive answer classes are unsupported')
        if name in found:
            return
        active.add(name)
        for slot in data['classes'][name]['attributes'].values():
            if slot.get('range') in data['classes']:
                visit(slot['range'])
        active.remove(name)
        found.add(name)

    visit(root)
    return found


def build(path):
    """Return exact wire strings and an independent external class inventory."""
    data = load_definition(path)
    answers, covered = {}, set()
    for root, cls in data['classes'].items():
        asking = cls.get('annotations', {}).get('asking')
        if asking is None:
            continue
        if not isinstance(asking, str) or not re.fullmatch('[a-z][a-z0-9_]*', asking) or asking in answers:
            raise ValueError(f'{root}: invalid or duplicate asking {asking}')
        found = reachable(data, root)
        covered.update(found)
        names = {name: data['classes'][name]['title'] for name in found}
        if len(set(names.values())) != len(names):
            raise ValueError(f'{root}: duplicate wire class titles')
        shape = class_shape(data, root, names)
        definitions = {names[name]: class_shape(data, name, names) for name in found - {root}}
        if definitions:
            shape['$defs'] = definitions
        # json.dumps defaults are part of the paid request: ASCII escapes, comma/colon
        # spaces, insertion order, and no trailing newline. Never use write_text here.
        answers[asking] = json.dumps(ordered(shape))
    if not answers or covered != data['classes'].keys():
        raise ValueError('answers: every class must be reachable from an asking')
    names = {name: name for name in data['classes']}
    definitions = {name: class_shape(data, name, names) for name in names}
    return answers, definitions
