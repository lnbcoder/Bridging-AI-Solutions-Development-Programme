# Write a function `two_sum(numbers, target)` that accepts a list of numbers and a target number.
# The function should return True if there exists a pair of distinct elements in the list that sum to the target.
# Otherwise, return False.

# Example:
# two_sum([2, 3, 5, 9], 7) #-> True
# two_sum([2, 3, 5, 9], 4) #-> False
# two_sum([6, 3, 4], 10) #-> True
# two_sum([6, 5, 1], 10) #-> False

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False   

print(two_sum([2, 3, 5, 9], 7)) #-> True
print(two_sum([2, 3, 5, 9], 4)) #-> False
print(two_sum([6, 3, 4], 10)) #-> True
print(two_sum([6, 5, 1], 10)) #-> False