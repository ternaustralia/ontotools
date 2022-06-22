from typing import Tuple

from rdflib import Graph

from ontotools.graph import serialize


def normalize_old(content: str) -> Tuple[str, bool]:
    """This is no longer used. Only suitable for N-Triples content

    Issue is blank node IDs are not preserved when using applications
    such as TopBraid Composer.
    """
    original_content = content.strip()
    # sort the file based on lines
    lines = sorted(original_content.split("\n"))
    new_content = "\n".join(lines).strip()
    changed = original_content != new_content
    return new_content, changed


def get_topbraid_metadata(content: str) -> str:
    """Get the TopBraid Composer metadata at the top of an ontology file."""
    lines = content.split("\n")
    comments = []
    for line in lines:
        if line.startswith("#"):
            comments.append(line)
        else:
            break

    if comments:
        return "\n".join(comments) + "\n"
    else:
        return ""


def normalize(content: str) -> Tuple[str, bool]:
    metadata = get_topbraid_metadata(content)

    g = Graph()
    g.parse(data=content, format="turtle")
    new_content = serialize(g)
    new_content = metadata + new_content
    changed = content != new_content
    return new_content, changed
