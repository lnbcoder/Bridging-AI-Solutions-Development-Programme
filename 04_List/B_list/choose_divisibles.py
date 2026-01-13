# Write a function `choose_divisibles(numbers, target)` that accepts a list of numbers and a target number.
# The function should return a new list containing only the elements divisible by the target.

# Example:
# choose_divisibles([40, 7, 22, 20, 24], 4) -> [40, 20, 24]
# choose_divisibles([9, 33, 8, 17], 3) -> [9, 33]
# choose_divisibles([4, 25, 1000], 10) -> [1000]

def choose_divisibles(numbers, target):
    new_list = []
    for i in numbers:
        if i % target == 0:
            new_list.append(i)
        
    return new_list

print(choose_divisibles([40, 7, 22, 20, 24], 4)) # -> [40, 20, 24]
print(choose_divisibles([9, 33, 8, 17], 3)) # -> [9, 33]
print(choose_divisibles([4, 25, 1000], 10)) # -> [1000]