from consts.background_mode import BackgroundMode
from emf_common import debug_print, info_print, enum_index_to_enum_val
from record_parsers.i_record_parser import IRecordParser, parse_as_le


class EmrSetBkModeParser(IRecordParser):
    def __init__(self, raw_record_data):
        super().__init__(raw_record_data)

    def parse(self, session):
        debug_print("Parsing SetBackgroundMode record")
        raw_bk_mode = parse_as_le(self._raw_record_data[8:12])

        bk_mode = enum_index_to_enum_val(raw_bk_mode, BackgroundMode)

        info_print(f"Background mode set to {bk_mode}")
        session.bk_mode = bk_mode
