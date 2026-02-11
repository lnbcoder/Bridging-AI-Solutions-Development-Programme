# Write a function `print2d(matrix)` that accepts a 2D list and prints all inner elements.

def print2d(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j])

array1 = [
    ["a", "b", "c", "d"],
    ["e", "f"],
    ["g", "h", "i"]
]

print2d(array1)
# prints:
# a
# b
# c
# d
# e
# f
# g
# h
# i

array2 = [[9, 3, 4], [11], [42, 100]]
print2d(array2)
# prints:
# 9
# 3
# 4
# 11
# 42
# 100

