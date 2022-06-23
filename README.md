# Ontotools

The tool currently normalises ontologies in the Turtle format for version control. It uses the `longturtle` serializer format from Python's RDFLib.

## Example usage

```bash
$ ontotools file normalize --help
Usage: ontotools file normalize [OPTIONS] FILENAME [OUTPUT_FILENAME]

Arguments:
  FILENAME           The Turtle file to be normalized  [required]
  [OUTPUT_FILENAME]  Output filename

Options:
  --check / --no-check            Check if the file will change without
                                  applying the effect  [default: no-check]
  --generate-formats / --no-generate-formats
                                  Generate other RDF formats (nt, n3, xml,
                                  jsonld)  [default: no-generate-formats]
  --help                          Show this message and exit.
```

## Development

Install the project in editable mode.

```
pip install -e .
```

### Run tests

```
pytest
```

## Contact

Edmond Chuc  
e.chuc@uq.edu.au
