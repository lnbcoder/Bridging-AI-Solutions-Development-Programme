# Write a function `lengthiest_word(sentence)` that accepts a string containing a sentence.
# The function should return the longest word in the sentence.
# If there is a tie, return the word that appears later in the sentence.

# Example:
# lengthiest_word("I am pretty hungry") -> 'hungry'
# lengthiest_word("we should think outside of the box") -> 'outside'
# lengthiest_word("down the rabbit hole") -> 'rabbit'
# lengthiest_word("simmer down") -> 'simmer'

def lengthiest_word(sentence):
    long_word = ""
    words = sentence.split()
    
    for i in words:
        if len(i) >= len(long_word):
            long_word = i
    return long_word

print(lengthiest_word("I am pretty hungry")) # -> 'hungry'
print(lengthiest_word("we should think outside of the box")) # -> 'outside'
print(lengthiest_word("down the rabbit hole")) # -> 'rabbit'
print(lengthiest_word("simmer down")) # -> 'simmer'