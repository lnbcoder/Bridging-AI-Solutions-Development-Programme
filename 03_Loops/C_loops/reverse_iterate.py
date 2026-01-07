# Write a function `reverse_iterate(text)` that prints each character of the string
# in reverse order. The function does not return a value, just prints.

# Example:
#reverse_iterate("carrot")
# t
# o
# r
# r
# a
# c

#reverse_iterate("box")
# x
# o
# b

def reverse_iterate(text):
    for i in text[::-1]:
        print(i)

reverse_iterate("carrot")
reverse_iterate("box")