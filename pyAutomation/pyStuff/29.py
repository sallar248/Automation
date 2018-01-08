#!/usr/bin/python
# Write function that cals liquid volume where radius "r" is always 10

from math import pi

def volume(h, r = 10):
    v = ((4 * pi *r**3) /3) - (pi * h**2 * (3*r - h) / 3)
    return v


print(volume(2))
