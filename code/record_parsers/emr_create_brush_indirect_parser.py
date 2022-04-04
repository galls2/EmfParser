from record_parsers.i_record_parser import IRecordParser, parse_as_le


class EmrCreateBrushIndirectParser(IRecordParser):
    def parse(self, session):
        brush_index = parse_as_le(self._raw_record_data[8:12])

    def __init__(self, raw_record_data):
        super().__init__(raw_record_data)
