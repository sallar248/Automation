# One file per letter
# Create script that generates 26 text files named a.txt, b.txt, z.txt


import string, os

if not os.path.exists("letters"):
    os.makedirs("letters")
for letter in string.ascii_lowercase:
    with open("letters/" + letter + ".txt", "w") as file:
        file.write(letter + "\n")
