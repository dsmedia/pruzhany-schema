"""Adapt the pinned LinkML JSON Schema output to the existing Python API.

LinkML's native Python generator drops inherited type bounds and changes null,
tuple and coercion behavior. This deliberately small backend consumes the same
complete class index as the contract gate. Unsupported field constructs fail.
Runtime rules stay in the hand-written modules; no LinkML dependency is emitted.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path


def canonical(value, definitions):
    """Normalize equivalent schema spellings, without erasing constraints."""
    if isinstance(value, list):
        return [canonical(v, definitions) for v in value]
    if not isinstance(value, dict):
        return value
    value = copy.deepcopy(value)
    if '$ref' in value:
        name = value['$ref'].rsplit('/', 1)[-1]
        target = definitions.get(name, {})
        if target.get('type') == 'string' and 'enum' in target:
            value = {**target, **{k: v for k, v in value.items() if k != '$ref'}}
        elif target.get('type') == 'object' and not target.get('properties') and isinstance(target.get('additionalProperties'), dict):
            value = {**target, **{k: v for k, v in value.items() if k != '$ref'}}
    value = {k: canonical(v, definitions) for k, v in value.items()
             if k not in {'title', 'description', 'default', '$defs', 'linkml_meta'}}
    if 'pattern' in value:
        # Rust regex's $ already means absolute end; LinkML/ECMA needs this guard.
        value['pattern'] = value['pattern'].replace('$(?![\\s\\S])', '$')
    if 'const' in value:
        value['enum'] = [value.pop('const')]
    if 'enum' in value:
        value['enum'] = sorted(value['enum'], key=repr)
    for python, standard in [('ge', 'minimum'), ('le', 'maximum')]:
        if python in value:
            value[standard] = value.pop(python)
    if value.get('type') == 'integer' and 'exclusiveMinimum' in value:
        bound = value['exclusiveMinimum']
        if isinstance(bound, int):
            value['minimum'] = value.pop('exclusiveMinimum') + 1
    if isinstance(value.get('type'), list):
        types = value['type']
        rest = {k: v for k, v in value.items() if k != 'type'}
        branches = [({'type': t} if t == 'null' else {'type': t, **rest}) for t in types
                    if t != 'null' or 'enum' not in rest or None in rest['enum']]
        value = branches[0] if len(branches) == 1 else {'anyOf': branches}
    if 'anyOf' in value:
        value['anyOf'] = sorted(value['anyOf'], key=lambda v: json.dumps(v, sort_keys=True))
    if value.get('propertyNames') == {'type': 'string'}:
        del value['propertyNames']
    if value.get('type') == 'object' and value.get('properties') == {}:
        del value['properties']
    return value


BOUNDS = {'minimum': 'ge', 'maximum': 'le', 'exclusiveMinimum': 'gt',
          'exclusiveMaximum': 'lt', 'minLength': 'min_length', 'maxLength': 'max_length',
          'minItems': 'min_length', 'maxItems': 'max_length', 'pattern': 'pattern'}
FIELD_KEYS = set(BOUNDS) | {'type', '$ref', 'enum', 'anyOf', 'items', 'prefixItems',
                          'additionalProperties', 'format'}


def expression(shape, path='field'):
    """Render only constructs actually supported by this backend."""
    unknown = set(shape) - FIELD_KEYS
    if unknown:
        raise ValueError(f'{path}: unsupported Python field constraints {sorted(unknown)}')
    if 'anyOf' in shape:
        if set(shape) != {'anyOf'}:
            raise ValueError(f'{path}: unsupported union siblings')
        return ' | '.join(expression(s, path) for s in shape['anyOf'])
    if '$ref' in shape:
        if set(shape) != {'$ref'} or not shape['$ref'].startswith('#/$defs/'):
            raise ValueError(f'{path}: unsupported reference siblings or external reference')
        return shape['$ref'].rsplit('/', 1)[-1]
    kind = shape.get('type')
    if 'enum' in shape:
        if not shape['enum']:
            raise ValueError(f'{path}: empty enum')
        result = 'Literal[' + ', '.join(repr(v) for v in shape['enum']) + ']'
    elif kind == 'array':
        if 'prefixItems' in shape:
            if 'items' in shape or shape.get('minItems') != len(shape['prefixItems']) or shape.get('maxItems') != len(shape['prefixItems']):
                raise ValueError(f'{path}: only fixed tuples are supported')
            result = 'tuple[' + ', '.join(expression(v, path) for v in shape['prefixItems']) + ']'
        elif isinstance(shape.get('items'), dict):
            result = f"list[{expression(shape['items'], path)}]"
        else:
            raise ValueError(f'{path}: array needs its item type')
    elif kind == 'object' and isinstance(shape.get('additionalProperties'), dict):
        result = f"dict[str, {expression(shape['additionalProperties'], path)}]"
    elif kind in {'string', 'integer', 'number', 'boolean', 'null'}:
        result = {'string': 'str', 'integer': 'int', 'number': 'float', 'boolean': 'bool', 'null': 'None'}[kind]
    else:
        raise ValueError(f'{path}: unsupported Python type {kind!r}')
    if 'format' in shape:
        # Existing Python URI policy is a pattern plus the named runtime check.
        # New format-bearing fields cannot silently become plain strings.
        raise ValueError(f'{path}: format needs an explicit Python compatibility entry')
    args = [f'{target}={shape[source]!r}' for source, target in BOUNDS.items() if source in shape]
    if args:
        result = f"Annotated[{result}, Field({', '.join(args)})]"
    return result


def checked_profile(linkml_dir, index):
    profile = json.loads((linkml_dir / 'python-compatibility.json').read_text(encoding='utf-8'))
    if set(profile['models']) != set(index['classes']):
        raise ValueError('Python model mapping is incomplete or has orphaned entries')
    for name, cfg in profile['models'].items():
        definition = index['$defs'][name]
        if set(cfg.get('fields', {})) - set(definition.get('properties', {})):
            raise ValueError(f'{name}: orphaned Python field compatibility setting')
        conditions = {k: canonical(definition[k], index['$defs']) for k in ('allOf', 'anyOf', 'oneOf', 'not', 'if', 'then', 'else') if k in definition}
        if cfg.get('conditions', {}) != conditions:
            raise ValueError(f'{name}: conditional rules changed; review retained Python enforcement')
        if set(cfg) - {'module', 'config', 'order', 'parent', 'fields', 'validators', 'field_validators', 'conditions'}:
            raise ValueError(f'{name}: unknown Python model compatibility setting')
    seen = set()
    for entry in profile['adjustments']:
        place = (entry['model'], entry['field'])
        if place in seen or not entry.get('reason') or not entry.get('source'):
            raise ValueError(f'{place}: duplicate or undocumented Python adjustment')
        seen.add(place)
        actual = canonical(index['$defs'][place[0]]['properties'][place[1]], index['$defs'])
        if actual != entry['definition'] or entry['definition'] == entry['python']:
            raise ValueError(f'{place}: stale Python adjustment; review its source and witness')
        expression(entry['python'], '.'.join(place))
    return profile


def build_python(linkml_dir, index):
    """Return generated package files, without consulting the old Python models."""
    profile = checked_profile(linkml_dir, index)
    adjustments = {(e['model'], e['field']): e['python'] for e in profile['adjustments']}
    lines = [
        '"""Generated from LinkML by linkml/generate.py. Do not edit."""',
        'from __future__ import annotations', '',
        'from functools import cache, partial',
        'from importlib import import_module',
        'from typing import Annotated, Literal',
        'from pydantic import AfterValidator, BeforeValidator, BaseModel, ConfigDict, Field, field_validator, model_validator', '',
        '@cache',
        'def _resolve(module, function):',
        '    return getattr(import_module(".." + module, __package__), function)', '',
        'def _call(module, function, *args):',
        '    return _resolve(module, function)(*args)', '',
        'def _typed_call(module, function, path, skip_none, value):',
        '    if value is None and skip_none:',
        '        return value',
        '    if path:',
        '        if not isinstance(value, (list, tuple)):',
        '            return value',
        '        return [_typed_call(module, function, path[1:], skip_none, item) for item in value]',
        '    return _call(module, function, value)', '',
        'class Strict(BaseModel):',
        '    model_config = ConfigDict(extra="forbid", strict=True)', '',
    ]
    done = set()
    aliases = set()
    pending = dict(profile['models'])
    while pending:
        ready = [name for name, cfg in pending.items() if not cfg.get('parent') or cfg['parent'] in done]
        if not ready:
            raise ValueError('Python model inheritance has a cycle or unknown parent')
        for name in sorted(ready):
            cfg = pending.pop(name)
            definition = index['$defs'][name]
            if definition.get('type') == 'object' and not definition.get('properties') and isinstance(definition.get('additionalProperties'), dict):
                lines += [f'{name} = {expression(canonical(definition, index["$defs"]), name)}', '']
                aliases.add(name)
                done.add(name)
                continue
            fields = definition['properties']
            order = cfg['order']
            if set(order) != set(fields) or len(order) != len(fields):
                raise ValueError(f'{name}: Python field order mapping is incomplete or duplicated')
            parent = cfg.get('parent') or ('Strict' if cfg['config'].get('strict') else 'BaseModel')
            lines += [f"class {name}({parent}):", f'    {definition.get("description", name)!r}',
                      f"    model_config = ConfigDict(**{cfg['config']!r})"]
            for field in order:
                shape = adjustments.get((name, field), canonical(fields[field], index['$defs']))
                annotation = expression(shape, f'{name}.{field}')
                settings = cfg.get('fields', {}).get(field, {})
                for hook in settings.get('type_hooks', []):
                    annotation = f"Annotated[{annotation}, {hook['mode']}Validator(partial(_typed_call, {hook['module']!r}, {hook['function']!r}, {hook['path']!r}, {hook['mode'] == 'After'!r}))]"
                required = field in definition.get('required', [])
                if 'required' in settings:
                    if settings['required'] == required:
                        raise ValueError(f'{name}.{field}: stale requiredness adjustment')
                    required = settings['required']
                default = '...' if required else repr(settings.get('default', None))
                extras = ''
                if settings.get('exclude_none'):
                    extras = ', exclude_if=lambda value: value is None'
                default_arg = f"default_factory={settings['default_factory']}" if settings.get('default_factory') else f'default={default}'
                lines += [f'    {field}: {annotation} = Field({default_arg}{extras})']
            for method in cfg.get('validators', []):
                lines += ['', f"    @model_validator(mode={method['mode']!r})",
                          f"    def {method['name']}(self):",
                          f"        return _call({method['module']!r}, {method['function']!r}, self)"]
            for method in cfg.get('field_validators', []):
                fields_arg = ', '.join(repr(v) for v in method['fields'])
                lines += ['', f"    @field_validator({fields_arg}, mode={method['mode']!r})", '    @classmethod',
                          f"    def {method['name']}(cls, value):",
                          f"        return _call({method['module']!r}, {method['function']!r}, cls, value)"]
            lines += ['', '']
            done.add(name)
    for name in sorted(done - aliases):
        lines += [f'{name}.model_rebuild()']
    lines += ['', '__all__ = ' + repr(sorted(done)), '']
    return {'models.py': '\n'.join(lines), '__init__.py': '"""Generated models; legacy modules retain their import paths."""\n'}
