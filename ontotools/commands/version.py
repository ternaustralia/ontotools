import sys

import typer

from ontotools.logging import logger
from ontotools.functions.version import compare as compare_func

app = typer.Typer()


@app.command()
def compare(
    version: str = typer.Argument(..., help="The version to compare"),
    filename: str = typer.Argument(..., help="The Turtle file with the version info"),
):
    """Exits with status code 1 if the version is not the same or version info is not found."""

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        result = compare_func(version, content)

        if result is None:
            logger.error("No version info found.")
            sys.exit(1)
        elif result is False:
            logger.error("The version is not the same.")
            sys.exit(1)
        elif result is True:
            logger.info("The version is the same.")
        else:
            raise RuntimeError(f"Unexpected result. Got {type(result)}.")
