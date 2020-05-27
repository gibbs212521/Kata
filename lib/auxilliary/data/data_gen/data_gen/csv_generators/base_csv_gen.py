

class BaseCSVGenerator():
    ''' Quasi-Abstract CSV Random Generator Method Class'''
    
    def __init__(self, output_filepath):
        self.output = output_filepath
        self.row_methods = []
        self.row_count = 1

    def generateCSV(self, row_count=None):
        if row_count is not None:
            self.setRowCount(row_count)
        csv = []
        for row in range(self.row_count):
            row = []
            [row.append(item()) for item in self.row_methods]


    def addColumn(self, gen_method, count=1):
        ''' Add count number of columns using gen_method to csv file. '''
        [self.row_methods.append(gen_method) for k in range(count)]

    def setRowCount(self, count):
        ''' Sets number of rows created in csv file. '''
