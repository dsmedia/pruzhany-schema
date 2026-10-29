"""A bounded public RDF view of the definition; no changes to the stored document contract."""

import hashlib
import json
from pathlib import Path

from rdflib import BNode, Graph, Literal, Namespace, RDF, RDFS, URIRef, XSD
from rdflib.namespace import OWL, SH

PC = "https://pruzhany.org/ns/sourced-entities#"
PREFIXES = {
    "pc": PC,
    "rdf": str(RDF),
    "rdfs": str(RDFS),
    "xsd": str(XSD),
    "rico": "https://www.ica.org/standards/RiC/ontology#",
    "ehri": "http://lod.ehri-project-test.eu/ontology#",
}


def expand(term):
    prefix, sep, local = term.partition(":")
    if sep and prefix in PREFIXES:
        return PREFIXES[prefix] + local
    if term.startswith(("https://", "http://")):
        return term
    raise ValueError("unknown RDF mapping: " + term)


def local(name):
    return URIRef(PC + "export_" + name)


def triples(graph):
    """N-Triples is valid Turtle; named shape/list nodes keep generation deterministic."""
    return (
        "\n".join(sorted(f"{s.n3()} {p.n3()} {o.n3()} ." for s, p, o in graph)) + "\n"
    )


def sequence(graph, values, name):
    if not values:
        return RDF.nil
    cells = [BNode(name + "_" + str(i)) for i in range(len(values))]
    for i, value in enumerate(values):
        graph.add((cells[i], RDF.first, value))
        graph.add((cells[i], RDF.rest, cells[i + 1] if i + 1 < len(cells) else RDF.nil))
    return cells[0]


def resolved(shape, contract, visited=()):
    """Resolve scalar ranges only. Object ranges are governed by the explicit public view."""
    if "$ref" in shape:
        ref = shape["$ref"].split("/")[-1]
        if ref in visited:
            raise ValueError("recursive RDF field reference: " + ref)
        return resolved(contract["$defs"][ref], contract, (*visited, ref))
    if "anyOf" in shape and shape.get("type") != "object":
        branches = [s for s in shape["anyOf"] if s.get("type") != "null"]
        if len(branches) == 1:
            return resolved(branches[0], contract, visited)
        raise ValueError("RDF field has an unsupported alternative branch")
    return shape


