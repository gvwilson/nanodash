"""Ark shortcode to include root Markdown files."""

import ark
from pathlib import Path
import re
import shortcodes
import util


# Level-1 Markdown heading.
FIRST_H1 = re.compile(r"^#\s+.+$", re.MULTILINE)


@shortcodes.register("rootfile")
def rootfile(pargs, kwargs, node):
    """Include a file from the root directory.

    Usage: [% rootfile FILE.md %] or [% rootfile FILE.md strip=False %].

    If `strip` is `True`, the first H1-style heading in the file is removed.
    """
    util.require(
        (len(pargs) == 1) and util.allowed(kwargs, {"strip"}, strict=False),
        f"Bad 'rootfile' in {node.path}: '{pargs}' and '{kwargs}'"
    )
    text = Path(ark.site.home(), pargs[0]).read_text()
    if kwargs.get("strip", 'True') == 'True' and text.startswith("#"):
        text = FIRST_H1.sub("", text)
    return text
