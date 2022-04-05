from emf_common import debug_print
from record_parsers.i_record_parser import IRecordParser, parse_as_le


class EmrEofParser(IRecordParser):
    def __init__(self, raw_record_data):
        super().__init__(raw_record_data)

    def _parse_palette(self, num_palette_entries, offset_palette):
        if num_palette_entries != 0:
            raise NotImplementedError()

    def parse(self, session):
        debug_print("Parsing EOF record")
        num_palette_entries = parse_as_le(self._raw_record_data[8:12])
        offset_palette = parse_as_le(self._raw_record_data[12:16])
        size_last = parse_as_le(self._raw_record_data[16:20])
        assert size_last == 20

        self._parse_palette(num_palette_entries, offset_palette)