def make_profile(index, config, contract):
    if set(config["models"]) & set(config["omitted_models"]) or set(
        index["models"]
    ) != set(config["models"]) | set(config["omitted_models"]):
        raise ValueError("RDF profile must account for every source model exactly once")
    if any(not reason for reason in config["omitted_models"].values()):
        raise ValueError("omitted RDF models need a reason")
    models = {}
    for name, settings in sorted(config["models"].items()):
        model = index["models"][name]
        source = {f["name"]: f for f in model["fields"]}
        selected, omitted = settings["fields"], settings["omitted"]
        if (
            len(selected) != len(set(selected))
            or set(selected) & set(omitted)
            or set(source) != set(selected) | set(omitted)
        ):
            raise ValueError(
                f"{name}: every field needs an export or omission decision"
            )
        if not settings["reason"] or any(not reason for reason in omitted.values()):
            raise ValueError(f"{name}: an export/omission reason is empty")
        optional = settings.get("optional", {})
        if not set(optional) <= set(selected) or any(
            not reason for reason in optional.values()
        ):
            raise ValueError(f"{name}: stale optional-field adjustment")
        required = settings.get("required", {})
        if not set(required) <= set(selected) or any(
            not reason for reason in required.values()
        ):
            raise ValueError(f"{name}: stale required-field adjustment")
        for category in ("references", "ranges", "predicates", "positions"):
            if not set(settings.get(category, {})) <= set(selected):
                raise ValueError(f"{name}: stale {category} adjustment")
        if not set(settings.get("json_fields", [])) <= set(selected) or set(
            optional
        ) & set(required):
            raise ValueError(f"{name}: stale or contradictory public-view adjustment")
        fields = {}
        for key in selected:
            f = source[key]
            target = settings.get("references", {}).get(key)
            range_name = settings.get("ranges", {}).get(key, f["range"])
            shape = resolved(f["shape"], contract)
            if f["multivalued"]:
                item = resolved(shape.get("items", {}), contract)
            else:
                item = shape
            supported = {
                "description",
                "title",
                "type",
                "enum",
                "const",
                "pattern",
                "format",
                "minLength",
                "maxLength",
                "minimum",
                "maximum",
                "exclusiveMinimum",
                "exclusiveMaximum",
                "items",
                "minItems",
                "maxItems",
                "properties",
                "required",
                "additionalProperties",
            }
            if item.get("type") == "object":
                supported.update(
                    {"allOf", "anyOf", "if", "then", "else"}
                )  # Private object conditions remain with the source Zod gate.
            if (set(shape) | set(item)) - supported:
                raise ValueError(f"{name}.{key}: unsupported RDF field constraints")
            nested = range_name if range_name in config["models"] else None
            is_json = key in settings.get("json_fields", [])
            if range_name in index["models"] and not (nested or is_json or target):
                raise ValueError(f"{name}.{key}: object has no public profile")
            predicate = expand(
                settings.get("predicates", {}).get(key, "pc:export_" + name + "_" + key)
            )
            fields[key] = {
                "predicate": predicate,
                "description": f["description"],
                "source_range": f["range"],
                "required": (f["required"] and key not in optional)
                or key in settings.get("required", {}),
                "list": f["multivalued"],
                "target": target,
                "nested": nested,
                "json": is_json,
                "constraint": {
                    k: v
                    for k, v in item.items()
                    if k
                    in (
                        "type",
                        "enum",
                        "const",
                        "pattern",
                        "format",
                        "minLength",
                        "maxLength",
                        "minimum",
                        "maximum",
                        "exclusiveMinimum",
                        "exclusiveMaximum",
                    )
                },
                "minimum_items": shape.get("minItems", 0),
                "maximum_items": shape.get("maxItems"),
                "positions": settings.get("positions", {}).get(key, []),
                "mappings": f["mappings"],
            }
        semantic_types = [
            expand(m["term"]) for m in model["mappings"] if m["kind"] == "class_uri"
        ]
        # Public relations lack the private evidence supporting the historical relation.
        # Their reified statement remains queryable without asserting the underlying edge.
        if name in ("SharedFact", "SourcedRelation"):
            semantic_types = [str(RDF.Statement)] + (
                [expand("rico:Relation")] if name == "SharedFact" else []
            )
        models[name] = {
            "iri": str(local(name)),
            "types": semantic_types,
            "fields": fields,
            "description": model["description"],
            "reason": settings["reason"],
            "source": model["source"],
            "omitted": omitted,
            "optional": optional,
            "required": required,
        }
    return {
        "version": 1,
        "models": models,
        "omitted_models": config["omitted_models"],
        "vocabularies": index["types"],
        "source_sha256": index["inputs"],
        "contract_sha256": index["contract_sha256"],
    }


def add_value_constraint(graph, node, field, tag, models):
    if field["target"] or field["nested"]:
        target = field["target"] or field["nested"]
        graph.add((node, SH.nodeKind, SH.IRI))
        target_class = local(target)
        if field["target"]:
            a, b = local(tag + "_target"), local(tag + "_reference")
            graph.add((a, SH["class"], target_class))
            graph.add((b, SH["class"], local("Reference")))
            expected = local(tag + "_expected")
            graph.add((b, SH.property, expected))
            graph.add((expected, SH.path, local("target_model")))
            graph.add((expected, SH.hasValue, Literal(target)))
            graph.add((node, SH["or"], sequence(graph, [a, b], tag + "_choices")))
        else:
            graph.add((node, SH["class"], target_class))
        return
    if field["json"]:
        graph.add((node, SH.datatype, RDF.JSON))
        return
    c = field["constraint"]
    types = c.get("type", "string")
    types = types if isinstance(types, list) else [types]
    types = [t for t in types if t != "null"]
    if len(types) != 1 or types[0] not in ("string", "integer", "number", "boolean"):
        raise ValueError(f"{tag}: unsupported literal shape {c}")
    if types[0] == "number":
        choices = []
        for i, datatype in enumerate([XSD.integer, XSD.double, XSD.decimal]):
            choice = local(tag + "_number_" + str(i))
            graph.add((choice, SH.datatype, datatype))
            choices.append(choice)
        graph.add((node, SH["or"], sequence(graph, choices, tag + "_numbers")))
    else:
        graph.add(
            (
                node,
                SH.datatype,
                {"string": XSD.string, "integer": XSD.integer, "boolean": XSD.boolean}[
                    types[0]
                ],
            )
        )
    for source, predicate in [
        ("minimum", SH.minInclusive),
        ("maximum", SH.maxInclusive),
        ("exclusiveMinimum", SH.minExclusive),
        ("exclusiveMaximum", SH.maxExclusive),
        ("pattern", SH.pattern),
        ("minLength", SH.minLength),
        ("maxLength", SH.maxLength),
    ]:
        if source in c:
            graph.add((node, predicate, Literal(c[source])))
    if c.get("format"):
        if c["format"] != "uri":
            raise ValueError(f"{tag}: unsupported RDF format {c['format']}")
        # Full RFC URI checking remains an explicit runtime FormatChecker gate.
        graph.add((node, SH.pattern, Literal(r"^[A-Za-z][A-Za-z0-9+.-]*:[^\s]*$")))
    if "enum" in c or "const" in c:
        values = c["enum"] if "enum" in c else [c["const"]]
        graph.add(
            (
                node,
                SH["in"],
                sequence(graph, [Literal(v) for v in values], tag + "_enum"),
            )
        )


