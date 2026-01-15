# Write a function `print_combinations(arr1, arr2)` that accepts two lists.
# The function should print all combinations taking one element from the first list
# and one from the second list. It doesn't need to return anything.

# Example:
# colors = ["gray", "cream", "cyan"]
# clothes = ["shirt", "flannel"]
# print_combinations(colors, clothes)
# prints:
# gray shirt
# gray flannel
# cream shirt
# cream flannel
# cyan shirt
# cyan flannel

def print_combinations(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            print(arr1[i] + " " + arr2[j])

colors = ["gray", "cream", "cyan"]
clothes = ["shirt", "flannel"]
print_combinations(colors, clothes)