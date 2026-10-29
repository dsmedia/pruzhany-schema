"""Encode an explicitly projected public view. Never read private archive records here.

JSON-LD 1.1 type-scoped contexts and @list: https://www.w3.org/TR/json-ld11/
SHACL Core and pySHACL 0.30.1's validate API: https://github.com/RDFLib/pySHACL
Checked against installed locked libraries on 2026-10-29. No remote contexts or imports.
"""

import hashlib
import json
import math
import runpy
from pathlib import Path
from urllib.parse import quote, urlsplit

from jsonschema import Draft201909Validator, FormatChecker
from pyshacl import validate
from rdflib import Graph, Literal, RDF, URIRef

PC = "https://pruzhany.org/ns/sourced-entities#"


def encoded(value):
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def sha(value):
    return hashlib.sha256(value).hexdigest()


def base_iri(value):
    parsed = urlsplit(value)
    if (
        parsed.scheme != "https"
        or not parsed.hostname
        or parsed.username
        or parsed.password
        or parsed.query
        or parsed.fragment
        or not value.endswith("/")
        or any(c.isspace() for c in value)
        or not value.isascii()
    ):
        raise ValueError(
            "base IRI must be an explicit ASCII HTTPS address ending in /, without credentials, query or fragment"
        )
    Draft201909Validator(
        {"type": "string", "format": "uri"}, format_checker=FormatChecker()
    ).validate(value)
    return value


def load_bundle(schema):
    folder = Path(schema) / "linkml"
    profile = json.loads(
        (folder / "generated/rdf/profile.json").read_text(encoding="utf-8")
    )
    for name, digest in profile["source_sha256"].items():
        # The documentation index records paths relative to the repository.
        if sha((folder.parent / name).read_bytes()) != digest:
            raise ValueError("stale RDF definition: " + name)
    for path, digest in [
        ("rdf-profile.yaml", profile["profile_sha256"]),
        ("generated/contract.json", profile["contract_sha256"]),
        ("generated/docs/model-index.json", profile["index_sha256"]),
    ]:
        if sha((folder / path).read_bytes()) != digest:
            raise ValueError("stale RDF profile: " + path)
    for name, digest in profile["artifacts_sha256"].items():
        if sha((folder / "generated/rdf" / name).read_bytes()) != digest:
            raise ValueError("stale RDF artifact: " + name)
    backend = runpy.run_path(str(folder / "rdf_generator.py"))
    expected = backend["make_profile"](
        json.loads(
            (folder / "generated/docs/model-index.json").read_text(encoding="utf-8")
        ),
        json.loads((folder / "rdf-profile.yaml").read_text(encoding="utf-8")),
        json.loads((folder / "generated/contract.json").read_text(encoding="utf-8")),
    )
    expected["source_sha256"]["vocabulary/profile.ttl"] = sha(
        (folder.parent / "vocabulary/profile.ttl").read_bytes()
    )
    if any(profile.get(key) != value for key, value in expected.items()):
        raise ValueError("stale generated RDF profile; regenerate from the definition")
    context = json.loads(
        (folder / "generated/rdf/context.jsonld").read_text(encoding="utf-8")
    )
    return profile, context["@context"], folder / "generated/rdf/shapes.ttl"


