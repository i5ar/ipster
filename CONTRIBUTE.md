# Contribute

## Install

- Uninstall previous version:

      sudo pip uninstall ipython-agnoster
- Activate virtual environment:

      source ./venv/bin/activate
- Contribute;
- Upgrade version in `__init__.py`;
- Create source distribution:

      python setup.py sdist
- Install and record the list of the installed files:

      python setup.py install --record files.log
- Deactivate virtual environment:

      deactivate

## Uninstall

Remove all files manually:

    cat files.log | xargs rm -rf

## Upload

Upload to PyPi:

    python setup.py sdist upload
You may need a `.pypirc` file in your home directory:

    [distutils]
    index-servers =
        pypi

    [pypi]
    repository: https://pypi.python.org/pypi
    username: foobar
