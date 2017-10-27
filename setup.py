# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup


def get_readme(readme):
    """Get long description."""
    # try:
    #     from pypandoc import convert_file, convert_text
    #     return convert_file(readme, 'rst')
    # except ImportError as e:
    #     with open(readme) as f:
    #         return f.read()
    with open(readme) as f:
        return f.read()


def get_version(package):
    """Return package version as listed in `__version__` in `init.py`."""
    f = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", f).group(1)


setup(
    name='ipython-agnoster',
    version=get_version('ipster'),
    description='A hipster theme for the IPython REPL',
    long_description=get_readme('README.rst'),
    author='Pierpaolo Rasicci',
    url='https://github.com/i5ar/ipster',
    license='MIT',
    keywords="ipython agnoster",
    packages=['ipster'],
    # Convert Markdown to reStructuredtext
    entry_points={
        'console_scripts': ['convert-rst=ipster.command_line:main'],
    },
    # Use Environment Markers to install IPython for Python 2
    install_requires=[
        'ipython>=5.0,<6.0;python_version<="2.7"',
        'ipython>=6.0;python_version>="3.3"',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Text Editors',
    ],
    zip_safe=False,
    test_suite='tests',
)
