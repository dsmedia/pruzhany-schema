"""Expose upstream faults without repairing the pin or claiming conformance.

Read 31 October 2026: EHRI/ehri-kg-mapping src/shapes/1.1 at 1c2325f9;
https://github.com/linkml/PyShEx (0.9.0 evaluator). Fictional controls only.
"""

import unittest

from pyshex import ShExEvaluator
from rdflib import Graph, Literal, Namespace, RDF, URIRef

from support import ROOT

PIN = ROOT / "standards/ehri-holdings-1.1-1c2325f9"
EHRI = Namespace("http://lod.ehri-project-test.eu/ontology#")
RICO = Namespace("https://www.ica.org/standards/RiC/ontology#")


class HoldingShapes(unittest.TestCase):
    def test_unchanged_shacl_is_unparseable_not_a_passing_check(self):
        for name in ("holdings", "repositories"):
            with self.subTest(pin=name), self.assertRaises(SyntaxError):
                Graph().parse(PIN / (name + ".shacl.ttl"), format="turtle")

    def test_repository_shex_accepts_name_and_refuses_missing_name(self):
        holder = URIRef("https://example.org/fictional-holder")
        graph = Graph()
        graph.add((holder, RDF.type, EHRI.Institution))
        graph.add((holder, RICO.name, Literal("Fictional Library", lang="en")))
        shape = (PIN / "repositories.shex").read_text()
        self.assertTrue(
            ShExEvaluator(rdf=graph, schema=shape, focus=holder, start=str(EHRI.Institution))
            .evaluate()[0]
            .result
        )
        graph.remove((holder, RICO.name, None))
        self.assertFalse(
            ShExEvaluator(rdf=graph, schema=shape, focus=holder, start=str(EHRI.Institution))
            .evaluate()[0]
            .result
        )

    def test_holding_shex_requires_ehri_holder_stem(self):
        holding = URIRef("https://example.org/fictional-paper")
        graph = Graph()
        graph.add((holding, RDF.type, EHRI.RecordSet))
        graph.add((holding, RICO.title, Literal("Fictional Paper", lang="en")))
        graph.add((holding, RICO.hasOrHadHolder, URIRef("https://example.org/fictional-holder")))
        shape = (PIN / "holdings.shex").read_text()
        self.assertFalse(
            ShExEvaluator(rdf=graph, schema=shape, focus=holding, start=str(EHRI.Holding))
            .evaluate()[0]
            .result
        )
        # Validator control only. The export must never invent this address.
        graph.set(
            (
                holding,
                RICO.hasOrHadHolder,
                URIRef("http://lod.ehri-project-test.eu/institutions/fictional"),
            )
        )
        self.assertTrue(
            ShExEvaluator(rdf=graph, schema=shape, focus=holding, start=str(EHRI.Holding))
            .evaluate()[0]
            .result
        )
