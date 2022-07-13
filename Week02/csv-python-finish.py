#!/usr/local/bin/python3

import sys
import csv

#INPUT = f'Input-CSV/{sys.argv[1]}'
#OUTPUT = f'Output-CSV/{sys.argv[2]}'

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

def concatenate(*args):
   new = ''
   for word in args:
      assert type(word) == type(new), f'{word} is not a string'
      new += word
   return new

def left(word, pos):
   assert type(word) == type(''), f'{word} is not a string'
   new = word[:pos]
   return new

def right(word, pos):
   assert type(word) == type(''), f'{word} is not a string'
   new = word[(pos-1):]
   return new


def budgetFilter(within_budget):
   if within_budget == 'Yes':
      return True

          

if __name__ == '__main__':
   c = concatenate('w','e','MEME')
   print(c)
   l = left('California', 3)
   print(l)
   r = right('California', 3)
   print(r)




