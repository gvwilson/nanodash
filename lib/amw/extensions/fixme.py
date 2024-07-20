"""Handle notes about work in progress in AMW theme."""

import shortcodes
import util


@shortcodes.register("fixme")
def fixme(pargs, kwargs, node):
    """Leave a note to self.

    Usage: [%fixme "some message" %]

    Multi-word messages must be quoted to form a single parameter.
    """
    util.require(
        (len(pargs) == 1) and (not kwargs),
        f"Bad 'fixme' in {node.path}: '{pargs}' and '{kwargs}'",
    )
    return f'<p class="fixme">FIXME: {util.markdownify(pargs[0])}</p>'
