#! /usr/bin/env python3
from sys import argv, path
from os import path as os_path

try:
    libpath = os_path.realpath(__file__ + './../../..')
except Exception:
    libpath = os_path.realpath(__file__ + '.\\..\\..\\..')
path.insert(0, libpath)

from lib.auxilliary.csv.csv_scorer import CSVScorer

### Kata for sorting names of top score contenders of a given .csv ###
#
#   input   :   .csv file with rows consisting of [NAME],[SURNAME],[SCORE]
#   output  :   plain text file containing top score names
#
###


    ### Retrieve and handle input and output filepaths  ###

if len(argv) == 1:
    INPUT_PATH = None
    OUTPUT_PATH = None
else:
    INPUT_PATH = argv[1]
    OUTPUT_PATH = argv[2]

if len(argv) > 3:
    MAX_NAME_LENGTH = argv[3]
else:
    MAX_NAME_LENGTH = 25

    ### Implement CSV Classes ###

csv_scorer = CSVScorer(INPUT_PATH, OUTPUT_PATH, MAX_NAME_LENGTH)



# Determine if system is Linux or Windows

print(argv)
print(argv[1])
print(argv[2])

