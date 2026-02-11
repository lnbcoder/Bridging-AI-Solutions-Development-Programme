# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.

# Example:
# no_ohs("code")
# c
# d
# e

def no_ohs(text):
    for i in text:
        if i != 'o':
            print(i)

no_ohs("code")

