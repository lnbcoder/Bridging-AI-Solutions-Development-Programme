# Write `average_of_four(a, b, c, d)` 
# returns the average of four numbers.

# Example Output:
# print(average_of_four(10, 4, 12, 3))     # 7.25
# print(average_of_four(-20, 50, 4, 21))   # 13.75
# print(average_of_four(5, 5, 3, 7))       # 5

def average_of_four(a, b, c, d):
    sum = a + b + c + d
    if sum % 4 == 0:
        return sum // 4 #returns average in int form
    return sum / 4 

print(average_of_four(10, 4, 12, 3))     # 7.25
print(average_of_four(-20, 50, 4, 21))   # 13.75
print(average_of_four(5, 5, 3, 7))       # 5

