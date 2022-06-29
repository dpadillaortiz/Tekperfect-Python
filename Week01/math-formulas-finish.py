#!/usr/bin/python3
'''
Intro to Functions
- talk about parameters
- in scope variables
'''
def pythm(a,b):
   aSide = a
   bSide = b
    
   aBSide = aSide**2 + bSide**2

   cSide = aBSide**(1/2)

   # Talk about return
   return cSide


print(pythm(3,4))

print('I can add the return value of python to something else like so:')
print('pythm + {0} => {1} + {0}'.format(5,pythm(3,4)))
'''
Introduce assert
- checks to test that a condition is met
- if not, raises an AssertionError with optional msg

When creating this function, we want to check that the args passed to the function
are tuples. We can do that with and if statement or we can use assert statement
'''
def slopeFormula(cord1, cord2):
   # Circle back to operators -> comparison
   assert type(cord1) == type(()) and type(cord2) == type(()), 'Expected a tuple'
   
   # unpacking a tuple 
   xPoint1, yPoint1 = cord1
   xPoint2, yPoint2 = cord2

   rise = yPoint2 - yPoint1
   run = xPoint2 - xPoint1

   slope = rise/run

   print('The slope of the line containing points {} and {} is {}'.format(cord1, cord2,slope))
   return slope

# We see that slopeFormula did not print only the slope - it printed the print statement
print('This is the function call')
slopeFormula((1,2), (2,4))

# This will cause the print statement to get executed
print('This is the function call assigned to a variable')
x = slopeFormula((1,2), (2,4))

# This will print out the return statement
print('This is printing the function call i.e. the return value')
print(x)


