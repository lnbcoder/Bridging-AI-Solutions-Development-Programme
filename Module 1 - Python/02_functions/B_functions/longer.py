# Write a function `longer` that accepts two strings.
# Return the string that is longer.
# If both strings have the same length, return the first string.

# print(longer("drum", "piranha"))       # "piranha"
# print(longer("basket", "fork"))        # "basket"
# print(longer("flannel", "sustainable"))# "sustainable"
# print(longer("disrupt", "ability"))    # "disrupt"
#  print(longer("bird", "shoe"))          # "bird"

def longer(word1, word2):
    if len(word1) >= len(word2):
        return word1
    else:
        return word2

print(longer("drum", "piranha"))       # "piranha"
print(longer("basket", "fork"))        # "basket"
print(longer("flannel", "sustainable"))# "sustainable"
print(longer("disrupt", "ability"))    # "disrupt"
print(longer("bird", "shoe"))          # "bird"
