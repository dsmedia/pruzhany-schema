"""Adapt the pinned LinkML JSON Schema class index to static Zod 4 shapes.

Only the house style is supported. Unknown constructs fail with their class/field
path; they never become z.any(). Class conditions deliberately stay in the retained
hand-written refinements (checks/documents.yaml and checks/record.yaml).

Zod, "Defining schemas", https://zod.dev/api, read 30 October 2026:
strictObject, enums, regex, numeric/array bounds, nullish and object composition.
Prettier, "Options", https://prettier.io/docs/options, read 30 October 2026:
tabs, single quotes, ES5 trailing commas, printWidth 100. Emit that form directly;
generation needs neither bun nor a formatter.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import PurePosixPath

from linkml_runtime.utils.schemaview import SchemaView


HEADER = '// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.'
META = {'description', 'title'}
CONDITIONS = {'allOf', 'anyOf', 'oneOf', 'not', 'if', 'then', 'else'}


def quoted(value):
    # Prettier prefers double quotes only when they avoid escaping single quotes.
    if "'" in value and '"' not in value:
        return json.dumps(value, ensure_ascii=False)
    return "'" + json.dumps(value, ensure_ascii=False)[1:-1].replace('\\"', '"').replace("'", "\\'") + "'"


def clean(shape):
    return {key: value for key, value in shape.items() if key not in META}


def regex_literal(pattern):
    """Escape delimiters outside character classes, preserving the regex source."""
    result = []
    backslashes = 0
    in_class = False
    for char in pattern:
        escaped = backslashes % 2 == 1
        if char == '/' and not escaped and not in_class:
            result.append('\\')
        if not escaped:
            if char == '[':
                in_class = True
            elif char == ']':
                in_class = False
        result.append(char)
        backslashes = backslashes + 1 if char == '\\' else 0
    return ''.join(result)


def refuse(path, message):
    raise ValueError(f'{path}: unsupported Zod {message}')


def checked_keys(shape, allowed, path):
    unknown = set(shape) - allowed
    if unknown:
        refuse(path, f'constraints {sorted(unknown)}')


def reference(value, definitions, path):
    if not isinstance(value, str) or not value.startswith('#/$defs/'):
        refuse(path, 'external reference')
    name = value[len('#/$defs/'):]
    if name not in definitions or '/' in name:
        refuse(path, f'unknown reference {value!r}')
    return name


def check_condition(value, path):
    """Recognize the pinned generator's condition grammar, without emitting rules."""
    checked_keys(value, CONDITIONS | {'properties', 'required', 'const', 'enum', 'pattern',
                                     'type', 'items'}, path)
    for key, child in value.items():
        if key in {'allOf', 'anyOf', 'oneOf'}:
            for i, branch in enumerate(child):
                check_condition(branch, f'{path}.{key}[{i}]')
        elif key in {'not', 'if', 'then', 'else', 'items'}:
            check_condition(child, f'{path}.{key}')
        elif key == 'properties':
            for name, branch in child.items():
                check_condition(branch, f'{path}.{name}')


def declaration(name, values):
    line = f'export const {name} = z.enum([{", ".join(quoted(v) for v in values)}]);'
    if len(line) <= 100:
        return line
    return '\n'.join([f'export const {name} = z.enum([',
                      *[f'\t{quoted(v)},' for v in values], ']);'])


def import_line(names, module):
    names = sorted(names)
    line = f'import {{ {", ".join(names)} }} from {quoted(module)};'
    if len(line) <= 100:
        return line
    return '\n'.join(['import {', *[f'\t{name},' for name in names], f'}} from {quoted(module)};'])


