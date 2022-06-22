from rdflib import Graph

from ontotools.graph import serialize


def test_graph_has_prefix_bindings():
    graph = Graph()

    content = """    
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX ns1: <https://w3id.org/tern/ontologies/tern/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <https://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

<https://linked.data.gov.au/def/test/dawe-cv/08429fce-4d70-4be4-9c64-ffc80f554ea7>
    a skos:Concept ;
    rdfs:isDefinedBy <https://linked.data.gov.au/def/nrm> ;
    skos:definition "Accuracy of fire event is an estimate of the time and date accuracy of the fire event, which is normally an estimate and/or cited from the most reliable source/s. It can range from hours to days to months or years." ;
    skos:prefLabel "accuracy of the fire" ;
    schema:url "https://github.com/ternaustralia/dawe-rlp-vocabs/tree/master/vocab_files/attribute_concepts/accuracy-of-the-fire.ttl" ;
    ns1:valueType ns1:DateTime ;
.
    """

    graph.parse(data=content, format="turtle")
    output = serialize(graph)
    assert "PREFIX tern: <https://w3id.org/tern/ontologies/tern/>" in output
