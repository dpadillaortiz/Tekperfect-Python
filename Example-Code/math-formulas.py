#! /usr/bin/python3

# Math Formulas

# Pythagoreom Theorem
# c^2 = a^2 + b^2
# -> c = sqrt(a^2 + b^2)

aSide = 5
bSide = 6
aBSide = aSide**2 + bSide**2

cSide = aBSide**(1/2)

print(cSide)

# Slope 
# Slope = (y2 - y1)/(x2 - x1) = rise/run

xPoint1 = 6
xPoint2 = 10

yPoint1 = 3
yPoint2 = 5

rise = yPoint2 - yPoint1
run = xPoint2 - xPoint1

slope = rise/run


# What if we wanted to do this for multiple inputs?
def pythm(a,b):
    aSide = a
    bSide = b
    
    aBSide = aSide**2 + bSide**2

    cSide = aBSide**(1/2)

    return cSide

def slopeFormula(cord1, cord2):
    xPoint1, yPoint1 = cord1
    xPoint2, yPoint2 = cord2

    rise = yPoint2 - yPoint1
    run = xPoint2 - xPoint1

    slope = rise/run

    return slope


