from typing import Tuple


def normalize_old(file_name) -> bool:
    with open(file_name, "r") as fread:
        original_content = fread.read()
        lines = original_content.strip()
        # sort the file based on lines
        lines = sorted(lines.split("\n"))

        new_content = "\n".join(lines).strip()

        changed = original_content != new_content

        with open(file_name, "w") as f:
            f.write(new_content)

        return changed


def normalize(content) -> Tuple[str, bool]:
    original_content = content.strip()
    # sort the file based on lines
    lines = sorted(original_content.split("\n"))
    new_content = "\n".join(lines).strip()
    changed = original_content != new_content
    return new_content, changed
