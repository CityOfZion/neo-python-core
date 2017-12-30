===============
neo-python-core
===============

Core functionality of [neo-python](https://github.com/CityOfZion/neo-python).


## Getting started

You need [Python 3.5](https://www.python.org/downloads/release/python-354/).


### Virtual Environment

Create a Python 3 virtual environment and activate it:

.. code-block:: console

    $ python3 -m venv venv
    $ source venv/bin/activate

Then install the requirements:

.. code-block:: console

    $ pip install -e .
    $ pip install -r requirements_dev.txt

### Linting and testing the code

.. code-block:: console

    make lint
    make test
    make test-all
    make coverage
