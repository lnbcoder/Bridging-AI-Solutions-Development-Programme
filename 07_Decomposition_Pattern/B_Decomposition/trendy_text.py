# Write a function `trendy_text` that accepts a sentence string as an argument.
# The function should return the sentence where the last vowel of every word
# is removed.

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

def trendy_text(sentence):
    new_sentence = []
    for word in sentence.split():
        temp_word = remove_last_vowel(word)
        new_sentence.append(temp_word)
    return ' '.join(new_sentence)


print(trendy_text("the concert will be epic"))
# 'th concrt wll be epc'

print(trendy_text("breakfast food is wonderful"))
# 'breakfst fod s wonderfl'

print(trendy_text("the weather will improve hopefully"))
# 'th weathr wll improv hopeflly'
