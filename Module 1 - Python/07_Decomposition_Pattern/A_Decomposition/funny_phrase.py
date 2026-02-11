# Write a function `funny_phrase` that accepts a sentence string.
# The function should return the sentence where **every other word** has its vowels repeated **twice consecutively**.
# Vowels are: `a, e, i, o, u`

from double_vowel import double_vowel 

def funny_phrase(sentence): 
    new_sentance = ""
    for word in sentence.split(" "):
        if len(word) >= 4:
            new_word = double_vowel(word) 
            new_sentance += new_word + " "
        else:
            new_sentance += word + " "
    return new_sentance

print(funny_phrase("she dreamed of being a runner"))
# 'she dreeaameed of beeiing a ruunneer'

print(funny_phrase("park near the stoplight"))
# 'park neeaar the stoopliight'

print(funny_phrase("we need many gardeners"))
# 'we neeeed many gaardeeneers'

