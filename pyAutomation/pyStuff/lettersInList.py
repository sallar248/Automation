# Script that extract letters from 26 text files in list

import glob

letters = []
file_list = glob.glob("letters/*.txt")
print(file_list)

for filename in file_list:
    with open(filename, "r") as file:
        letters.append(file.read().strip("\n"))

print(letters)