class Encoder:
    """Identifiers remain exact literals; IRIs encode them reversibly and never join names."""

    def __init__(self, profile, context, base):
        self.profile, self.context, self.base = profile, context, base_iri(base)
        self.nodes, self.models, self.references = {}, {}, {}
        self.validators = {}
        for model, definition in profile["models"].items():
            for key, field in definition["fields"].items():
                self.validators[model, key] = Draft201909Validator(
                    field["constraint"], format_checker=FormatChecker()
                )

    def iri(self, identifier):
        if not isinstance(identifier, str) or not identifier.strip():
            raise ValueError("empty or non-string stored identifier")
        return self.base + "id/" + quote(identifier, safe="")

    def derived(self, parent, field, value):
        return self.base + "node/" + sha(encoded([parent, field, value]).encode())

    def reference(self, identifier, target):
        iri = self.iri(identifier)
        if iri in self.references and self.references[iri] != target:
            raise ValueError("identifier has conflicting target kinds: " + identifier)
        self.references[iri] = target
        return {"@id": iri}

    def literal(self, model, key, field, value):
        errors = list(self.validators[model, key].iter_errors(value))
        if (
            errors
            or value is None
            or isinstance(value, float)
            and not math.isfinite(value)
        ):
            raise ValueError(
                f"{model}.{key}: invalid literal {errors[0].message if errors else 'null/non-finite'}"
            )
        return value

    def value(self, model, key, field, value, parent):
        if field["target"]:
            self.literal(model, key, field, value)
            return self.reference(value, field["target"])
        if field["nested"]:
            return {
                "@id": self.add(
                    field["nested"], value, self.derived(parent, key, value)
                )
            }
        if field["json"]:
            if not isinstance(value, dict) or not all(
                isinstance(k, str) and isinstance(v, str) for k, v in value.items()
            ):
                raise ValueError(f"{model}.{key}: expected string-map qualifiers")
            return {"@value": value, "@type": "@json"}
        return self.literal(model, key, field, value)

    def add(self, model, value, iri=None):
        definition = self.profile["models"][model]
        if not isinstance(value, dict) or set(value) - set(definition["fields"]):
            raise ValueError(f"{model}: unknown fields or non-object")
        missing = [
            k
            for k, f in definition["fields"].items()
            if f["required"] and k not in value
        ]
        if missing:
            raise ValueError(f"{model}: missing required fields {missing}")
        iri = iri or self.iri(value["id"])
        if iri in self.models:
            if self.models[iri] != (model, value):
                raise ValueError("conflicting public definitions of " + iri)
            return iri
        self.models[iri] = model, value
        node = {"@id": iri, "@type": [model, *definition["types"]]}
        for key, original in value.items():
            field = definition["fields"][key]
            if field["list"]:
                if (
                    not isinstance(original, list)
                    or len(original) < field["minimum_items"]
                    or field["maximum_items"] is not None
                    and len(original) > field["maximum_items"]
                ):
                    raise ValueError(f"{model}.{key}: invalid list length")
                for index, bounds in enumerate(field["positions"]):
                    if index >= len(original):
                        raise ValueError(
                            f"{model}.{key}: missing tuple position {index}"
                        )
                    Draft201909Validator({"type": "number", **bounds}).validate(
                        original[index]
                    )
                node[key] = [self.value(model, key, field, v, iri) for v in original]
            else:
                node[key] = self.value(model, key, field, original, iri)
        if model == "SharedEvent":
            terms = {
                v["value"]: v
                for v in self.profile["vocabularies"]["EventTypes"]["values"]
            }
            term = next(
                m["term"]
                for m in terms[value["type"]]["mappings"]
                if m["kind"] == "meaning"
            )
            prefix, suffix = term.split(":", 1)
            node["event_type"] = self.context[prefix] + suffix
            for role in self.profile["vocabularies"]["EventParts"]["values"]:
                people = sorted(
                    {
                        self.iri(p["person_id"])
                        for p in value["main_people"]
                        if p["part"] == role["value"]
                    }
                )
                if people:
                    node["role_" + role["value"]] = people
        if model == "SharedFact":
            node["evidence_sources"] = sorted(
                {self.iri(c["source_id"]) for c in value["citations"]}
            )
            node["assertion_predicate"] = PC + "export_assertion_" + value["type"]
            # Reify the complete public claim; "perished" is not a death date.
            payload = {
                k: v
                for k, v in value.items()
                if k not in ("id", "subject_id", "citations", "attribution", "review")
            }
            node["assertion_object"] = {"@value": payload, "@type": "@json"}
        if model == "SourcedRelation":
            terms = {
                v["value"]: v
                for v in self.profile["vocabularies"]["RelationshipTypes"]["values"]
            }
            term = terms[value["relationship_type"]]
            meaning = next(
                m["term"] for m in term["mappings"] if m["kind"] == "meaning"
            )
            prefix, name = meaning.split(":", 1)
            node["assertion_predicate"] = self.context[prefix] + name
        self.nodes[iri] = node
        return iri

    def document(self):
        for iri, target in self.references.items():
            if iri in self.models:
                if self.models[iri][0] != target:
                    raise ValueError("reference points at the wrong model: " + iri)
            else:
                self.nodes[iri] = {
                    "@id": iri,
                    "@type": "Reference",
                    "target_model": target,
                }
        return {
            "@context": self.context,
            "@graph": [self.nodes[k] for k in sorted(self.nodes)],
        }


def check_lists(graph):
    """SHACL property paths do not reject cycles or multiple rest edges on their own."""
    cells = set(graph.subjects(RDF.first)) | set(graph.subjects(RDF.rest))
    if RDF.nil in cells:
        raise ValueError("rdf:nil must not have first/rest edges")
    done = {RDF.nil}
    for start in cells:
        path, node = set(), start
        while node not in done:
            if node in path:
                raise ValueError("cyclic RDF list")
            path.add(node)
            first, rest = (
                list(graph.objects(node, RDF.first)),
                list(graph.objects(node, RDF.rest)),
            )
            if len(first) != 1 or len(rest) != 1 or isinstance(rest[0], Literal):
                raise ValueError("malformed RDF list")
            node = rest[0]
        done.update(path)