def make_artifacts(profile):
    context = {"@version": 1.1, **PREFIXES}
    ontology, shapes = Graph(), Graph()
    ignored = sequence(shapes, [RDF.type], "ignored")
    for name, model in profile["models"].items():
        cls, shape = URIRef(model["iri"]), local(name + "_Shape")
        ontology.add((cls, RDF.type, OWL.Class))
        ontology.add(
            (cls, RDFS.comment, Literal(model["description"] + " " + model["reason"]))
        )
        for kind in model["types"]:
            ontology.add((cls, RDFS.subClassOf, URIRef(kind)))
        shapes.add((shape, RDF.type, SH.NodeShape))
        shapes.add((shape, SH.targetClass, cls))
        shapes.add((shape, SH.closed, Literal(True)))
        shapes.add((shape, SH.ignoredProperties, ignored))
        scoped = {}
        for key, field in model["fields"].items():
            pred = URIRef(field["predicate"])
            prop = local(name + "_" + key + "_Shape")
            if str(pred).startswith(PC + "export_"):
                ontology.add((pred, RDF.type, RDF.Property))
                ontology.add(
                    (
                        pred,
                        RDFS.comment,
                        Literal(
                            field["description"]
                            + " Public source-scoped field; it does not assert an unqualified biographical relationship."
                        ),
                    )
                )
            for mapping in field["mappings"]:
                ontology.add((pred, RDFS.seeAlso, URIRef(expand(mapping["term"]))))
            term = {"@id": str(pred)}
            if field["target"]:
                term["@type"] = "@id"
            if field["list"]:
                term["@container"] = "@list"
            scoped[key] = term
            shapes.add((shape, SH.property, prop))
            shapes.add((prop, SH.path, pred))
            shapes.add((prop, SH.maxCount, Literal(1)))
            if field["required"]:
                shapes.add((prop, SH.minCount, Literal(1)))
            if not field["list"]:
                add_value_constraint(
                    shapes, prop, field, name + "_" + key, profile["models"]
                )
                continue
            shapes.add((prop, SH.nodeKind, SH.BlankNodeOrIRI))
            list_shape = local(name + "_" + key + "_List")
            shapes.add((prop, SH.node, list_shape))
            star = BNode(name + "_" + key + "_rest")
            shapes.add((star, SH.zeroOrMorePath, RDF.rest))
            item = local(name + "_" + key + "_Item")
            shapes.add((list_shape, SH.property, item))
            shapes.add(
                (
                    item,
                    SH.path,
                    sequence(shapes, [star, RDF.first], name + "_" + key + "_items"),
                )
            )
            add_value_constraint(
                shapes,
                item,
                {**field, "list": False},
                name + "_" + key + "_value",
                profile["models"],
            )
            for bound, count in [
                ("minimum", field["minimum_items"]),
                ("maximum", field["maximum_items"]),
            ]:
                if count is None or (bound == "minimum" and count == 0):
                    continue
                node = local(name + "_" + key + "_" + bound)
                position = count - 1 if bound == "minimum" else count
                path = (
                    RDF.first
                    if position == 0
                    else sequence(
                        shapes,
                        [RDF.rest] * position + [RDF.first],
                        name + "_" + key + "_" + bound + "_path",
                    )
                )
                shapes.add((list_shape, SH.property, node))
                shapes.add((node, SH.path, path))
                shapes.add(
                    (
                        node,
                        SH.minCount if bound == "minimum" else SH.maxCount,
                        Literal(1 if bound == "minimum" else 0),
                    )
                )
            for position, bounds in enumerate(field["positions"]):
                node = local(name + "_" + key + "_position_" + str(position))
                shapes.add((list_shape, SH.property, node))
                shapes.add(
                    (
                        node,
                        SH.path,
                        RDF.first
                        if position == 0
                        else sequence(
                            shapes,
                            [RDF.rest] * position + [RDF.first],
                            name + "_" + key + "_position_path_" + str(position),
                        ),
                    )
                )
                add_value_constraint(
                    shapes,
                    node,
                    {
                        **field,
                        "list": False,
                        "constraint": {"type": "number", **bounds},
                    },
                    name + "_" + key + "_position_" + str(position),
                    profile["models"],
                )
        # Reification does not assert the subject/predicate/object triple.
        if name in ("SharedFact", "SourcedRelation"):
            for key, pred in [
                ("assertion_predicate", RDF.predicate),
                ("assertion_object", RDF.object),
            ]:
                if name == "SourcedRelation" and pred == RDF.object:
                    continue
                scoped[key] = {
                    "@id": str(pred),
                    **({"@type": "@id"} if pred == RDF.predicate else {}),
                }
                prop = local(name + "_" + key + "_Shape")
                shapes.add((shape, SH.property, prop))
                shapes.add((prop, SH.path, pred))
                shapes.add((prop, SH.minCount, Literal(1)))
                shapes.add((prop, SH.maxCount, Literal(1)))
                if pred == RDF.predicate:
                    shapes.add((prop, SH.nodeKind, SH.IRI))
                else:
                    shapes.add((prop, SH.datatype, RDF.JSON))
        if name == "SharedFact":
            # An ordered citation locator is not a RiC-O RecordResource. Keep it in a
            # local list property; connect the source-scoped Relation to each Source.
            predicate = URIRef(expand("rico:isEvidencedBy"))
            scoped["evidence_sources"] = {
                "@id": str(predicate),
                "@type": "@id",
                "@container": "@set",
            }
            prop = local(name + "_evidence_sources_Shape")
            shapes.add((shape, SH.property, prop))
            shapes.add((prop, SH.path, predicate))
            shapes.add((prop, SH.minCount, Literal(1)))
            add_value_constraint(
                shapes,
                prop,
                {"target": "Source", "nested": None},
                name + "_evidence_sources",
                profile["models"],
            )
        if name == "SharedEvent":
            for value in profile["vocabularies"]["EventParts"]["values"]:
                role = value["value"]
                predicate = URIRef(
                    expand(
                        next(
                            m["term"]
                            for m in value["mappings"]
                            if m["kind"] == "meaning"
                        )
                    )
                )
                scoped["role_" + role] = {
                    "@id": str(predicate),
                    "@type": "@id",
                    "@container": "@set",
                }
                prop = local(name + "_role_" + role + "_Shape")
                shapes.add((shape, SH.property, prop))
                shapes.add((prop, SH.path, predicate))
                add_value_constraint(
                    shapes,
                    prop,
                    {"target": "SharedPerson", "nested": None},
                    name + "_role_" + role,
                    profile["models"],
                )
            predicate = URIRef(expand("rico:hasEventType"))
            scoped["event_type"] = {"@id": str(predicate), "@type": "@id"}
            prop = local(name + "_event_type_Shape")
            shapes.add((shape, SH.property, prop))
            shapes.add((prop, SH.path, predicate))
            shapes.add((prop, SH.minCount, Literal(1)))
            shapes.add((prop, SH.maxCount, Literal(1)))
            types = [
                URIRef(
                    expand(
                        next(m["term"] for m in v["mappings"] if m["kind"] == "meaning")
                    )
                )
                for v in profile["vocabularies"]["EventTypes"]["values"]
            ]
            shapes.add((prop, SH["in"], sequence(shapes, types, name + "_event_types")))
            for kind in types:
                ontology.add((kind, RDF.type, URIRef(expand("rico:EventType"))))
        context[name] = {"@id": str(cls), "@context": scoped}
    context["Reference"] = {
        "@id": str(local("Reference")),
        "@context": {"target_model": str(local("target_model"))},
    }
    for term, kind, reason in [
        (
            local("Reference"),
            OWL.Class,
            "A target identifier present in the final public data; no private identity details are supplied.",
        ),
        (
            local("target_model"),
            RDF.Property,
            "The expected kind of a public reference whose details are outside this export.",
        ),
    ]:
        ontology.add((term, RDF.type, kind))
        ontology.add((term, RDFS.comment, Literal(reason)))
    refshape, refprop = local("Reference_Shape"), local("Reference_property")
    shapes.add((refshape, RDF.type, SH.NodeShape))
    shapes.add((refshape, SH.targetClass, local("Reference")))
    shapes.add((refshape, SH.closed, Literal(True)))
    shapes.add((refshape, SH.ignoredProperties, ignored))
    shapes.add((refshape, SH.property, refprop))
    shapes.add((refprop, SH.path, local("target_model")))
    shapes.add((refprop, SH.minCount, Literal(1)))
    shapes.add((refprop, SH.maxCount, Literal(1)))
    shapes.add((refprop, SH.datatype, XSD.string))
    # Each fact-kind predicate is deliberately distinct from an unqualified date/place predicate.
    for value in profile["vocabularies"]["FactTypes"]["values"]:
        term = local("assertion_" + value["value"])
        ontology.add((term, RDF.type, RDF.Property))
        ontology.add(
            (
                term,
                RDFS.comment,
                Literal(
                    "A source-scoped "
                    + value["value"]
                    + " assertion. Its object is the preserved statement value, not an unqualified date or historical event. "
                    + value["description"]
                ),
            )
        )
        for m in value["mappings"]:
            ontology.add((term, RDFS.seeAlso, URIRef(expand(m["term"]))))
    return {
        "context.jsonld": json.dumps(
            {"@context": context}, ensure_ascii=False, indent=2, sort_keys=True
        ),
        "ontology.ttl": triples(ontology),
        "shapes.ttl": triples(shapes),
    }


