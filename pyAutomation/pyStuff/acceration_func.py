#!/usr/bin/python
# Script that does acceleration calculations
# Create a function that calcs acceleration

def acceleration(v1, v2, t1, t2):
    a = (v2-v1) / (t2 -t1)
    return a

print(acceleration(0,10,0,20))

# First threee lines are wher we create the function
# Last line print out the functioA

def acceleration(v1, v2, t1, t2):
    a = float(v2 -v1) / float(t2 -t1)
    return a

print(acceleration(0,10,0,20))
