"""Migrate the legacy ND.owl into an ODK edit file (as RDF/XML; ROBOT converts it to OFN).

What changes, and nothing else:
1. The ontology header is replaced: the IRI becomes http://purl.obolibrary.org/obo/nd.owl,
   the broken legacy owl:imports are replaced by the ODK import modules, and the
   description, licence, contributors and comment are carried over as dcterms annotations.
2. IRIs written with the typo base "http://purl.obolibrary.obo/obo/" are rewritten to
   "http://purl.obolibrary.org/obo/". These are 59 ND classes (ND_0008000-ND_0008063).

All other triples are copied unchanged, including annotations and axioms on external terms
and the local ND# classes and properties. Those are left for separate, reviewed changes.
"""
import sys

import rdflib
from rdflib import DCTERMS, OWL, RDF, RDFS, Literal, URIRef

LEGACY, OUT = sys.argv[1], sys.argv[2]
DC = rdflib.Namespace("http://purl.org/dc/elements/1.1/")
OLD_ONT = URIRef("http://purl.obolibrary.org/obo/ND")
NEW_ONT = URIRef("http://purl.obolibrary.org/obo/nd.owl")
IMPORTS = ["bfo", "fma", "iao", "ncbitaxon", "obi", "ogms", "pr", "ro", "uberon"]
BAD, GOOD = "http://purl.obolibrary.obo/obo/", "http://purl.obolibrary.org/obo/"

g = rdflib.Graph()
g.parse(LEGACY, format="xml")
before = len(g)

# Header: read what we keep, then drop every triple about the old ontology node.
description = next(g.objects(OLD_ONT, DC.description))
comment = next(g.objects(OLD_ONT, RDFS.comment))
contributors = list(g.objects(OLD_ONT, DC.contributor))
licence = next(g.objects(OLD_ONT, DC.license))
assert str(licence) == "http://creativecommons.org/licenses/by/4.0/", licence
header = list(g.triples((OLD_ONT, None, None)))
assert not list(g.triples((None, None, OLD_ONT))), "old ontology IRI is used as an object"
for t in header:
    g.remove(t)

# Typo IRIs: rename everywhere, refusing to merge into an IRI that already exists.
def fix(term):
    if isinstance(term, URIRef) and str(term).startswith(BAD):
        return URIRef(GOOD + str(term)[len(BAD):])
    return term

existing = set(g.all_nodes()) | set(g.predicates())
renamed = {t for t in existing if isinstance(t, URIRef) and str(t).startswith(BAD)}
collisions = {fix(t) for t in renamed} & existing
assert not collisions, f"typo fix would merge with existing IRIs: {sorted(collisions)[:5]}"
for s, p, o in list(g):
    ns, np_, no = fix(s), fix(p), fix(o)
    if (ns, np_, no) != (s, p, o):
        g.remove((s, p, o))
        g.add((ns, np_, no))

# Relations used in owl:equivalentProperty axioms must be declared, or the OWL parser drops
# the axiom. The legacy file relied on its (now unloadable) imports for those declarations.
typed = {s for s, o in g.subject_objects(RDF.type)
         if o in (OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)}
declared = set()
for a, b in g.subject_objects(OWL.equivalentProperty):
    for side in (a, b):
        if side not in typed:
            g.add((side, RDF.type, OWL.ObjectProperty))
            declared.add(side)
print(f"object property declarations added for equivalence axioms: {len(declared)}")

# New header.
g.add((NEW_ONT, RDF.type, OWL.Ontology))
for name in IMPORTS:
    g.add((NEW_ONT, OWL.imports, URIRef(f"http://purl.obolibrary.org/obo/nd/imports/{name}_import.owl")))
g.add((NEW_ONT, DCTERMS.title, Literal("Neurological Disease Ontology")))
g.add((NEW_ONT, DCTERMS.description, Literal(str(description))))
g.add((NEW_ONT, DCTERMS.license, URIRef("https://creativecommons.org/licenses/by/4.0/")))
for c in contributors:
    g.add((NEW_ONT, DCTERMS.contributor, Literal(str(c))))
g.add((NEW_ONT, RDFS.comment, Literal(str(comment), lang="en")))
for p in (DCTERMS.title, DCTERMS.description, DCTERMS.license, DCTERMS.contributor):
    g.add((p, RDF.type, OWL.AnnotationProperty))

g.serialize(OUT, format="xml")
print(f"legacy triples {before}; header triples removed {len(header)}; "
      f"typo IRIs renamed {len(renamed)}; contributors {len(contributors)}; output triples {len(g)}")
