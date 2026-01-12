# Write a function `filter_long_words(words)` that accepts a list of strings.
# The function should return a new list containing only the words that have
# less than 5 characters.

# Example:
# filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]) #-> ['kale', 'cat', 'axe']
# filter_long_words(["disrupt", "pour", "trade", "pic"]) #-> ['pour', 'pic']

def filter_long_words(words):
    new_list = []
    for i in words:
        if len(i) < 5:
            new_list.append(i)

    return new_list

print(filter_long_words(["kale", "cat", "retro", "axe", "heirloom"])) #-> ['kale', 'cat', 'axe']
print(filter_long_words(["disrupt", "pour", "trade", "pic"])) #-> ['pour', 'pic']