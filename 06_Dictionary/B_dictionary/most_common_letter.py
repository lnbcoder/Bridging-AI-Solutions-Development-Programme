# Write a function `most_common_letter` that accepts a string as an argument.
# The function should return the character that appears **most frequently** in the string.
# You may assume:
# - There are **no ties**
# - The string contains only lowercase letters

def most_common_letter(str):
    dict = {}
    for i in str.lower():
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    max_value = 0
    max_key = ""
    for key, value in dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key 
    
print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'

