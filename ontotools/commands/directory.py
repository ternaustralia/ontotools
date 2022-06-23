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
    fail_if_changed: bool = typer.Option(False, help="Fail if files would changed"),
):
    """Normalizes the format of Turtle files in a given directory."""
    try:
        normalize_dir(directory, fail_if_changed)
    except FailOnChangeError as err:
        logger.error(err)
        sys.exit(1)
