# Write a function `wacky_word` that accepts two strings.
# Return a new string made from:
# - the first 3 characters of the first string
# - the last 2 characters of the second string
#
# The first string is at least 3 chars long.
# The second string is at least 2 chars long.

# Example:
# print(wacky_word("very", "kindly"))       # "verly"
# print(wacky_word("forever", "sick"))      # "forck"
# print(wacky_word("cellar", "door"))       # "celor"
# print(wacky_word("bagel", "sweep"))       # "bagep"

def wacky_word(first_word, second_word):
    new_word = first_word[:3] + second_word[-2::]
    return new_word

print(wacky_word("very", "kindly"))       # "verly"
print(wacky_word("forever", "sick"))      # "forck"
print(wacky_word("cellar", "door"))       # "celor"
print(wacky_word("bagel", "sweep"))       # "bagep"