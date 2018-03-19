Library for working with NEO related data in Python, without database dependencies.

.. image:: https://travis-ci.org/CityOfZion/neo-python-core.svg?branch=master
        :target: https://travis-ci.org/CityOfZion/neo-python-core

.. image:: https://coveralls.io/repos/github/CityOfZion/neo-python-core/badge.svg
        :target: https://coveralls.io/github/CityOfZion/neo-python-core


* Datatypes like ``UInt160``, ``KeyPair``, and basic string to address and address to ``UInt160`` methods
* Includes a useful cli-tool ``np-utils`` (see help with ``np-utils -h``)
* Used by `neo-python <https://github.com/CityOfZion/neo-python>`_
* https://pypi.python.org/pypi/neocore


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

.. code-block:: console

    # In case you want to increase the version number again (eg. scope changed from patch to minor):
    bumpversion --no-tag minor|major

    # Update ``HISTORY.rst`` with the new version number and the changes and commit this
    vi HISTORY.rst
    git commit -m "Updated HISTORY.rst" HISTORY.rst

    # Set the release version number and create the tag
    bumpversion release

    # Increase patch number and add `-dev`
    bumpversion --no-tag patch

    # Push to GitHub, which also updates the PyPI package
    git push && git push --tags
