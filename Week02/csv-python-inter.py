#!/usr/local/bin/python3

import sys
import csv

'''
Simple csv writer
- how to write a row to a csv
- use 'a' to append to the file
- using 'w' will overwrite the file contents
'''

def simpleWrite():
   CSV_FILE = f'Sample-CSV/{sys.argv[1]}'  
   with open(CSV_FILE, 'a') as csvfile:
      writeToCSV = csv.writer(csvfile)
      writeToCSV.writerow([1,2,3,4,5,6,7])

INPUT = f'Input-CSV/{sys.argv[1]}'
OUTPUT = f'Input-CSV/{sys.argv[2]}'

'''
IF function
Syntax: =IF(logical test, value if true, value if false)

zillow.csv has 7 headers
'''
def budget(budget):
   with open(INPUT, 'r') as f:
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

def budget(price, budget):
   if int(price) <= budget:
      return True

def withinBudget(budget):
   with open(INPUT, 'r') as r:
      with open(OUTPUT, 'w') as w:
         csvReader = csv.reader(f)
         csvWriter = csv.writer(c)
         for row in csvReader:
            if 'Index' in row:
               csvWriter.writerow(row + ['Within Budget'])
               continue
            if budget(row[6], budget):
               csvWriter.writerow(row + ['Yes'])
            else:
               csvWriter.writerow(row + ['No'])



'''
CONCATENATE function
Syntax: =CONCATENATE(text1, text2, ...)
'''

def fullname(first, last):
   fullname = f'{first} {last}'
   return fullname

def username(f_initial, last_name):
   user = f_initial + last_name
   return user

def email(user):
   email = f'{user}@tekperfect.com'
   return email

def employee():
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
   
'''
FILTER funciton
Syntax: =FILTER(array, include, if empty)
'''
def withinBudget(budget):
   if budget == 'Yes':
      print(budget)

def availableRooms(rooms):
   desiredRooms = 3
   if rooms <= desiredRooms:
      return True

def budgetFilter():
   with open(INPUT,'r') as r:
      csvReader = csv.reader(r)
      for index,row in enumerate(csvReader):
         if index == 0:
            continue
         if row[7] == 'Yes':
            print(row)   
         
def myFilter():
   with open(INPUT,'r') as r:
      csvReader = csv.reader(r)
      for index, row in enumerate(csvReader):
         if index == 0:
            continue
         if availableRooms(int(row[2])):
            print(row)
            

if __name__ == '__main__':
   print('Adding the budget column')
   withinBudget(200000)
   print('Houses under my budget')
   budgetFilter()
   print('Houses with 3 rooms or less')
   myFilter()










