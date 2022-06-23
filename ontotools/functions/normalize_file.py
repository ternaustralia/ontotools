import pathlib

from rdflib import Graph

from ontotools.logging import logger
from ontotools.functions.normalize import normalize
from ontotools.utils import get_filename_without_extension


class FailOnChangeError(Exception):
    """File changed due to normalization function."""

    pass


def normalize_file(
    filename: pathlib.Path,
    fail_if_changed: bool,
    generate_formats: bool,
    output_filename: pathlib.Path = None,
) -> bool:
    # Ensure the file exists.
    path = pathlib.Path(filename).resolve()
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path.absolute()}")

    with open(path, "r", encoding="utf-8") as fread:
        content = fread.read()

        content, changed = normalize(content)
        if changed:
            if fail_if_changed:
                raise FailOnChangeError(f"The file {path} contains changes that can be normalized.")
            else:
                logger.info("The file %s has been normalized.", path)

            # Didn't fail and file has changed, so write to file.
            with open(
                output_filename if output_filename else path, "w", encoding="utf-8"
            ) as fwrite:
                fwrite.write(content)

    if generate_formats:
        logger.info("Writing Turtle file to N-Triples, N3, RDF/XML and JSON-LD.")
        graph = Graph()
        graph.parse(data=content, format="turtle")

        formats = (
            ("nt", "nt"),
            ("n3", "n3"),
            ("xml", "xml"),
            ("json-ld", "jsonld"),
        )
        for format_ in formats:
            filename_without_file_extension = get_filename_without_extension(
                output_filename if output_filename else path
            )
            logger.info("Writing %s.%s", filename_without_file_extension, format_[1])
            graph.serialize(
                f"{filename_without_file_extension}.{format_[1]}", format=format_[0]
            )

    return changed
