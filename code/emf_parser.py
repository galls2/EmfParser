from emf_common import info_print
from record_parsers.emr_bitblt_parser import EmrBitBltParser
from record_parsers.emr_delete_object_parser import EmrDeleteObjectParser
from record_parsers.emr_select_object_parser import EmrSelectObjectParser
from record_parsers.emr_setbkmode_parser import EmrSetBkModeParser
from parser_session import EmfParserSession
from record_parsers.emr_arcto_parser import EmrArcToParser
from record_parsers.emr_create_brush_indirect_parser import EmrCreateBrushIndirectParser
from record_parsers.emr_eof_parser import EmrEofParser
from record_parsers.emr_header_parser import EmrHeaderParser
from record_parsers.i_record_parser import parse_as_le


class EmfParser:
    def __init__(self, emf_path):
        with open(emf_path, "rb") as f:
            self._raw_data = f.read()

        self.records_mapping = {
            1: EmrHeaderParser,
            55: EmrArcToParser,
            37: EmrSelectObjectParser,
            39: EmrCreateBrushIndirectParser,
            14: EmrEofParser,
            76: EmrBitBltParser,
            18: EmrSetBkModeParser,
            40: EmrDeleteObjectParser

            #                                   Impl: bitblt-how to parse the bitmap, 82, 84
        }

    def parse(self):

        session = EmfParserSession()

        curr_index = 0
        count_records = 0
        while curr_index < len(self._raw_data):
            if len(self._raw_data[curr_index:]) < 8:
                info_print("Invalid structure: new record but no room for type and size")
            record_type = parse_as_le(self._raw_data[curr_index:curr_index + 4])
            record_size = parse_as_le(self._raw_data[curr_index + 4:curr_index + 8])

            if record_size == 0:
                info_print(f"Encountered illegal record of size 0! Record Type: f{record_type}")
                break

            count_records += 1
            info_print(f'Found record of type {record_type} and of size {record_size}!')
            if record_type in self.records_mapping.keys():
                record_raw_data = self._raw_data[curr_index: curr_index + record_size]
                record_parser = self.records_mapping[record_type](record_raw_data)
                record_parser.parse(session)
            else:
                info_print(f"No parser for RecordType={record_type}")

            curr_index += record_size
            info_print("-------------------------------")
            if record_type == 14:  ## EOF
                info_print(f"Done parsing EMF after encountered EOF record! Parsed {count_records} records.")
                break

        ## TODO Need to validate the count_records is equal to emr_header's num records. As well as for the num handles
