# Write a function `stay_positive(numbers)` that accepts a list of numbers.
# The function should return a new list containing only the positive numbers.

# Example:
# stay_positive([10, -4, 3, 6]) #-> [10, 3, 6]
# stay_positive([-5, 11, -40, 30.3, -2]) #-> [11, 30.3]
# stay_positive([-11, -30]) #-> []

def stay_positive(numbers):
    new_list = []
    for i in range(len(numbers)):
        if numbers[i] > 0:
            new_list.append(numbers[i])

    return new_list

print(stay_positive([10, -4, 3, 6])) #-> [10, 3, 6]
print(stay_positive([-5, 11, -40, 30.3, -2])) #-> [11, 30.3]
print(stay_positive([-11, -30])) #-> []