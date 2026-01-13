# Write a function `starts_with_r` that accepts a string as an argument.
# The function should return True if the string starts with 'r' or 'R'.
# Otherwise, return False.

# print(starts_with_r("roger that"))        # True
# print(starts_with_r("Row, row, row your boat"))  # True
# print(starts_with_r("slip"))              # False
# print(starts_with_r("Taxicab"))           # False


def starts_with_r(str):
    if str.startswith('r') or str.startswith('R'):
        return True
    else:
        return False

print(starts_with_r("roger that"))        # True
print(starts_with_r("Row, row, row your boat"))  # True
print(starts_with_r("slip"))              # False
print(starts_with_r("Taxicab"))           # False