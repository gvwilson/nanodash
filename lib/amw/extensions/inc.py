"""Manage file inclusions."""

import ark
import re
import shortcodes

import util


MULTI = re.compile(r'^(.+?).\[(.+?)\]$')


@shortcodes.register("inc")
def inclusion(pargs, kwargs, node):
    """Show code-formatted link to external file.

    Usage: [%inc filename %] or [%inc stem.[py,html,txt] %]
    """
    util.require(
        (len(pargs) == 1) and (not kwargs),
        f"Bad 'incref' shortcode: must have one file expression not '{pargs}' and '{kwargs}'",
    )
    m = MULTI.match(pargs[0])
    if not m:
        return _fmt(pargs[0])
    stem = m.group(1)
    extensions = (ext.strip() for ext in m.group(2).split(","))
    return ", ".join(_fmt(f"{stem}.{ext}") for ext in extensions)


def _fmt(path):
    """Format a single filename for display."""
    return f'<a href="./{path}"><code>{path}</code></a>'
