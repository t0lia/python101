#!/usr/local/bin/python3
import os
import sys

if len(sys.argv) != 2:
    print(f"Please use 1 argument", file=sys.stderr)
    exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename):
    print(f"File doesn't exist", file=sys.stderr)
    exit(2)

with open(sys.argv[1], 'r') as reader:
    print(f"Please use 1 argument", file=sys.stderr)
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()
