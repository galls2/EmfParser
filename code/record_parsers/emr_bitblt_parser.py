from consts.dib_colors import DIBColors
from consts.ternary_raster_operation import TernaryRasterOperation
from emf_common import info_print, debug_print, enum_index_to_enum_val
from objects.color_ref import ColorRef
from objects.device_independent_bitmap import DIB
from objects.rectangle import Rectangle
from record_parsers.i_record_parser import IRecordParser, parse_as_le


class EmrBitBltParser(IRecordParser):
    def __init__(self, raw_record_data):
        super().__init__(raw_record_data)

    def parse(self, session):
        debug_print("Parsing bitblt record")

        bounds = Rectangle.parse_from_bytes(self._raw_record_data[8:24])
        x_dest = parse_as_le(self._raw_record_data[24:28])
        y_dest = parse_as_le(self._raw_record_data[28:32])
        rectangle_width = parse_as_le(self._raw_record_data[32:36])
        rectangle_height = parse_as_le(self._raw_record_data[36:40])

        raw_bit_blt_raster_operation = parse_as_le(self._raw_record_data[40:44])
        bitblt_raster_op = enum_index_to_enum_val(raw_bit_blt_raster_operation, TernaryRasterOperation)

        x_src = parse_as_le(self._raw_record_data[44:48])
        y_dst = parse_as_le(self._raw_record_data[48:52])

        raw_xform_src = self._raw_record_data[52:76]  ## TODO parse me

        background_color_src = ColorRef.parse_from_bytes(self._raw_record_data[76:80])
        usage_src = enum_index_to_enum_val(parse_as_le(self._raw_record_data[80:84]), DIBColors)
        dib_offset = parse_as_le(self._raw_record_data[84:88])
        dib_len = parse_as_le(self._raw_record_data[88:92])
        src_bitmap_bit_offset = parse_as_le(self._raw_record_data[92:96])
        src_bitmap_bits_len = parse_as_le(self._raw_record_data[96:100])

        if dib_len == 0:
            return

        dib = DIB.parse_from_bytes(self._raw_record_data[dib_offset:dib_offset+dib_len], usage_src)
