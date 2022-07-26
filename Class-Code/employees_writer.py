import sys
import csv
import csv_tools as csvtools

class Employee():
   
   def fullname(self, first_name, last_name):
      name = csvtools.concantenate(first_name, ' ', last_name)
      return name

   def username(self, first_name, last_name):
      f_initial = csvtools.left(first_name,1)
      user = csvtools.concantenate(f_initial, last_name).lower()
      return user

   def email(self, user):
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

def add_emp_info(first_name, last_name):
   name = Employee().fullname(first_name, last_name)
   user = Employee().username(first_name, last_name)
   email = Employee().email(user)

   return [name, user, email]

def run():
   updatedRows = []
   readFrom = sys.argv[1]
   writeTo = sys.argv[2]
   
   with open(readFrom) as f:
      reader = csv.reader(f)
      for index, row in enumerate(reader):
         if index == 0:
            updatedRows.append(row)
         else:
            first_name = csvtools.trim(row[0])
            last_name = csvtools.trim(row[1])
            updatedRows.append(row + add_emp_info(first_name, last_name))
   
   csvtools.writeManyRows(writeTo, 'w', updatedRows)
   csvtools.readFile(writeTo)

run()
