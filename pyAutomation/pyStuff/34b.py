# local vs global variables
# Adding global c fixes the code, makes name c in the 
# global namespace.

def foo():
    global c
    c = 1
    return c
foo()
print(c) 

