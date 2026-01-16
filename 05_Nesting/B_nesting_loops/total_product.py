# Write a function `total_product(matrix)` that returns the product of all numbers in a 2D list.

def total_product(matrix):
    product = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            product *= matrix[i][j]
    return product
   

array1 = [[3, 5, 2], [6, 2]]
array2 = [[4, 6], [2, 3], [1, 2]]

print(total_product(array1))  # 360
print(total_product(array2))  # 288

