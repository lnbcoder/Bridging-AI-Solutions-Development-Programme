# Write a function `contains(str1, str2)` that:
# Returns **True** if `str2` is found inside `str1`
# Ignore capitalization differences

# Example Output:
# print(contains("caterpillar", "pill"))     # True
# print(contains("lion's share", "on"))      # True
# print(contains("SORRY", "or"))             # True
# print(contains("tangent", "gem"))          # False
# print(contains("clock", "ok"))             # False

def contains(str1, str2):
    if str2 in str1.lower():
        return True
    else:
        return False
    
print(contains("caterpillar", "pill"))     # True
print(contains("lion's share", "on"))      # True
print(contains("SORRY", "or"))             # True
print(contains("tangent", "gem"))          # False
print(contains("clock", "ok"))             # False

