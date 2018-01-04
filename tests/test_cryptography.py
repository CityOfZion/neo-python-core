import binascii
from neocore.Cryptography import Helper
from neocore.Cryptography.Crypto import Crypto
from unittest import TestCase
from neocore.KeyPair import KeyPair


class HelperTestCase(TestCase):
    def test_xor_bytes(self):
        a = b"12345"
        b = b"09876"
        expected_result = b'\x01\x0b\x0b\x03\x03'

        # Should work
        result = Helper.xor_bytes(a, b)
        self.assertEqual(result, expected_result)

        # Should not work on inequal length byte objects
        with self.assertRaises(AssertionError) as context:
            Helper.xor_bytes(a, b"x")

    def test_base256_encode(self):
        val = 1234567890
        res = Helper.base256_encode(val)
        self.assertEqual(res, bytearray(b'\xd2\x02\x96I'))

    def test_random_key(self):
        a = Helper.random_key()
        self.assertEqual(len(a), 64)

        b = Helper.random_key()
        self.assertNotEqual(a, b)

    def test_double_sha256(self):
        expected_hash = '4f8b42c22dd3729b519ba6f68d2da7cc5b2d606d05daed5ad5128cc03e6c6358' #https://www.dlitz.net/crypto/shad256-test-vectors/
        result = Helper.double_sha256(b'abc')
        self.assertEqual(result, expected_hash)

    def test_publickey_to_redeemscript_to_scripthash_to_address(self):
        # NEP 2 testvector
        expected_redeemscript = binascii.unhexlify('21026241e7e26b38bb7154b8ad49458b97fb1c4797443dc921c5ca5774f511a2bbfcac')
        expected_scripthash = binascii.unhexlify('79ecf967a02f9bdbd147fc97b18efd7877d27f78')
        expected_address = 'AStZHy8E6StCqYQbzMqi4poH7YNDHQKxvt'

        priv_key = KeyPair.PrivateKeyFromWIF('L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP')
        kp = KeyPair(priv_key=priv_key)
        pub_bytes = kp.PublicKey.encode_point(True)
        redeemscript = Helper.pubkey_to_redeem(pub_bytes)
        scripthash = Helper.redeem_to_scripthash(redeemscript)
        address = Helper.scripthash_to_address(scripthash)

        self.assertEqual(redeemscript, expected_redeemscript)
        self.assertEqual(scripthash, expected_scripthash)
        self.assertEqual(address, expected_address)

    def test_publickey_to_scripthash(self):
        expected_scripthash = binascii.unhexlify('79ecf967a02f9bdbd147fc97b18efd7877d27f78')
        priv_key = KeyPair.PrivateKeyFromWIF('L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP')
        kp = KeyPair(priv_key=priv_key)
        pub_bytes = kp.PublicKey.encode_point(True)

        result = Helper.pubkey_to_pubhash(pub_bytes)
        self.assertEqual(result, expected_scripthash)
