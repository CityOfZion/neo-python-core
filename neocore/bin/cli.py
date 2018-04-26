#!/usr/bin/env python3
"""
This cli utility will be installed as `np-utils`. You can see the help with `np-utils -h`.
"""
import sys
import argparse
import base58
import hashlib

from neocore import __version__
from neocore.Cryptography.Crypto import Crypto
from neocore.UInt160 import UInt160


class ConversionError(Exception):
    pass


def address_to_scripthash(address):
    data = bytes(base58.b58decode(address))

    # Make sure signature byte is correct. In python 3, data[0] is bytes, and in 2 it's str.
    # We use this isinstance checke to make it work with both Python 2 and 3.
    is_correct_signature = data[0] != 0x17 if isinstance(data[0], bytes) else b'\x17'
    if not is_correct_signature:
        raise ConversionError("Invalid address: wrong signature byte")

    # Make sure the checksum is correct
    if data[-4:] != hashlib.sha256(hashlib.sha256(data[:-4]).digest()).digest()[:4]:
        raise ConversionError("Invalid address: invalid checksum")

    # Return only the scripthash bytes
    return data[1:-4]


def scripthash_to_address(scripthash):
    try:
        return Crypto.ToAddress(UInt160.ParseString(scripthash))
    except Exception as e:
        raise ConversionError("Wrong format")


def main():
    parser = argparse.ArgumentParser()

    # Show the neo-python version
    parser.add_argument("--version", action="version",
                        version="neocore v{version}".format(version=__version__))

    parser.add_argument("--address-to-scripthash", nargs=1, metavar="address",
                        help="Convert an address to scripthash")

    parser.add_argument("--scripthash-to-address", nargs=1, metavar="scripthash",
                        help="Convert scripthash to address")

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        exit(1)

    # print(args)
    if args.address_to_scripthash:
        try:
            scripthash = address_to_scripthash(args.address_to_scripthash[0])
            print('Script Hash: 0x{} -- Python format: {!r}'.format(scripthash[::-1].hex(), scripthash))
        except ConversionError as e:
            print(e)
            exit(1)

    if args.scripthash_to_address:
        try:
            address = scripthash_to_address(args.scripthash_to_address[0])
            print(address)
        except ConversionError as e:
            print(e)
            exit(1)


if __name__ == "__main__":
    main()
