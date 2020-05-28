from lib.auxilliary.csv.base_parser import BaseParser

class CSVScorer(BaseParser):
    '''
    CSV Class dedicated to sort .csv scores.  
    input   :   .csv file with rows consisting of [NAME],[SURNAME],[SCORE]
    output  :   plain text file containing top score names
    '''

    def __init__(self, input_path=None, output_path=None, max_name_length=25):
        super().__init__()
        if input_path is None or output_path is None:
            raise TypeError('''
                CSVScorer has invalid input or output parameters.
                This class requires a valid and existing .csv for its input parameter
                and a valid plain text file for its output parameter.
                ''')
        self.max_name_length = max_name_length
            ### Configure input and output  ###
        [self.input_filepath, input_dir] = self.setPathSeparators(input_path)
        [self.output_filepath, output_dir] = self.setPathSeparators(output_path)

    def getTopScorers(self, splitter=',', line_ending='\n'):
        ''' Takes input csv file and generates plain text file listing top scorers. '''
        output = '| '
        top_scorers = ''
        _file_ = open(self.input_filepath, 'r')
        # Reading for potential headers in CSV File
        line = _file_.readline().rstrip()
        line = line.split(splitter)
        try:
            max_score = float(line[2])
            top_scorers = line[0] + ' | ' + line[1] + ' | '  + line_ending + '| '
        except ValueError:
            headers = line
            for header in headers[:2]:
                output += header + ' | '
            output += line_ending + '| '
            max_score = -1
        # Reading Throughout CSV File
        for line in _file_:
            line = line.rstrip().split(splitter)
            score = float(line[2])
            if score > max_score:
                max_score = score
                top_scorers = ''
            if score >= max_score:
                top_scorers += line[0] + ' | ' + line[1] + ' | '  + line_ending + '| '
        top_scorers = top_scorers.rstrip('| ').rstrip() # Remove last end of line
        output += top_scorers
        _file_.close()
        # Writing results to plain text file
        _file_ = open(self.output_filepath, 'w')
        _file_.write(output)
        _file_.close()
