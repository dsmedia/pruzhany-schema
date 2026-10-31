"""JSON Schema for external wire contracts with explicit nullability and legacy unions.

LinkML's JSON Schema generator defaults to nullable optional slots. Impresso
distinguishes optional non-null fields, nullable fields and nullable list members.
The definition records these choices in annotations, consumed here through the
generator's lifecycle hook. No field names or external schema are encoded here. Bounded annotations also preserve
legacy scalar/array/object unions and minimum string length.

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


def wire_types(element, name, shape):
    """Preserve heterogeneous legacy JSON unions without constraining array contents.

    LinkML JSON Schema, Slots, Advanced features and Arrays documentation, read
    31 October 2026: https://linkml.io/linkml/schemas/advanced.html. These bounded
    wire annotations describe unions that native scalar/list ranges cannot express.
    They may replace only an unconstrained string placeholder, never other rules.
    """
    annotations = element.annotations
    annotation = (annotations.get(name) if isinstance(annotations, dict)
                  else getattr(annotations, name, None))
    if annotation is None:
        return
    types = str(annotation.value).split(',')
    if (len(types) < 2 or len(set(types)) != len(types)
            or not set(types) <= {'string', 'integer', 'object', 'array'}
            or shape != {'type': 'string'}):
        raise ValueError(f'{element.name}: unsupported {name} union or constrained placeholder')
    shape['type'] = types


class ExplicitNullGenerator(JsonSchemaGenerator):
    """Keep native rules, aliases, bounds and openness; adapt declared wire edges."""

    def after_generate_class_slot(self, result, cls, sv):
        slot = sv.induced_slot(result.source.name, cls.name)
        shape = result.schema_
        # Descriptions are metadata, not constraints on the placeholder.
        description = shape.pop('description', None)
        wire_types(slot, 'json_types', shape)
        if 'json_item_types' in slot.annotations:
            if not slot.multivalued or shape.get('type') != 'array':
                raise ValueError(f'{cls.name}.{slot.name}: json_item_types needs a list')
            wire_types(slot, 'json_item_types', shape['items'])
        if 'json_min_length' in slot.annotations:
            value = str(slot.annotations['json_min_length'].value)
            if shape.get('type') != 'string' or not value.isdecimal():
                raise ValueError(f'{cls.name}.{slot.name}: json_min_length needs a string and integer')
            shape['minLength'] = int(value)
        if description is not None:
            shape['description'] = description
        if flag(slot, 'nullable'):
            if 'type' in shape:
                types = shape['type'] if isinstance(shape['type'], list) else [shape['type']]
                shape['type'] = [*types, 'null']
            else:
                raise ValueError(f'{cls.name}.{slot.name}: nullable reference is unsupported')
        if flag(slot, 'nullable_items'):
            if not slot.multivalued or shape.get('items', {}).get('type') != 'string':
                raise ValueError(f'{cls.name}.{slot.name}: nullable_items needs a string list')
            shape['items']['type'] = ['string', 'null']
        return result


class ReleaseGenerator(JsonSchemaGenerator):
    """Honor deactivated rules and explicitly typed conditions in released contracts.

    Read 31 October 2026: LinkML Advanced features (Rules), JSON Schema (Rules),
    and https://linkml.io/linkml-model/latest/docs/deactivated/; pinned 1.12.1
    handle_class ignores deactivated and anonymous conditions omit their types.
    The opt-in annotation below preserves a condition's declared range, including
    rejection of null. Existing unannotated conditions retain their exact behavior.
    """

    def get_subschema_for_anonymous_class(self, cls, properties_required=False):
        result = super().get_subschema_for_anonymous_class(cls, properties_required)
        if cls:
            for slot in cls.slot_conditions.values():
                if flag(slot, 'json_schema_typed_range'):
                    if not slot.range:
                        raise ValueError(f'{slot.name}: typed condition needs an explicit range')
                    result['properties'][self.aliased_slot_name(slot)] = self.get_subschema_for_slot(
                        slot, omit_type=False, include_null=False)
        return result


def release_rules(generator):
    """Filter a generator's private SchemaView, never the source definition."""
    for cls in generator.schemaview.all_classes().values():
        cls.rules = [rule for rule in cls.rules if not rule.deactivated]
    return generator


def generator(schema, top_class):
    """Select explicit nulls only when the schema definition requests them."""
    native = ReleaseGenerator(str(schema), top_class=top_class, not_closed=False)
    annotation = native.schemaview.schema.annotations.get('json_schema_nulls')
    if annotation is None:
        return release_rules(native)
    if str(annotation.value) != 'explicit':
        raise ValueError('unsupported json_schema_nulls policy')
    return ExplicitNullGenerator(str(schema), top_class=top_class,
                                 not_closed=False, include_null=False)
