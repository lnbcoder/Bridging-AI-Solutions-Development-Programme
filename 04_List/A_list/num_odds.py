# Write a function `num_odds(numbers)` that accepts a list of numbers.
# The function should return the count of odd numbers in the list.

# Example:
# num_odds([4, 7, 2, 5, 9]) #-> 3
# num_odds([11, 31, 58, 99, 21, 60]) #-> 4
# num_odds([100, 40, 4]) #-> 0

def num_odds(numbers):
    odd_nums = 0
    for i in numbers:
        if i % 2 != 0:
            odd_nums += 1

    return odd_nums

print(num_odds([4, 7, 2, 5, 9])) #-> 3
print(num_odds([11, 31, 58, 99, 21, 60])) #-> 4
print(num_odds([100, 40, 4])) #-> 0