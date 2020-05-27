from os import path
from platform import system as CURRENT_OS


class BaseParser():
    ''' Base Parser Class.  Abstract'''

    def __init__(self):

            ### OS Check for filepath purposes  ###

        OS_TYPE = CURRENT_OS()
        if 'Windows' in OS_TYPE:
            self.path_separator = '\\'
            self.anti_path_separator = '/'
        else: # Linux or Darwin
            self.path_separator = '/'
            self.anti_path_separator = '\\'

    def setPathSeparators(self, filepath):
        ''' 
            Reconfigures filepath to OS specific conventions and automatically 
            runs troubleshooting measures.
            Returns corrected strings of both the filepath and directory.
        '''

        if self.anti_path_separator in filepath:
            filepath = filepath.replace(
                self.anti_path_separator, self.path_separator
                )
        path_list = filepath.split(self.path_separator)
        path_dir = ''
        for seg in path_list[:-1]:
            path_dir += seg + self.path_separator
        if path.isdir(path_dir):
            return [filepath, path_dir]
        #   Check for landing error     #
        print(path_list)
        if '.' not in path_dir[0] or ':' not in path_dir[0:3]:
            LandingChecks = ['.', '.' + self.path_separator] 
            for LandingCheck in LandingChecks:
                if path.isdir(path_dir):
                    continue
                if path.isdir(LandingCheck + path_dir):
                    path_dir = LandingCheck + path_dir
        filepath = path_dir + path_list[-1]
        if not path.isdir(path_dir):
            raise FileNotFoundError('Could not locate directory %s'% path_dir)
        return [filepath, path_dir]
