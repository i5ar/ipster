from __future__ import (unicode_literals, absolute_import, print_function)

from warnings import warn

from ipster.since_5 import IPsterPrompts


def load_ipython_extension(ipython):
    """Load IPster prompt.

    Like running ``c.TerminalInteractiveShell.prompts_class = IPsterPrompts``
    from the config file.
    """
    ipython.prompts_class = IPsterPrompts
    ipython.prompts = IPsterPrompts(ipython)
    warn(DeprecationWarning(
        'The extension post_0_11 is deprecated since IPython 5.\n'
        'It is suggested to import the module directly:\n'
        '    from ipster.since_5 import IPsterPrompts\n'
        '    c.TerminalInteractiveShell.prompts_class = IPsterPrompts\n'))
