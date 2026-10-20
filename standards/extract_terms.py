"""Extract a pinned ontology; run with rdflib==7.1.4 (no imports are fetched)."""
import argparse
import hashlib
import json
from pathlib import Path
from rdflib import Graph, URIRef, RDF, RDFS, OWL


def extract(path, repo, commit, source_path):
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
            "sha256": hashlib.sha256(raw).hexdigest(), "read_on": "2026-10-20",
            "namespace": namespace, "ontology_metadata": metadata,
            "license_and_attribution": attribution,
            "terms": sorted(terms, key=lambda t: (t["iri"], t["kind"]))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ontology", type=Path)
    for name in ("repo", "commit", "path", "out"):
        parser.add_argument("--" + name, required=True)
    args = parser.parse_args()
    result = extract(args.ontology, args.repo, args.commit, args.path)
    Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
