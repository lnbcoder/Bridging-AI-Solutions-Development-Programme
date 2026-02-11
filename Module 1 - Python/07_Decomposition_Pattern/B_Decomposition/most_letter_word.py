# Write a function `most_letter_word(sentence, char)` that accepts:
# - a sentence string
# - a single character
#
# The function should return the word in the sentence that contains the
# character the greatest number of times.
#
# You can assume the sentence contains at least one word.
# If there is a tie, return the word that appears first in the sentence.

def most_letter_word(sentence, char):
    long_word = ''
    for word in sentence.split():
        if len(word) > len(long_word) and char in word:
            long_word = word
    return long_word

print(most_letter_word(
'she received an award for excellence in science','e'
))# 'excellence'

print(most_letter_word(
'she received an award for excellence in science','a'
))# 'award'

print(most_letter_word(
'I hope sophomore year comes soon','o'
))# 'sophomore'

print(most_letter_word(
'I hope sophomore year comes soon','s'
))# 'sophomore'
