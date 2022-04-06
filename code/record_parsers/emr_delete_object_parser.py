from emf_common import info_print, debug_print
from record_parsers.i_record_parser import IRecordParser, parse_as_le


class EmrDeleteObjectParser(IRecordParser):
    def __init__(self, raw_record_data):
        super().__init__(raw_record_data)

    def parse(self, session):
        obj_to_delete_index = parse_as_le(self._raw_record_data[8:12])
        if obj_to_delete_index not in session.obj_table.keys():
            info_print(f">>>>> Error: Attempting to delete non existing object index: {obj_to_delete_index}!")
            return
        debug_print(f"Deleted obj of index {obj_to_delete_index}")
        session.obj_table.pop(obj_to_delete_index)
