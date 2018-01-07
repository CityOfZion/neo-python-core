import binascii
from neocore.Cryptography import Helper
from unittest import TestCase
from neocore.KeyPair import KeyPair
from neocore.Cryptography.MerkleTree import MerkleTree
from neocore.UInt256 import UInt256


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
        expected_hash = '4f8b42c22dd3729b519ba6f68d2da7cc5b2d606d05daed5ad5128cc03e6c6358'  # https://www.dlitz.net/crypto/shad256-test-vectors/
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

    def test_base256_zero_input(self):
        result = Helper.base256_encode(0)
        self.assertEqual(bytearray.fromhex('00'), result)

    def test_base256_negative_input(self):
        with self.assertRaises(ValueError) as context:
            Helper.base256_encode(-1)
        self.assertTrue("Negative numbers not supported" in str(context.exception))

    def test_base256_padding(self):
        result = Helper.base256_encode(1230, minwidth=5)
        self.assertEqual(5, len(result))


class MerkleTreeTestCase(TestCase):
    def test_compute_root_single_hash(self):
        data = binascii.unhexlify(b'aa' * 32)
        hash1 = UInt256(data=data)
        root = MerkleTree.ComputeRoot([hash1])

        self.assertEqual(data, root.ToArray())

    def test_compute_root_multiple_hashes(self):
        expected_hash = Helper.bin_dbl_sha256(binascii.unhexlify(b'aa' * 32 + b'bb' * 32))

        hash1 = UInt256(data=binascii.unhexlify(b'aa' * 32))
        hash2 = UInt256(data=binascii.unhexlify(b'bb' * 32))
        hashes = [hash1, hash2]
        root = MerkleTree.ComputeRoot(hashes)

        self.assertEqual(expected_hash, root.ToArray())

    def test_computer_root_no_input(self):
        with self.assertRaises(Exception) as context:
            MerkleTree.ComputeRoot([])
        self.assertTrue("Hashes must have length" in str(context.exception))

    def test_build_no_leaves(self):
        with self.assertRaises(Exception) as context:
            MerkleTree([]).__Build([])
        self.assertTrue("Leaves must have length" in str(context.exception))

    def test_to_hash_array(self):
        hash1 = UInt256(data=binascii.unhexlify(b'aa' * 32))
        hash2 = UInt256(data=binascii.unhexlify(b'bb' * 32))
        hash3 = UInt256(data=binascii.unhexlify(b'cc' * 32))
        hash4 = UInt256(data=binascii.unhexlify(b'dd' * 32))
        hash5 = UInt256(data=binascii.unhexlify(b'ee' * 32))
        hashes = [hash1, hash2, hash3, hash4, hash5]

        m = MerkleTree(hashes)
        hash_array = m.ToHashArray()

        for i, h in enumerate(hashes):
            self.assertEqual(h.ToBytes(), hash_array[i].ToBytes())

    def test_trim_node1(self):
        hash1 = UInt256(data=binascii.unhexlify(b'aa' * 32))
        hash2 = UInt256(data=binascii.unhexlify(b'bb' * 32))
        hash3 = UInt256(data=binascii.unhexlify(b'cc' * 32))
        hashes = [hash1, hash2, hash3]
        m = MerkleTree(hashes)

        depth = 2
        flags = bytearray.fromhex('11110000')  # 1 byte left node , 1 byte right node  00=delete, non-00 is keep
        m._TrimNode(m.Root, 1, depth, flags)
        self.assertEqual(None, m.Root.LeftChild)
        self.assertEqual(None, m.Root.RightChild)

    def test_trim_node2(self):
        hash1 = UInt256(data=binascii.unhexlify(b'aa' * 32))
        hash2 = UInt256(data=binascii.unhexlify(b'bb' * 32))
        hash3 = UInt256(data=binascii.unhexlify(b'cc' * 32))
        hash4 = UInt256(data=binascii.unhexlify(b'dd' * 32))
        hash5 = UInt256(data=binascii.unhexlify(b'ee' * 32))
        hash6 = UInt256(data=binascii.unhexlify(b'11' * 32))
        hash7 = UInt256(data=binascii.unhexlify(b'22' * 32))
        hash8 = UInt256(data=binascii.unhexlify(b'33' * 32))
        hash9 = UInt256(data=binascii.unhexlify(b'44' * 32))
        hashes = [hash1, hash2, hash3, hash4, hash5, hash6, hash7, hash8, hash9]
        m = MerkleTree(hashes)

        depth = 3
        flags = bytearray.fromhex('111100000000')
        m._TrimNode(m.Root, 1, depth, flags)
        self.assertEqual(None, m.Root.LeftChild)
        self.assertEqual(None, m.Root.RightChild)

    def test_trim_node3(self):
        hash1 = UInt256(data=binascii.unhexlify(b'aa' * 32))
        hash2 = UInt256(data=binascii.unhexlify(b'bb' * 32))
        hashes = [hash1, hash2]
        m = MerkleTree(hashes)

        depth = 1
        flags = bytearray.fromhex('0000')
        m._TrimNode(m.Root, 1, depth, flags)

        self.assertNotEqual(None, m.Root.LeftChild)
        self.assertNotEqual(None, m.Root.RightChild)

    def test_trim_tree(self):
        hash1 = UInt256(data=binascii.unhexlify(b'aa' * 32))
        hash2 = UInt256(data=binascii.unhexlify(b'bb' * 32))
        hash3 = UInt256(data=binascii.unhexlify(b'cc' * 32))
        hashes = [hash1, hash2, hash3]
        m = MerkleTree(hashes)

        flags = bytearray.fromhex('0000')
        m.Trim(flags)

        self.assertEqual(None, m.Root.LeftChild)
        self.assertEqual(None, m.Root.RightChild)

    def test_node_methods(self):
        hash1 = UInt256(data=binascii.unhexlify(b'aa' * 32))
        hash2 = UInt256(data=binascii.unhexlify(b'bb' * 32))
        # hash3 = UInt256(data=binascii.unhexlify(b'cc' * 32))
        # hash4 = UInt256(data=binascii.unhexlify(b'dd' * 32))
        # hash5 = UInt256(data=binascii.unhexlify(b'ee' * 32))
        # hashes = [hash1, hash2, hash3, hash4, hash5]
        hashes = [hash1, hash2]
        m = MerkleTree(hashes)

        self.assertEqual(True, m.Root.IsRoot())
        self.assertEqual(False, m.Root.IsLeaf())
        self.assertEqual(False, m.Root.LeftChild.IsRoot())
        self.assertEqual(True, m.Root.LeftChild.IsLeaf())

        # I have no acceptable test vector
        m.Root.LeftChild.Size()
