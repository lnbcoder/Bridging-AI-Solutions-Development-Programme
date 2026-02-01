# Write a function `lala_language` that accepts a sentence string as an argument.
# The function should return a new sentence where words longer than 3 characters
# are modified.
#
# Modified words should have each vowel followed by 'l' and the same vowel again.
# See the examples below.

def lala_language(sentence):
    vowels = 'aeiou'
    new_sentence = []
    for word in sentence.split():
        new_word = ''
        for letter in word:
            if len(word) > 3 and letter in vowels:
                new_word += letter + 'l' + letter
            else:
                new_word += letter
        new_sentence.append(new_word)
    return ' '.join(new_sentence)


print(lala_language('this is pretty strange'))
# 'thilis is preletty stralangele'

print(lala_language('can you speak our language'))
# 'can you spelealak our lalangulualagele'
