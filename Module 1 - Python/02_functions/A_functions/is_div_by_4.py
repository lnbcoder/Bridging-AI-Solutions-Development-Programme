# Write a function `is_div_by_4` that accepts a number as an argument.
# The function should return a boolean indicating whether or not
# the number is divisible by 4.

# print(is_div_by_4(8))   # True
# print(is_div_by_4(12))  # True
# print(is_div_by_4(24))  # True
# print(is_div_by_4(9))   # False
# print(is_div_by_4(10))  # False


def is_div_by_4(number):
    if number % 4 == 0:
        return True
    else:
        return False
    
print(is_div_by_4(8))
print(is_div_by_4(12))
print(is_div_by_4(24))
print(is_div_by_4(9))
print(is_div_by_4(10))