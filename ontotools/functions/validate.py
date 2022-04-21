from json import JSONDecodeError
from xml.sax._exceptions import SAXParseException

from rdflib import Graph
from rdflib.plugins.parsers import notation3
from rdflib.exceptions import ParserError


class RDFSyntaxError(Exception):
    def __init__(self, format_: str) -> None:
        super().__init__()
        self.format = format_


def validate_syntax(data: str, format_: str) -> bool:
    """Checks if rdflib can parse the data.

    Returns True on success, else False.
    """
    g = Graph()

    try:
        g.parse(data=data, format=format_)
    except (
        notation3.BadSyntax,
        SAXParseException,
        JSONDecodeError,
        ParserError,
        Exception,
    ) as err:
        raise RDFSyntaxError(format_) from err

    return True
