# Print out each line homologous items of the two sequences
# use "zip" function if you want to iterate thru more than one
# sequence

a = [1, 2, 3]
b = (4, 5, 6)

for i, j in zip(a,b):
    print(i +j)
