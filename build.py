# build script to convert JSON-LD classes into single ontology file.

import pathlib
import rdflib

pathway = pathlib.Path.cwd() / 'classes'
classes = sorted([x for x in pathway.iterdir() if x.suffix == '.json'])

graph = rdflib.Graph()

ont = rdflib.URIRef('https://fiafcore.org/ontology/')
graph.add((ont, rdflib.RDF.type, rdflib.OWL.Ontology))
graph.add((ont, rdflib.URIRef('http://purl.org/dc/elements/1.1/title'), rdflib.Literal('FIAFcore')))
graph.add((ont, rdflib.URIRef('http://purl.org/dc/elements/1.1/contributor'), rdflib.Literal('Paul Duchesne')))
graph.add((ont, rdflib.OWL.versionInfo, rdflib.Literal('0.02')))

for c in classes:
    ontology_path = pathlib.Path.cwd() / 'FIAFcore.ttl'
    graph += rdflib.Graph().parse(file=open(str(c), "r"), format='json-ld')

save_path = pathlib.Path.cwd() / 'FIAFcore.ttl'
graph.serialize(destination=str(save_path), format="turtle")
print(len(graph), 'triples.')