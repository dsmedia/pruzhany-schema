"""The LinkML definition and Zod agree on every model's fields, required keys and enums.

Reads generated JSON only, so the existing Pydantic environment does not acquire
LinkML's incompatible dependency versions. Regeneration verifies this index in
the separate LinkML environment. The explicit model map cannot silently omit a
new class or a Zod model; the two runtime carriers are named exclusions.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def at(root, pointer):
    node = root
    for part in pointer.split('/')[1:]:
        key = part.replace('~1', '/').replace('~0', '~')
        node = node[int(key)] if isinstance(node, list) else node[key]
    return node


def expand(node, root, seen=()):
    if '$ref' not in node:
        return node
    reference = node['$ref']
    if not reference.startswith('#/') or reference in seen:
        raise ValueError(f'unsupported or cyclic reference {reference}')
    target = expand(at(root, reference[1:]), root, (*seen, reference))
    siblings = {key: value for key, value in node.items() if key != '$ref'}
    return {'allOf': [target, siblings]} if siblings else target


def literal_pattern(pattern):
    """Only anchored finite version alternatives; never approximate arbitrary regexes."""
    if not isinstance(pattern, str):
        return None
    pattern = pattern.removesuffix(r'(?![\s\S])')
    if not pattern.startswith('^') or not pattern.endswith('$'):
        return None
    body = pattern[1:-1]
    if body.startswith('(?:') and body.endswith(')'):
        body = body[3:-1]
    elif body.startswith('(') and body.endswith(')'):
        body = body[1:-1]
    if not re.fullmatch(r'(?:[A-Za-z0-9_-]|\\\.|\|)+', body):
        return None
    return frozenset(part.replace(r'\.', '.') for part in body.split('|'))


def enum_values(node, root):
    node = expand(node, root)
    if node.get('type') == 'null':
        return frozenset()  # Nullability is checked by the comparison, not enum membership.
    constraints = []
    if 'enum' in node:
        constraints.append(frozenset(v for v in node['enum'] if v is not None))
    if 'const' in node:
        constraints.append(frozenset([node['const']]) if node['const'] is not None else frozenset())
    if finite := literal_pattern(node.get('pattern')):
        constraints.append(finite)
    if 'allOf' in node:
        constraints += [values for child in node['allOf']
                        if (values := enum_values(child, root)) is not None]
    for word in ('anyOf', 'oneOf'):
        if word in node:
            branches = [enum_values(child, root) for child in node[word]]
            if all(value is not None for value in branches):
                constraints.append(frozenset().union(*branches))
    return frozenset.intersection(*constraints) if constraints else None


def object_shape(node, root):
    node = expand(node, root)
    if 'allOf' not in node:
        return node
    properties, required = dict(node.get('properties', {})), set(node.get('required', []))
    for child in node['allOf']:
        part = object_shape(child, root)
        properties.update(part.get('properties', {}))
        required.update(part.get('required', []))
    return {**node, 'properties': properties, 'required': sorted(required)}


def problems(zod, index, mapping):
    found = []
    pairs = mapping['models']
    if set(pairs) != set(index['classes']):
        found.append(f"LinkML model map differs from owned classes: {sorted(set(pairs) ^ set(index['classes']))}")
    covered = {pair['zod'] for pair in pairs.values()} | set(mapping['runtime_carriers'])
    if covered != set(zod):
        found.append(f'Zod model coverage differs: {sorted(covered ^ set(zod))}')
    known = {p['file'] + '#' + p['pointer'] for entry in index['known_looser']
             if entry['kind'] == 'required-key-nullable' for p in entry['where']}
    exceptions = mapping['required_exceptions']
    used = set()
    for name, pair in pairs.items():
        try:
            old_root = zod[pair['zod']]
            old = object_shape(at(old_root, pair['pointer']), old_root)
            new = object_shape(index['$defs'][name], index)
            old_fields, new_fields = old.get('properties', {}), new.get('properties', {})
            if set(old_fields) != set(new_fields):
                found.append(f'[{name}] fields differ: {sorted(set(old_fields) ^ set(new_fields))}')
            required_old, required_new = set(old.get('required', [])), set(new.get('required', []))
            for field in required_old ^ required_new:
                key = f'{name}.{field}'
                pointer = exceptions.get(key)
                if (field in required_old and pointer in known
                        and pointer.endswith('/properties/' + field)):
                    used.add(key)
                else:
                    found.append(f'[{key}] required differs: Zod={field in required_old}, LinkML={field in required_new}')
            for field in old_fields.keys() & new_fields.keys():
                before = enum_values(old_fields[field], old_root)
                after = enum_values(new_fields[field], index)
                if before != after:
                    found.append(f'[{name}.{field}] enum differs: Zod={sorted(before or [], key=str)}, '
                                 f'LinkML={sorted(after or [], key=str)}')
        except (KeyError, TypeError, ValueError) as error:
            found.append(f'[{name}] cannot compare: {error}')
    if stale := set(exceptions) - used:
        found.append(f'stale or invalid required exceptions: {sorted(stale)}')
    return found


def check(zod):
    index = json.loads((ROOT / 'linkml/generated/contract.json').read_text(encoding='utf-8'))
    mapping = json.loads((ROOT / 'linkml/model-map.json').read_text(encoding='utf-8'))
    found = problems(zod, index, mapping)
    if found:
        raise SystemExit('LinkML<->Zod contract drift:\n' + '\n'.join('  - ' + p for p in found))
    print(f"contract: {len(mapping['models'])} LinkML/Zod models in lockstep; "
          f"{len(mapping['required_exceptions'])} exact required/null exceptions")
