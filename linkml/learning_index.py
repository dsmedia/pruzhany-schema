"""Resolved documentation for learning tools, separate from document validation."""

import json
import hashlib
import yaml


def mapping(element):
    result = []
    for key in ('class_uri', 'slot_uri', 'meaning', 'exact_mappings', 'close_mappings',
                'related_mappings', 'narrow_mappings', 'broad_mappings'):
        value = getattr(element, key, None)
        for term in (value if isinstance(value, list) else [value] if value else []):
            result.append({'kind': key, 'term': str(term)})
    return result


def excerpts(path):
    text = path.read_text(encoding='utf-8')
    node = yaml.compose(text)
    classes = next((v for k, v in node.value if k.value == 'classes'), None)
    if classes is None:
        return {}
    lines = text.splitlines()
    return {key.value: '\n'.join(lines[key.start_mark.line:value.end_mark.line]).rstrip() + '\n'
            for key, value in classes.value}


def build_index(linkml_dir, views, contract):
    models, types = {}, {}
    for entry, view in views:
        source = 'linkml/' + entry['schema']
        source_text = excerpts(linkml_dir / entry['schema'])
        for name, cls in sorted(view.all_classes(imports=False).items()):
            fields = []
            for slot in sorted(view.class_induced_slots(name), key=lambda s: s.alias or s.name):
                field = slot.alias or slot.name
                annotations = slot.annotations or {}
                annotation = annotations['references'] if 'references' in annotations else None
                references = [s.strip() for s in str(annotation.value).split(',')] if annotation else []
                fields.append({
                    'name': field, 'description': str(slot.description or ''),
                    'range': str(slot.range or 'string'), 'required': bool(slot.required),
                    'multivalued': bool(slot.multivalued),
                    'relationship': 'reference' if references else 'contains' if slot.range in contract['classes'] else 'value',
                    'references': references, 'mappings': mapping(slot),
                    'shape': contract['$defs'][name].get('properties', {}).get(field, {}),
                })
            models[name] = {'description': str(cls.description or ''), 'source': source,
                            'parent': str(cls.is_a) if cls.is_a else None,
                            'mappings': mapping(cls), 'fields': fields, 'yaml': source_text[name]}
        for name, typ in sorted(view.all_types(imports=False).items()):
            types[name] = {'description': str(typ.description or ''), 'mappings': mapping(typ)}
        for name, enum in sorted(view.all_enums(imports=False).items()):
            types[name] = {'description': str(enum.description or ''), 'mappings': mapping(enum),
                           'values': [{'value': str(value), 'description': str(term.description or ''),
                                       'mappings': mapping(term)}
                                      for value, term in enum.permissible_values.items()]}
    validate_references(models)
    sources = sorted((linkml_dir / 'schema').glob('*.yaml'))
    return {'version': 1, 'models': models, 'types': types,
            'inputs': {'linkml/' + p.relative_to(linkml_dir).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in sources},
            'contract_sha256': hashlib.sha256((json.dumps(contract, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode()).hexdigest()}


def validate_references(models):
    for name, model in models.items():
        for field in model['fields']:
            references = field['references']
            if len(references) != len(set(references)):
                raise ValueError(f'{name}.{field["name"]}: duplicate reference target')
            for reference in references:
                target, separator, key = reference.partition('.')
                if not separator or target not in models or key not in {f['name'] for f in models[target]['fields']}:
                    raise ValueError(f'{name}.{field["name"]}: unknown reference target {reference}')


def write_index(linkml_dir, destination, views, contract, write_text):
    write_text(destination / 'docs/model-index.json',
               json.dumps(build_index(linkml_dir, views, contract), ensure_ascii=False, indent=2, sort_keys=True))