def check_terms(graph, profile):
    """Check formats, reference-only kind tags and reification semantics after parsing."""
    allowed = {URIRef(m["iri"]): (name, m) for name, m in profile["models"].items()}
    allowed[URIRef(PC + "export_Reference")] = ("Reference", {"fields": {}})
    described = set()
    relations = {
        v["value"]: v for v in profile["vocabularies"]["RelationshipTypes"]["values"]
    }
    for cls, (name, model) in allowed.items():
        for node in graph.subjects(RDF.type, cls):
            described.add(node)
            for key, field in model["fields"].items():
                values = list(graph.objects(node, URIRef(field["predicate"])))
                if field["list"]:
                    for head in values:
                        if head != RDF.nil and (head, RDF.first, None) not in graph:
                            raise ValueError("missing RDF list cell")
                elif field["constraint"].get("format"):
                    validator = Draft201909Validator(
                        field["constraint"], format_checker=FormatChecker()
                    )
                    for value in values:
                        validator.validate(str(value))
            if name == "SharedEvent":
                heads = graph.objects(
                    node, URIRef(model["fields"]["main_people"]["predicate"])
                )
                participants = [p for head in heads for p in graph.items(head)]
                fields = profile["models"]["LifeEventMainPerson"]["fields"]
                for role in profile["vocabularies"]["EventParts"]["values"]:
                    term = next(
                        m["term"] for m in role["mappings"] if m["kind"] == "meaning"
                    )
                    wanted = {
                        graph.value(p, URIRef(fields["person_id"]["predicate"]))
                        for p in participants
                        if str(graph.value(p, URIRef(fields["part"]["predicate"])))
                        == role["value"]
                    }
                    if (
                        set(graph.objects(node, URIRef(PC + term.removeprefix("pc:"))))
                        != wanted
                    ):
                        raise ValueError(
                            "event role edges differ from its ordered participants"
                        )
                kind = str(
                    graph.value(node, URIRef(model["fields"]["type"]["predicate"]))
                )
                types = {
                    v["value"]: v
                    for v in profile["vocabularies"]["EventTypes"]["values"]
                }
                term = next(
                    m["term"] for m in types[kind]["mappings"] if m["kind"] == "meaning"
                )
                if set(
                    graph.objects(
                        node,
                        URIRef(
                            "https://www.ica.org/standards/RiC/ontology#hasEventType"
                        ),
                    )
                ) != {URIRef(PC + term.removeprefix("pc:"))}:
                    raise ValueError("event type differs from its stated kind")
            if name in ("SharedFact", "SourcedRelation"):
                kind_key = "type" if name == "SharedFact" else "relationship_type"
                kind = str(
                    graph.value(node, URIRef(model["fields"][kind_key]["predicate"]))
                )
                if name == "SharedFact":
                    expected = PC + "export_assertion_" + kind
                    citation_heads = graph.objects(
                        node, URIRef(model["fields"]["citations"]["predicate"])
                    )
                    cited = {
                        source
                        for head in citation_heads
                        for citation in graph.items(head)
                        for source in graph.objects(
                            citation,
                            URIRef(
                                profile["models"]["Citation"]["fields"]["source_id"][
                                    "predicate"
                                ]
                            ),
                        )
                    }
                    evidence = set(
                        graph.objects(
                            node,
                            URIRef(
                                "https://www.ica.org/standards/RiC/ontology#isEvidencedBy"
                            ),
                        )
                    )
                    if cited != evidence:
                        raise ValueError(
                            "evidence source edges differ from citation locators"
                        )
                else:
                    term = next(
                        m["term"]
                        for m in relations[kind]["mappings"]
                        if m["kind"] == "meaning"
                    )
                    expected = (
                        "https://www.ica.org/standards/RiC/ontology#"
                        + term.removeprefix("rico:")
                    )
                if set(graph.objects(node, RDF.predicate)) != {URIRef(expected)}:
                    raise ValueError("assertion predicate differs from its stated kind")
    cells = set(graph.subjects(RDF.first))
    if set(graph.subjects()) - described - cells:
        raise ValueError("export contains an unprofiled node")


def check_graph(document, shapes, profile=None):
    """No inference, remote contexts, JS, imports or EHRI ingestion validation."""
    if not isinstance(document.get("@context"), dict):
        raise ValueError("export requires its inline generated context")
    graph = Graph().parse(data=encoded(document), format="json-ld")
    if not len(graph):
        raise ValueError("empty export graph")
    check_lists(graph)
    if profile is None:
        profile = json.loads(
            (Path(shapes).parent / "profile.json").read_text(encoding="utf-8")
        )
    check_terms(graph, profile)
    conforms, _, report = validate(
        graph,
        shacl_graph=str(shapes),
        inference="none",
        advanced=False,
        js=False,
        do_owl_imports=False,
    )
    if not conforms:
        raise ValueError("public export SHACL failed:\n" + str(report)[:12000])
    return {
        "conforms": True,
        "triples": len(graph),
        "nodes": len(document["@graph"]),
        "profile": "Pruzhany public view; not EHRI ingestion acceptance",
    }
