# Write a function `raise_power(base, exponent)` that returns the result of
# base raised to the exponent using loops (do not use ** operator or math.pow).

# Example:
# raise_power(2, 5)  #-> 32
# raise_power(4, 3)  #-> 64
# raise_power(10, 4) #-> 10000
# raise_power(7, 2)  #-> 49

def raise_power(base, exponent):
    result = 1
    for i in range(1, exponent + 1):
        result *= base
    return result


print(raise_power(2, 5))  #-> 32
print(raise_power(4, 3))  #-> 64
print(raise_power(10, 4)) #-> 10000
print(raise_power(7, 2))  #-> 49