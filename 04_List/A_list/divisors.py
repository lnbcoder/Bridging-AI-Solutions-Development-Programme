# Write a function `divisors(num)` that accepts a number.
# The function should return a list containing all positive numbers that divide num exactly.

# Example:
# divisors(15) #-> [1, 3, 5, 15]
# divisors(7) #-> [1, 7]
# divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]


def divisors(num):
    new_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            new_list.append(i)

    return new_list

print(divisors(15)) #-> [1, 3, 5, 15]
print(divisors(7)) #-> [1, 7]
print(divisors(24)) #-> [1, 2, 3, 4, 6, 8, 12, 24]

