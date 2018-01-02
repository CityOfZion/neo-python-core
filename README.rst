===============
neo-python-core
===============

Basic library for working with NEO related data in Python, without database
dependencies.

Includes datatypes like ``UInt160``, ``KeyPair``, and basic string to address and
address to `UInt160` methods.

Used by `neo-python <https://github.com/CityOfZion/neo-python>`_.

Getting started
---------------

You need `Python 3.5 <https://www.python.org/downloads/release/python-354/>`_.

Create a Python 3 virtual environment and activate it:

.. code-block:: console

    $ python3 -m venv venv
    $ source venv/bin/activate

Then install the requirements:

.. code-block:: console

    $ pip install -e .
    $ pip install -r requirements_dev.txt

Linting and testing the code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ make lint
    $ make test
    $ make coverage
