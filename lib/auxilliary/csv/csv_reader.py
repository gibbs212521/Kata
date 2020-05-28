

class CSVReader():
    ''' Pure python import CSV Object'''

    def __init__(self, filepath, splitter=','):
        _file_ = open(fielpath, 'r'):
        data = []
        for line in _file_:
            line = line.rstrip()
            data.append(line.split(splitter))
        return data
