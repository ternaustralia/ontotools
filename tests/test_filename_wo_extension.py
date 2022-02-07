from ontotools.utils import get_filename_without_extension


def test_filename_wo_extension():
    files = (
        ("ontology.nt", "ontology"),
        ("ontology.shacl.nt", "ontology.shacl"),
        ("ontology.1.0.0.nt", "ontology.1.0.0"),
    )

    for file in files:
        assert get_filename_without_extension(file[0]) == file[1]