def write_rdf(linkml_dir, destination, index, contract, write_text):
    config_path = linkml_dir / "rdf-profile.yaml"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    profile = make_profile(index, config, contract)
    profile["profile_sha256"] = hashlib.sha256(config_path.read_bytes()).hexdigest()
    profile["index_sha256"] = (
        hashlib.sha256((destination / "docs/model-index.json").read_bytes()).hexdigest()
        if (destination / "docs/model-index.json").exists()
        else hashlib.sha256(
            (linkml_dir / "generated/docs/model-index.json").read_bytes()
        ).hexdigest()
    )
    vocabulary_path = linkml_dir.parent / "vocabulary/profile.ttl"
    profile["source_sha256"] = {
        **profile["source_sha256"],
        "vocabulary/profile.ttl": hashlib.sha256(
            vocabulary_path.read_bytes()
        ).hexdigest(),
    }
    outputs = make_artifacts(profile)
    # Reuse the approved role/type declarations with their exact domain, range and reason.
    vocab = Graph().parse(vocabulary_path, format="turtle")
    ontology = Graph().parse(data=outputs["ontology.ttl"], format="turtle")
    for kind in ("EventParts", "EventTypes"):
        for value in profile["vocabularies"][kind]["values"]:
            term = URIRef(
                expand(
                    next(m["term"] for m in value["mappings"] if m["kind"] == "meaning")
                )
            )
            for triple in vocab.triples((term, None, None)):
                ontology.add(triple)
    outputs["ontology.ttl"] = triples(ontology)
    outputs["profile.json"] = json.dumps(
        profile, ensure_ascii=False, indent=2, sort_keys=True
    )
    lines = [
        "# Public RDF view coverage",
        "",
        "Generated from the LinkML model index and `rdf-profile.yaml`. Every model and field has an explicit export or omission decision. This is the project’s public-view profile, not EHRI ingestion conformance.",
        "",
        "Literal formats are checked with an enabled JSON Schema FormatChecker as well as SHACL patterns. RDF lists are checked for structure, order, length and position; arbitrary list cycles are rejected by the runtime before SHACL. Scalar and list constraints come from generated field shapes; position bounds come from the existing Zod tuple contract, cited in the profile.",
        "",
    ]
    for name, model in profile["models"].items():
        lines += [
            "## " + name,
            "",
            model["reason"],
            "",
            "| Field | Export predicate or omission |",
            "|---|---|",
        ]
        lines += [
            f"| `{key}` | `{f['predicate']}` |" for key, f in model["fields"].items()
        ]
        lines += [
            f"| `{key}` | Omitted: {why} |" for key, why in model["omitted"].items()
        ]
        lines += [
            "",
            *[
                f"Public optional field `{key}`: {why}"
                for key, why in model["optional"].items()
            ],
            *[
                f"Public required field `{key}`: {why}"
                for key, why in model["required"].items()
            ],
            "",
        ]
    lines += ["## Models outside this view", ""] + [
        f"- `{name}`: {why}" for name, why in profile["omitted_models"].items()
    ]
    outputs["coverage.md"] = "\n".join(lines) + "\n"
    profile["artifacts_sha256"] = {
        name: hashlib.sha256(content.rstrip().encode() + b"\n").hexdigest()
        for name, content in outputs.items()
        if name != "profile.json"
    }
    outputs["profile.json"] = json.dumps(
        profile, ensure_ascii=False, indent=2, sort_keys=True
    )
    for name, content in outputs.items():
        write_text(destination / "rdf" / name, content)
