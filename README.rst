Library for working with NEO related data in Python, without database dependencies.

.. image:: https://travis-ci.org/CityOfZion/neo-python-core.svg?branch=master
        :target: https://travis-ci.org/CityOfZion/neo-python-core

.. image:: https://coveralls.io/repos/github/CityOfZion/neo-python-core/badge.svg
        :target: https://coveralls.io/github/CityOfZion/neo-python-core


* Datatypes like ``UInt160``, ``KeyPair``, ``BigInteger`` and basic string to address and address to ``UInt160`` methods
* Includes a useful cli-tool ``np-utils`` (see help with ``np-utils -h``)
* Compatible with Python 3.5+
* Used by `neo-python <https://github.com/CityOfZion/neo-python>`_
* https://pypi.python.org/pypi/neocore

``np-utils`` examples:

.. code-block:: console

    $ np-utils -h
    usage: np-utils [-h] [--version] [--address-to-scripthash address]
                    [--scripthash-to-address scripthash] [--create-wallet]

    optional arguments:
    -h, --help            show this help message and exit
    --version             show program's version number and exit
    --address-to-scripthash address
                            Convert an address to scripthash
    --scripthash-to-address scripthash
                            Convert scripthash to address
    --create-wallet       Create a wallet

    $ np-utils --create-wallet
    {
    "private_key": "KwJqCbjsmGUCqbkp83Nxi9MJ9mA7F8EN4tebJVWjYZBEoWCNxCaF",
    "address": "AHVvg26CNz1vxteJfeHy4R8P4VN8SydCM6"
    }

    $ np-utils --address-to-scripthash AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y
    Scripthash big endian:  0xe9eed8dc39332032dc22e5d6e86332c50327ba23
    Scripthash little endian: 23ba2703c53263e8d6e522dc32203339dcd8eee9
    Scripthash neo-python format: b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'

    $ np-utils --scripthash-to-address 0xe9eed8dc39332032dc22e5d6e86332c50327ba23
    AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y

    $ np-utils --scripthash-to-address 23ba2703c53263e8d6e522dc32203339dcd8eee9
    Detected little endian scripthash. Converting to big endian for internal use.
    Big endian scripthash: 0xe9eed8dc39332032dc22e5d6e86332c50327ba23
    AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y


Getting started
---------------

You need Python 3.5 or higher!

You can install `neocore` from PyPI with ``easy_install`` or ``pip``:

.. code-block:: console

    $ pip install -U neocore

Alternatively, if you want to work on the code, clone this repository and setup your venv:

* Clone the repo: ``git clone https://github.com/CityOfZion/neo-python-core.git``
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

    # Only in case you want to increase the version number again (eg. scope changed from patch to minor):
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
