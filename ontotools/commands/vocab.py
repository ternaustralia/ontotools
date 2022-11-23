import pathlib
from typing import List, Optional

import httpx
import typer
from jinja2 import Template
from rdflib import Graph, URIRef, Literal, SKOS, DCTERMS, SDO, XSD

app = typer.Typer()


def _get_uris(
    concept_scheme: str, sparql_endpoint: str, named_graph: Optional[str] = None
) -> List[str]:
    template_query = Template(
        """
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT *
        WHERE {
            {% if named_graph %}
            GRAPH <{{ named_graph }}> {
                ?id skos:inScheme <{{ concept_scheme }}> .
            }
            {% else %}
            ?id skos:inScheme <{{ concept_scheme }}> .
            {% endif %}
        }
        """
    )
    query = template_query.render(
        concept_scheme=concept_scheme, named_graph=named_graph
    )

    response = httpx.post(
        url=sparql_endpoint,
        data=query,
        headers={
            "content-type": "application/sparql-query",
            "accept": "application/sparql-results+json",
        },
    )
    response.raise_for_status()

    data = response.json()

    concepts = [item["id"]["value"] for item in data["results"]["bindings"]]

    uris = []
    uris.append(concept_scheme)
    uris += concepts
    return uris


def _get_data(
    uris: List[str], sparql_endpoint: str, named_graph: Optional[str] = None
) -> Graph:
    template_query = Template(
        """
        CONSTRUCT {
            ?s ?p ?o .
        }
        WHERE {
            VALUES (?s) {
                {% for uri in uris %}
                (<{{ uri }}>)
                {% endfor %}
            }

            {% if named_graph %}
            GRAPH <{{ named_graph }}> {
                ?s ?p ?o .
            }
            {% else %}
            ?s ?p ?o .
            {% endif %}
        }
        """
    )
    query = template_query.render(uris=uris, named_graph=named_graph)

    response = httpx.post(
        url=sparql_endpoint,
        data=query,
        headers={
            "content-type": "application/sparql-query",
            "accept": "application/n-triples",
        },
    )
    response.raise_for_status()

    data = response.text
    return Graph().parse(data=data, format="application/n-triples")


def bind_namespaces(graph: Graph):
    graph.bind("skos", SKOS)
    graph.bind("dcterms", DCTERMS)
    graph.bind("schema", SDO)


def get_label(uri: str, graph: Graph) -> str:
    template_query = Template(
        """
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT *
        WHERE {
            <{{ uri }}> skos:prefLabel ?label .
            FILTER(lang(?label) = "en" || lang(?label) = "")
        }
        """
    )
    query = template_query.render(uri=uri)
    result = list(graph.query(query))
    if result:
        label: str = result[0]["label"]
        return label.replace(" ", "-").lower()
    else:
        raise RuntimeError(f"Failed to find label for {uri}")


@app.command()
def init(
    directory: str = typer.Argument(
        ..., help="The directory of the output files in RDF Turtle."
    ),
    concept_scheme: str = typer.Argument(..., help="The IRI of the concept scheme."),
    sparql_endpoint: str = typer.Argument(
        ..., help="The SPARQL endpoint containing the concept scheme."
    ),
    named_graph: str = typer.Argument(
        None, help="The named graph containing the concept scheme."
    ),
    github_url: str = typer.Argument(
        None,
        help="The base GitHub URL to be added to each resource. E.g., https://github.com/ternaustralia/dawe-rlp-vocabs/tree/main/vocab_files/",
    ),
):
    output_path = pathlib.Path(directory).resolve()

    print("Directory:", output_path)
    print("Concept scheme:", concept_scheme)
    print("SPARQL endpoint:", sparql_endpoint)
    print("Named graph:", named_graph)

    uris = _get_uris(concept_scheme, sparql_endpoint, named_graph)
    graph = _get_data(uris, sparql_endpoint)

    bind_namespaces(graph)

    for uri in uris:
        cbd = graph.cbd(URIRef(uri))
        bind_namespaces(cbd)
        label = get_label(uri, cbd) + ".ttl"
        if github_url:
            cbd.add(
                (URIRef(uri), SDO.url, Literal(github_url + label, datatype=XSD.anyURI))
            )
        cbd.serialize(output_path / label, format="longturtle")
