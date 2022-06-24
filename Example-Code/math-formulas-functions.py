#!/usr/bin/python3


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


