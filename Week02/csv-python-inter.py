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
OUTPUT = f'Output-CSV/{sys.argv[2]}'

'''
IF function
Syntax: =IF(logical test, value if true, value if false)

zillow.csv has 7 headers
'''

def withinBudget(price, budget):
   assert type(price) == type(budget) == type(20), 'non int was passed to `withinBudget`'
   if price <= budget:
      return True

def budget(budget):
   updatedRows = []
   assert type(budget) == type(20), 'non int was passed to `budget`'
   with open(INPUT, 'r') as f:
      csvReader = csv.reader(f)
      for row in csvReader:
         if 'Index' in row:
            updatedRows.append(row + ['Within Budget'])
            continue
         listingPrice = int(row[6]) 
         if withinBudget(listingPrice, budget):
            updatedRows.append(row + ['Yes'])
         else:
            updatedRows.append(row + ['No'])
   
   for row in updatedRows:
      print(row)

   with open(OUTPUT, 'w') as f:
      csvWriter = csv.writer(f)
      csvWriter.writerows(updatedRows)
   

'''
CONCATENATE function
Syntax: =CONCATENATE(text1, text2, ...)
'''

def fullname(first, last):
   assert type(first) == type(last) == type(''), 'non str was passed to `fullname`'
   fullname = f'{first} {last}'
   return fullname

def username(f_initial, last_name):
   assert type(f_initial) == type(last_name) == type(''), 'non str was passed to `username`'
   user = f_initial + last_name
   return user.lower()

def email(user):
   assert type(user) == type(''), 'non str was passed to `email`'
   email = f'{user}@tekperfect.com'
   return email.lower()

# Introducing enumerate()
def employee():
   updatedRows = []
   with open(INPUT, 'r') as f:
      csvReader = csv.reader(f)
      for line, row in enumerate(csvReader):
         if line == 0:
            updatedRows.append(row)
         else:
            first = row[0]
            last = row[1]
            user = username(first[0], last)
            newData = [fullname(first, last), user, email(user)]
            updatedRows.append(row + newData)
   for row in updatedRows:
      print(row)
   with open(OUTPUT, 'w') as f:
      csvWriter = csv.writer(f)
      csvWriter.writerows(updatedRows)

   
'''
FILTER funciton
Syntax: =FILTER(array, include, if empty)
'''

def budgetFilter(within_budget):
   if within_budget == 'Yes':
      return True

def roomFilter(listing_rooms, min_rooms = None, max_rooms = None):
   if max_rooms != None:
      if listing_rooms < min_rooms or listing_rooms > max_rooms:
         return False
   elif listing_rooms < min_rooms:
      return False
   else:
      return True
   
def applyBudgetFilter():
   with open(OUTPUT, 'r') as f:
      csvReader = csv.reader(f)
      for line, row in enumerate(csvReader):
         budgetCol = row[7]
         if line == 0:
            print(row)
         elif budgetFilter(budgetCol):
            print(row)
          
def applyRoomFilter(min = None, max = None):
   with open(INPUT, 'r') as f:
      csvReader = csv.reader(f)
      for line, row in enumerate(csvReader):
         listingRooms = row[2]
         if line == 0:
            print(row)
         elif max != None:
            if roomFilter(int(listingRooms), int(min), int(max)):
               print(row)
         elif roomFilter(int(listingRooms), int(min)):
            print(row)
           

if __name__ == '__main__':
   print('Adding the budget column')
   budget(200000)  
   #print('Employee Info')
   #employee()
   print('Houses under my budget')
   applyBudgetFilter()
   print('Houses with 3 rooms or less')
   applyRoomFilter(3)










