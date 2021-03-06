from emf_common import debug_print
from record_parsers.i_record_parser import IRecordParser


class EmrArcToParser(IRecordParser):
    def parse(self, session):
        debug_print("Parsing arcto record")

    def __init__(self, raw_record_data):
        super().__init__(raw_record_data)
