import sys

import typer

from ontotools.functions.normalize_dir import normalize_dir, FailOnChangeError
from ontotools.logging import logger

app = typer.Typer()


@app.command()
def normalize(
    directory: str = typer.Argument(
        ..., help="The directory of Turtle files to be normalized"
    ),
    check: bool = typer.Option(
        False, help="Check what files will be normalized without applying the effect."
    ),
):
    """Normalizes the format of Turtle files in a given directory."""
    try:
        normalize_dir(directory, check)
    except FailOnChangeError as err:
        logger.error(err)
        sys.exit(1)
