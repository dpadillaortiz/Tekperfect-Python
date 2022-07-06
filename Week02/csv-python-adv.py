#!/usr/local/bin/python3

import sys
import csv

CSV_FILE = f'Sample-CSV/{sys.argv[1]}'

'''
Default
- how to write a row to a csv
- use 'a' to append to the file
- using 'w' will overwrite the file contents
'''

def simpleWrite():
   with open(CSV_FILE, 'a') as csvfile:
      writeToCSV = csv.writer(csvfile)
      writeToCSV.writerow([1,2,3,4,5,6,7])

'''
IF function
Syntax: =IF(logical test, value if true, value if false)

zillow.csv has 7 headers
'''
def budget(budget):
   OUTPUT = 'Output-CSV/budget.csv'
   with open(CSV_FILE, 'r') as f:
      with open(OUTPUT, 'w') as c:
         csvReader = csv.reader(f)
         csvWriter = csv.writer(c)
         for row in csvReader:
            if 'Index' in row:
               csvWriter.writerow(row + ['Within Budget'])
               continue
            if int(row[6]) <= int(budget):
               csvWriter.writerow(row + ['Yes'])
            else:
               csvWriter.writerow(row + ['No'])

'''
CONCATENATE function
Syntax: =CONCATENATE(text1, text2, ...)
'''
INPUT = f'Output-CSV/{sys.argv[1]}'

def fullname(first, last):
   fullname = f'{first} {last}'
   return fullname

def username(f_initial, last_name):
   user = f_initial + last_name
   return user

def email(user):
   email = f'{user}@tekperfect.com'
   return email

def name():
   OUTPUT = 'Output-CSV/fullname.csv'
   with open(INPUT,'r') as r:
      with open(OUTPUT,'w') as w:
         csvReader = csv.reader(r)
         csvWriter = csv.writer(w)
    
         for index, row in enumerate(csvReader):
            if index == 0:
               csvWriter.writerow(row)
            else:
               csvWriter.writerow(row+[fullname(row[0], row[1])])

def emp_data():
   OUTPUT = 'Output-CSV/fullname.csv' 
   with open(INPUT,'r') as r:
      with open(OUTPUT,'w') as w:
         csvReader = csv.reader(r)
         csvWriter = csv.writer(w)
    
         for index, row in enumerate(csvReader):
            name = fullname(row[0], row[1])
            user = username(name[0], row[1]).lower()
            mail = email(user)
            if index == 0:
               csvWriter.writerow(row)
            else:
               csvWriter.writerow(row + [name, user, mail])
   
emp_data()

# VLOOKUP function

# UNIQUE function

# FILTER funciton


