from neocore.UIntBase import UIntBase


class UInt160(UIntBase):
    def __init__(self, data=None):
        super(UInt160, self).__init__(num_bytes=20, data=data)

    @staticmethod
    def ParseString(value):
        if value[0:2] == '0x':
            value = value[2:]
        if not len(value) == 40:
            raise Exception("Invalid UInt160 Format: %s chars != 40 chars" % len(value))
        reversed_data = bytearray.fromhex(value)
        reversed_data.reverse()
        return UInt160(data=reversed_data)
