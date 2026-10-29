"""JSON Schema for external wire contracts with explicit nullability.

LinkML's JSON Schema generator defaults to nullable optional slots. Impresso
distinguishes optional non-null fields, nullable fields and nullable list members.
The definition records these choices in annotations, consumed here through the
generator's lifecycle hook. No field names or external schema are encoded here.

Read 29 October 2026: https://linkml.io/linkml/generators/json-schema.html
and linkml 1.12.1's generators/jsonschemagen.py (handle_class_slot and
after_generate_class_slot); the latter is tested in the locked environment.
"""

from linkml.generators.jsonschemagen import JsonSchemaGenerator


def flag(element, name):
    annotations = element.annotations
    annotation = (annotations.get(name) if isinstance(annotations, dict)
                  else getattr(annotations, name, None))
    if annotation is None:
        return False
    if str(annotation.value).lower() not in {'true', 'false'}:
        raise ValueError(f'{element.name}: {name} must be true or false')
    return str(annotation.value).lower() == 'true'


class ExplicitNullGenerator(JsonSchemaGenerator):
    """Keep native rules, aliases, bounds and openness; specialize only nulls."""

    def after_generate_class_slot(self, result, cls, sv):
        slot = sv.induced_slot(result.source.name, cls.name)
        shape = result.schema_
        if flag(slot, 'nullable'):
            if slot.required:
                raise ValueError(f'{cls.name}.{slot.name}: required nullable is unsupported')
            if 'type' in shape:
                shape['type'] = [shape['type'], 'null']
            else:
                raise ValueError(f'{cls.name}.{slot.name}: nullable reference is unsupported')
        if flag(slot, 'nullable_items'):
            if not slot.multivalued or shape.get('items', {}).get('type') != 'string':
                raise ValueError(f'{cls.name}.{slot.name}: nullable_items needs a string list')
            shape['items']['type'] = ['string', 'null']
        return result


def generator(schema, top_class):
    """Select explicit nulls only when the schema definition requests them."""
    native = JsonSchemaGenerator(str(schema), top_class=top_class, not_closed=False)
    annotation = native.schemaview.schema.annotations.get('json_schema_nulls')
    if annotation is None:
        return native
    if str(annotation.value) != 'explicit':
        raise ValueError('unsupported json_schema_nulls policy')
    return ExplicitNullGenerator(str(schema), top_class=top_class,
                                 not_closed=False, include_null=False)
