from unittest import TestCase

from neocore.bin import cli


class CliTestCase(TestCase):
    def test_address_to_scripthash(self):
        address = "AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"
        scripthash = cli.address_to_scripthash(address)
        self.assertEqual(len(scripthash), 20)

        address = "AK2nJJpJr6o664CWJKi1QRXjqeic2zRpxx"
        with self.assertRaises(cli.ConversionError):
            scripthash = cli.address_to_scripthash(address)
