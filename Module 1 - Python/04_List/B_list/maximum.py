# Write a function `maximum(numbers)` that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

# Example:
# maximum([5, 6, 3, 7]) -> 7
# maximum([17, 15, 19, 11, 2]) -> 19
# maximum([]) -> None

def maximum(numbers):
    
    if numbers == []:
        return "None"

    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i

    return max_num

print(maximum([5, 6, 3, 7])) # -> 7
print(maximum([17, 15, 19, 11, 2]) )# -> 19
print(maximum([34, 15, 19, 11, 2]) )
print(maximum([])) # -> None