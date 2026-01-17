# Write a function `spam(pairs)` that accepts a 2D list. Each inner list contains
# a word and a number. The function returns a string with each word repeated
# the specified number of times, separated by spaces.

def spam(pairs):
    words_repeated = ""
    for i in range(len(pairs)):
        for j in range(pairs[i][1]):
            words_repeated += pairs[i][0] + " "
    return words_repeated



# Example usage:
array1 = [["hi", 3], ["bye", 2]]
print(spam(array1))  # 'hi hi hi bye bye'

array2 = [["cat", 1], ["dog", 2], ["bird", 4]]
print(spam(array2))  # 'cat dog dog bird bird bird bird'