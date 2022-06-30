#! /usr/bin/python3

import csv
import sys

# Introducing sys module

def sysModule():
   script, first, second = argv
   print(f'This is the script being called: {script}')
   print(f'This is the first arguement pass: {first}')
   print(f'This is the second arguement pass: {second}')

# Introducing csv module

FILE = f'Sample-CSV/{sys.argv[1]}'

# Simple csv reader in function
def csvModule():
   with open(FILE, 'r') as f:
      csvFile = csv.reader(f)
      for row in csvFile:
         print(row)
'''
Task: Create function that will read and print a csv from Sample-CSV 
- Pass one of the sample csvs with sys argv
- Print csv and remove any empty rows
'''
def printFile(file):
   with open(file, 'r') as csvFile:
      csvData = csv.reader(csvFile)
      for row in csvData:
         if len(row) > 1:
            print(row)

# printFile(FILE)

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

#cleanOutput(FILE)

'''
['133', '145', '26', '7', '3', '1', '42', '0.36', '3059']

This output has been cleaned up. Let's change it so that it writes to a file
'''

def loopThru(row):
   newRow = []
   for i in range(len(row)):
      if len(row) <= 1:
         print('yo')
         continue
      newRow.append(row[i].strip().strip('"'))
   return newRow

def loopThruCSV(csvFile):
   cleanRow = []
   for row in csvFile:
      if len(row) <= 1:
         continue
      for i in range(len(row)):
         cleanRow.append(row[i].strip().strip('"'))
      return cleanRow
   

def cleanToFile(clean, output):
   with open(clean, 'r') as csvRead:
      with open(output, 'w') as csvWrite:
      
         csvToClean = csv.reader(csvRead)
         ctcLength = len(csvRead.readlines())
         csvToWrite = csv.writer(csvWrite)
         
         for row in range(ctcLength):
            cleanRow = loopThruCSV(csvToClean)   
            print(cleanRow)
            #csvToWrite.writerow(cleanRow)

'''
         for row in csvToClean:
            if len(row) <= 1:
               continue
            print(loopThru(row))
            csvToWrite.writerow(loopThru(row))  
'''
cleanToFile(FILE, 'test.csv')
