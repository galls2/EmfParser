from emf_common import info_print
from record_parsers.emr_arcto_parser import EmrArcToParser
from record_parsers.emr_eof_parser import EmrEofParser
from record_parsers.emr_header_parser import EmrHeaderParser
from record_parsers.i_record_parser import parse_as_le


class EmfParser:
    def __init__(self, emf_path):
        with open(emf_path, "rb") as f:
            self._raw_data = f.read()

        self.records_mapping = {
            1: EmrHeaderParser,
            37: EmrArcToParser,
            14: EmrEofParser

        }

    def parse(self):
        curr_index = 0
        while curr_index < len(self._raw_data):
            if len(self._raw_data[curr_index:]) < 8:
                info_print("Invalid structure: new record but no room for type and size")
            record_type = parse_as_le(self._raw_data[curr_index:curr_index + 4])
            record_size = parse_as_le(self._raw_data[curr_index + 4:curr_index + 8])
            if record_size == 0:
                info_print(f"Encountered illegal record of size 0! Record Type: f{record_type}")
                break

            info_print(f'Found record of type {record_type} and of size {record_size}!')
            if record_type in self.records_mapping.keys():
                record_raw_data = self._raw_data[curr_index + 8: curr_index + record_size]
                record_parser = self.records_mapping[record_type](record_raw_data)
                record_parser.parse()
            else:
                info_print(f"No parser for RecordType={record_type}")

            curr_index += record_size

            if record_type == 14:  ## EOF
                info_print("Done parsing EMF after encountered EOF record!")
                break

