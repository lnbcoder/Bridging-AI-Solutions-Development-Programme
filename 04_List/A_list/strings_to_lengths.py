# Write a function `strings_to_lengths(strings)` that accepts a list of strings.
# The function should return a new list containing the lengths of each string.

# Example:
# strings_to_lengths(["belly", "echo", "irony", "pickled"]) #-> [5, 4, 5, 7]
# strings_to_lengths(["on", "off", "handmade"]) #-> [2, 3, 8]

def strings_to_lengths(strings):
    new_list = []
    for i in strings:
        length = len(i)
        new_list.append(length)

    return new_list


print(strings_to_lengths(["belly", "echo", "irony", "pickled"])) #-> [5, 4, 5, 7]
print(strings_to_lengths(["on", "off", "handmade"])) #-> [2, 3, 8]