# Function that takes text file as input
# Returns the number of words contained in text file
# Considers comma's and spaces


def count_words(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string = string.replace(",", "")
        string_list = string.split("")
        return len(string_list)

print(count_words("words2.txt"))
