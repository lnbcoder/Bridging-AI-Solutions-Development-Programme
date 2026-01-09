# Write a function `fizz_buzz(max_num)` that prints all numbers <= max_num
# that are divisible by 3 or 5 but not both.
# The function does not return a value, just prints.

# Example:
# fizz_buzz(18)
# 3
# 5
# 6
# 9
# 10
# 12
# 18

# fizz_buzz(33)
# 3
# 5
#...
# 25
# 27
# 33

def fizz_buzz(max_num):
    for i in range(1, max_num + 1):
        if (i % 3 == 0) ^ (i % 5 == 0):
            print(i)

fizz_buzz(18)


'''
def fizz_buzz(max_num):
    for i in range(1, max_num + 1):
        if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
            print(i)
'''