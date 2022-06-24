#!/usr/bin/python3

# What if we wanted to do this for multiple inputs?

# Intro to Functions
# - talk about parameters
# - in scope variables

def pythm(a,b):
   aSide = a
   bSide = b
    
   aBSide = aSide**2 + bSide**2

   cSide = aBSide**(1/2)

   # Talk about return
   return cSide

# note parameters should be a tuple

# Introduce assert
# - checks to test that a condition is met
# - if not, raises an AssertionError with optional msg
def slopeFormula(cord1, cord2):
   assert type(cord1) == type(()) and type(cord2) == type(()), 'Expected a tuple'
   
   # unpacking a tuple 
   xPoint1, yPoint1 = cord1
   xPoint2, yPoint2 = cord2

   rise = yPoint2 - yPoint1
   run = xPoint2 - xPoint1

   slope = rise/run

   return slope

# Won't display anthing to us
slopeFormula((1,2), (2,4))

# Now it will but doesn't need to be assigned to variable
# can be done by passing the function to print()
x = slopeFormula((1,2), (2,4))
print(x)


