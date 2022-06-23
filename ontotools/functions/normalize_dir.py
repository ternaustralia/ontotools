from pathlib import Path

from ontotools.functions.normalize_file import normalize_file, FailOnChangeError
from ontotools.logging import logger


def normalize_dir(path: Path, check: bool):
    path = Path(path).resolve()

    files = list(path.glob("**/*.ttl"))

    changed_files = []

    for file in files:
        try:
            changed = normalize_file(file, check, False)

            if changed:
                changed_files.append(file)
        except FailOnChangeError as err:
            logger.info(err)
            changed_files.append(file)

    if check:
        raise FailOnChangeError(
            f"{len(changed_files)} out of {len(files)} files will change."
        )
    else:
        logger.info("%s out of %s files changed.", len(changed_files), len(files))
