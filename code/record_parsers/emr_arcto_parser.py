from record_parsers.i_record_parser import IRecordParser


class EmrArcToParser(IRecordParser):
    def parse(self):
        pass

    def __init__(self, raw_record_data):
        super().__init__(raw_record_data)
