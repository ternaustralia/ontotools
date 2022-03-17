import pathlib

import typer
from rdflib import Graph

from ontotools.logging import logger
from ontotools.functions.normalize import normalize as normalize_func
from ontotools.utils import get_filename_without_extension
from ontotools.functions.validate import validate_syntax, SyntaxError

app = typer.Typer()


@app.command()
def normalize(
    filename: str = typer.Argument(..., help="The Turtle file to be normalized"),
    fail_if_changed: bool = typer.Option(False, help="Fail if the file was changed"),
    generate_formats: bool = typer.Option(
        False, help="Generate other RDF formats (nt, n3, xml, jsonld)"
    ),
):
    # Ensure the file exists.
    path = pathlib.Path(filename).resolve()
    if not path.exists():
        logger.error(f"File '{filename}' does not exist.")
        exit(1)

    with open(filename, "r") as fread:
        content = fread.read()

        content, changed = normalize_func(content)
        if changed:
            logger.info("The file has been normalized.")

            if fail_if_changed:
                logger.info("Exiting with status code 1 due to changed.")
                exit(1)

            # Didn't fail and file has changed, so write to file.
            with open(filename, "w") as fwrite:
                fwrite.write(content)

    if generate_formats:
        logger.info("Writing Turtle file to N-Triples, N3, RDF/XML and JSON-LD.")
        g = Graph()
        g.parse(data=content, format="turtle")

        formats = (
            ("nt", "nt"),
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


@app.command()
def validate(
    filename: str = typer.Argument(
        ..., help="The file to be validated for syntax errors"
    ),
    format: str = typer.Option("turtle", help="The format of the file to be validated"),
):
    # Ensure the file exists.
    path = pathlib.Path(filename).resolve()
    if not path.exists():
        logger.error(f"File '{filename}' does not exist.")
        exit(1)

    with open(filename, "r") as f:
        data = f.read()

        try:
            validate_syntax(data, format)
            logger.info(
                f"File '{filename}' with format '{format}' parsed successfully with RDFLib."
            )
        except SyntaxError:
            logger.error(f"File '{filename}' with format '{format}' has syntax errors.")
        except Exception as e:
            logger.error(f"Unknown error has occurred.")
            logger.error({e})
            exit(1)
