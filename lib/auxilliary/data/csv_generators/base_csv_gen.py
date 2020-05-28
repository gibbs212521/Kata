

class BaseCSVGenerator():
    ''' Quasi-Abstract CSV Random Generator Method Class'''
    
    def __init__(self, output_filepath):
        self.output = output_filepath
        self.column_names = []
        self.row_methods = []
        self.row_count = 1

    def generateCSV(self, row_count=None, line_ending='\n'):
        if row_count is not None:
            self.setRowCount(row_count)
        csv = []
        text = ''
        for name in self.column_names:
            text += name + ','
        if bool(len(self.column_names)):
            csv.append(self.column_names)
        for indx in range(self.row_count):
            row = []
            [row.append(item()) for item in self.row_methods]
            csv.append(row)
            [text.append(str(value) + ',') for value in row]
            [text.append(line_ending)]
        csv_text = text.rstrip()



    def addColumn(self, gen_method, column_name=None):
        ''' Add count number of columns using gen_method to csv file. '''
        consistancy 
        if column_name is not None:
            if len(self.column_names) != len(self.row_methods):
             raise TypeError('BaseCSVGenerator.addColumn method requires consistent column naming')   
            self.column_names.append(column_name)
        elif bool(len(self.column_names)):
            raise TypeError('BaseCSVGenerator.addColumn method requires consistent column naming')

        self.row_methods.append(gen_method)

    def clearColumns(self):
        self.column_names.clear()
        self.row_methods.clear()

    def setRowCount(self, count):
        ''' Sets number of rows created in csv file. '''
        self.row_count = count
