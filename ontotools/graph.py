from rdflib import Graph, Namespace


TERN = Namespace("https://w3id.org/tern/ontologies/tern/")
URNC = Namespace("urn:class:")
URNP = Namespace("urn:property:")


def serialize(graph: Graph) -> str:
    # Reading files overrides pre-bound prefixes in RDFLib graphs.
    # This serialize function will bind the prefixes before serializing
    graph.bind("tern", TERN)
    graph.bind("urnc", URNC)
    graph.bind("urnp", URNP)
    return graph.serialize(format="longturtle")
