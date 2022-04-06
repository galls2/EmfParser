from consts.stock_objects import StockObjects
from emf_common import info_print, debug_print
from record_parsers.i_record_parser import IRecordParser, parse_as_le


class EmrSelectObjectParser(IRecordParser):
    def __init__(self, raw_record_data):
        super().__init__(raw_record_data)

    def parse(self, session):
        selected_obj_index = parse_as_le(self._raw_record_data[8:12])
        if selected_obj_index not in session.obj_table.keys() and selected_obj_index not in StockObjects.keys():
            info_print(f">>>>> Error: Attempting to select a non-existing object index: {selected_obj_index}")
            return

        if selected_obj_index in session.obj_table.keys():
            session.selected_obj = session.obj_table[selected_obj_index]
            debug_print(f"Selected obj of index {selected_obj_index} from object table")
        else:
            session.selected_obj = StockObjects[selected_obj_index][0]
            brush_name = StockObjects[selected_obj_index][1]
            debug_print(f"Selected obj of index {selected_obj_index} from stock object enumeration ({brush_name})")
