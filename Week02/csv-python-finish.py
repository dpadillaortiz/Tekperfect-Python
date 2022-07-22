#!/usr/local/bin/python3

import sys
import csv
import csv_python_basic as cpb

class Employee():

   def fullname(self, first_name, last_name):
      assert type(first_name) == type(last_name) == type(''), 'non str was passed to `fullname`'
      fullname = cpb.concatenate(first_name, ' ', last_name)
      return fullname

   def username(self, first_name, last_name):
      assert type(first_name) == type(last_name) == type(''), 'non str was passed to `username`'
      f_initial = cpb.left(first_name, 1)
      user = cpb.concatenate(f_initial, last_name).lower()
      return user

   def email(self, user):
      assert type(user) == type(''), 'non str was passed to `email`'
      email = f'{user}@tekperfect.com'
      return email
  
   def email_group(self, dept):
      departments = {'Engineering': email('eng-dept'), 
         'Security': email('sec-dept'),
         'CSM': email('csm-dept'),
         'IT': email('it-dept'),
         'Human Resources': email('hr-dept')
      }
      return departments[dept]

def add_emp_info(first, last):
   fullname = Employee().fullname(first, last)
   first_initial = cpb.left(first, 1)
   username = Employee().username(first_initial, last)
   email = Employee().email(username)
   return [fullname, username, email]

def main():
   inputDir = 'Input-CSV/'
   outputDir = 'Output-CSV/'
   sampleDir = 'Sample-CSV/'
   
   updatedRows = []
   with open(f'{inputDir}{sys.argv[1]}') as f:
      reader = csv.reader(f)
      for index, row in enumerate(reader):
          if index == 0:
             updatedRows.append(row)
          else:
             if len(row) == 0:
                continue
             print(row)
             first_name = row[0]
             last_name = row[1]
             updatedRows.append(row + add_emp_info(first_name, last_name)) 
   print(updatedRows)
   with open(f'{outputDir}{sys.argv[2]}', 'w') as f:
      writer = csv.writer(f)
      writer.writerows(updatedRows)
   cpb.readFile(f'{outputDir}{sys.argv[2]}')


if __name__ == '__main__':
   main()

