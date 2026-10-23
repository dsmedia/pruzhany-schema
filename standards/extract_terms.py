"""Extract a pinned ontology; run with rdflib==7.1.4 (no imports are fetched)."""
import argparse
import hashlib
import json
from pathlib import Path
from rdflib import Graph, URIRef, RDF, RDFS, OWL
from rdflib.collection import Collection


def extract(path, repo, commit, source_path, read_on):
    raw = path.read_bytes()
    graph = Graph().parse(data=raw, format="xml")
    ontologies = sorted(graph.subjects(RDF.type, OWL.Ontology), key=str)
    namespace = ("http://lod.ehri-project-test.eu/ontology#" if "EHRI" in repo
                 else "https://www.ica.org/standards/RiC/ontology#")
    kinds = {OWL.Class: "class", OWL.ObjectProperty: "object property",
             OWL.DatatypeProperty: "datatype property", OWL.AnnotationProperty: "annotation property"}
    terms = []
    for kind, label in kinds.items():
        for term in graph.subjects(RDF.type, kind):
            if not isinstance(term, URIRef) or not str(term).startswith(namespace):
                continue
            entry = {"iri": str(term), "kind": label,
                     "label": sorted(str(v) for v in graph.objects(term, RDFS.label) if v.language == "en")}
            if "EHRI" in repo:
                for predicate, key in ((RDFS.subClassOf, "superclasses"), (RDFS.subPropertyOf, "superproperties")):
                    entry[key] = sorted(str(v) for v in graph.objects(term, predicate) if isinstance(v, URIRef))
            terms.append(entry)
    metadata = {}
    for ontology in ontologies:
        metadata[str(ontology)] = {str(p): sorted(str(v) for v in graph.objects(ontology, p))
                                   for p in sorted(set(graph.predicates(ontology)), key=str)}
    attribution = sorted({str(v) for s, p, v in graph if any(
        token in str(p).lower() for token in ("license", "licence", "rights", "creator", "contributor", "publisher"))})
    return {"repo": repo, "commit": commit, "path": source_path,
            "sha256": hashlib.sha256(raw).hexdigest(), "read_on": read_on,
            "namespace": namespace, "ontology_metadata": metadata,
            "license_and_attribution": attribution,
            "terms": sorted(terms, key=lambda t: (t["iri"], t["kind"]))}


CHARACTERISTICS = {OWL.SymmetricProperty: "symmetric", OWL.TransitiveProperty: "transitive",
                   OWL.FunctionalProperty: "functional", OWL.InverseFunctionalProperty: "inverse functional",
                   OWL.AsymmetricProperty: "asymmetric", OWL.IrreflexiveProperty: "irreflexive",
                   OWL.ReflexiveProperty: "reflexive"}
CARDINALITIES = {OWL.minQualifiedCardinality: "min", OWL.maxQualifiedCardinality: "max",
                 OWL.qualifiedCardinality: "exactly"}


def extract_axioms(path, repo, commit, source_path, read_on):
    """The ontology's own axioms on its terms, as stated: never inferred, closed or completed."""
    raw = path.read_bytes()
    graph = Graph().parse(data=raw, format="xml")
    namespace = "https://www.ica.org/standards/RiC/ontology#"

    def named(node):
        if not isinstance(node, URIRef):
            raise ValueError(f"unexpected anonymous node in {source_path}")
        return str(node)

    def alternatives(node):
        # A domain or range is one class, or a union of classes (any of them).
        if isinstance(node, URIRef):
            return [str(node)]
        members = graph.value(node, OWL.unionOf)
        if members is None or len(set(graph.predicates(node)) - {RDF.type, OWL.unionOf}):
            raise ValueError(f"unexpected class expression in {source_path}")
        return sorted(named(m) for m in Collection(graph, members))

    axioms = []
    for term in sorted({s for s in graph.subjects() if isinstance(s, URIRef) and str(s).startswith(namespace)}, key=str):
        entry = {}
        for predicate, key in ((RDFS.domain, "domain"), (RDFS.range, "range")):
            values = list(graph.objects(term, predicate))
            if len(values) > 1:
                raise ValueError(f"{term}: more than one {key} statement")
            if values:
                entry[key] = alternatives(values[0])
        supers = {"superclasses": [], "superproperties": [], "cardinalities": []}
        for value in graph.objects(term, RDFS.subClassOf):
            if isinstance(value, URIRef):
                supers["superclasses"].append(str(value))
                continue
            counts = [(CARDINALITIES[p], int(graph.value(value, p))) for p in CARDINALITIES if graph.value(value, p) is not None]
            if len(counts) != 1 or graph.value(value, OWL.onProperty) is None or graph.value(value, OWL.onClass) is None:
                raise ValueError(f"{term}: unexpected superclass expression")
            supers["cardinalities"].append({"on_property": named(graph.value(value, OWL.onProperty)),
                                            "on_class": alternatives(graph.value(value, OWL.onClass)), counts[0][0]: counts[0][1]})
        supers["superproperties"] = [named(v) for v in graph.objects(term, RDFS.subPropertyOf)]
        for key, values in supers.items():
            if values:
                entry[key] = sorted(values, key=lambda v: json.dumps(v, sort_keys=True))
        for predicate, key in ((OWL.inverseOf, "inverse_of"), (OWL.disjointWith, "disjoint_with")):
            values = sorted(named(v) for v in graph.objects(term, predicate))
            if values:
                entry[key] = values
        characteristics = sorted(CHARACTERISTICS[t] for t in graph.objects(term, RDF.type) if t in CHARACTERISTICS)
        if characteristics:
            entry["characteristics"] = characteristics
        chains = sorted([named(p) for p in Collection(graph, chain)] for chain in graph.objects(term, OWL.propertyChainAxiom))
        if chains:
            entry["property_chains"] = chains
        selves = []
        for value in graph.objects(term, OWL.equivalentClass):
            if isinstance(value, URIRef) or graph.value(value, OWL.hasSelf) is None:
                raise ValueError(f"{term}: unexpected equivalent class")
            selves.append(named(graph.value(value, OWL.onProperty)))
        if selves:
            # RiC-O's rolification: the Relation class is what this property relates to itself.
            entry["rolified_by"] = sorted(selves)
        if entry:
            axioms.append({"iri": str(term), **entry})
    return {"repo": repo, "commit": commit, "path": source_path,
            "sha256": hashlib.sha256(raw).hexdigest(), "read_on": read_on, "namespace": namespace,
            "axioms": axioms}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ontology", type=Path)
    for name in ("repo", "commit", "path", "read-on", "out"):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--axioms", action="store_true", help="write the RiC-O axioms list instead of the terms list")
    args = parser.parse_args()
    make = extract_axioms if args.axioms else extract
    result = make(args.ontology, args.repo, args.commit, args.path, args.read_on)
    Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
