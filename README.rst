IPython Agnoster
================

IPython Agnoster (aka IPster) is a hipster theme for the IPython REPL.
It was designed to provide a consistent terminal experience around my
`Agnoster Zsh theme <https://github.com/i5ar/agnoster-zsh-theme>`__ fork.

IPster is optimized for people who use:

-  Solarized colorscheme;
-  Unicode-compatible fonts.

| For GNOME GNU/Linux users, I highly recommend GNOME Terminal + Solarized dark + DejaVu Sans Mono Nerd.
| For KDE GNU/Linux users, I highly recommend Konsole + `Solarized Dark <https://github.com/phiggins/konsole-colors-solarized>`__ + DejaVu Sans Mono Nerd.
| For Mac users, I highly recommend iTerm 2 + Solarized Dark.

    With some extra hassle this theme works on Windows too.

Installation
------------

For ``IPython>=5.0`` install the package:

::

    pip install -U pip setuptools  # update environment markers support
    pip install ipython-agnoster

For ``IPython>=0.11,<5.0`` clone the repository and copy the ``ipster``
module to the extensions directory (deprecated):

::

    git clone --depth=1 https://github.com/i5ar/ipster.git
    cd ipster
    cp -r ipster "$HOME/.ipython/extensions"

Configuration
-------------

Once the module is installed you need to configure it.

Edit your configuration file
``~/.ipython/profile_default/ipython_config.py``:

::

    ## Use 24bit colors instead of 256 colors in prompt highlighting.
    c.TerminalInteractiveShell.true_color = True

    ## Set the color scheme (NoColor, Neutral, Linux, or LightBG).
    c.InteractiveShell.colors = 'Linux'

    ##
    c.InteractiveShell.separate_in = ''

For ``IPython>=5.0`` only add the following lines:

::

    from ipster.since_5 import IPsterPrompts, IPsterStyle

    c.TerminalInteractiveShell.prompts_class = IPsterPrompts

    highlighting_ipstyle = IPsterStyle().overrides_linux()
    c.TerminalInteractiveShell.highlighting_style_overrides = highlighting_ipstyle

For ``IPython>=0.11,<5.0`` only add the following lines (deprecated):

::

    from pygments.token import Token

    # Define prompt colors
    style_overrides_linux = {
        Token.IPsterPromptVirtualenv: 'bg:#859900 #002b36',
        Token.IPsterPowerlinePromptVirtualenv: 'bg:#073642 #859900',
        Token.Prompt: 'bg:#073642 #93a1a1',
        Token.PromptNum: 'bg:#073642 #859900 bold',
        Token.OutPrompt: 'bg:#073642 #93a1a1',
        Token.OutPromptNum: 'bg:#073642 #dc322f bold',
        Token.IPsterPowerlinePrompt: '#073642',
        Token.IPsterPromptSpace: '#839496',
    }

    # Override prompt colors
    c.TerminalInteractiveShell.highlighting_style_overrides = style_overrides_linux

    # Load extension
    c.InteractiveShellApp.extensions = [
        'ipster.post_0_11'
    ]

Compatibility
-------------

Tmux
~~~~

True color support must be enabled in the configuration file
``~/.tmux.conf`` for Solarized colorscheme to work properly:

::

    # Override screen 256 color with true color
    set-option -ga terminal-overrides ",xterm-256color:Tc"

If this fix doesn't work your version of Tmux is probably too old.

Roadmap
-------

When using `IPython
shortcuts <http://ipython.readthedocs.io/en/stable/config/shortcuts/#multi-filtered-shortcuts>`__
for Vi mode, the current mode indication might be very helpful. It would
be great if IPster could show in a right prompt the Vi mode.

Contribute
----------

Suggestions and pull requests are welcome.

Extras
------

If you already use Powerline for IPython, install the IPster theme under
the ``extras`` directory, please.

TODO
----

-  Vi mode detection in the `right
   prompt <https://github.com/jonathanslenders/python-prompt-toolkit/issues/237>`__;
