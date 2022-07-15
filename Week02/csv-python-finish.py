#!/usr/local/bin/python3

import sys
import csv
import csv_python_basic as cpb

class Housing:
   def withinBudget(price, budget):
      assert type(price) == type(budget) == type(20), 'non int was passed to `withinBudget`'
      if price <= budget:
         return True

   def budgetColumn(file, budget):
      assert type(budget) == type(20), 'non int was passed to `budget`'
      updatedRows = []
      with open(file, 'r') as f:
         reader = csv.reader(f)
         for index, row in enumerate(reader):
            listingPrice = row[-1]
            if index == 0:
               updatedRows.append(row + ['Within Budget'])
            elif withinBudget(int(listingPrice), budget):
               updatedRows.append(row + ['Yes'])
            else:
               updatedRows.append(row + ['No'])
      cpb.writeManyRows(file, 'w', updatedRows)

   def budgetFilter(file, price, budget):
      assert type(budget) == type(20), 'non int was passed to `budget`'
      with open(file, 'r') as f:
         reader = csv.reader(f)
         for index, row in enumerate(reader):
            if index == 0:
               print(row)
            elif withinBudget(price, budget):
               print(row)

class Employee:
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

   def additionalInfo(first, last):
      fullname = Employee.fullname(first, last)
      firstInitial = cpb.left(first, 1)
      username = Employee.username(firstInitial, last)
      email = Employee.email(username)
      return [fullname, username, email]


def writeEmployeeInfo(file):
   updatedRows = []
   with open(file, 'r') as f:
      reader = csv.reader(f)
      for index, row in enumerate(reader):
         print(row)
         print(row[0])
'''
         firstname = row[0]
         lastname = row[1]
         if index == 0:
            updatedRows.append(row)
         else:
            info = Employee.additionalInfo(firstname, lastname)
            updatedRows.append(info)
   print(updatedRows)
'''
if __name__ == '__main__':
   inputDir = 'Input-CSV/'
   outputDir = 'Output-CSV/'
   sampleDir = 'Sample-CSV/'

   #Housing.budgetColumn(f'{inputDir}zillow.csv', 200000)

   writeEmployeeInfo(f'{inputDir}employees.csv')




