#!/usr/local/bin/python3

import sys
import csv
import csv_python_basic as cpb

'''
IF function
Syntax: =IF(logical test, value if true, value if false)
'''
def budgetFilter(within_budget):
   if within_budget == 'Yes':
      return True

def roomFilter(listing_rooms, min_rooms = None, max_rooms = None):
   if max_rooms != None and (listing_rooms < min_rooms or listing_rooms > max_rooms):
      return False
   elif listing_rooms < min_rooms:
      return False
   else:
      return True
 
def withinBudget(price, budget):
   assert type(price) == type(budget) == type(20), 'non int was passed to `withinBudget`'
   if price <= budget:
      return True


def budget(file, budget):
   assert type(budget) == type(20), 'non int was passed to `budget`'
   budgetColumn = []
   with open(file, 'r') as f:
      reader = csv.reader(f)
      for index, row in enumerate(reader):
         listingPrice = row[-1]
         if index == 0:
            budgetColumn.append('Within Budget')
         elif withinBudget(int(listingPrice), budget):
            budgetColumn.append('Yes')
         else:
            budgetColumn.append('No')
   print(budgetColumn)
   cpb.writeOneRow(file, 'a', budgetColumn)


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
   print(updatedRows)
   for row in updatedRows:
      print(row)
   with open(OUTPUT, 'w') as f:
      csvWriter = csv.writer(f)
      csvWriter.writerows(updatedRows)

   
'''
FILTER funciton
Syntax: =FILTER(array, include, if empty)
'''

  
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
   inputDir = 'Input-CSV/'
   outputDir = 'Output-CSV/'
   sampleDir = 'Sample-CSV/'

   path = f'{outputDir}{sys.argv[1]}'
   print('Adding the budget column')
   budget(path,200000)  
   cpb.readFile(path)   
   #print('Employee Info')
   #employee()
   #print('Houses under my budget')
   #applyBudgetFilter()
   #print('Houses with 3 rooms or less')
   #applyRoomFilter(1,3)










