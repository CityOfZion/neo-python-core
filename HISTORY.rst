=======
History
=======

0.4.4 (2018-04-30)
------------------
* make unhexlify in Crypto.VerifySignature optional (`PR #48 <https://github.com/CityOfZion/neo-python-core/pull/48>`_)


0.4.2 (2018-04-26)
------------------
* ``np-utils`` now supports ``--scripthash-to-address`` (thx @belane)


0.4.1 (2018-04-26)
-----------------------------
* ``np-utils`` cli tool (see ``cli.py``, `PR #40 <https://github.com/CityOfZion/neo-python-core/pull/40>`_)
* alter initialization of Crypto signature curve


0.3.10 (2018-03-21)
----------------------------
* Fix formatting of ``ToNeoJsonString()`` which was cutting off trailing zeroes from integers.


0.3.8 (2018-03-14)
------------------
* Fix travis deploy to be compatible with recent neo-python changes
* Update scrypt and logzero dependency versions


0.3.6 (2018-02-26)
------------------
* Enabled Python >= 3.4 in setup.py


0.3.5 (2018-02-15)
------------------
* Bugfix: Dont unhex when writing var bytes (`PR #36 <https://github.com/CityOfZion/neo-python-core/pull/36>`_)


0.3.4 (2018-01-25)
------------------
* Added ``ParseString`` method to UInt160/UInt256 (`PR #35 <https://github.com/CityOfZion/neo-python-core/pull/35>`_)


0.3.3 (2018-01-25)
------------------
* Added ``Fixed8.ToJsonString()`` (`PR #33 <https://github.com/CityOfZion/neo-python-core/pull/33>`_)


0.3.2 (2018-01-23)
------------------
* Added UInt ``To0xString`` method


0.3.1 (2018-01-09)
------------------
* Documentation update
* Moved the ``cryptography`` dependency to ``requirements_dev.txt``


0.3.0 (2018-01-09)
------------------
* Added ``neo.Cryptography`` and ``KeyPair``
* Changed signature of ``neocore.Cryptography.Crypto.Sign()`` to remove unused ``public_key`` argument
* Removed redundant ``neocore.Cryptography.Helper.hash_to_wallet_address()`` function, use  ``neocore.Cryptography.Helper.scripthash_to_address()`` instead.
* Removed unused ``neocore.Cryptography.Helper`` functions: ``random_string``, ``bytes_to_hex_string``, ``bin_sha256``, ``sha256``, ``random_key``.


0.2.4 + 0.2.5 (2018-01-03)
--------------------------
* Bugfix for deploying from Travis to PyPI/neocore


0.2.3 (2018-01-03)
------------------
* Bugfix for BinaryWriter (`PR #13 <https://github.com/CityOfZion/neo-python-core/pull/13>`_)


0.2.1 (2018-01-02)
------------------
* Added UInt*, Fixed8 and neo.IO.Binary* (`PR #9 <https://github.com/CityOfZion/neo-python-core/pull/9>`_)


0.1.1 - 0.1.2 (2017-12-30)
--------------------------
* Testing of releases on PyPI with Travis CI.


0.1.0 (2017-12-28)
------------------
* First release on PyPI.
