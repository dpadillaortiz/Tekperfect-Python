#! /usr/bin/python3

import csv
import sys
import csv_python_basic as cpb


'''
Let's print one of the files we have
In the main function:
path = f'{sampleDir}{sys.argv[1]}'
cpb.readFile(path)
'''

   
'''
['   41', '    9', '   35', ' "N"', '     81', '   14', '   23', ' "W"', ' "Ravenna"', ' OH ']

This is the current output. We need to clean up the extra spaces.

Task: Remove the extra spacing from the start and end of each item
- Clean up any additional fluff
'''

def clean(file):
   with open(file, 'r') as f:
      reader = csv.reader(f)
      # Introduce enumerate 
      for index, row in enumerate(reader):
         # Introduce range-len
         for item in range(len(row)):
            # Added .strip(") to remove the extra "
            row[item] = cpb.trim(row[item]).strip('"')
         print(row)
             

'''
['133', '145', '26', '7', '3', '1', '42', '0.36', '3059']

This output has been cleaned up. Let's change it so that it writes to a file
'''
def writeClean(input, output):
   cleanRows = []
   with open(input, 'r') as f:
      reader = csv.reader(f)
      for index, row in enumerate(reader):
         cleanRows.append(cleanRow(row))
   print(cleanRows)
   cpb.writeManyRows(output, 'w', cleanRows)

# Can define functions anywhere

def cleanRow(row):
   assert type(row) == type([]), 'Argument passed to cleanRow was not a list'
   for col, item in enumerate(row):
      row[col] = cpb.trim(item).strip('"')
   return row

if __name__ == '__main__':
   inputDir = 'Input-CSV/'
   outputDir = 'Output-CSV/'
   sampleDir = 'Sample-CSV/'

   path = f'{sampleDir}{sys.argv[1]}'
   print("Original File")
   cpb.readFile(path)

   print("Cleaned File")
   clean(path)

   print("Writing to new file")
   writeClean(path, f'{outputDir}{sys.argv[2]}')
   print('Printing the new file')
   cpb.readFile(f'{outputDir}{sys.argv[2]}')
