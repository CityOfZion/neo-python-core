from neocore.UIntBase import UIntBase


class UInt256(UIntBase):
    def __init__(self, data=None):
        super(UInt256, self).__init__(num_bytes=32, data=data)

    @staticmethod
    def ParseString(value):
        if value[0:2] == '0x':
            value = value[2:]
        if not len(value) == 64:
            raise Exception("Invalid UInt256 Format: %s chars != 64 chars" % len(value))
        reversed_data = bytearray.fromhex(value)
        reversed_data.reverse()
        return UInt256(data=reversed_data)
