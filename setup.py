# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='ipython-agnoster',
    version='0.0.3',
    description='A hipster theme for the IPython REPL',
    author='Pierpaolo Rasicci',
    url='https://github.com/i5ar/ipster',
    license='MIT',
    keywords="ipython agnoster",
    packages=['ipster'],
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
    zip_safe=False
)
