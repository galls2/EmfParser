from emf_common import info_print
from objects.emf_object import EmfObj
from record_parsers.i_record_parser import parse_as_le


class Rectangle(EmfObj):
    def __init__(self, left, top, right, bottom):
        super().__init__()
        self.top_left = (left, top)
        self.bottom_right = (right, bottom)

        ## TODO validate legal values

    @staticmethod
    def parse_from_bytes(byte_seq):
        if len(byte_seq) < 16:
            info_print(f"Failed parsing rectangle from {byte_seq}")
            return None

        rectangle = Rectangle(*[parse_as_le(byte_seq[(i*4):(i+1)*4]) for i in range(4)])
        return rectangle
