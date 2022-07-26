#!/usr/local/bin/python3

import sys
import csv

def readFile(file):
   with open(file, 'r') as f:
      csvfile = csv.reader(f)
      for row in csvfile:
         print(row)

def sysmodule():
   script, first, second = sys.argv
   print(f'This is the name of the script: {script}')
   print(f'This is the first arguement: {first}')
   print(f'This is the second arguement: {second}')

def writeOneRow(file, mode, row):
   with open(file, mode) as f:
      writer = csv.writer(f)
      writer.writerow(row)

def writeManyRows(file, mode, rows):
   with open(file, mode) as f:
      writer = csv.writer(f)
      writer.writerows(rows)

def concantenate(*args):
   new = ''
   for word in args:
      assert type(word) == type(new), f'{word} is not a string'
      new += word
   return new

def left(word, position):
   assert type(word) == type(''), f'{word} is not a string'
   leftSide = word[:position]
   return leftSide

def trim(word):
   assert type(word) == type(''), f'{word} is not a string'
   return word.strip()

print('Hello')

if __name__ == '__main__':
   print('Runs from command') 
