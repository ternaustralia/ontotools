import pytest

from ontotools.functions.validate import validate_syntax, SyntaxError


def test_validate_syntax_pass():
    data = "<a> <b> <c> ."

    assert validate_syntax(data, "turtle")


def test_validate_syntax_fail():
    data = "<a> <b> <c>"

    with pytest.raises(SyntaxError):
        assert validate_syntax(data, "turtle")
