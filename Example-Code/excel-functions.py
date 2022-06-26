#! /usr/bin/python3

import csv
import sys

# Adding this so that we don't have to make changes to the file to change file names

FILE = f'Sample-CSV/{sys.argv[1]}'

# Using python to print the file
def printFile(file):
   with open(FILE, 'r') as csvFile:
      csvData = csv.reader(csvFile)
      for row in csvData:
         if len(row) > 1:
            print(row)


'''
['   41', '    9', '   35', ' "N"', '     81', '   14', '   23', ' "W"', ' "Ravenna"', ' OH ']

This is the current output. We need to clean up the extra spaces.
'''

def cleanOutput(file):
   with open(FILE, newline='') as csvFile:
      csvData = csv.reader(csvFile)
      for row in csvData:
         for i in range(len(row)):
            row[i] = row[i].strip().strip('"')
         print(row)

'''
['133', '145', '26', '7', '3', '1', '42', '0.36', '3059']

This output has been cleaned up. Let's change it so that it writes to a file
'''

def loopThru(data):
   newRow = []
   for i in range(len(data)):
      newRow.append(data[i].strip())
   return newRow

        
def cleanToFile(clean, output):
   with open(clean, 'r') as csvRead:
      with open(output, 'w') as csvWrite:
      
         csvToClean = csv.reader(csvRead)
         csvToWrite = csv.writer(csvWrite)

         for row in csvToClean:
            if len(row) == 1:
               continue
            print(loopThru(row))
            csvToWrite.writerow(loopThru(row))  
 

