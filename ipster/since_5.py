"""IPster style and prompt.

Configuration required::

    ## Use 24bit colors instead of 256 colors in prompt highlighting.
    c.TerminalInteractiveShell.true_color = True

    ## Set the color scheme (NoColor, Neutral, Linux, or LightBG).
    c.InteractiveShell.colors = 'Linux'

"""
from __future__ import (unicode_literals, absolute_import)

import os
import sys

from pygments.token import (
    Token,
    # Keyword,
    # Name,
    # Comment,
    # String,
    # Error,
    # Number,
    # Operator,
    # Generic
)

from prompt_toolkit.layout.utils import token_list_width

from IPython.terminal.prompts import Prompts


class IPsterStyle(object):
    """Override prompt colors.

    Configuration example::

        from ipster.since_5 import IPsterStyle
        ipstyle = IPsterStyle()
        ipstyle_linux = ipstyle.overrides_linux()
        c.TerminalInteractiveShell.highlighting_style_overrides = ipstyle_linux

    """

    # TODO: Define Solarized colorscheme
    style_overrides_linux = {
        Token.IPsterPromptVirtualenv: 'bg:#859900 #073642',
        Token.IPsterPowerlinePromptVirtualenv: 'bg:#073642 #859900',
        Token.Prompt: 'bg:#073642 #839496',
        Token.PromptNum: 'bg:#073642 #859900 bold',
        Token.OutPrompt: 'bg:#073642 #839496',
        Token.OutPromptNum: 'bg:#073642 #dc322f bold',
        Token.IPsterPowerlinePrompt: '#073642',
        Token.IPsterPromptSpace: '#839496',
    }

    # TODO: Override NoColor, Neutral and LightBG prompt colors
    def overrides_linux(self):
        """Override prompt colors."""
        return self.style_overrides_linux


class IPsterPrompts(Prompts):
    """Prompt with Powerline patched font.

    .. _Configuration details:
        http://ipython.readthedocs.io/en/stable/config/details.html

    """
    def __init__(self, shell):
        self.shell = shell

        virtualenv = os.path.basename(os.path.normpath(sys.prefix))
        self.prompt_virtualenv = [
            (Token.IPsterPromptVirtualenv, ' \ue73c ' + virtualenv + ' '),
            (Token.IPsterPowerlinePromptVirtualenv, '\ue0b0'),
            (Token.Prompt, ' '),
        ]

    def is_venv(self):
        """Determine if running inside a virtual environment.

        .. _Determine virtual environment:
            https://stackoverflow.com/questions/1871549/

        """
        return (hasattr(sys, 'real_prefix') or (
            hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

    def add_segment(self, pt):
        """Add Virtual Environments segment if activated."""
        if self.is_venv():
            prompt_ipster_main = self.prompt_virtualenv + pt
        else:
            # prompt_ipster_main = pt
            prompt_ipster_main = [(Token.Prompt, ' '), ] + pt
        return prompt_ipster_main

    def in_prompt_tokens(self, cli=None):
        # return [(Token, os.getcwd()), (Token.Prompt, ' >>>')]
        prompt_in = [
            (Token.Prompt, 'In ['),
            (Token.PromptNum, str(self.shell.execution_count)),
            (Token.Prompt, '] '),
            (Token.IPsterPowerlinePrompt, '\ue0b0'),
            (Token.IPsterPromptSpace, ' ')
        ]
        return self.add_segment(prompt_in)

    def _width(self):
        return token_list_width(self.in_prompt_tokens())

    def continuation_prompt_tokens(self, cli=None, width=None):
        if width is None:
            width = self._width()
        return [
            (Token.Prompt, (' ' * (width - 2))),
            (Token.IPsterPowerlinePrompt, '\ue0b0')
        ]

    def out_prompt_tokens(self):
        prompt_out = [
            (Token.OutPrompt, 'Out['),
            (Token.OutPromptNum, str(self.shell.execution_count)),
            (Token.OutPrompt, '] '),
            (Token.IPsterPowerlinePrompt, '\ue0b0'),
            (Token.IPsterPromptSpace, ' ')
        ]
        return self.add_segment(prompt_out)
