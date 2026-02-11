# Write a function `reverse_array(arr)` that accepts a list as an argument.
# The function should return a list containing the elements of the original list in reverse order.

# Example:
# reverse_array(["zero", "one", "two", "three"]) -> ['three', 'two', 'one', 'zero']
# reverse_array([7, 1, 8]) -> [8, 1, 7]


def reverse_array(arr):
    new_array = []
    for i in arr[::-1]:
        new_array.append(i)

    return new_array

print(reverse_array(["zero", "one", "two", "three"])) # -> ['three', 'two', 'one', 'zero']
print(reverse_array([7, 1, 8])) # -> [8, 1, 7]