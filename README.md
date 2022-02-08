# Ontotools

The tool currently normalises ontologies in the N-Triples format for version control. It sorts the N-Triples file and removes empty lines.

## Example usage

```bash
$ ontotools file normalize --help
Usage: ontotools file normalize [OPTIONS] FILENAME

Arguments:
  FILENAME  The N-Triples file to be normalized  [required]

Options:
  --fail-if-changed / --no-fail-if-changed
                                  Fail if the file was changed  [default: no-
                                  fail-if-changed]
  --generate-formats / --no-generate-formats
                                  Generate other RDF formats (ttl, n3, xml,
                                  jsonld)  [default: no-generate-formats]
  --help                          Show this message and exit.
```

## Contact

Edmond Chuc  
e.chuc@uq.edu.au
