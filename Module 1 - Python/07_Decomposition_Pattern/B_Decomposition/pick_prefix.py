# Write a function `pick_prefix(strings, prefix)` that accepts:
# - a list of strings
# - a prefix string
#
# The function should return a list of words that begin with the prefix.

def pick_prefix(strings, prefix):
    prefix_len = len(prefix)
    new_strings = []
    for word in strings:
        if word[:prefix_len] == prefix:
            new_strings.append(word)
    return new_strings


print(pick_prefix(['connect','company','concert','cram'],'con'))
# ['connect', 'concert']

print(pick_prefix(['miner','mistake','misspeak','moose','mission'],'mis'))
# ['mistake', 'misspeak', 'mission']

