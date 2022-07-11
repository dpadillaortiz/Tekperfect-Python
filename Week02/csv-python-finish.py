#!/usr/local/bin/python3

import sys
import csv

INPUT = f'Input-CSV/{sys.argv[1]}'
OUTPUT = f'Output-CSV/{sys.argv[2]}'

def printFile(file):
   with open(file, 'r') as f:
      reader = csv.reader(f)
      for row in reader:
         print(row)

def writeOneRow(file, mode, row):
   with open(file, mode) as f:
      writer = csv.writer(f)
      writer.writerow(row)

def writeManyRows(file, mode, rows):
   with open(file, mode) as f:
      writer = csv.writer(f)
      writer.writerows(rows)


def withinBudget(price, budget):
   assert type(price) == type(budget) == type(20), 'non int was passed to `withinBudget`'
   if price <= budget:
      return True

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

def budgetFilter(within_budget):
   if within_budget == 'Yes':
      return True

          

if __name__ == '__main__':






