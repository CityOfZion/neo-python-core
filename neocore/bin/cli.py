#!/usr/bin/env python3
"""
This cli utility will be installed as `np-utils`. You can see the help with `np-utils -h`.
"""
import argparse
import base58
import hashlib

from neocore import __version__
from neocore.Cryptography.Crypto import Crypto


def address_to_scripthash(address):
    data = bytes(base58.b58decode(address))
    if data[0] != b'\x17': return None
    if data[-4:] != hashlib.sha256(hashlib.sha256(data[:-4]).digest()).digest()[:4]: return None
    return data[1:-4]


def main():
    parser = argparse.ArgumentParser()

    # Show the neo-python version
    parser.add_argument("--version", action="version",
                        version="neocore v{version}".format(version=__version__))

    parser.add_argument("--address-to-scripthash", nargs=1, metavar="address",
                        help="Convert an address to scripthash")

    args = parser.parse_args()
    # print(args)

    if args.address_to_scripthash:
        print([address_to_scripthash(args.address_to_scripthash[0])])


if __name__ == "__main__":
    main()
