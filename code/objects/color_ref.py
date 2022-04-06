from emf_common import info_print
from objects.emf_object import EmfObj
from record_parsers.i_record_parser import parse_as_le


class ColorRef(EmfObj):
    def __init__(self, r, g, b):
        super().__init__()
        self.r = r
        self.g = g
        self.b = b


    @staticmethod
    def parse_from_bytes(byte_seq):
        if len(byte_seq) < 4:
            info_print(f"Failed parsing rectangle from {byte_seq}")
            return None

        color_ref = ColorRef(*[byte_seq[i] for i in range(3)])
        assert byte_seq[3] == 0
        return color_ref
