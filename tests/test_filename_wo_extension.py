import pytest

from ontotools.utils import get_filename_without_extension


@pytest.mark.parametrize(
    "filename,expected",
    [
        ("ontology.nt", "ontology"),
        ("ontology.shacl.nt", "ontology.shacl"),
        ("ontology.1.0.0.nt", "ontology.1.0.0"),
        ("/workspaces/ontotools/ontology.nt", "/workspaces/ontotools/ontology"),
    ],
)
def test_filename_wo_extension(filename, expected):
    assert get_filename_without_extension(filename) == expected
