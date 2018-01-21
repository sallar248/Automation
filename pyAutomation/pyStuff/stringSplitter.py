# Create script that will split a string

def count_words(strng):
    strng_list = strng.split()
    return len(strng_list)

print(count_words("Hey there its me"))
