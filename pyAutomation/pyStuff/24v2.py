#!/usr/bin/python
# Print the expected Output
# Print b values, c values, a values


d = dict(a =  list(range(1,11)), b = list(range(11,21)), c = list(range(21,31)))

print(d.items())

for key, value in d.items():
    print(key, "has value", value)
