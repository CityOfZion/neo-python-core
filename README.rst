Library for working with NEO related data in Python, without database dependencies.

.. image:: https://travis-ci.org/CityOfZion/neo-python-core.svg?branch=master
        :target: https://travis-ci.org/CityOfZion/neo-python-core

.. image:: https://coveralls.io/repos/github/CityOfZion/neo-python-core/badge.svg
        :target: https://coveralls.io/github/CityOfZion/neo-python-core


* Includes datatypes like ``UInt160``, ``KeyPair``, and basic string to address and address to ``UInt160`` methods.
* Used by `neo-python <https://github.com/CityOfZion/neo-python>`_.
* https://pypi.python.org/pypi/neocore

Currently in alpha development.


Getting started
---------------

You need `Python 3.5 <https://www.python.org/downloads/release/python-354/>`_.

You can install `neocore` from PyPI with ``easy_install`` or ``pip``:


.. code-block:: console

    $ pip install -U neocore

Alternatively, if you want to work on the code, clone this repository and setup your venv:

* Clone the repo: ``git@github.com:CityOfZion/neo-python-core.git``
* Create a Python 3 virtual environment and activate it:

.. code-block:: console

    $ python3 -m venv venv
    $ source venv/bin/activate

* Then install the requirements:

.. code-block:: console

    $ pip install -e .
    $ pip install -r requirements_dev.txt


Useful commands
^^^^^^^^^^^^^^^

.. code-block:: console

    $ make lint
    $ make test
    $ make coverage


Release checklist
^^^^^^^^^^^^^^^^^

(Only for admins)

Releasing a new version on GitHub automatically uploads this release to PyPI.
This is a checklist for releasing a new version:

* Update ``HISTORY.rst`` with the new version number and the changes
* Git commit: ``git commit -am "Updated HISTORY.rst for release```
* Update the version number and create the tag: ``bumpversion patch|minor|major``
* Update patch version ``bumpversion --no-tag patch``
* Push to GitHub: ``git push && git push --tags``
