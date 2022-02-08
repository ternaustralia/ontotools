from typing import Tuple


def normalize(content) -> Tuple[str, bool]:
    original_content = content.strip()
    # sort the file based on lines
    lines = sorted(original_content.split("\n"))
    new_content = "\n".join(lines).strip()
    changed = original_content != new_content
    return new_content, changed
