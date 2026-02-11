# Write `sum_upto(n)`
# Return the sum of numbers from 1 → n

# Example:
# print(sum_upto(5))   # 15
# print(sum_upto(10))  # 55

def sum_upto(n):
    sum_value = sum(range(1, n + 1))
    return sum_value

print(sum_upto(5))   # 15
print(sum_upto(10))  # 55