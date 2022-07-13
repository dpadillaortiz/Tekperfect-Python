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
def test_print_file(file):
   printFile(file)

def writeOneRow(file, mode, row):
   with open(file, mode) as f:
      writer = csv.writer(f)
      writer.writerow(row)
def test_write_one_row(file, mode, row):
   writeOneRow(file, mode, row)
   printFile(file)

def writeManyRows(file, mode, rows):
   with open(file, mode) as f:
      writer = csv.writer(f)
      writer.writerows(rows)
def test_write_many_rows(file, mode, rows):
   writeManyRows(file, mode, rows)
   printFile(file)

def concatenate(*args):
   new = ''
   for word in args:
      assert type(word) == type(new), f'{word} is not a string'
      new += word
   return new
def test_concatenate(*args):
   c = concatentate(*args)
   print(c)

def left(word, pos):
   assert type(word) == type(''), f'{word} is not a string'
   leftSide = word[:pos]
   return leftSide
def test_left(word, pos):
   l = left(word, pos)
   print(l)

def right(word, pos):
   assert type(word) == type(''), f'{word} is not a string'
   rightSide = word[(pos-1):]
   return rightSide
def test_right(word, pos):
   r = right(word, pos)
   print(r)

def trim(word):
   assert type(word) == type(''), f'{word} is not a string'
   return word.strip()
def test_trim(word):
   t = trim(word)
   print(t)

def unique(array):
   assert type(array) == type([]), f'{array} is not a list'
   return set(array)
def test_unique(array):
   u = unique(array)
   print(u)

def sort(array, order):
   assert type(array) == type([]), f'{array} is not a list'
   assert type(order) == type(''), f'{order} is not a str'
   assert order.lower() in ['a', 'd'], f'Order must be "a" for ascending or "b" for descending'
   if order.lower() == 'a':
      array.sort()
      return array
   else:
      array.sort(reverse=True)  
      return array
def test_sort(array, order):
   s = sort(array, order)
   print(s)

if __name__ == '__main__':
   print('Testing unique')
   toBeUnique = ['a','a','apple','mate',1,1]
   test_unique(toBeUnique)

   print('Testing sort')
   toBeSorted = ['star', 'wars', 'darth', 'vader']
   test_sort(toBeSorted, 'a')
   test_sort(toBeSorted, 'd')
   
