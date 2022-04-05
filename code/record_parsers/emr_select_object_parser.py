from emf_common import info_print, debug_print
from record_parsers.i_record_parser import IRecordParser, parse_as_le


class EmrSelectObjectParser(IRecordParser):
    def __init__(self, raw_record_data):
        super().__init__(raw_record_data)

    def parse(self, session):
        selected_obj_index = parse_as_le(self._raw_record_data[8:12])
        if selected_obj_index not in session.obj_table.keys():
            info_print(f">>>>> Error: Attempting to select a non-existing object index: {selected_obj_index}")
            return
        debug_print(f"Selected obj of index {selected_obj_index}")
        session.selected_obj_idx = selected_obj_index
