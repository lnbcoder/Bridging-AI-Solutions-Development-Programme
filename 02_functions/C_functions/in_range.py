# Write a function `in_range(min_val, max_val, n)`
# Return True if `n` is between `min_val` and `max_val` (inclusive).

# Example
# print(in_range(5, 13, 8))     # True
# print(in_range(5, 13, 29))    # False
# print(in_range(100, 125, 100))# True

def in_range(min_val, max_val, n):
    if n in range(min_val, max_val + 1):
        return True
    else:
        return False

print(in_range(5, 13, 8))     # True
print(in_range(5, 13, 29))    # False
print(in_range(100, 125, 100))# True
print(in_range(100, 125, 99)) # False
print(in_range(40, 45, 44))   # True
print(in_range(40, 45, 45))   # True
print(in_range(40, 45, 46))   # False

