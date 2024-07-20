"""Processing filters used by AMW theme."""

import ark
import util

EXCLUSIONS = {
    "__pycache__",
}


@ark.filters.register(ark.filters.Filter.LOAD_NODE_DIR)
def keep_dir(value, path):
    """Do not process directories excluded by parent."""
    return path.name not in EXCLUSIONS


@ark.filters.register(ark.filters.Filter.LOAD_NODE_FILE)
def keep_file(value, path):
    """Only process .md Markdown files."""
    return path.suffix == ".md"
