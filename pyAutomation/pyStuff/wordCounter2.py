# another way to get word count

import re

def count_words_re(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string_list = re.split(", | ", string)
print(count_words_re("words2.txt"))
