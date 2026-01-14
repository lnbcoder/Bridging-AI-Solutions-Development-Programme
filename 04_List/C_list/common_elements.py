# Write a function `common_elements(arr1, arr2)` that accepts two lists as arguments.
# The function should return a new list containing the elements that are found in both input lists.
# The order of elements in the output list doesn't matter.

# Example:
# common_elements(["a", "c", "d", "b"], ["b", "a", "y"]) -> ['a', 'b']
# common_elements([4, 7], [32, 7, 1, 4]) -> [4, 7]

def common_elements(arr1, arr2):
    common = []

    for i in arr1:
        if i in arr2:
            common.append(i)
    
    return common

print(common_elements(["a", "c", "d", "b"], ["b", "a", "y"])) # -> ['a', 'b']
print(common_elements([4, 7], [32, 7, 1, 4])) # -> [4, 7]