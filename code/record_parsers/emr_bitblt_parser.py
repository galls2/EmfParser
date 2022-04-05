from emf_common import info_print, debug_print
from record_parsers.i_record_parser import IRecordParser, parse_as_le


class EmrBitBltParser(IRecordParser):
    def __init__(self, raw_record_data):
        super().__init__(raw_record_data)

    def parse(self, session):
        debug_print("Parsing bitblt record")

