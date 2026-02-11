# Write a function `remove_last_vowel` that accepts a string as an argument.
# The function should return the string with its last vowel removed.
# Vowels are the letters: a, e, i, o, u

def remove_last_vowel(word):
    vowels = 'aeiou'
    temp_word = []
    new_word = ''
    for i in word[::-1]:
        if temp_word == [] and i in vowels:
            temp_word.append(i)
        else:
            new_word += i
    return new_word[::-1]

print(remove_last_vowel("speaker"))# 'speakr'
print(remove_last_vowel("trading"))# 'tradng'
print(remove_last_vowel("thunder"))# 'thundr'
print(remove_last_vowel("myth"))# 'myth'

