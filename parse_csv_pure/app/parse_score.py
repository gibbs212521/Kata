#! usr/bin/env python3
from sys import argv
from platform import system as CURRENT_OS

    ### OS Check for filepath purposes  ###
OS = CURRENT_OS()
if 'Windows' in OS:
    division = '\\'
else: # Linux or Darwin
    division = '/'


# Determine if system is Linux or Windows

print(argv)
print(argv[1])
print(argv[2])

