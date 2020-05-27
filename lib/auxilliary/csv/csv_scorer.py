from lib.auxilliary.csv.base_parser import BaseParser


class CSVScorer(BaseParser):
    '''
        CSV Class dedicated to sort .csv scores.  
        input   :   .csv file with rows consisting of [NAME],[SURNAME],[SCORE]
        output  :   plain text file containing top score names
    '''

    def __init__(self, input_path, output_path, max_name_length=25):

        self.max_name_length = max_name_length

            ### Configure input and output  ###
        [self.input_filepath, self.input_dir] = self.setPathSeparators(input_path)
        [self.output_filepath, self.output_dir] = self.setPathSeparators(output_path)

