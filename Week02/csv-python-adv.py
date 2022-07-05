#!/usr/local/bin/python3

import sys
import csv

CSV_FILE = sys.argv[1]

'''
Default
- how to write a row to a csv
- use 'a' to append to the file
- using 'w' will overwrite the file contents
'''
'''
with open(CSV_FILE, 'a') as csvfile:
   writeToCSV = csv.writer(csvfile)
   writeToCSV.writerow([1,2,3,4,5,6,7])
'''
'''
IF function
Syntax: =IF(logical test, value if true, value if false)

zillow.csv has 7 headers
'''

def fileLength():
   with open(CSV_FILE, 'r') as f:
      file = f.readlines()
      return len(file)

fileLength()

def budget(budget):
   '''
   - Need to open the csv file to read it
      - if the condition is true, save into a variable
   - Need to open the csv file to write to it
      - write to list from above to the csv file
   '''
   newRows = []
   with open(CSV_FILE, 'r') as f:
      csvFile = csv.reader(f)
      for row in csvFile:
         if 'Index' in row:
            yo = row.append(['Within budget'])
            newRows.append(yo)
            continue
         if int(row[6]) <= int(budget):
            yo = row.append(['Yes'])
            newRows.append(yo)
         else:
            yo = row.append(['No'])
            newRows.append(yo)
   print(newRows)
   
   with open(CSV_FILE, 'w') as f:
      csvFile = csv.writer(f)
      for row in newRows:
         csvFile.writerow([row])
         

budget(200000)
# CONCATENATE function

# VLOOKUP function

# UNIQUE function

# FILTER funciton


