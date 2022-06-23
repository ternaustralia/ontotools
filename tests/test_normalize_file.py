from pathlib import Path

import pytest

from ontotools.functions.normalize_file import (
    normalize_file,
    FailOnChangeError,
    normalize,
)

parent_path = Path(__file__).resolve().parent
data_path = parent_path / "data"


@pytest.fixture
def output_path():
    path = parent_path / "output_dir"
    path.mkdir(exist_ok=True)
    yield path

    # Clean up.
    files = [file for file in path.glob("**/*")]
    for file in files:
        file.unlink()
    path.rmdir()


@pytest.fixture
def filepath():
    return data_path / "not_normalized_file.ttl"


def test_normalize_file_not_found():
    with pytest.raises(FileNotFoundError):
        normalize_file(data_path / "non_existent_file.ttl", False, False)


def test_normalize_with_fail_flag_will_raise(filepath: Path):
    with pytest.raises(FailOnChangeError):
        normalize_file(filepath, True, False)


def test_normalize_file(filepath: Path, output_path: Path):
    output_file = output_path / "output.ttl"
    normalize_file(filepath, False, False, output_filename=output_file)

    with open(output_file, "r", encoding="utf-8") as f:
        output_content = f.read()
        _, changed = normalize(output_content)
        assert not changed


def test_normalize_file_generate_formats(filepath: Path, output_path: Path):
    output_file = output_path / "output.ttl"
    normalize_file(filepath, False, True, output_filename=output_file)

    files = [file for file in output_path.iterdir() if file.is_file()]

    assert len(files) == 5
    assert output_path / "output.ttl" in files
    assert output_path / "output.nt" in files
    assert output_path / "output.n3" in files
    assert output_path / "output.jsonld" in files
    assert output_path / "output.xml" in files
