#!/usr/bin/python
# Sequence Item Picking
# Script prints out a list slice containing letters a, c, e, g, and i

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[::2])

# syntax of list slicing is [start:end:step]
# when you dont pass a step, ptyhon assumes the step is 1
# [:] get everything from start to end
# [::2] means get everything from start to end at a step of two
