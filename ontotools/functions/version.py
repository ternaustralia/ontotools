from typing import Optional

from rdflib import Graph, OWL


def get_version_info(g: Graph):
    for _, _, version_info in g.triples((None, OWL.versionInfo, None)):
        return version_info


def compare(version: str, content: str, content_type: str = "turtle") -> Optional[bool]:
    """Compare the version of the ontology and the content.

    Assumes only one owl:versionInfo in the content.

    Returns None if no version info was found. Otherwise returns True if
    the versions match, else False.
    """

    g = Graph()
    g.parse(data=content, format=content_type)

    version_info = get_version_info(g)

    if version_info is None:
        return None
    else:
        return str(version_info.toPython()) == str(version)
