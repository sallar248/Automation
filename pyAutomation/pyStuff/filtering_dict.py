#!/usr/bin/python
# Filter the dictionary by removing all items with the value greater than 1


d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value <=1)
print(d)

# Using a dictionary comprehension
# Comprehension is the expression inside dict()
# Comprehension iterates thru and if less than or equal 1 item is added to new dict
# new dict assigned to d
# d is now filtered
