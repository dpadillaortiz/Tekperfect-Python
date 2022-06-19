#! /usr/bin/python3

import csv
import sys

FILE = sys.argv[1]

with open(FILE, newline='') as csvFile:
    data = csv.reader(csvFile)
    for row in data:
        print(row)
