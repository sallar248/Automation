#!/usr/bin/python
# Negative Slicing
# Print out a list slice containing last 3 items

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-3:])

# -3: means from item with index -3 to the very last item of the list
# When you don't put any index to the right of the colon everything is included and upper-bound exclusivity is ignored.
