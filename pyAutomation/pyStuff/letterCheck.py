# Script iterates thru each text file
# Script checks for letter 
# puts letter in list

import glob

letters = []
file_list = glob.iglob("letters/*.txt")
check = "python"

for filename in file_list:
    with open(filename, "r") as file:
        letter = file.read().strip("\n")
        if letter in check:
            letters.append(letter)


print(letters)