class Renderer:
    def __init__(self, definitions, owners, enums):
        self.definitions = definitions
        self.owners = owners
        self.enums = enums
        self.dependencies = set()
        self.patterns = {}

    def expression(self, raw, path, optional=False):
        shape = clean(raw)
        nullable = False
        kind = shape.get('type')
        if isinstance(kind, list):
            if len(kind) != 2 or kind.count('null') != 1:
                refuse(path, f'type union {kind!r}')
            shape['type'] = next(t for t in kind if t != 'null')
            nullable = True
        if 'anyOf' in shape:
            checked_keys(shape, {'anyOf'}, path)
            branches = shape['anyOf']
            nonnull = [s for s in branches if s != {'type': 'null'}]
            if len(branches) != 2 or len(nonnull) != 1:
                refuse(path, 'union other than a nullable field')
            result = self.expression(nonnull[0], path)
            nullable = True
        elif '$ref' in shape:
            checked_keys(shape, {'$ref', 'enum'}, path)
            name = reference(shape['$ref'], self.definitions, path)
            if 'enum' in shape:
                target = self.definitions[name]
                if not set(shape['enum']) <= set(target.get('enum', [])):
                    refuse(path, 'enum intersection outside its referenced enum')
                result = self.enum(shape['enum'], path)
            else:
                result = self.enums[tuple(self.definitions[name]['enum'])] if 'enum' in self.definitions[name] else name + 'Shape'
                self.dependencies.add(result)
        elif 'enum' in shape:
            checked_keys(shape, {'type', 'enum'}, path)
            if shape.get('type') != 'string':
                refuse(path, 'non-string enum')
            result = self.enum(shape['enum'], path)
            nullable = False  # enum excludes null even when type includes it.
        elif 'const' in shape:
            checked_keys(shape, {'type', 'const'}, path)
            if shape.get('type') != 'string' or not isinstance(shape['const'], str):
                refuse(path, 'non-string const')
            result = f'z.literal({quoted(shape["const"])})'
            nullable = False
        else:
            kind = shape.get('type')
            allowed = {'type'}
            if kind == 'string':
                allowed |= {'pattern', 'minLength', 'maxLength', 'format'}
                if 'format' in shape and shape['format'] != 'uri':
                    refuse(path, f'format {shape["format"]!r}')
                result = 'z.url()' if 'format' in shape else 'z.string()'
                for key, method in [('minLength', 'min'), ('maxLength', 'max')]:
                    if key in shape:
                        self.cardinality(shape[key], path, key)
                        result += f'.{method}({shape[key]})'
                if 'pattern' in shape:
                    pattern = shape['pattern']
                    if not isinstance(pattern, str) or not pattern or any(c in pattern for c in '\n\r\u2028\u2029'):
                        refuse(path, 'non-literal regex pattern')
                    self.patterns.setdefault(pattern, f'pattern{len(self.patterns) + 1}')
                    result += f'.regex({self.patterns[pattern]})'
                    # Zod 4.3.5's stringProcessor lets regex overwrite the URL format
                    # in JSON exports. Metadata restores the generated URI constraint
                    # while both runtime checks remain active (source read 30 Oct 2026:
                    # zod/src/v4/core/json-schema-processors.ts, stringProcessor).
                    if 'format' in shape:
                        result += ".meta({ format: 'uri' })"
            elif kind in {'number', 'integer'}:
                allowed |= {'minimum', 'maximum', 'exclusiveMinimum', 'exclusiveMaximum'}
                result = 'z.number().int()' if kind == 'integer' else 'z.number()'
                for key, method in [('minimum', 'min'), ('maximum', 'max'),
                                    ('exclusiveMinimum', 'gt'), ('exclusiveMaximum', 'lt')]:
                    if key in shape:
                        if (isinstance(shape[key], bool) or not isinstance(shape[key], (int, float))
                                or not math.isfinite(shape[key])):
                            refuse(path, f'non-numeric {key}')
                        result += f'.{method}({shape[key]})'
            elif kind == 'array':
                allowed |= {'items', 'minItems', 'maxItems'}
                if not isinstance(shape.get('items'), dict):
                    refuse(path, 'array without an item type')
                result = f'z.array({self.expression(shape["items"], path + "[]")})'
                for key, method in [('minItems', 'min'), ('maxItems', 'max')]:
                    if key in shape:
                        self.cardinality(shape[key], path, key)
                        result += f'.{method}({shape[key]})'
            elif kind == 'object':
                allowed |= {'additionalProperties'}
                if not isinstance(shape.get('additionalProperties'), dict):
                    refuse(path, 'object other than a typed map')
                result = f'z.record(z.string(), {self.expression(shape["additionalProperties"], path + "{}")})'
            elif kind in {'boolean', 'null'}:
                result = f'z.{kind}()'
            else:
                refuse(path, f'type {kind!r}')
            checked_keys(shape, allowed, path)
        return result + ('.nullish()' if optional and nullable else
                         '.nullable()' if nullable else '.optional()' if optional else '')

    def enum(self, values, path):
        if not values or not all(isinstance(v, str) for v in values) or len(set(values)) != len(values):
            refuse(path, 'empty, duplicated or non-string enum')
        result = self.enums[tuple(values)]
        self.dependencies.add(result)
        return result

    @staticmethod
    def cardinality(value, path, key):
        if type(value) is not int or value < 0:
            refuse(path, f'non-negative integer {key} needed')


