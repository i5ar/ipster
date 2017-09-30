from __future__ import (unicode_literals, absolute_import)

from unittest import TestCase
import types

from IPython.terminal.prompts import Prompts

from ipster import since_5


prompts = since_5.IPsterPrompts(Prompts)


class TestIPster(TestCase):
    """IPster test case.
    Run test::

        $ python setup.py test

    """
    def test_type(self):
        """Test type."""
        # TODO: Use Type Hints with Mypy in Python 3.6
        # Same as ``assert isinstance(prompts.is_venv(), bool)``
        self.assertIs(type(prompts.is_venv()), bool)

    def test_subclass(self):
        """Test correct instance of the prompt."""
        # Same as ``assert issubclass(since_5.IPsterPrompts, Prompts)``
        self.assertIsInstance(prompts, Prompts)


if __name__ == '__main__':
    unittest.main()
