"""Utilities for AMW theme."""

import markdown
import re
import sys


# Match inside HTML paragraph markers.
INSIDE_PARAGRAPH = re.compile(r"<p>(.+?)</p>", re.DOTALL)

# Markdown extensions.
MD_EXTENSIONS = [
    "markdown.extensions.extra",
    "markdown.extensions.smarty"
]


def allowed(kwargs, allowed):
    """Check that dictionary keys are a subset of those allowed."""
    return set(kwargs.keys()).issubset(allowed)


def fail(msg):
    """Fail unilaterally."""
    warn(msg)
    raise AssertionError(msg)


def markdownify(text, strip_p=True):
    """Convert Markdown to HTML."""
    result = markdown.markdown(text, extensions=MD_EXTENSIONS)
    if strip_p and result.startswith("<p>"):
        result = INSIDE_PARAGRAPH.match(result).group(1)
    return result


def require(cond, msg):
    """Fail if condition untrue."""
    if not cond:
        fail(msg)


def warn(msg):
    """Print warning message."""
    print(msg, file=sys.stderr)
