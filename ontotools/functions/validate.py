from json import JSONDecodeError
from rdflib import Graph
from rdflib.plugins.parsers import notation3
from rdflib.exceptions import ParserError
from xml.sax._exceptions import SAXParseException


class SyntaxError(Exception):
    def __init__(self, format: str) -> None:
        super().__init__()
        self.format = format


def validate_syntax(data: str, format: str) -> bool:
    """Checks if rdflib can parse the data.

    Returns True on success, else False.
    """
    g = Graph()

    try:
        g.parse(data=data, format=format)
    except (
        notation3.BadSyntax,
        SAXParseException,
        JSONDecodeError,
        ParserError,
        Exception,
    ):
        raise SyntaxError(format)

    return True
