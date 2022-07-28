#! /usr/bin/python3

# Intro to Comments

# Math Formulas
'''
# Pythagoreom Theorem
# c^2 = a^2 + b^2
# -> c = sqrt(a^2 + b^2)
'''

# c represents the hypothenuse 
# a, b represent the other two sides

# Variables and Data Types
- can only access variables declared before it i.e. above the line you're on
aSide = 5
bSide = 6

# Introduce operators -> Math operations with python
aBSide = aSide**2 + bSide**2

cSide = aBSide**(1/2)

print(cSide)

# Slope 
# Slope = (y2 - y1)/(x2 - x1) = rise/run
# x, y are numbers representing the points in a graph

xPoint1 = 6
xPoint2 = 10

yPoint1 = 3
yPoint2 = 5

rise = yPoint2 - yPoint1
run = xPoint2 - xPoint1

slope = rise/run

# Introduce user input
# Replace the hard coded numbers with input()
# i.e. aSide = input()

