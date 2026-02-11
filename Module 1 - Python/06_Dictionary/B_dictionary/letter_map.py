# Write a function `letter_map` that accepts:
# - a string
# - a dictionary
# The function should return a new string where characters that appear as keys in the dictionary are replaced with their corresponding values.

def letter_map(str, dict):
    new_word = ""
    for i in str:
        if i in dict:
            i = dict[i]
        new_word += i
    return new_word


print(letter_map("symbolic", {"y":"i","o":"a","c":"k" }))
# 'simbalik'

print(letter_map("colossal", {"o":"x","s":"p" }))
# 'cxlxppal'

print(letter_map("miniscule", {"u":"t","i":"f","e":"q" }))
# 'mfnfsctlq'

