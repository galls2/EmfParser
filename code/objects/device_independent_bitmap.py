from consts.bitcount import BitCount
from emf_common import enum_index_to_enum_val
from objects.emf_object import EmfObj
from record_parsers.i_record_parser import parse_as_le


class DIB(EmfObj):
    def __init__(self):
        super().__init__()

    @staticmethod
    def parse_bitmap_info_header(byte_seq):
        bitmapheader_size = parse_as_le(byte_seq[:4])
        width = parse_as_le(byte_seq[4:8])
        height = parse_as_le(byte_seq[8:12])
        planes = parse_as_le(byte_seq[12:14])
#        assert planes == 1

        raw_bit_count = parse_as_le(byte_seq[14:16])
        bit_count = enum_index_to_enum_val(raw_bit_count, BitCount)
        compression = parse_as_le(byte_seq[16:20])
        image_size = parse_as_le(byte_seq[20:24])
        x_pixel_per_meter = parse_as_le(byte_seq[24:28])
        y_pixel_per_meter = parse_as_le(byte_seq[28:32])

        ## TODO NEED TO GO ON PARSING THIS HEADER AND THE REST OF THE BMP

    @staticmethod
    def parse_from_bytes(byte_seq, usage_src):
        header_size = parse_as_le(byte_seq[:4])
        if header_size == 12:
            print("BITMAPCOREHEADER")
            raise NotImplementedError()

        ## Parsing BITMAPINFOHEADER
        ## This is actually like the BMP header
        DIB.parse_bitmap_info_header(byte_seq[4:])
