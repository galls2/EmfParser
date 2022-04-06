from emf_common import debug_print
from objects.rectangle import Rectangle
from record_parsers.i_record_parser import IRecordParser, parse_as_le


class EmrHeaderParser(IRecordParser):
    def __init__(self, raw_record_data):
        super().__init__(raw_record_data)
        self._emf_header_bytes = raw_record_data[8:80+8]

    def _parse_basic_header_obj(self, session):
        ## TODO parse
        session.image_bounds = Rectangle.parse_from_bytes(self._emf_header_bytes[:16])
        frame = Rectangle.parse_from_bytes(self._emf_header_bytes[16:32])
        record_sig = self._emf_header_bytes[32:36]
        assert record_sig == b' EMF'

        version = parse_as_le(self._emf_header_bytes[36:40])
        metafile_size = parse_as_le(self._emf_header_bytes[40:44])
        metafile_num_records = parse_as_le(self._emf_header_bytes[44:48])
        metafile_num_handles = parse_as_le(self._emf_header_bytes[48:50])
        reserved_zeros = parse_as_le(self._emf_header_bytes[50:52])
        assert reserved_zeros == 0
        self._len_description = parse_as_le(self._emf_header_bytes[52:56])
        self._offset_description = parse_as_le(self._emf_header_bytes[56:60])
        num_palette_entries = parse_as_le(self._emf_header_bytes[60:64])

        # 2 more things i don't care about

    def _parse_emf_header_ext1(self):
        extension1_bytes = self._raw_record_data[80+8:92+8]
        self._size_pixel_fd = parse_as_le(extension1_bytes[:4])
        self._offset_pixel_fd = parse_as_le(extension1_bytes[4:8])
        b_is_open_gl = parse_as_le(extension1_bytes[8:12]) > 0

    def _parse_header_obj(self, session):
        self._parse_basic_header_obj(session)

        header_size = 88
        if len(self._raw_record_data) >= 88:
            header_size = len(self._raw_record_data)
        else:
            return  ## No Extension

        if self._offset_description >= 88 and (
                self._offset_description + 2 * self._len_description <= len(self._raw_record_data)):
            header_size = self._offset_description

        if header_size < 100:
            return  ## No Extension

        self._parse_emf_header_ext1()

        description = self._raw_record_data[self._offset_description: self._offset_description+2*self._len_description].decode(encoding='utf-16le')
#        print(description)

        if 100 <= self._offset_pixel_fd < header_size and \
                (self._offset_pixel_fd + self._size_pixel_fd <= len(self._raw_record_data)):
            header_size = self._offset_pixel_fd

        ## TODO parse 2nd extension with its shit

    def parse(self, session):
        debug_print("Parsing Header record")
        self._parse_header_obj(session)
