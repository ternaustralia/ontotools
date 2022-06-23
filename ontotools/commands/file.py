import pathlib
import sys
from typing import Optional

import typer

from ontotools.logging import logger
from ontotools.functions.normalize_file import normalize_file, FailOnChangeError
from ontotools.functions.validate import validate_syntax, RDFSyntaxError

app = typer.Typer()


@app.command()
def normalize(
    filename: str = typer.Argument(..., help="The Turtle file to be normalized"),
    output_filename: Optional[str] = typer.Argument(None, help="Output filename"),
    check: bool = typer.Option(
        False, help="Check if the file will change without applying the effect"
    ),
    generate_formats: bool = typer.Option(
        False, help="Generate other RDF formats (nt, n3, xml, jsonld)"
    ),
):
    try:
        normalize_file(
            filename, check, generate_formats, output_filename=output_filename
        )
    except (FileNotFoundError, FailOnChangeError) as err:
        logger.error(err)
        sys.exit(1)


@app.command()
def validate(
    filename: str = typer.Argument(
        ..., help="The file to be validated for syntax errors"
    ),
    fileformat: str = typer.Option(
        "turtle", help="The format of the file to be validated"
    ),
):
    # Ensure the file exists.
    path = pathlib.Path(filename).resolve()
    if not path.exists():
        logger.error("File '%s' does not exist.", filename)
        sys.exit(1)

    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()

        try:
            validate_syntax(data, fileformat)
            logger.info(
                "File '%s' with format '%s' parsed successfully with RDFLib.",
                filename,
                fileformat,
            )
        except RDFSyntaxError:
            logger.error(
                "File '%s' with format '%s' has syntax errors.", filename, fileformat
            )
            sys.exit(1)
        except Exception as err:
            logger.error("Unknown error has occurred.")
            logger.error(str(err))
            sys.exit(2)
