from consts.brush_style import BrushStyle
from consts.hatch_style import HatchStyle
from emf_common import info_print, parse_color_ref, debug_print
from objects.brush import Brush
from record_parsers.i_record_parser import IRecordParser, parse_as_le


class EmrCreateBrushIndirectParser(IRecordParser):
    def parse(self, session):
        debug_print("Parsing create brush indirect record")
        # 8 first bytes are type, size
        brush_index = parse_as_le(self._raw_record_data[8:12])
        if brush_index in session.obj_table.keys():
            info_print(f">>>>> Warning: Brush index overwriting existsing object in object type: {brush_index}")

        brush_style_index = parse_as_le(self._raw_record_data[12:16])
        brush_style = BrushStyle(brush_style_index)
        raw_brush_color_bytes = self._raw_record_data[16:20]
        brush_hatch_enum_index = parse_as_le(self._raw_record_data[20:24])

        if brush_style not in [BrushStyle.BS_NULL, BrushStyle.BS_SOLID, BrushStyle.BS_HATCHED]:
            info_print(f">>>>> Warning: Possibly illegal brush style: {brush_style}")

        brush_rgb = parse_color_ref(raw_brush_color_bytes) if brush_style != BrushStyle.BS_NULL else (-1, -1, -1)
        brush_hatch = HatchStyle._value2member_map_[brush_hatch_enum_index] \
            if brush_style == BrushStyle.BS_HATCHED and brush_hatch_enum_index in HatchStyle._value2member_map_.keys() \
            else -1

        debug_print(f"Creating brush of index {brush_index} in the object table")
        brush = Brush(brush_style, brush_rgb, brush_hatch)
        session.obj_table[brush_index] = brush

    def __init__(self, raw_record_data):
        super().__init__(raw_record_data)
