"""Unchanged EHRI corporate-body shapes on fictional validator controls.

Read 2026-10-31: EHRI/ehri-kg-mapping src/shapes/1.1/cb.{shacl.ttl,shex}
at 1c2325f9d2267a8a0c639cd041be54ec9a73e517; validator APIs at
https://github.com/RDFLib/pySHACL/tree/v0.30.1 and
https://github.com/linkml/PyShEx/blob/v0.9.0/pyshex/shex_evaluator.py.
"""

import unittest

from pyshacl import validate
from pyshex import ShExEvaluator
from rdflib import Graph, Literal, Namespace, RDF, URIRef

from support import ROOT

PIN = ROOT / "standards/ehri-cb-1.1-1c2325f9"
EHRI = Namespace("http://lod.ehri-project-test.eu/ontology#")
RICO = Namespace("https://www.ica.org/standards/RiC/ontology#")
BODY = URIRef("https://example.org/fictional-society")


def fictional(identifier=BODY):
    graph = Graph()
    graph.add((identifier, RDF.type, EHRI.CorporateBody))
    graph.add((identifier, RICO.name, Literal("Fictional reading society", lang="und")))
    return graph


class EhriCorporateBodies(unittest.TestCase):
    def check_both(self, graph, shacl_good, shex_good=None):
        focuses = list(graph.subjects(RDF.type, EHRI.CorporateBody))
        self.assertTrue(focuses, "an empty graph proves nothing")
        conforms, _, _ = validate(
            graph,
            shacl_graph=str(PIN / "cb.shacl.ttl"),
            inference="none",
            advanced=False,
            js=False,
            do_owl_imports=False,
        )
        results = ShExEvaluator(
            rdf=graph,
            schema=(PIN / "cb.shex").read_text(encoding="utf-8"),
            focus=focuses,
            start=str(EHRI.CBAndFamily),
        ).evaluate()
        self.assertEqual(len(results), len(focuses))
        self.assertEqual({r.focus for r in results}, set(focuses))
        self.assertEqual(bool(conforms), shacl_good)
        self.assertEqual(all(r.result for r in results), shacl_good if shex_good is None else shex_good)

    def test_fictional_corporate_body_and_each_fault(self):
        self.check_both(fictional(), True)
        for fault in ("missing-name", "plain-name", "two-names", "extra-type", "literal-link"):
            graph = fictional()
            if fault == "missing-name":
                graph.remove((BODY, RICO.name, None))
            elif fault == "plain-name":
                graph.set((BODY, RICO.name, Literal("Fictional society")))
            elif fault == "two-names":
                graph.add((BODY, RICO.name, Literal("Another name", lang="en")))
            elif fault == "extra-type":
                graph.add((BODY, RDF.type, RICO.CorporateBody))
            else:
                graph.add((BODY, Namespace("http://www.w3.org/2000/01/rdf-schema#").seeAlso, Literal("bad")))
            with self.subTest(fault=fault):
                self.check_both(graph, False)

    def test_nested_names_dates_and_upstream_address_stem(self):
        # These EHRI-stem addresses are fictional upstream validator controls,
        # never identifiers minted by the Pruzhany exporter.
        inverse = URIRef("http://lod.ehri-project-test.eu/vocabularies/ehri-cb/fictional")
        graph = fictional(inverse)
        for kind, suffix in ((EHRI.AlternateAgentName, "other"), (EHRI.ParallelAgentName, "parallel")):
            name = URIRef("https://example.org/" + suffix)
            graph.add((inverse, RICO.hasOrHadAgentName, name))
            graph.add((name, RDF.type, kind))
            graph.add((name, RICO.name, Literal("Fictional " + suffix)))
            graph.add((name, RICO.isOrWasAgentNameOf, inverse))
        date = URIRef("https://example.org/date")
        graph.add((inverse, RICO.hasBeginningDate, date))
        graph.add((date, RDF.type, RICO.Date))
        graph.add((date, RICO.normalizedDateValue, Literal("1900")))
        graph.add((date, RICO.isBeginningDateOf, inverse))
        self.check_both(graph, True)
        for predicate in (RICO.normalizedDateValue, RICO.isOrWasAgentNameOf):
            broken = Graph() + graph
            subject = next(broken.subjects(predicate))
            broken.remove((subject, predicate, None))
            with self.subTest(predicate=predicate):
                self.check_both(broken, False)
        broken = Graph() + graph
        broken.set((date, RICO.isBeginningDateOf, BODY))
        self.check_both(broken, True, False)
