from pathlib import Path

from ontotools.functions.normalize_file import normalize_file, FailOnChangeError
from ontotools.logging import logger


def normalize_dir(path: Path, fail_if_changed: bool):
    path = Path(path).resolve()

    files = list(path.glob("**/*.ttl"))

    changed_files = []

    for file in files:
        try:
            changed = normalize_file(file, fail_if_changed, False)

            if changed:
                changed_files.append(file)
        except FailOnChangeError:
            changed_files.append(file)

    if fail_if_changed:
        raise FailOnChangeError(
            f"{len(changed_files)} out of {len(files)} files will change."
        )
    else:
        logger.info("%s out of %s files changed.", len(changed_files), len(files))
