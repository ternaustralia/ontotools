import logging
import pathlib

import typer
from rdflib import Graph

from ontotools.normalize import normalize
from ontotools.utils import get_filename_without_extension


def main(
    filename: str = typer.Argument(..., help="The N-Triples file to be normalized"),
    fail_if_changed: bool = typer.Option(False, help="Fail if the file was changed"),
    generate_formats: bool = typer.Option(
        False, help="Generate other RDF formats (ttl, n3, xml, jsonld)"
    ),
):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Ensure the file exists.
    path = pathlib.Path(filename).resolve()
    if not path.exists():
        logger.error(f"File '{filename}' does not exist.")
        exit(1)

    with open(filename, "r") as fread:
        content = fread.read()

        content, changed = normalize(content)
        if changed:
            logger.info("The ontology has been normalized.")

            if fail_if_changed:
                logger.info("Exiting with status code 1 due to changed.")
                exit(1)

    with open(filename, "w") as fwrite:
        fwrite.write(content)

    if generate_formats:
        logger.info("Writing N-Triples file to Turtle, N3, RDF/XML and JSON-LD.")
        g = Graph()
        g.parse(data=content, format="nt")

        formats = (
            ("turtle", "ttl"),
            ("n3", "n3"),
            ("xml", "xml"),
            ("json-ld", "jsonld"),
        )
        for format in formats:
            filename_without_file_extension = get_filename_without_extension(filename)
            logger.info(f"Writing {filename_without_file_extension}.{format[1]}")
            g.serialize(
                f"{filename_without_file_extension}.{format[1]}", format=format[0]
            )


def run():
    typer.run(main)
