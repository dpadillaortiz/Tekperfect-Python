#! /Usr/bin/python3

# Math Formulas

'''
Pythagoreom Theorem
c^2 = a^2 + b^2
=> c = sqrt(a^2 + b^2)

c represents the hypothenuse 
a, b represent the other two sides
'''

# Intro to input()
print('Enter input for pythagoreom theroem:')
# Anything passed into input becomes a str - use int() to convert to int
aSide = int(input('Side a: '))
bSide = int(input('Side b: '))
aBSide = aSide**2 + bSide**2
cSide = aBSide**(1/2)
# A + sign will concatenate a str so need to turn cSide to str since it's int
print('Your hypothenuse is ' + str(cSide))

'''
Slope formula 
Slope = (y2 - y1)/(x2 - x1) = rise/run
x, y are numbers representing the points in a graph
'''

print('Enter input for slope formula')
print('Coordinate 1')
x1 = int(input('Enter x point: '))
y1 = int(input('Enter y point: '))
print('Coordinate 2')
x2 = int(input('Enter x point: '))
y2 = int(input('Enter y point: '))

cord1 = (x1, y1)
cord2 = (x2, y2)

rise = cord2[1] - cord1[1]
run = cord2[0] - cord1[0]
slope = rise/run

print(f'Your slope is {str(slope)}')

