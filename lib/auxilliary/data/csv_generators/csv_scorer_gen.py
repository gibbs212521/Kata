from lib.auxilliary.data.static_data.get_values import \
    Get_Random_First_Names, Get_Random_Last_Names, Get_Random_Scores

class CSVScorerDataGenerator():
    ''' Concrete CSV Random Generator Method Class for CSV Scorer Kata. '''

    def __init__(self, row_count, output_filepath):
        super().__init__(output_filepath)
        first_names = Get_Random_First_Names(row_count)
        last_names = Get_Random_Last_Names(row_count)
        scores = Get_Random_Scores(row_count)
        self.addColumn(first_names.pop, 'NAME')
        self.addColumn(last_names.pop, 'SURNAME')
        self.addColumn(scores.pop, 'SCORE')
        self.generateCSV(row_count)

    

