#!/usr/local/bin/python3

import sys
import csv


# Introducing sys module

def sysModule():
   script, first, second = argv
   print(f'This is the script being called: {script}')
   print(f'This is the first arguement pass: {first}')
   print(f'This is the second arguement pass: {second}')

#INPUT = f'Input-CSV/{sys.argv[1]}'
#OUTPUT = f'Output-CSV/{sys.argv[2]}'


# Introducing csv module

def readFile(file):
   with open(file, 'r') as f:
      reader = csv.reader(f)
      for row in reader:
         print(row)
def test_read_file(file):
   readFile(file)

def writeOneRow(file, mode, row):
   with open(file, mode) as f:
      writer = csv.writer(f)
      writer.writerow(row)
def test_write_one_row(file, mode, row):
   writeOneRow(file, mode, row)
   readFile(file)

def writeManyRows(file, mode, rows):
   with open(file, mode) as f:
      writer = csv.writer(f)
      writer.writerows(rows)
def test_write_many_rows(file, mode, rows):
   writeManyRows(file, mode, rows)
   readFile(file)


# Excel functions

'''
CONCATENATE function
Syntax: =CONCATENATE(text1, text2, ...)
The CONCATENATE function combines the values from multiple cells into one.
'''
def concatenate(*args):
   new = ''
   for word in args:
      assert type(word) == type(new), f'{word} is not a string'
      new += word
   return new
def test_concatenate(*args):
   c = concatentate(*args)
   print(c)

'''
LEFT function
Syntax: =LEFT(text, num chars)
The LEFT function will extract a specified number of characters from the start and end of text.
'''
def left(word, pos):
   assert type(word) == type(''), f'{word} is not a string'
   leftSide = word[:pos]
   return leftSide
def test_left(word, pos):
   l = left(word, pos)
   print(l)

'''
RIGHT function
Syntax: =RIGHT(text, num chars)
The RIGHT function will extract a specified number of characters from the start and end of text.
'''
def right(word, pos):
   assert type(word) == type(''), f'{word} is not a string'
   rightSide = word[(pos-1):]
   return rightSide
def test_right(word, pos):
   r = right(word, pos)
   print(r)

'''
TRIM function
Syntax: =TRIM(text)
This brilliant function will remove all spaces from a cell except the single spaces between words.
'''
def trim(word):
   assert type(word) == type(''), f'{word} is not a string'
   return word.strip()
def test_trim(word):
   t = trim(word)
   print(t)

'''
UNIQUE function
Syntax: =UNIQUE(array, by col, exactly once)
'''
def unique(array):
   assert type(array) == type([]), f'{array} is not a list'
   return set(array)
def test_unique(array):
   u = unique(array)
   print(u)

'''
SORT function
Syntax: =SORT(array, sort index,sort order, by col)
'''
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
   
