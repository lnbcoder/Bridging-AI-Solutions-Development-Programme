# Write a function `half` that accepts a number as an argument.
# The function should return half of the number.

# print(half(8))    # 4
# print(half(15))   # 7.5
# print(half(90))   # 45


def half(number):
    if number % 2 == 0:
        return number // 2
    
    return number / 2


print(half(8))
print(half(15))
print(half(90))