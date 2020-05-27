#! usr/bin/env python3
from sys import argv
from os import path

from lib.auxilliary.csv.csv_scorer import CSV_Scorer

### Kata for sorting names of top score contenders of a given .csv ###
#
#   input   :   .csv file with rows consisting of [NAME],[SURNAME],[SCORE]
#   output  :   plain text file containing top score names
#
###


    ### Retrieve and handle input and output filepaths  ###

INPUT_PATH = argv[1]
OUTPUT_PATH = argv[2]
if len(argv) > 3:
    MAX_NAME_LENGTH = argv[3]
else:
    MAX_NAME_LENGTH = 25

csv_scorer = CSV_Scorer(INPUT_PATH, OUTPUT_PATH, MAX_NAME_LENGTH)




    ### troubleshoot input and output filepaths  ###
#################################################################### Functionalize --> OOP
for indx, path in enumerate([input_dir, output_dir]):
        ##  In case of lacking initial landing    ##
    if path.isdir(path):
        continue
    if '.' != path[0]   # check if landing point is missing present directory character
        if path.isdir('.'+path):
            path = '.' + path
        if 


print(path.exists(argv[0]), path.isdir(input_dir))

    ### OS Check for filepath purposes  ###


# Determine if system is Linux or Windows

print(argv)
print(argv[1])
print(argv[2])

