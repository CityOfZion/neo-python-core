# -*- coding:utf-8 -*-
"""
Description:
    Cryptography Helper
Usage:
    from neocore.Cryptography.Helper import *
"""

from bitcoin import *
import os
import time
import random
import hashlib
import binascii
import base58

long = int

ADDRESS_VERSION = 23


def double_sha256(ba):
    """
    Perform two SHA256 operations on the input.

    Args:
        ba (bytes): data to hash.

    Returns:
        str: hash as a double digit hex string.
    """
    d1 = hashlib.sha256(ba)
    d2 = hashlib.sha256()
    d1.hexdigest()
    d2.update(d1.digest())
    return d2.hexdigest()


def pubkey_to_redeem(pubkey):
    """
    Convert the public key to the redeemscript format.

    Args:
        pubkey (bytes): public key.

    Returns:
        bytes: redeemscript.
    """
    return binascii.unhexlify(b'21' + pubkey + b'ac')


def redeem_to_scripthash(redeem):
    """
    Convert a redeem script to a script hash.

    Args:
        redeem (bytes):

    Returns:
        bytes: script hash.
    """
    return bin_hash160Bytes(redeem)


def scripthash_to_address(scripthash):
    """
    Convert a script hash to a public address.

    Args:
        scripthash (bytes):

    Returns:
        str: base58 encoded string representing the wallet address.
    """
    sb = bytearray([ADDRESS_VERSION]) + scripthash
    c256 = bin_dbl_sha256(sb)[0:4]
    outb = sb + bytearray(c256)
    return base58.b58encode(bytes(outb)).decode("utf-8")


def pubkey_to_pubhash(pubkey):
    """
    Convert a public key to a script hash.

    Args:
        pubkey (bytes):

    Returns:
        bytes: script hash.
    """
    return redeem_to_scripthash(pubkey_to_redeem(pubkey))


def bin_dbl_sha256(s):
    """
    Perform a double SHA256 operation on the input.

    Args:
        s(str): message to hash.

    Returns:
        bytes: hash.
    """
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()


def bin_hash160Bytes(bts):
    """
    Get a hash of the provided message using the ripemd160 algorithm.

    Args:
        bts (str): message to hash.

    Returns:
        bytes: hash.
    """
    intermed = hashlib.sha256(bts).digest()
    return hashlib.new('ripemd160', intermed).digest()


def bin_hash160(string):
    """
    Get a hash of the provided message using the ripemd160 algorithm.

    Args:
        string (str): message to hash.

    Returns:
        str: hash as a double digit hex string.
    """
    intermed = hashlib.sha256(string).digest()
    return hashlib.new('ripemd160', intermed).hexdigest()


def base256_encode(n, minwidth=0):  # int/long to byte array
    """
    Encode the input with base256.

    Args:
        n (int): input value.
        minwidth: minimum return value length.

    Raises:
        ValueError: if a negative number is provided.

    Returns:
        bytearray:
    """
    if n > 0:
        arr = []
        while n:
            n, rem = divmod(n, 256)
            arr.append(rem)
        b = bytearray(reversed(arr))
    elif n == 0:
        b = bytearray(b'\x00')
    else:
        raise ValueError("Negative numbers not supported")

    if minwidth > 0 and len(b) < minwidth:  # zero padding needed?
        padding = (minwidth - len(b)) * b'\x00'
        b = bytearray(padding) + b
    b.reverse()

    return b


def xor_bytes(a, b):
    """
    XOR on two bytes objects

    Args:
        a (bytes): object 1
        b (bytes): object 2

    Returns:
        bytes: The XOR result
    """
    assert isinstance(a, bytes)
    assert isinstance(b, bytes)
    assert len(a) == len(b)
    res = bytearray()
    for i in range(len(a)):
        res.append(a[i] ^ b[i])
    return bytes(res)
