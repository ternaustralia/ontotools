from rdflib import Graph, Namespace


TERN = Namespace("https://w3id.org/tern/ontologies/tern/")


def serialize(graph: Graph) -> str:
    # Reading files overrides pre-bound prefixes in RDFLib graphs.
    # This serialize function will bind the prefixes before serializing
    graph.bind("tern", TERN)
    return graph.serialize(format="longturtle")