def definition_field_orders(linkml_dir, index):
    """Definition order, ancestors first; induced slots supply the final wire aliases.

    Read 30 October 2026: linkml-runtime 1.12.1, utils/schemaview.py,
    SchemaView.class_ancestors, class_slots and induced_slot (the locked source).
    class_slots(direct=True) preserves slots then YAML attributes; ancestor closure
    is child-first, so reverse it and retain the first position of repeated slots.
    Induce in the final class context so slot_usage/aliases keep their precedence.
    """
    views = {}
    result = {}
    for name, source in index['classes'].items():
        if source not in views:
            views[source] = SchemaView(str(linkml_dir / source))
        view = views[source]
        slots = dict.fromkeys(slot for ancestor in reversed(view.class_ancestors(name))
                              for slot in view.class_slots(ancestor, direct=True))
        result[name] = [str(slot.alias or slot.name)
                        for slot in (view.induced_slot(slot, name) for slot in slots)]
    return result


def build_zod(index, field_orders=None):
    """Return module -> text for the owned site graph, without reading hand Zod."""
    definitions = index['$defs']
    owners = {name: PurePosixPath(source).stem for name, source in index['classes'].items()}
    # Small isolated renderer fixtures can supply their own property order. Production
    # always supplies definition_field_orders; never trust the sorted JSON index there.
    if field_orders is not None and field_orders.keys() != owners.keys():
        raise ValueError('Zod field orders must cover every owned class exactly once')
    for name in owners:
        if not re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', name):
            refuse(name, 'class name')
        if name not in definitions:
            refuse(name, 'missing class definition')
        if not re.fullmatch(r'[a-z][a-z0-9_]*', owners[name]) or owners[name] == 'enums':
            refuse(name, 'module name')
    # Named and inline enums share one declaration per ordered value list.
    enums = {}
    def collect(raw, suggested):
        shape = clean(raw)
        if 'enum' in shape:
            values = shape['enum']
            if not values or not all(isinstance(v, str) for v in values) or len(set(values)) != len(values):
                refuse(suggested, 'empty, duplicated or non-string enum')
            enums.setdefault(tuple(values), suggested + 'Enum')
        for key, value in shape.items():
            if key in {'properties'}:
                for field, child in value.items():
                    collect(child, suggested + field[0].upper() + field[1:])
            elif key in {'items', 'additionalProperties'} and isinstance(value, dict):
                collect(value, suggested + 'Item')
            elif key == 'anyOf' and 'type' not in shape:
                for child in value:
                    collect(child, suggested)
    for name, shape in sorted(definitions.items()):
        if 'enum' in shape:
            checked_keys(clean(shape), {'type', 'enum'}, name)
            collect(shape, name)
    for name in sorted(owners):
        for field, shape in definitions[name].get('properties', {}).items():
            collect(shape, name + field[0].upper() + field[1:])
    if len(set(enums.values())) != len(enums):
        raise ValueError('Zod enum declaration names collide')
    symbol_owner = {name + 'Shape': module for name, module in owners.items()}
    symbol_owner.update({symbol: 'enums' for symbol in enums.values()})
    output = {'enums.ts': '\n\n'.join([HEADER + "\nimport { z } from 'zod/v4';",
                                       *[declaration(symbol, values) for values, symbol in enums.items()]]) + '\n'}
    pending = set(owners)
    done = set()
    rendered = {}
    while pending:
        progress = False
        for name in sorted(pending):
            shape = clean(definitions[name])
            checked_keys(shape, {'type', 'properties', 'required', 'additionalProperties'} | CONDITIONS, name)
            for key in CONDITIONS & shape.keys():
                check_condition({key: shape[key]}, name)
            if shape.get('type') != 'object':
                refuse(name, 'non-object class')
            renderer = Renderer(definitions, owners, enums)
            if not shape.get('properties') and isinstance(shape.get('additionalProperties'), dict):
                body = f'export const {name}Shape = {renderer.expression({k: v for k, v in shape.items() if k not in CONDITIONS | {"required", "properties"}}, name)};'
            else:
                if shape.get('additionalProperties') is not False:
                    refuse(name, 'open class')
                fields = shape.get('properties', {})
                order = list(fields) if field_orders is None else field_orders[name]
                if len(order) != len(set(order)) or set(order) != fields.keys():
                    refuse(name, 'definition field order differs from generated properties')
                required = shape.get('required', [])
                if len(set(required)) != len(required) or set(required) - fields.keys():
                    refuse(name, 'required fields outside the class or duplicated')
                lines = [f'export const {name}Shape = z.strictObject({{']
                for field in order:
                    value = fields[field]
                    if field == '__proto__' or not re.fullmatch(r'[A-Za-z_$][A-Za-z0-9_$]*', field):
                        refuse(f'{name}.{field}', 'property name')
                    expr = renderer.expression(value, f'{name}.{field}', field not in required)
                    lines.append(f'\t{field}: {expr},')
                lines.append('});')
                body = '\n'.join(lines)
            dependencies = {s[:-5] for s in renderer.dependencies if s.endswith('Shape')}
            unknown = dependencies - owners.keys()
            if unknown:
                refuse(name, f'unowned references {sorted(unknown)}')
            if dependencies - done:
                continue
            rendered[name] = (body, renderer)
            done.add(name)
            pending.remove(name)
            progress = True
        if not progress:
            raise ValueError(f'Zod class reference cycle: {sorted(pending)}')
    module_dependencies = {}
    for module in sorted(set(owners.values())):
        imports = {}
        patterns = []
        bodies = []
        module_patterns = {}
        for name, (body, renderer) in rendered.items():
            if owners[name] != module:
                continue
            # Renderer-local names are replaced simultaneously, so pattern1 cannot
            # accidentally replace the prefix of pattern10 or a newly assigned name.
            renames = {}
            for pattern, local in renderer.patterns.items():
                module_patterns.setdefault(pattern, f'pattern{len(module_patterns) + 1}')
                renames[local] = module_patterns[pattern]
            body = re.sub(r'\bpattern\d+\b', lambda m: renames[m[0]], body)
            bodies.append(body)
            for symbol in renderer.dependencies:
                owner = symbol_owner[symbol]
                if owner != module:
                    imports.setdefault(owner, set()).add(symbol)
        for pattern, symbol in module_patterns.items():
            # Escape literal slashes only; retain the regex source and its end guard.
            literal = regex_literal(pattern)
            line = f'const {symbol} = /{literal}/;'
            patterns.append(line if len(line) <= 100 else f'const {symbol} =\n\t/{literal}/;')
        sections = [HEADER + "\nimport { z } from 'zod/v4';" + ''.join(
            '\n' + import_line(symbols, './' + owner) for owner, symbols in sorted(imports.items()))]
        if patterns:
            sections.append('\n'.join(patterns))
        sections.extend(bodies)
        output[module + '.ts'] = '\n\n'.join(sections) + '\n'
        module_dependencies[module] = set(imports) - {'enums'}
    while module_dependencies:
        ready = {m for m, deps in module_dependencies.items() if not deps & module_dependencies.keys()}
        if not ready:
            raise ValueError(f'Zod module import cycle: {sorted(module_dependencies)}')
        module_dependencies = {m: deps for m, deps in module_dependencies.items() if m not in ready}
    return output
