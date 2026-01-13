# Write a function `your_average_function(numbers)` that accepts a list of numbers.
# The function should return the average of all elements in the list.
# If the list is empty, the function should return None.

# Example:
# your_average_function([5, 2, 7, 24]) -> 9.5
# your_average_function([100, 6]) -> 53
# your_average_function([31, 32, 40, 12, 33]) -> 29.6
# your_average_function([]) -> None


def your_average_function(numbers):
    sum = 0
    num_length = len(numbers)
  
    for i in numbers:
        sum += i

    if len(numbers) != 0:
        return sum / num_length
    else:
        return "None"
    
'''
def your_average_function(numbers):

    if len(numbers) != 0:
        return sum(numbers) / len(numbers)
    else:
        return "None"'''


print(your_average_function([5, 2, 7, 24])) # -> 9.5
print(your_average_function([100, 6])) # -> 53
print(your_average_function([31, 32, 40, 12, 33])) # -> 29.6
print(your_average_function([])) # -> None
