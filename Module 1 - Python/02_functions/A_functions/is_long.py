# Write a function `is_long` that accepts a string as an argument.
# The function should return a boolean indicating whether the string
# is longer than 5 characters.

# print(is_long("pie"))         # False
# print(is_long("kite"))        # False
# print(is_long("kitty"))       # False
# print(is_long("telescope"))   # True
# print(is_long("thermometer")) # True
# print(is_long("restaurant"))  # True

def is_long(str):
    if len(str) > 5:
        return True
    else:
        return False

print(is_long("pie")) 
print(is_long("kite"))
print(is_long("kitty")) 
print(is_long("telescope")) 
print(is_long("thermometer")) 
print(is_long("restaurant"))