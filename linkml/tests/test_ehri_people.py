"""Both unchanged EHRI person shapes, on the pilot and fictional controls.

Read 2026-10-31: https://github.com/linkml/PyShEx/tree/v0.9.0
and https://github.com/RDFLib/pySHACL/tree/v0.30.1 (Python APIs).
These validators are already in linkml/requirements.lock. No JVM is needed.
"""

import importlib.util
import json
import sys
import unittest

from pyshacl import validate
from pyshex import ShExEvaluator
from rdflib import Graph, Literal, Namespace, RDF, URIRef

from support import ROOT

PIN = ROOT / "standards/ehri-people-1.1-1c2325f9"
EHRI = Namespace("http://lod.ehri-project-test.eu/ontology#")
RICO = Namespace("https://www.ica.org/standards/RiC/ontology#")


def pilot_module(name):
    path = ROOT / "pilots/sourced-entities" / (name + ".py")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


build = pilot_module("build")
cases = pilot_module("contract_cases")


class EhriPeople(unittest.TestCase):
    def check_both(self, graph, good):
        focuses = list(graph.subjects(RDF.type, EHRI.Person))
        self.assertTrue(focuses, "an empty graph proves nothing")
        shacl, _, _ = validate(
            graph,
            shacl_graph=str(PIN / "people.shacl.ttl"),
            inference="none",
            advanced=False,
            js=False,
            do_owl_imports=False,
        )
        results = ShExEvaluator(
            rdf=graph,
            schema=(PIN / "people.shex").read_text(encoding="utf-8"),
            focus=focuses,
            start=str(EHRI.Person),
        ).evaluate()
        self.assertEqual(len(results), len(focuses))
        self.assertEqual(bool(shacl), good)
        self.assertEqual(all(r.result for r in results), good)

    def test_pilot_people_conform_without_changing_pending_assertions(self):
        graph = Graph().parse(
            data=json.dumps(build.rico_export(build.make_pilot())), format="json-ld"
        )
        self.assertEqual(len(set(graph.subjects(RDF.type, EHRI.Person))), 12)
        self.check_both(graph, True)
        self.assertFalse(list(graph.triples((None, RICO.hasDeathDate, None))))

    def test_fictional_pilot_and_each_original_fault(self):
        document = build.rico_export(cases.synthetic())
        baseline = Graph().parse(data=json.dumps(document), format="json-ld")
        self.check_both(baseline, True)
        person = next(baseline.subjects(RDF.type, EHRI.Person))
        for fault in ("missing-name", "extra-type", "two-names", "language-name"):
            graph = Graph() + baseline
            if fault == "missing-name":
                graph.remove((person, RICO.name, None))
            elif fault == "extra-type":
                graph.add((person, RDF.type, RICO.Person))
            elif fault == "two-names":
                graph.add((person, RICO.name, Literal("Another fictional name")))
            else:
                graph.set((person, RICO.name, Literal("Fictional name", lang="en")))
            with self.subTest(fault=fault):
                self.check_both(graph, False)

    def test_nested_names_dates_and_upstream_address_stem(self):
        # EHRI's ShEx inverse edges require its own address stem. These are
        # fictional validator controls, never identifiers minted by our exporter.
        person = URIRef("http://lod.ehri-project-test.eu/vocabularies/ehri-pers/fictional")
        graph = Graph()
        graph.add((person, RDF.type, EHRI.Person))
        graph.add((person, RICO.name, Literal("Fictional person")))
        for kind, shape in (
            (EHRI.AlternateAgentName, "alternate"),
            (EHRI.ParallelAgentName, "parallel"),
        ):
            name = URIRef("https://example.org/" + shape)
            graph.add((person, RICO.hasOrHadAgentName, name))
            graph.add((name, RDF.type, kind))
            graph.add((name, RICO.name, Literal("Fictional " + shape)))
            graph.add((name, RICO.isOrWasAgentNameOf, person))
        date = URIRef("https://example.org/date")
        graph.add((person, RICO.hasBirthDate, date))
        graph.add((date, RDF.type, RICO.Date))
        graph.add((date, RICO.normalizedDateValue, Literal("1900")))
        graph.add((date, RICO.isBirthDateOf, person))
        self.check_both(graph, True)
        for predicate in (RICO.normalizedDateValue, RICO.isOrWasAgentNameOf):
            broken = Graph() + graph
            subject = next(broken.subjects(predicate))
            broken.remove((subject, predicate, None))
            with self.subTest(predicate=predicate):
                self.check_both(broken, False)
        # Do not pretend SHACL's IRI-only inverse rule checks the ShEx stem.
        broken = Graph() + graph
        name = next(broken.subjects(RICO.isOrWasAgentNameOf))
        broken.set((name, RICO.isOrWasAgentNameOf, URIRef("https://example.org/our-person")))
        results = ShExEvaluator(
            rdf=broken,
            schema=(PIN / "people.shex").read_text(),
            focus=[person],
            start=str(EHRI.Person),
        ).evaluate()
        self.assertFalse(all(r.result for r in results))
