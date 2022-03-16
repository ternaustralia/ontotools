from ontotools.functions.version import compare


def test_compare_true():
    content = """
        <https://w3id.org/tern/ontologies/tern/> <http://www.w3.org/2002/07/owl#versionInfo> "0.4.0" .
    """
    result = compare("0.4.0", content)
    assert result == True


def test_compare_false():
    content = """
        <https://w3id.org/tern/ontologies/tern/> <http://www.w3.org/2002/07/owl#versionInfo> "0.4.0" .
    """
    result = compare("0.3.0", content)
    assert result == False


def test_compare_not_found():
    content = ""
    result = compare("0.4.0", content)
    assert result is None
