from emf_parser import EmfParser

EMF_PATH = '../imgs/example.emf'

if __name__ == '__main__':
    emf_parser = EmfParser(EMF_PATH)
    emf_parser.parse()
