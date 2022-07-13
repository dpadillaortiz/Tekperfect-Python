#! /usr/bin/python3

import csv
import sys
import csv_python_basic as cpb

def printFile(file):
   with open(file, 'r') as csvFile:
      csvData = csv.reader(csvFile)
      for row in csvData:
         if len(row) > 1:
            print(row)


'''
['   41', '    9', '   35', ' "N"', '     81', '   14', '   23', ' "W"', ' "Ravenna"', ' OH ']

This is the current output. We need to clean up the extra spaces.

Task: Remove the extra spacing from the start and end of each item
- Clean up any additional fluff
'''
def cleanOutput(file):
   with open(file, newline='') as csvFile:
      csvData = csv.reader(csvFile)
      for row in csvData:
         if len(row) <= 1:
            continue
         for i in range(len(row)):
            row[i] = row[i].strip().strip('"')
         print(row)


'''
['133', '145', '26', '7', '3', '1', '42', '0.36', '3059']

This output has been cleaned up. Let's change it so that it writes to a file
'''

def loopThru(row):
   cleanRow = []
   for i in range(len(row)):
      cleanRow.append(row[i].strip().strip('"'))
   return cleanRow

FILE = f'Sample-CSV/{sys.argv[1]}'
CLEANED = f'Input-CSV/{sys.argv[2]}'

def cleanToFile(input, output):
   with open(input, 'r') as csvRead:
      with open(output, 'w') as csvWrite:
      
         csvToClean = csv.reader(csvRead)
         csvToWrite = csv.writer(csvWrite)
         
         for row in csvToClean:
            if len(row) <= 1:
               continue
            cleanRow = loopThru(row)
            print(cleanRow)
            csvToWrite.writerow(cleanRow)

if __name__ == '__main__':
   print('Hello, World!')
   cleanToFile(FILE, CLEANED)
