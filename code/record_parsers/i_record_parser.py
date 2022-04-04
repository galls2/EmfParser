from abc import abstractmethod

def parse_as_le(bytes_to_parse):
    return int.from_bytes(bytes_to_parse, byteorder='little')

class IRecordParser:
    def __init__(self, raw_record_data):
        self._raw_record_data = raw_record_data

    @abstractmethod
    def parse(self, session):
        pass